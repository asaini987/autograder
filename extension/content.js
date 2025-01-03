// content.js
function init() {
    const answerElement = document.querySelector('.form--textArea-readOnly span');
    if (answerElement) {
        const answerText = answerElement.textContent;
        console.log('Extracted Answer:', answerText);

        // Send the extracted text to the extension
        chrome.runtime.sendMessage({ type: 'answerData', data: answerText }, (response) => {
            if (chrome.runtime.lastError) {
                console.error('Error sending message:', chrome.runtime.lastError.message);
            } else if (response?.status === 'success') {
                console.log('Message sent successfully');
            } else {
                console.log('Message failed');
            }
        });
    } else {
        console.error('Answer element not found!');
    }
}

// Wait for the DOM to load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}
