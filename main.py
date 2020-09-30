import speech_recognition as sr
import keyboard  
from time import sleep
from winsound import Beep
import subprocess
import os
import webbrowser
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math


# Initialize
r = sr.Recognizer()
mic = sr.Microphone()
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
currentVolumeDb = volume.GetMasterVolumeLevel()

		
def main():
	with mic as source:
		r.adjust_for_ambient_noise(source)
		print("BEEEEP")
		Beep(500,100)
		Beep(500,100)
		Beep(300,100)
		Beep(700,100)
		while True:
			try:
				print("waiting for keyboard")
				keyboard.wait('ctrl+shift+space')
				sleep(0.2)
				Beep(1000,200)
				mute_volume()
				sleep(0.2)
				audio = r.listen(source)
				command = r.recognize_google(audio)
				restore_volume()
				execute(command)
			except sr.UnknownValueError:
				print("ERROR")
				restore_volume()
				Beep(300,1000)
				
def execute(command):
	print(command)
	if command == "signal":
		subprocess.Popen(['C:\\Users\\axano1\\AppData\\Local\\Programs\\signal-desktop\\Signal.exe'],  creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP)
	elif (command == "Facebook"):
		webbrowser.open_new_tab("https://facebook.com")
	elif (command == "news" or command == "News"):
		webbrowser.open_new_tab("http://vps594237.ovh.net/news/avrakataavra.php")
		webbrowser.open_new_tab("https://coinmarketcap.com/")		
	elif (command == "trance"):
		webbrowser.open_new_tab("https://www.youtube.com/watch?v=6n4m_KPMQU4&list=PLbb13Pg0p3XkfTCi8KY_9NxW6Rr-BE8K8&index=1")
	elif (command == "mail"):
		webbrowser.open_new_tab("https://outlook.office.com/owa/?realm=ordina.be&path=/mail/sentitems")
	elif (command == "Messenger"):
		webbrowser.open_new_tab("https://www.messenger.com")
	elif command == "game":
		subprocess.Popen(['C:\\gog games\\Kingdom Come Deliverance\\bin\Win64\\KingdomCome.exe'],  creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP)
	else:
		print("Command not recognized")
		Beep(300,1000)
		
def mute_volume():
	print("Muting")
	global currentVolumeDb
	currentVolumeDb = volume.GetMasterVolumeLevel()
	volume.SetMasterVolumeLevel(-65.25, None)
	
def restore_volume():
	print("Restoring")
	global currentVolumeDb
	global volume
	volume.SetMasterVolumeLevel(currentVolumeDb, None)

main()