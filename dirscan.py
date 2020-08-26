import requests
import threading
from threading import Thread
lock = threading.Lock()

print("""
██████╗ ██╗██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██║██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
██║  ██║██║██████╔╝███████╗██║     ███████║██╔██╗ ██║
██║  ██║██║██╔══██╗╚════██║██║     ██╔══██║██║╚██╗██║
██████╔╝██║██║  ██║███████║╚██████╗██║  ██║██║ ╚████║
╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝                    
                By Raptor Root """)

print("\n---------------------------------------------")
website = input("Enter The Website Domain/IP (e.g https://google.com/): ")
wlist = input("Enter Your Wordlist Name (e.g wordlist.txt): ")

a = open(wlist, 'r').readlines()
wordlist = [s.rstrip() for s in a]
for word in wordlist:
	r = requests.get(website + word)
	if r.status_code == 200:
		lock.acquire()
		print('[+]'+ r.url + ' Found!')
		lock.release()
	elif r.status_code == 404:
		lock.acquire()
		print('[-]'+ r.url + ' Not Found!')
		lock.release()
	else:
		lock.acquire()
		print('[x]' + r.url + ' Found! Resp Code:' +  r.status_code)
		lock.release()
