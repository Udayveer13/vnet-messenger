[app]

# (str) Title of your application
title = VNet Messenger

# (str) Package name
package.name = vnetmessenger

# (str) Package domain (needed for android packaging)
package.domain = org.udayveer

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let's make sure json and html are included)
source.include_exts = py,png,jpg,kv,atlas,html,js,css,json

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Added 'android' and 'pyjnius' so your main.py can talk to the System WebView
requirements = python3,kivy==2.3.0,requests,cryptography,openssl,android,pyjnius

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# These are essential for PeerJS and local network mesh discovery
android.permissions = INTERNET, ACCESS_WIFI_STATE, CHANGE_WIFI_STATE, ACCESS_COARSE_LOCATION, ACCESS_FINE_LOCATION, NEARBY_WIFI_DEVICES

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android NDK API to use. This is the minimum API your app will support.
android.ndk_api = 21

# (list) Architecture to build for (v8a is for modern 64-bit phones)
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup
android.allow_backup = True

# (str) The Python version to use for the build
python_version = 3.11

# (bool) If True, then skip trying to update the libs
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only.
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
