import os
from kivy.app import App
from kivy.uix.modalview import ModalView
from android.runnable import run_on_ui_thread

# The Bridge: This connects Python to the Android System WebView
from jnius import autoclass

WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
PythonActivity = autoclass('org.kivy.android.PythonActivity')

class VNetApp(App):
    def build(self):
        # We start the WebView on the Android UI thread for performance
        self.create_webview()
        # Return an empty view while the webview loads over it
        return ModalView()

    @run_on_ui_thread
    def create_webview(self):
        activity = PythonActivity.mActivity
        webview = WebView(activity)
        
        # Essential settings for VNet's Mesh/PeerJS logic
        webview.getSettings().setJavaScriptEnabled(True)
        webview.getSettings().setDomStorageEnabled(True)  # Saves your contacts
        webview.getSettings().setAllowFileAccess(True)
        webview.getSettings().setAllowContentAccess(True)
        
        # Prevents links from opening in an external browser
        webview.setWebViewClient(WebViewClient())
        
        # Locate your index.html inside the packaged APK
        path = os.path.join(os.getcwd(), "index.html")
        webview.loadUrl(f"file://{path}")
        
        # Set the WebView as the primary screen
        activity.setContentView(webview)

if __name__ == "__main__":
    VNetApp().run()
