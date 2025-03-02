import pygame 
pygame.init()
width=800
height=800
screen=pygame.display.set_mode((width,height))
screen.fill("black")
y=0
#macking the blueprints
class mrcircle():
    def __init__ (self,color,pos,radius,width=0):
        self.color=color
        self.radius=radius
        self.pos=pos
        self.screen=screen
        self.width=width

    def draw(self):
        pygame.draw.circle(self.screen,self.color,self.pos,self.radius,self.width)
    def bigcircle(self,y):
        self.radius+=y
        pygame.draw.circle(self.screen,self.color,self.pos,self.radius,self.width)
#creatinf the objects

bigcircle1=mrcircle("violet",(400,400),150)
bigcircle2=mrcircle("pink",(400,400),125)
bigcircle3=mrcircle("blue",(400,400),100)
bigcircle4=mrcircle("green",(400,400),75)
bigcircle5=mrcircle("yellow",(400,400),50)
bigcircle6=mrcircle("orange",(400,400),25)
bigcircle7=mrcircle("red",(400,400),10)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
       
            bigcircle1.draw()
            bigcircle2.draw()
            bigcircle3.draw()
            bigcircle4.draw()
            bigcircle5.draw()
            bigcircle6.draw()
            bigcircle7.draw()
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
           
            bigcircle1.bigcircle(10)
            bigcircle2.bigcircle(4)
            bigcircle3.bigcircle(4)
            bigcircle4.bigcircle(4)
            bigcircle5.bigcircle(4)
            bigcircle6.bigcircle(4)
            bigcircle7.bigcircle(4)
            pygame.display.update()

        elif event.type==pygame.MOUSEMOTION:
            bob=pygame.mouse.get_pos()

            whitecircle=mrcircle("white",(bob),5)
            whitecircle.draw()
            pygame.display.update()



            
    

















