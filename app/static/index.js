async function translateText() {
    const inputElement = document.getElementById("input-text");
    const langElement = document.getElementById("target-language");
    const outputElement = document.getElementById("output-text");
    const btnElement = document.getElementById("translate-btn");

    const text = inputElement.value.trim();
    const targetLanguage = langElement.value.trim();

    if (text === "" || targetLanguage === "") {
        alert("Please enter text and select a target language.");
        return;
    }
    else{
        try {

            btnElement.disabled = true;
            btnElement.textContent = "Translating...";

            
            const res = await fetch("/translate", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({text, targetLanguage})
            });

            const data = await res.json();
            if(!res.ok){
                throw new Error(data.error || "Translation failed");
            }

            outputElement.textContent = data.reply;
        }
        catch (error) {
            alert("Error: " + error.message);
            return;
        }
        finally {
            btnElement.disabled = false;
            btnElement.textContent = "Translate";
        }


    }
}
