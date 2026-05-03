import os
from kivy.app import App
from kivy.uix.webbrowser import WebView
from kivy.core.window import Window

class VNetApp(App):
    def build(self):
        # This tells Android to find your index.html in the same folder
        path = os.path.abspath("index.html")
        # Initialize the webview and point it to your file
        return WebView(url=f"file://{path}", enable_javascript=True, enable_hw_accel=True)

if __name__ == "__main__":
    VNetApp().run()
