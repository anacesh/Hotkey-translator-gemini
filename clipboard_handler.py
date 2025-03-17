import keyboard
import pyperclip
import time
import sys
import langdetect
import threading
from config import config
from translator import translate_text, process_with_gemini

HOTKEY = config.get("hotkey", "ctrl+shift+t")
ENABLE_ALT_COPY = config.get("enable_alt_copy", True)
DEFAULT_TARGET_LANGUAGE = config.get("default_target_language", "en")


def detect_language(text):
    try:
        return langdetect.detect(text)
    except:
        return "en"


def copy_text():
    original_clipboard = pyperclip.paste()

    if sys.platform == 'win32':
        keyboard.send('ctrl+c')
    else:
        keyboard.send('command+c' if sys.platform == 'darwin' else 'ctrl+c')

    time.sleep(0.5)
    text = pyperclip.paste()

    if ENABLE_ALT_COPY and (not text or text == original_clipboard):
        keyboard.send('ctrl+insert')
        time.sleep(0.5)
        text = pyperclip.paste()

    return text


def process_selected_text():
    text = copy_text()
    if not text:
        print("Не удалось скопировать текст.")
        return

    source_lang = detect_language(text)
    target_lang = config.get("languages", {}).get(source_lang, {}).get("target", DEFAULT_TARGET_LANGUAGE)

    translated_text = translate_text(text, source_lang, target_lang)
    improved_text = process_with_gemini(text, translated_text)

    pyperclip.copy(improved_text)
    keyboard.send('ctrl+v')
    keyboard.send('backspace')


def hotkey_listener():
    while True:
        keyboard.wait(HOTKEY)
        process_selected_text()


def start_hotkey_listener():
    listener_thread = threading.Thread(target=hotkey_listener, daemon=True)
    listener_thread.start()
