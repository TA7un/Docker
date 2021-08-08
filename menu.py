import pyttsx3
import pyaudio
import webbrowser
import speech_recognition as sr
engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
engine.setProperty('rate', 180)     # setting up new voice rate


#"""VOLUME"""
#volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print (volume)                          #printing current volume level
#engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
pyttsx3.speak("I am your virtual assistant")
pyttsx3.speak("\t\t\t How can i help you...?")
while True:
	print("Tell me what can i do for you :" , end='')
	r = sr.Recognizer()
	with sr.Microphone() as source :
		print("start saying...")
		audio = r.listen(source)
		print("please wait...")
	p = r.recognize_google(audio)
	print(p)
	if (("run" in p) or ("create" in p) or ("open" in p)) and (("docker" in p) or ("container" in p)):
		pyttsx3.speak("Please wait ")
		webbrowser.open("http://192.168.43.223/drun.html")
	elif (("stop" in p) or ("terminate" in p) or ("quit" in p)) and (("docker" in p) or ("container" in p)):
		pyttsx3.speak("Please wait ")
		webbrowser.open("http://192.168.43.223/dstop.html")

		break
	else:
		print("sorry this command is not availabe please try again")
		pyttsx3.speak("sorry sir this command is not availabe please try again")