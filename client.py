import requests
import json
import time
import subprocess

link = 'http://localhost:5000/time'
currTime = time.time()
r = requests.get(link)
afterTime = time.time()
elapsedTime = afterTime - currTime
timeAdjusted = elapsedTime / 2
print( " That took " + str(elapsedTime) + " secs")
data = json.loads(r.text)
print(data['time'])
finalTime = data['time'] + timeAdjusted 
print(" Ajusted new time for RTT " + str(finalTime))
subprocess.call("sudo gdate -s '@" + str(finalTime) +"'" , shell=True)
print("DONE")
