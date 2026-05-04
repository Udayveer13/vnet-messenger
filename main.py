import os
from kivy.app import App
from kivy.uix.modalview import ModalView
from android.runnable import run_on_ui_thread

# This bridges Python to the Android System WebView
from jnius import autoclass

WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
PythonActivity = autoclass('org.kivy.android.PythonActivity')

class VNetApp(App):
    def build(self):
        # We start the WebView on the Android UI thread
        self.create_webview()
        # Return an empty view while the webview loads over it
        return ModalView()

    @run_on_ui_thread
    def create_webview(self):
        activity = PythonActivity.mActivity
        webview = WebView(activity)
        webview.getSettings().setJavaScriptEnabled(True)
        webview.getSettings().setDomStorageEnabled(True) # Vital for contact saving
        webview.getSettings().setAllowFileAccess(True)
        webview.setWebViewClient(WebViewClient())
        
        # Absolute path to your local HTML file
        path = os.path.join(os.getcwd(), "index.html")
        webview.loadUrl(f"file://{path}")
        activity.setContentView(webview)

if __name__ == "__main__":
    VNetApp().run()
