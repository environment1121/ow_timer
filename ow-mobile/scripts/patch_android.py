# 안드로이드 매니페스트 보정: 가로 고정 + 음성 인식 서비스 조회 허용 + 마이크 권한
import re
p = "android/app/src/main/AndroidManifest.xml"
s = open(p, encoding="utf-8").read()
if "sensorLandscape" not in s:
    s = s.replace("<activity", '<activity android:screenOrientation="sensorLandscape"', 1)
if "RecognitionService" not in s:
    s = s.replace("<application", '<queries><intent><action android:name="android.speech.RecognitionService"/></intent></queries>\n    <application', 1)
if "RECORD_AUDIO" not in s:
    s = s.replace("</manifest>", '    <uses-permission android:name="android.permission.RECORD_AUDIO"/>\n</manifest>')
open(p, "w", encoding="utf-8").write(s)
print("manifest patched")
