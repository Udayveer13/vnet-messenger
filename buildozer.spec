[app]
title = VNet Messenger
package.name = vnetmessenger
package.domain = org.udayveer
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,js,css,json
version = 0.1
requirements = python3,kivy,requests,cryptography
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.permissions = INTERNET, ACCESS_WIFI_STATE, CHANGE_WIFI_STATE, ACCESS_COARSE_LOCATION, ACCESS_FINE_LOCATION
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
python_version = 3.12

[buildozer]
log_level = 2
warn_on_root = 1

