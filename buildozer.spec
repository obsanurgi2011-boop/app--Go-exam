[app]
title = ExamSystem
package.name = examsystem
package.domain = org.gamachu

source.dir = .
source.include_exts = py,kv,png,jpg,json

version = 1.0

requirements = python3,kivy,reportlab

orientation = portrait

android.api = 33
android.minapi = 21
android.archs = arm64-v8a,armeabi-v7a

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
