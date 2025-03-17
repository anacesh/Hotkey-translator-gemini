import requests
from google import genai
from google.genai.types import GenerateContentConfig

from config import config, debug_print

GEMINI_API_KEY = config.get("gemini_api_key", "YOUR_GEMINI_API_KEY")
USE_GEMINI = config.get("use_gemini", True)
SEND_ORIGINAL_TO_GEMINI = config.get("send_original_to_gemini", False)


def translate_text(text, source_lang, target_lang):
    debug_print(f"Перевод текста: {text}")
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": source_lang,
        "tl": target_lang,
        "dt": "t",
        "q": text
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        result = response.json()
        translation = ''.join([sentence[0] for sentence in result[0] if sentence[0]])
        debug_print(f"Перевод ({source_lang} → {target_lang}): {translation}")
        return translation
    except Exception as e:
        print(f"Ошибка перевода: {e}")
        return text


def process_with_gemini(original_text, translated_text):
    if not USE_GEMINI or not GEMINI_API_KEY:
        return translated_text

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)

        system_prompt = config.get("system_prompt", "")
        extra_prompt = config.get("gemini_extra_prompt", "")

        contents = [translated_text]
        if SEND_ORIGINAL_TO_GEMINI:
            contents.insert(0, f"Original: {original_text}\n{extra_prompt}")

        config_data = GenerateContentConfig(system_instruction=system_prompt)

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            config=config_data,
            contents=contents
        )

        improved_text = response.text
        debug_print("Gemini обработал текст:", improved_text)
        return improved_text
    except Exception as e:
        print(f"Ошибка Gemini API: {e}")
        return translated_text