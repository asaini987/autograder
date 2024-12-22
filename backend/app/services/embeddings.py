from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama.llms import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pypdf import PdfReader
from io import BytesIO
from ..db.pinecone_client import pc


model = SentenceTransformer("all-MiniLM-L6-v2")

def extract_text_from_pdf(file_bytes):
    pdf_reader = PdfReader(BytesIO(file_bytes))
    return "\n".join(page.extract_text() for page in pdf_reader.pages)

def embed_doc(doc_text, doc_name):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,  # Adjust based on LLM or embedding model limits
        chunk_overlap=50,  # Small overlap for context continuity
        length_function=len,
    )
    chunks = text_splitter.split_text(doc_text)

    embeddings = []
    for idx, chunk in enumerate(chunks):
        embedding = model.encode(chunk)
        embeddings.append({ # fix dictionary form to be comaptible with pinecone
            "embedding": embedding,
            "metadata": {
                "chunk_index": idx,
                "text": chunk,
                "source_file": doc_name
            }
        })

    return embeddings

def retrieve_top_vectors(user_id, query):
    embedding = model.encode(query)
    return pc.query_data(user_id, embedding)

def ask_llm(question, response, rubric): # tell llm we are going to give u the question number
    prompt = PromptTemplate(
        template="""You are an assistant for grading student responses to assignment questions.
        Use the following information from the rubric to help you grade the student response. Tell
        me how many points the student should receive. Follow this rubric exactly, do not deviate from it. 
        Base your decision off of the rubric only. If you truly do not know, say you do not know. 
        Use three sentences maximum and keep your answer concise. 
        Here is the question, the student's response, and the rubric:
        Question: {question}
        Student's Response: {response}
        Rubric Information: {rubric}""",
        input_variables=[question, response, rubric]
    )
    llm = OllamaLLM(model="llama3", temperature=0) # change to one instance
    rag_chain = prompt | llm | StrOutputParser()
    answer = rag_chain.invoke({"question": question, "response": response, "rubric": rubric})
    return answer
    # for chunks in llm.stream(question):
    #     print(chunks, end="")