catx = []
caty = []
speedx = []
speedy = []
catCount = 0

def setup():
    size(600, 600)
    
def draw():
    global catx, caty, speed
    background(0)
    
    # show()
    for i in range(len(catx)):
        if(i % 3 == 0):
            fill(255)
            circle(catx[i], caty[i], 30)
        elif(i % 3 == 1):
            fill(255, 0 , 0)
            circle(catx[i], caty[i], 30)
    # update 
    for i in range(len(catx)):
        if(i % 3 == 0):
            catx[i] += speedx[i]
        elif(i % 3 == 1):
            caty[i] +=speedy[i]
        
    # boundary checking
    for i in range(len(catx)):
        if(i % 3 == 0):
            if (catx[i] < 0 or catx[i] > width):
                speedx[i] *= -1
        elif(i % 3 == 1):
            if (caty[i] < 0 or caty[i] > height):
                speedy[i] *= -1
            
def mousePressed():
   catx.append(mouseX)
   global catCount
   caty.append(mouseY)
   speedx.append(1)
   speedy.append(1)
   catCount += 1
   print(catCount)
