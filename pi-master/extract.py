#Tesseract works best on images which have a DPI of at least 300 dpi, so it may be beneficial to resize images.

from PIL import Image
import sys
import pytesseract
import pygame
from gtts import gTTS
 
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("output.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
#out=[]    

if len(sys.argv) != 2:
    print ("%s input_file output_file" % (sys.argv[0]))
    sys.exit()
else:
    text=pytesseract.image_to_string(Image.open(sys.argv[1]))
    '''   for ch in text:
        if ch in "abcdefghijklmnopqrstuvwxyz" or "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or "1234567890" or '@':
            out.append(ch)
    '''     
    #print (text)
    #print (out)
    speak(text)
