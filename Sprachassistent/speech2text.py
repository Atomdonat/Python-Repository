import speech_recognition as sr

def input_listen(ausgabe):
    spr = sr.Recognizer()
    with sr.Microphone() as micro:
        print(ausgabe)
        audio = spr.listen(micro)
        print("ich verarbeite...")
        text = spr.recognize_google(audio, language="de-DE")
        text = text.lower().replace("ä","ae").replace("ö","oe").replace("ü","ue")
        print(text)
        return text

    
