# -*- coding: cp1252 -*-
"""
import re
regex = re.compile(r"^(\d+)x(\d+)x(\d+)$")
m = regex.match("123x45x678")
if m:
    h = int(m.group(1))
"""


data=open("adventofcode2_input.txt","r")
area=0
ribbon=0
for line in data:
    curr_present=line.rstrip()
    j=0
    i=0
    length=0
    width=0
    height=0
    #Bestimmung von Länge, Breite und Höhe
    while i < len(curr_present):
        if curr_present[i] == "x":
           j += 1
           i += 1
        if j == 0:
            length=length*10+int(curr_present[i])
        if j == 1:
            width=width*10+int(curr_present[i])
        if j == 2:
            height=height*10+int(curr_present[i])
        i += 1
    #Bestimmung der kleinsten Fläche
    if length >= width:
        a=width
        if length >= height:
            b=height
        else:
            b=length
    if length < width:
        a=length
        if width >= height:
            b=height
        else:
            b=width
    #Fläche des aktuellen Geschenks dazurechnen
    area=area + a*b + 2*length*width + 2*width*height + 2*height*length
    ribbon=ribbon + 2*a + 2*b + length*width*height
print "Area:", area
print "Ribbon:", ribbon
