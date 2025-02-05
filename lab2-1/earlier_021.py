#!/usr/bin/env python3

# s/i = one + LINES OF TXT FROM STDIN
#      the lines are in 24hr format eg 15:03

# s/o = the time 47 mins earlier

import sys

# def minus(hour, mins):
# 	# deal w mins first
# 	mins = int(mins)
# 	hour = int(hour)
# 	if mins - 47 < 0:
# 		newmins = 60 + mins - 47
# 		newhour = hour - 1
# 	else:
# 		newmins = mins - 47
# 		newhour = hour
# 	return(newhour, )

for lines in sys.stdin:
	hour, mins = lines.strip().split(":")
	mins = int(mins)
	hour = int(hour)
	if mins - 47 < 0:
		newmins = 60 + mins - 47
		if hour == 0:
			newhour = "23:"
		else:
			newhour = str(hour - 1) + ":"

	else:
		newmins = mins - 47
		newhour = str(hour) + ":"
	print(f"{newhour:0>3s}"f"{newmins:0>2d}")