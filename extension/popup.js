// Get the active tab's URL and check if it matches the Gradescope student submission pattern
chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const currentTab = tabs[0];
    const url = currentTab?.url || "";

    // Regex to check if the URL matches a student submission page
    if (/submissions\/\d+\/grade$/.test(url)) {
        document.getElementById("status").textContent = "On a student's answer";
        document.getElementById("status").style.color = "green";
    } else {
        document.getElementById("status").textContent = "Not on a student's answer";
        document.getElementById("status").style.color = "red";
    }
});

// popup.js

// Listen for messages from content.js
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.type === 'answerData') {
        console.log('Received message in popup:', message);

        // Display the received text in the popup
        const answerContainer = document.getElementById('answer');
        if (answerContainer) {
            answerContainer.textContent = `Answer: ${message.data}`;
            sendResponse({ status: 'success' }); // Acknowledge the message
        } else {
            console.error('Answer container not found in popup!');
        }
    }
});




