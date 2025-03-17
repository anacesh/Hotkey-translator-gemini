from clipboard_handler import start_hotkey_listener
from tray_icon import start_tray_icon

if __name__ == "__main__":
    start_hotkey_listener()
    start_tray_icon()
    input()