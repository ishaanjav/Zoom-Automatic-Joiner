import webbrowser, sys, setup
from datetime import datetime
from time import sleep

links = setup.links
names = setup.names
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
waitTime = (int) ((startTime - orig).total_seconds()) - 4
hours = int(waitTime / 3600)
minutes = int((waitTime - 3600 * hours) / 60)
seconds = waitTime % 60

print("Joining ", end = '')
if len(names) > idx and names[idx] != ("name " + str(idx + 1)):
	print(names[idx], end = '')
print(" in ", end='')
if hours != 0:
	print(hours, "hrs ", end = '')
if minutes != 0:
	print(minutes, "min ", end = '')
if seconds != 0:
	print(seconds, "sec ", end = '')

print()

sleep(waitTime)
join(links[idx][0])