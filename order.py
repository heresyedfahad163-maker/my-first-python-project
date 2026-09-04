import webbrowser
import os

# 1. Website کھولنا
website = input("کون سی ویب سائٹ کھولنی ہے؟ youtube / google / facebook: ")

if website == "youtube":
    webbrowser.open("https://www.youtube.com")
elif website == "google":
    webbrowser.open("https://www.google.com")
elif website == "facebook":
    webbrowser.open("https://www.facebook.com")

# 2. App کھولنا - Windows کے لیے
app = input("کون سی ایپ کھولنی ہے؟ notepad / calculator: ")

if app == "notepad":
    os.system("notepad")
elif app == "calculator":
    os.system("calc")