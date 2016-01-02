"""
besucht= dict()
besucht[0]=[0]
x=0
y=0
counter=1
with open("adventofcode3_input.txt","r") as data:
    befehle=data.read().strip()
for char in befehle:
    if char == ">":
        x += 1
    elif char == "<":
        x -= 1
    elif char == "^":
        y += 1
    else:
        y -= 1
    if x not in besucht:
        besucht[x] = [y]
        counter += 1
        continue
    elif y not in besucht[x]:
        besucht[x].append(y)
        counter += 1
        continue
print(counter)
"""

vis=[(0,0)]
counter=1
x=0
y=0
with open ("adventofcode3_input.txt","r") as data:
    befehle=data.read().strip()
for char in befehle:
    if char == ">":
        x += 1
    elif char == "<":
        x -= 1
    elif char == "^":
        y += 1
    else:
        y -= 1
    if (x,y) not in vis:
        vis.append((x,y))
        counter += 1
print counter


#Teil 2

vis=[(0,0)]
counter=1
x=[0,0]
y=[0,0]
j=0
with open ("adventofcode3_input.txt","r") as data:
    befehle=data.read().strip()
for char in befehle:
    if char == ">":
        x[j] += 1
    elif char == "<":
        x[j] -= 1
    elif char == "^":
        y[j] += 1
    else:
        y[j] -= 1
    if (x[j],y[j]) not in vis:
        vis.append((x[j],y[j]))
        counter += 1
    if j == 0:
        j=1
    else:
        j=0
print counter  
