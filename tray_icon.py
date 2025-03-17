from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw
import os
import threading
from config import config, debug_print

ICON_PATH = config.get("icon_path", "assets/icon.png")


class TrayIcon:
    def __init__(self):
        self.tray_icon = Icon("translator")
        self.tray_icon.icon = self._load_icon()
        self.tray_icon.menu = Menu(
            MenuItem("Exit", self.exit_app)
        )

    def _load_icon(self):
        if os.path.exists(ICON_PATH):
            debug_print(f"Загружаем иконку из {ICON_PATH}")
            return Image.open(ICON_PATH)

        debug_print("Иконка не найдена, создаём стандартную...")
        return self._generate_default_icon()

    def _generate_default_icon(self):
        icon_size = (64, 64)
        image = Image.new("RGB", icon_size, (0, 128, 255))
        draw = ImageDraw.Draw(image)
        draw.rectangle([16, 16, 48, 48], outline="white", width=3)
        return image

    def exit_app(self, icon, item):
        self.tray_icon.stop()
        os._exit(0)

    def run(self):
        self.tray_icon.run()


def start_tray_icon():
    tray = TrayIcon()
    thread = threading.Thread(target=tray.run, daemon=True)
    thread.start()
