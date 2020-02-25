import time
import hashlib
from threading import Thread
import itertools
import threading
hash2crack = input("Please enter the hash one wishes to be decrypted, make sure itis free of whitespaces: ")
f = input("Enter the name of the password list file youwish to use, include its extension :")
f = str(f)
match = False
tries = 0
h = hashlib
answer = "None"
class guesser(threading.Thread):

    def __init__(self, b):
        threading.Thread.__init__(self)
        self.b = b


    def run(self):
        global match
        global hash2crack
        global tries
        global answer
        global f
        with open(f, 'r') as f:
            checkList = f.readlines()
            o = 0
            for i in checkList:
                if (o % 2 == 0 ) == self.b:
                    print(i)
                    i = str(i).strip()
                    v = h.sha1(i.encode('utf-8')).hexdigest()
                    tries += 1
                    if hash2crack == v:
                        match = True
                        answer = i
                        print("Gotem!")
                        break
                o += 1
                if match:
                    return

startTime = time.time()
crackerList = []
b = False
crackerList.append(guesser(False))
crackerList.append(guesser(True))
i = 0
while i < 2:
    crackerList[i].start()
    i += 1
while not match:
    continue
endTime = time.time()
time_lapsed0 = (endTime - startTime)
time_lapsed = (endTime - startTime)/60
time_lapsed2 = time_lapsed/60
print("number of tries amount to " + str(tries))
print("the un-hashed password is " + answer)
print("the time taken to complete this was " + str(time_lapsed0) + " in seconds or " + str(time_lapsed) + " in minutes or " + str(time_lapsed2) + " in hours")