const inputElement = document.getElementById("input-text");
const langElement = document.getElementById("target-language");
const outputElement = document.getElementById("output-text");
const btnElement = document.getElementById("translate-btn");


document.addEventListener('DOMContentLoaded', () => {
    btnElement.addEventListener('click', translateText);
    inputElement.addEventListener('input', saveData);
    langElement.addEventListener('input', saveData);
});


async function translateText() {
    const inputText = inputElement.value.trim();
    const targetLanguage = langElement.value.trim();


    if (inputText === "" || targetLanguage === "") {
        alert("Please enter text and select a target language.");
        return;
    }
    else {
        try {

            btnElement.disabled = true;
            btnElement.textContent = "Translating...";

            inputElement.disabled = true;
            langElement.disabled = true;

            //change to your domain
            const res = await fetch("http://smart-translator-backend-xhc2dl-56f44e-72-62-125-194.traefik.me/translate", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ inputText, targetLanguage })
            });

            const data = await res.json();
            if (!res.ok) {
                throw new Error(data.error || "Translation failed");
            }

            outputElement.value = data.reply;
        }
        catch (error) {
            alert("Error: " + error.message);
            return;
        }
        finally {
            btnElement.disabled = false;
            btnElement.textContent = "Translate";

            inputElement.disabled = false;
            langElement.disabled = false;

            saveData();
        }

    }
}

// SAVE DATA LOCALLY

function saveData() {
    const data = {
        inputText: inputElement.value,
        targetLanguage: langElement.value,
        outputText: outputElement.value
    };
    chrome.storage.local.set({ translatorData: data });
}
function loadData() {
    chrome.storage.local.get("translatorData", (result) => {
        const data = result.translatorData;
        if (data) {
            const { inputText, targetLanguage, outputText } = data;
            inputElement.value = inputText;
            langElement.value = targetLanguage;
            outputElement.value = outputText;
        }
    });
}

loadData();

