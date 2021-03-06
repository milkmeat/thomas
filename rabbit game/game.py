#1
import pygame
from pygame.locals import*
import math
import random
import time
#2
shootInterval=15
shootTimer=0
badtimer=100
badtimer1=0
badguys=[]
healthvalue=194
acc=[0,0]
arrows=[]
keys=[False,False,False,False]
autoshoot=False
playerpos=[100,100]
pygame.init()
width,height=1000,750
screen=pygame.display.set_mode((width,height))
pygame.mixer.init()
#3
player=pygame.image.load("resources/images/dude.png")
grass=pygame.image.load("resources/images/grass.png")
castle=pygame.image.load("resources/images/castle.png")
arrow=pygame.image.load('resources/images/bullet.png')
badguyimg1 = pygame.image.load("resources/images/badguy.png")
healthbar = pygame.image.load("resources/images/healthbar.png")
health=pygame.image.load("resources/images/health.png")
badguyimg=badguyimg1
gameover = pygame.image.load("resources/images/gameover.png")
gameoverFull=pygame.transform.scale(gameover,(width,height))
youwin = pygame.image.load("resources/images/youwin.png")
youwinFull=pygame.transform.scale(youwin,(width,height))
#3.1
hit = pygame.mixer.Sound("resources/audio/explode.wav")
enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
shoot = pygame.mixer.Sound("resources/audio/shoot.wav") 
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)     
pygame.mixer.music.load('resources/audio/moonlight.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)
#4
running = 1
exitcode = 0
while running:
    time.sleep(0.01)
    badtimer-=1
    #5
    screen.fill([0,255,0])
    
    #6
    '''
    for x in range(width/grass.get_width()+1):
        for y in range (height/grass.get_height()+1):
            screen.blit(grass,(x*100,y*100))
    '''
    for x in range (1,5):
        screen.blit(castle,(0,height/5*x-50))

    #6.1
    position=pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)
    #6.2
    for bullet in arrows:
        velx=math.cos(bullet[0])*5
        vely=math.sin(bullet[0])*5
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            del bullet
    for projectile in arrows:
        arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
        screen.blit(arrow1, (projectile[1], projectile[2]))
    #6.3
    if badtimer==0:
        badguys.append([width, random.randint(50,height-50)])
        badtimer=100-(badtimer1*2)
        if badtimer1>=35:
            badtimer1=35
        else:
            badtimer1+=5
    
    index=0
    for badguy in badguys:
        if badguy[0]<-64:
            badguys.pop(index)
        badguy[0]-=10
        badrect=pygame.Rect(badguyimg.get_rect())
        badrect.top=badguy[1]
        badrect.left=badguy[0]
        if badrect.left<64:
            healthvalue -= random.randint(5,20)
            badguys.pop(index)
            hit.play()
           
        #6.3.2
        index1=0
        for bullet in arrows:
            bullrect=pygame.Rect(arrow.get_rect())
            bullrect.left=bullet[1]
            bullrect.top=bullet[2]
            if badrect.colliderect(bullrect):
                acc[0]+=1
                badguys.pop(index)
                arrows.pop(index1)
                enemy.play()
            index1+=1
        index+=1    
                
    for badguy in badguys:
        screen.blit(badguyimg, badguy)
    #6.4
    font=pygame.font.Font(None,24)
    survivedtext = font.render(str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[635,5]
    screen.blit(survivedtext, textRect)
    #6.5
    screen.blit(healthbar, (5,5))
    for health1 in xrange(healthvalue):
        screen.blit(health,(health1+8,8))
    #7
    pygame.display.flip()
    #8
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            autoshoot=True
        if event.type==pygame.MOUSEBUTTONUP:
            autoshoot=False
        
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False
    
    if autoshoot and shootTimer<=0:   
        position=pygame.mouse.get_pos()
        acc[1]+=1
        arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
        shoot.play()
        shootTimer=shootInterval
    shootTimer-=1
    #9
    if keys[0]:
        playerpos[1]-=5        
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5
    #10
    if pygame.time.get_ticks()>=90000:
        running=0
        exitcode=1
    if healthvalue<=0:
        running=0
        exitcode=0
    if acc[1]!=0:
        accuracy=acc[0]*1.0/acc[1]*100
    else:
        accuracy=0
        
#11
if exitcode==0:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (255,0,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(gameoverFull, (0,0))
    screen.blit(text, textRect)
else:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (0,255,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(youwinFull, (0,0))
    screen.blit(text, textRect)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
