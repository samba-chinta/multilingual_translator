from deep_translator import GoogleTranslator
import speech_recognition as sr
from gtts import gTTS
import os 

class LangTranslator:
  def __init__(self, target_lang):
    self.r = sr.Recognizer()
    self.text = ''
    self.target_lang = target_lang
    self.audio = None
    self.translated = ''
  
  def takeInputText(self):
    with sr.Microphone() as source:
      print("Say something: ")
      self.audio = self.r.listen(source)
      self.text = self.getTextFormatOfAudio()
  
  def getTextFormatOfAudio(self):
    try:
      return self.r.recognize_google(self.audio)
    except sr.UnknownValueError:
      print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
      print("Could not request results; {0}".format(e))
  
  def getTranslatedText(self):
    self.translated = GoogleTranslator(source='auto', target=self.target_lang).translate(self.text)

  def getTranslatedAudio(self):
    myobj = gTTS(self.translated, lang = self.target_lang)
    return myobj

target_lang = input("Enter the Target Language: ")
langTransObj = LangTranslator(target_lang)

langTransObj.takeInputText()
langTransObj.getTranslatedText()

audioObj = langTransObj.getTranslatedAudio()

audioObj.save('myAudio.mp3')
os.system("start myAudio.mp3")