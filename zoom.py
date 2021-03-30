import webbrowser, sys, setup
from datetime import datetime
from time import sleep

links = setup.links
if (len(links) == 0):
	print("No links provided")
	quit()

def join(lnk):
	webbrowser.open_new_tab(lnk)

idx = 0
found = False
orig = datetime.now()
now = orig.strftime("%H:%M:%S")

# find the zoom link that will have to be joined next
for i in range(len(links)):
	idx = i
	if(links[i][1] > now):
		found = True
		break

if(not found):
	print("No links to join")
	quit()

startTime = datetime.strptime(links[idx][1], "%H:%M:%S")
startTime = startTime.replace(year=orig.year, month=orig.month, day=orig.day)

# Difference in seconds between time to join and current time
waitTime = (int) ((startTime - orig).total_seconds()) - 5
print("Waiting: ", waitTime, "seconds")

sleep(waitTime)
join(links[idx][0])