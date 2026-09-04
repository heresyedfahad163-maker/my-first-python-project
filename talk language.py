import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Optional: Adjust speech rate (speed) and volume
engine.setProperty('rate', 150)    # Speed (words per minute)
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# Queue the text to be spoken
engine.say("Hello Syed Fahad. Python chal gaya. mera naam fahad ha. Hello Syed Fahad")

# Process the speech queue
engine.runAndWait()
