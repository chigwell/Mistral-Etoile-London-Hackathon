const captureCooldown = 5000; // 5 seconds cooldown

chrome.runtime.onInstalled.addListener(() => {
  setInterval(() => {
    console.log('Taking screenshot...');
    chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
      if (tabs[0]) {
        console.log('Capturing tab:', tabs[0].id);
        chrome.tabs.captureVisibleTab({format: 'png'}, (image) => {
          if (chrome.runtime.lastError) {
            console.error('Error capturing tab:', chrome.runtime.lastError.message);
            return;
          }

          const data = JSON.stringify({ image: image });

          fetch('http://0.0.0.0/screenshot', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: data
          })
          .then(response => response.json())
          .then(data => {
            console.log('Success:', data);
            if (data.message === 1) {
              // Hide the content on the active tab
              chrome.scripting.executeScript({
                target: { tabId: tabs[0].id },
                function: hideElement
              });
            }
          })
          .catch((error) => {
            console.error('Error:', error);
          });
        });
      }
    });
  }, captureCooldown);
});

function hideElement() {
  const elements = document.querySelectorAll('body');
  elements.forEach(element => {
    element.style.display = 'none';
  });
}
