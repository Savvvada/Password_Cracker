#**Savada Wilson**
##**Assignment2_Password_Cracker**

This is a small program which uses password lists to decrypt the entered hash
To run thi program one must make sure that the password list they wish to use is in the same directory as the program itself.  
Afterwards, one only needs to start the program and they will be immediately prompted to enter the hash they wish to be decrypted. It is imperative to make sure there are no whitespaces following the pasted hash.Subsequently, the program will prompt the user again for input, this time for the name of the textfile containing the passwords they wish to decrypt. The extension must be added to it. After entering the textfile name of one the many included in the directory, the program should run.The improved version, runs exactly the same with the only difference being that it uses two threads, alternating through the lines of a given text file.During the start of the threads, the improved version spits out an error, but the program will still run given approximately 7 seconds. Although the speed wasn't increased in the first problem due to the time it takes for the threads to start, I believe that in extremely larg Gigabyte sized password lists, that the multithreading would be an improvement due to it having a higher chance to result in less attempts needing to be made, and the division of tasks to dual or quad processors.

The standard version is called "etTuBruteSha1.py", the multithreaded version is called "ImprovedEtTuBruteSha1.py".


*Questions*
a.) The hash b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3 can be cracked using the directory "10_million.txt" , the un-hashed password it represents is "letmein"
