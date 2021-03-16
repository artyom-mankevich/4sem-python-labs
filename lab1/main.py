import os
import hashlib
import time

for item in os.listdir(os.getcwd()):
    if os.path.isfile(item):
        with open(item, "rb") as file:
            print(item + "\t" + hashlib.sha3_256(file.read()).hexdigest(), sep='\n')
while True:
	time.sleep(5)
