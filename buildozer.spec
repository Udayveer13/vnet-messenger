[app]
title = VNet Messenger
package.name = vnetmessenger
package.domain = org.udayveer
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,js,css,json
version = 0.1

# 1. Added 'openssl'—this is mandatory for 'cryptography' to work on Android
# 2. Removed cython from requirements (Buildozer handles this internally)
requirements = python3,kivy==2.3.0,requests,cryptography,openssl

orientation = portrait
fullscreen = 0

# Permissions are correct for P2P/Mesh
android.permissions = INTERNET, ACCESS_WIFI_STATE, CHANGE_WIFI_STATE, ACCESS_COARSE_LOCATION, ACCESS_FINE_LOCATION, NEARBY_WIFI_DEVICES

android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Match this exactly with the version in your GitHub Actions YAML
python_version = 3.11

[buildozer]
log_level = 2
warn_on_root = 1
