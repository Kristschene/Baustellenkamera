import os
import glob
import ntpath
import time

# Define sleep time constant
CONST_SLEEP_TIME = 3600 # take picture every 1 hour

# When Startup --> check which photo was latest
var = 0
pics = glob.glob('/home/pi/Desktop/Baustelle/pics/*.jpg')

for pic in pics:
	filename, extension = os.path.splitext(pic)
	filename = ntpath.basename(filename)
	#print(int(filename))
	if int(filename) > var:
		var = int(filename)

if not pics:
	piccounter = 0
else:
	piccounter = var + 1


# Infinite loop -> Take picture and store it correctly
infinite = 1
while infinite  == 1:
	command = "raspistill -o /home/pi/Desktop/Baustelle/pics/{}.jpg".format(piccounter)
	os.popen(command)
	piccounter += 1
	time.sleep(CONST_SLEEP_TIME)
