chrome.webNavigation.onCompleted.addListener((details) => {
    if (details.url.includes("gradescope.com")) {
        chrome.action.openPopup();
    }
}, { url: [{ hostContains: 'gradescope.com' }] });

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    console.log(sender.tab ?
        "from a content script:" + sender.tab.url :
        "from the extension");
    if (message.type === 'answerData') {
        const answerText = message.data;

        // Update the popup HTML
        const answerContainer = document.getElementById('answer');
        if (answerContainer) {
            answerContainer.textContent = `Answer: ${answerText}`;
        }

        // Send a response back
        sendResponse({ status: 'success' });
    }
});