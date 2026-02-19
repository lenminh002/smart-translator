from dotenv import load_dotenv
import os

from google import genai

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

systemInstruction = """
            You are a helpful assistant that translates text from one language to another.
            Only translate the text and DO NOT provide any additional information or explanations.
            Make sure to maintain the original meaning and context of the text while translating.
                    """

async def translate_text(text, target_language):
    try:
        client = genai.Client(api_key=gemini_api_key)
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
    except Exception as e:
        print(f"Error during translation: {e}")
        raise e

    translated_text = response.text.strip()
    print(f"Translated text: {translated_text}")
    return translated_text


