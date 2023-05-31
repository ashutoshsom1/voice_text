from translate import Translator
import speech_recognition as sr
# from gtts import gTTS
import pygame
from io import BytesIO
from gtts import gTTS
# translator= Translator(to_lang="Hindi")
# translation = translator.translate("Good Morning!")
# print (translation)

pygame.init()
pygame.mixer.init()

r = sr.Recognizer()
mic = sr.Microphone()
lang_code_google=  {
"Hindi": "hi-IN",
"Bengali": "bn-IN",
"Gujarati": "gu-IN",
"Kannada": "kn-IN",
"Malayalam": "ml-IN",
"Marathi": "mr-IN",
"Tamil": "ta-IN",
"Telugu": "te-IN"
}

lang_code_gtts = {
"Hindi": "hi",
"Bengali": "bn",
"Gujarati": "gu",
"Kannada": "kn",
"Malayalam": "ml",
"Marathi": "mr",
"Tamil": "ta",
"Telugu": "te"
}

translate_code = {
"Hindi": "hi",
"Bengali": "bn",
"Gujarati": "gu",
"Kannada": "kn",
"Malayalam": "ml",
"Marathi": "mr",
"Tamil": "ta",
"Telugu": "te"
}


lang_code = input("Enter language code (e.g. Hindi , Bengali): ")
##############################################################################################################
def recognize_speech(listen_time=15):
    lang_code_ = lang_code_google[lang_code]
    with mic as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=listen_time)
        print("Transcribing...")
    try:
        text = r.recognize_google(audio, language= lang_code_)
        print("Transcription:", text)
        return text
    except sr.UnknownValueError:
        # print("Could not understand audio")
        return "Could not understand audio"
    except sr.RequestError as e:
        # print("Could not request results; {0}".format(e))
        return "Request error"

def speak_text(text):
    with BytesIO() as file:
        lang_code1=lang_code_gtts[lang_code]
        tts = gTTS(text=text, lang=lang_code1)
        tts.write_to_fp(file)
        file.seek(0)
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)



def Translate_to_Englsih(Text__):
    lang_code__ = translate_code[lang_code] 
    translator= Translator(to_lang="en",from_lang=lang_code__)
    translated_text = translator.translate(Text__)
    print("Translated Text :", translated_text)


# example usage
def main():
    # lang_code = input("Enter language code (e.g. Hindi , Bengali): ")
    transcript = recognize_speech()
    speak_text(transcript)
    Translate_to_Englsih(transcript)
    
    
    
    
def Translate_to_Englsih(Text__):
    lang_code__ = translate_code[lang_code] 
    translator= Translator(to_lang="en",from_lang=lang_code__)
    translated_text = translator.translate(Text__)
    print("Translated Text :", translated_text)
    

   
    
    
if __name__ == "__main__":
    main()  
