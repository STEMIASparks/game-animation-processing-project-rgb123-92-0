colr = 0
colg = 0
colb = 0
siz = 50
def setup():
    fullScreen()
    size(1920,1080)
    background(0,0,0)
def draw():
    global colr,colg,colb,siz

    if(mousePressed):       
        noStroke()
        circle(mouseX,mouseY,siz)
        fill(colr,colg,colb)
    if(colr >= 255):
        colr = 0
    if(colg >= 255):
        colg = 0
    if(colb >= 255):
        colb = 0
    elif(keyPressed == True and key == 'r'):
        colr += 5
    elif(keyPressed == True and key == 'g'):
        colg += 5
    elif(keyPressed == True and key == 'b'):
        colb += 5
    if(keyPressed == True and key == '1'):
        siz = 5
    if(keyPressed == True and key == '2'):
        siz = 10
    if(keyPressed == True and key == '3'):
        siz = 20
    if(keyPressed == True and key == '4'):
        siz = 50
    if(keyPressed == True and key == '5'):
        siz = 70
    if(keyPressed == True and key == '6'):
        siz = 85
    if(keyPressed == True and key == '7'):
        siz = 100
    if(keyPressed == True and key == '8'):
        siz = 150
    if(keyPressed == True and key == '9'):
        siz = 200
    if(keyPressed == True and key == '0'):
        siz = 500
    if(keyPressed == True and key == 't'):
        img = loadImage("Eu9trp9.png")
        image(img, 0, 0, width / 1, height / 1)
    if(keyPressed == True and key == 'y'):
        img = loadImage("communityIcon_el2g3ukyrwy71.png")
        image(img, 0, 0, width / 1, height / 1)
    if(keyPressed == True and key == 'u'):
        img = loadImage("Walter-White-Breaking-Bad-PNG-Picture.png")
        image(img, 0, 0, width / 1, height / 1)
    if(keyPressed == True and key == 'i'):
        img = loadImage("ppmanbgf.png")
        image(img, 0, 0, width / 1, height / 1)
    if(keyPressed == True and key == 'o'):
        img = loadImage("Screenshot 2022-09-14 200037.png")
        image(img, 0, 0, width / 1, height / 1)
    if(keyPressed == True and key == 'p'):
        img = loadImage("Screenshot 2022-09-27 131850.png")
        image(img, 0, 0, width / 1, height / 1)
    if(keyPressed == True and key == 'w'):
        img = loadImage("pure-white-background-85a2a7fd.jpg")
        image(img, 0, 0, width / 1, height / 1)
    if(keyPressed == True and key == 'e'):
        img = loadImage("maxresdefault.jpg")
        image(img, 0, 0, width / 1, height / 1)
    if(keyPressed == True and key == ' '):
        img = loadImage("Walter-White-Breaking-Bad-PNG-Picture.png")
        image(img, mouseX, mouseY, width / 12, height / 12)
