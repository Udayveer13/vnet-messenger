[app]
title = VNet Messenger
package.name = vnetmessenger
package.domain = org.udayveer
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,js,css,json
version = 0.1

# Added 'cython' and 'setuptools' to requirements to ensure the build doesn't fail
requirements = python3,kivy==2.3.0,requests,cryptography,cython==0.29.33,setuptools

orientation = portrait
fullscreen = 0

# Permissions needed for P2P/Mesh
android.permissions = INTERNET, ACCESS_WIFI_STATE, CHANGE_WIFI_STATE, ACCESS_COARSE_LOCATION, ACCESS_FINE_LOCATION, NEARBY_WIFI_DEVICES

# API 33 is the sweet spot for modern Android builds on GitHub Actions
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Matches the Python version in your build.yml
python_version = 3.12

[buildozer]
log_level = 2
warn_on_root = 1
