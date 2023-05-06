#Import the required module for text   
from gtts import gTTS

#The file you want to convert
print("Enter the Specific Path of a file or the name of the file you want to convert into speech:")
filename = input()
print("Enter the name of the file you want to store:")
#The name of the output file 
MP3File=input()
with open(f'{filename}', 'r') as myFile:
    fileRead = myFile.read()

#passing file and language to the engine
myObj = gTTS(text = fileRead, lang = 'en', slow =False)
myObj.save(f'{MP3File}')