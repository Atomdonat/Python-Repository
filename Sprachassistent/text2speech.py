import play_audio as play
from gtts import gTTS

def output_speak(text):
    tts = gTTS(text=text, lang="de")
    text = text.lower().replace(" ", "").replace("ä","ae").replace("ö","oe").replace("ü","ue")
    filename = str(text[0:20]+ ".mp3")
    tts.save(filename)
    play.audio(filename)

# output_speak("Guten Abend meine Damen und Herren ich begrueße Sie")