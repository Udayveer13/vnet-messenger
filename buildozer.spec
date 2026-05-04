[app]
title = VNet Messenger
package.name = vnetmessenger
package.domain = org.udayveer
source.dir = .
[span_2](start_span)source.include_exts = py,png,jpg,kv,atlas,html,js,css,json,json[span_2](end_span)
version = 0.1

# Added 'android' and 'pyjnius' for the Native WebView bridge
requirements = python3,kivy==2.3.0,requests,cryptography,openssl,android,pyjnius

orientation = portrait
fullscreen = 0

# Mesh/P2P Permissions
android.permissions = INTERNET, ACCESS_WIFI_STATE, CHANGE_WIFI_STATE, ACCESS_COARSE_LOCATION, ACCESS_FINE_LOCATION, NEARBY_WIFI_DEVICES

android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

python_version = 3.11

[buildozer]
log_level = 2
warn_on_root = 1
