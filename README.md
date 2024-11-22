# Autograder: An AI powered grader for GradeScope

Let's fix manual grading. It's too menial.

1. Frontend: Chrome Extension
Use React.js with Webpack for a clean UI and easy component management.
Use the Chrome Extension API for permissions and DOM manipulation.

3. DOM Parsing
Use native DOM APIs or MutationObserver to detect changes on Gradescope pages (e.g., new answers loaded).
Leverage unique identifiers in the Gradescope interface to locate specific elements like answers and grade fields.

5. Rubric Handling
Store rubric data in a structured format like JSON within local storage or synced via Chrome Storage API.
Provide a UI in the extension for instructors to input, save, and manage rubrics.

7. Short Answer Parsing
For text processing, integrate an NLP library like spaCy (via a backend or local worker) or use OpenAI's API for more nuanced answer analysis.
Implement pattern matching with Regex for simpler text parsing tasks.

9. Automation (Selecting Grades)
Write a script to programmatically "click" or fill in grades based on parsed results using JavaScript event handling (e.g., click() or dispatchEvent).

11. Backend (Optional)
If you want to enable cross-device syncing or advanced NLP, use Firebase or a lightweight backend like FastAPI or Express.js.

13. Testing & Debugging Tools
Use Puppeteer or Playwright to test the extension on Gradescope.
Chrome DevTools for debugging DOM interactions.

Project Architecture Flow
Input: Instructor uploads rubric data into the extension.
Parse: DOM script scans Gradescope for student answers.
Process: Short answers are analyzed using predefined patterns or an NLP engine.
Output: Grades are selected programmatically based on rubric rules.
This setup would allow you to effectively parse and grade short answers while being scalable for future features. Let me know if you'd like more details about any specific component!






