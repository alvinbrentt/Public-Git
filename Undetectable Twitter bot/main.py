from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"

        return MDLabel(text="Hello, world!", halign="center")
    

if __name__ == "__main__":
    MainApp().run()