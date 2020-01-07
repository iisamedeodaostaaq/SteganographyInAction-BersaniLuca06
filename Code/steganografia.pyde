def setup():
    global img
    size(600,400)
    img=createImage(600,400,RGB)
    creaImg()
    
    
def creaImg():
    img.loadPixels()
    
    for i in range(600*400):
        img.pixels[i]=color(random(255),random(255),random(255))
    img.updatePixels()
    
    image(img,0,0)
    
    
