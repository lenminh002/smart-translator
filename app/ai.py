from dotenv import load_dotenv
import os

from google import genai

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=gemini_api_key)

systemInstruction = """
            You are a helpful assistant that translates text from one language to another.
            Only translate the text and DO NOT provide any additional information or explanations.
            Make sure to maintain the original meaning and context of the text while translating.
                    """

async def translate_text(text, target_language):
    response = await client.aio.models.generate_content(
        model="gemini-3-flash-preview",
        config={
            "system_instruction": systemInstruction,
            "temperature": 0.3
        },
        contents=[
            {
                "role": "user",
                "parts": [{"text": f"Translate the following text to {target_language}: {text}"}]
            }
        ]
    )

    translated_text = response.text.strip()
    print(f"Translated text: {translated_text}")
    return translated_text



# for testing purposes:
if __name__ == "__main__":
    import asyncio

    result = asyncio.run(translate_text("Hello, how are you?", "Vietnamese"))
    print(result)