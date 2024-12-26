from gtts import gTTS # we have imported this module for text to speech conversion
import os
 
abc = open('fiel/path/filename.txt') # add file name which you have to convert
text = abc.read() # text that you want to convert
 
language = 'en' # en is for english language
 
obj = gTTS(text = text, Lang=language, slow = False)
 
#we have used slow False because our converted video will have a high speed
obj.save("sample.mp3")
 
#to open the video file automatically we have to import os
os.system("sample.mp3")
