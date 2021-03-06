import pygame
import BinLib
from PIL import Image
import time
from threading import Thread

RAM = [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]

"""
RAM for screen
Memory mapped each cell is one row of pixels
"""

buffer = Image.new("RGB",(16,16),"black")
running = True    
ports = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0}
def screen():
    global buffer
    global running
    pygame.init()

    screen = pygame.display.set_mode((640,640))
    while running:
        for x in xrange(16):
        # print RAM[x],ram.read(RAM[x])
            q = BinLib.toTwoComp(ports[x])

            for y in xrange(16):
                buffer.putpixel((y, x), (255 * int(q[y]), 255 * int(q[y]), 255 * int(q[y])))
        t = buffer.resize((640,640)).tobytes()
        img=pygame.image.frombuffer(t,(640,640),"RGB")
        screen.blit(img,(0,0))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
    

class MemMappedScreen:
    def __init__(self):
        self.TickTime = 0
        self.currentTick = 0
        self.screenThread = Thread(target=screen)
        self.screenThread.start()
        print("Initalizing pygame.")
        time.sleep(.5)
    def tick(self,ram,prom):
        global ports
        ports = ram.data
       
        if not running:
            exit()
    def CleanUp(self):
        pass