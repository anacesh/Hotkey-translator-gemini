# Text Translator & Enhancer

✨ Application for instant text translation and enhancement via Gemini API with hotkey support

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Key Features

- One-click translation of selected text
- Translation enhancement using Gemini AI
- Flexible configuration via config file

## Usage Examples

1. Select the text you want to translate.
2. Press `ctrl+shift+t` (or your configured hotkey).
3. The translated and enhanced text will be automatically pasted in place of the original.

## Installation

Clone the repository:

```bash
git clone https://github.com/anacesh/Hotkey-translator-gemini
cd text-translator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Obtaining a Gemini API Key
1. Go to [Google AI](https://aistudio.google.com/apikey) Studio.
2. Click "Get API key" in the menu.
3. Create a new API key.

Copy the key to config.json:

```json
"gemini_api_key": "YOUR_GEMINI_KEY"
```

❗ **Important:** The Gemini API is not available in all countries. [Check the list of supported regions](https://www.gemini.com/areas-of-availability).

## Configuration
The config.json file contains the main settings:
```json
{
  "hotkey": "ctrl+shift+t",
  "enable_alt_copy": true,
  "default_target_language": "en",
  "use_gemini": true,
  "send_original_to_gemini": true,
  "system_prompt": "...",
  "gemini_extra_prompt": "...",
  "languages": {
    "ru": { "target": "en" },
    "en": { "target": "ru" }
  }
}
```
## Main Parameters:

-   `hotkey`: Hotkey for activation (e.g., `ctrl+shift+t`).
-   `use_gemini`: Enable translation enhancement via Gemini API (`true` or `false`).
-   `system_prompt`: System prompt for the Gemini model.
-   `languages`: Translation language settings (e.g., `{"ru": {"target": "en"}}`).

## ️ Run

```bash
python main.py
```

## ️ Project Structure

    text-translator/
    ├── clipboard_handler.py  # Clipboard handling
    ├── config.py             # Configuration manager
    ├── main.py               # Entry point
    ├── translator.py         # Translation and Gemini API logic
    ├── tray_icon.py          # System tray icon
    ├── config.json           # Configuration file
    └── requirements.txt      # Dependencies


## Ограничения

    -   Administrative privileges are required for keyboard event handling.
    -   The Gemini API may have request limitations.
    -   X11/Wayland is required for Linux operation.

📄 License
MIT License © 2025 [anacesh]
