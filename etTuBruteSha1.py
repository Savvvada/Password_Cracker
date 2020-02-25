import time
import hashlib
import itertools
import threading
hash2crack = input("Please enter the hash one wishes to be decrypted, make sure itis free of whitespaces: ")
f = input("Enter the name of the password list file youwish to use, include its extension :")
match = False
tries = 0
h = hashlib
answer = "None"
def crack(f):
    global match
    global hash2crack
    global tries
    global answer
    print("here1")
    with open(f, 'r') as f:
        checkList = f.readlines()
        i = 0
        for i in checkList:
            print(i)
            i = str(i).strip()
            v = h.sha1(i.encode('utf-8')).hexdigest()
            tries += 1
            if match:
                return
            #print(v)
            if hash2crack == v:
                match = True
                answer = i
                print("Gotem!")
                break

startTime = time.time()
crack(f)
endTime = time.time()
time_lapsed0 = (endTime - startTime)
time_lapsed = (endTime - startTime)/60
time_lapsed2 = time_lapsed/60
print("number of tries amount to " + str(tries))
print("the un-hashed password is " + answer)
print("the time taken to complete this was " + str(time_lapsed0) + " in seconds or " + str(time_lapsed) + " in minutes or " + str(time_lapsed2) + " in hours")