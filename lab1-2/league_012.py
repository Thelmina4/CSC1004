#!/usr/bin/env python3

# s/i = lines of a football leage.

# s/o = fancy format

import sys
posm, clubm, pm, wm, dm, lam, gfm, gam, gdm, ptsm = "POS", "CLUB", "P", "W", "D", "L", "GF", "GA", "GD", "PTS"
lines = sys.stdin.readlines()

maxl = 0
for line in lines:
   line = line.strip().split()
   line, stats = line[:len(line) - 8], line[len(line) - 8:]
   club = " ".join(line[1:])
   if maxl < len(club):
      maxl = len(club)

# print(maxl)

print("POS", f"{clubm:<{maxl:d}s}"f"{pm:>3s}", f"{wm:>3s}", f"{dm:>3s}", f"{lam:>3s}", f"{gfm:>3s}", f"{gam:>3s}", f"{gdm:>3s}", f"{ptsm:>3s}")

for line in lines:
   line = line.strip().split()
   line0, line, stats = [line[0]], line[:len(line) - 8], line[len(line) - 8:]
   club = [" ".join(line[1:])]
   # print(club, stats)
   line = line0 + club + stats
   # print(line)
   pos, club, p, w, d, la, gf, ga, gd, pts = line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9]
   # print(pos, club, p, w, d, la, gf, ga, gd, pts)
   print(f"{pos:>3s}", f"{club:<{(maxl):d}s}"f"{p:>3s}", f"{w:>3s}", f"{d:>3s}", f"{la:>3s}", f"{gf:>3s}", f"{ga:>3s}", f"{gd:>3s}", f"{pts:>3s}")
