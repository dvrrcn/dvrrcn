##
##  Project 3: Ship Rekt!
##  Darren Cronover
##  ITCS 1950
##  May 2 2021
##
####################

import pygame, random, sys, time
from pygame.locals import *
           
class Characters(object):
    
    def __init__(self, role):
        self.role = role
        self.MOVESPEED = 4
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False

        if self.role == 'user':
            self.x, self.y = 200, 375
            self.baseRect = pygame.Rect(self.x, self.y, 50, 50)
            self.image = pygame.image.load('blue_pirate.png')

        elif self.role == 'drunk':
            self.image = pygame.image.load('drunkard.png')
            self.baseRect = pygame.Rect(350, 100, 50, 50)
            self.correct = pygame.image.load('drunk1.png')
            self.gift = pygame.image.load('drunk5.png')
            riddleList = ['drunk2.png', 'drunk3.png', 'drunk4.png']
            self.riddleChoice = random.choice(riddleList)
            self.riddle = pygame.image.load(self.riddleChoice)
            
        elif self.role == 'crew':
            self.image = pygame.image.load('crewmate.png')
            self.textbox1 = pygame.image.load('crewmatetext1.png')
            self.textbox2 = pygame.image.load('crewmatetext2.png')
            self.textbox3 = pygame.image.load('crewmatetext3.png')
            self.fitTextbox1 = pygame.transform.scale(self.textbox1, (450, 90))
            self.fitTextbox2 = pygame.transform.scale(self.textbox2, (450, 90))
            self.fitTextbox3 = pygame.transform.scale(self.textbox3, (300, 60))

            self.baseRect = pygame.Rect(400, 225, 50, 50)
            
        self.fitImage = pygame.transform.scale(self.image, (60, 60))

    def movement(self, event, SCR_HEI, SCR_WID, status):
        if status == 1:
            if event.type == KEYDOWN:
                # Change the keyboard variables.
                if event.key == K_LEFT or event.key == K_a:
                    self.moveRight = False
                    self.moveLeft = True
                if event.key == K_RIGHT or event.key == K_d:
                    self.moveLeft = False
                    self. moveRight = True
                if event.key == K_UP or event.key == K_w:
                    self.moveDown = False
                    self.moveUp = True
                if event.key == K_DOWN or event.key == K_s:
                    self.moveUp = False
                    self.moveDown = True              
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_LEFT or event.key == K_a:
                    self.moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    self.moveRight = False
                if event.key == K_UP or event.key == K_w:
                    self.moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    self.moveDown = False
                    
        if status == 2: # this block needs to run after the background is drawn, hence the status conditional
            if self.moveDown and self.baseRect.bottom < SCR_HEI:
                self.baseRect.top += self.MOVESPEED
            if self.moveUp and self.baseRect.top > 0:
                self.baseRect.top -= self.MOVESPEED
            if self.moveLeft and self.baseRect.left > 0:
                self.baseRect.left -= self.MOVESPEED
            if self.moveRight and self.baseRect.right < SCR_WID:
                self.baseRect.right += self.MOVESPEED
                     
    def draw(self, screen):
        screen.blit(self.fitImage, self.baseRect)

class Deck(object):
    
    def __init__(self, deck):
        if deck == 'maindeck':
            self.bg = 'main_deck.png'
            self.boundary01 = pygame.Rect(345, 420, 15, 50)
            self.boundary02 = pygame.Rect(0, 0, 110, 750)
            self.boundary03 = pygame.Rect(467, 0, 550, 750)
            self.boundary04 = pygame.Rect(0, 0, 550, 135)
            self.boundary05 = pygame.Rect(0, 550, 750, 550)
        if deck == 'belowdeck':
            self.bg = 'below_deck.png'
            self.boundary01 = pygame.Rect(130, 110, 25, 50)
            self.boundary02 = pygame.Rect(350, 180, 25, 25)
            self.boundary03 = pygame.Rect(0, 0, 80, 750)
            self.boundary04 = pygame.Rect(467, 0, 550, 750)
            self.boundary05 = pygame.Rect(0, 0,  550, 110)
            self.boundary06 = pygame.Rect (0, 500, 550, 750)
            self.boundary07 = pygame.Rect(450, 400, 500, 460)
            
        if deck == 'flooded':
            self.bg = 'flooded.png'
            self.boundary01 = pygame.Rect(385, 170, 15, 110)
            self.boundary02 = pygame.Rect(525, 120, 5, 5)
            self.boundary03 = pygame.Rect(75, 45, 150, 50)

        if deck == 'victory':
            self.bg = 'victory.png'

        if deck == 'capsized':
            self.bg = 'capsized.png'
            
        self.location = pygame.image.load(self.bg)
        
    def draw(self, screen):
        screen.blit(self.location, (0,0))
                    
def main():
    
    pygame.init()
    mainClock = pygame.time.Clock()
    GAMELENGTH = 90



    SCR_WID, SCR_HEI = 550, 750
    screen = pygame.display.set_mode((SCR_WID, SCR_HEI), 0, 32)
    pygame.display.set_caption('ShipRekt!')
    pygame.mixer.music.load('bg_music.wav')
    pygame.mixer.music.play(-1,0.0)
    transition = pygame.mixer.Sound('transition.ogg')

    player1 = Characters('user')
    drunkard = Characters('drunk')
    drunkard2 = Characters('drunk')
    crewmate1 = Characters('crew')
    crewmate2 = Characters('crew')
    crewmate3 = Characters('crew')
    main_deck = Deck('maindeck')
    below_deck = Deck('belowdeck')
    flooded_deck = Deck('flooded')
    victory_deck = Deck('victory')
    capsized_deck = Deck('capsized')
    introtext = pygame.image.load('introtext1.png')
    crashtext = pygame.image.load('introcrash.png')
    inventory = pygame.image.load('emptyinv.png')
    nailsFound = pygame.image.load('foundnail.png')
    woodFound = pygame.image.load('foundwood.png')
    congrats = pygame.image.load('holerepair.png')
    thanks = pygame.image.load('thanks.png')
    failure = pygame.image.load('failure.png')
    
    stage = 0
    
    
    riddleAnswered = False
    barrelSearched = False
    froggy = False
    timeLeft = pygame.time.get_ticks()
    
    while True:
        seconds = (pygame.time.get_ticks() - timeLeft)/1000 #calculate the seconds (get tickes returns in milliseconds)
        for event in pygame.event.get():
            if event.type == QUIT:
                print('Game exited by player')
                pygame.quit()
                sys.exit()
            player1.movement(event, SCR_HEI, SCR_WID, 1)
        screen.fill((0,0,0))
        if seconds > GAMELENGTH:
            if not froggy and not barrelSearched and not riddleAnswered:
                stage = 7
            
        if stage == 0: # intro
            main_deck.draw(screen)
            player1.draw(screen)
            screen.blit(introtext, (0,0))
            pygame.display.update()
            time.sleep(5)
            screen.blit(crashtext, (0,0))
            pygame.display.update()
            time.sleep(3)
            stage = 1

        if stage == 1: # instruction
            main_deck.draw(screen)
            crewmate2.draw(screen)
            player1.draw(screen)
            screen.blit(crewmate2.fitTextbox1, (50, 100))
            pygame.display.update()
            time.sleep(6)
            screen.blit(crewmate2.fitTextbox2, (50, 100))
            pygame.display.update()
            time.sleep(3)
            
            stage = 2
                    
        if stage == 2: # maindeck
            player1.movement(event, SCR_HEI, SCR_WID, 2)
            main_deck.draw(screen)
            crewmate2.draw(screen)
            drunkard.draw(screen)
            player1.draw(screen)
            screen.blit(inventory, (SCR_WID-151, 0))
            if pygame.Rect.colliderect(player1.baseRect, main_deck.boundary02):
                player1.baseRect.left += player1.MOVESPEED
            if pygame.Rect.colliderect(player1.baseRect, main_deck.boundary03):
                player1.baseRect.left -= player1.MOVESPEED
            if pygame.Rect.colliderect(player1.baseRect, main_deck.boundary04):
                player1.baseRect.top += player1.MOVESPEED
            if pygame.Rect.colliderect(player1.baseRect, main_deck.boundary05):
                player1.baseRect.top -= player1.MOVESPEED
            
            if pygame.Rect.colliderect(player1.baseRect, drunkard.baseRect):
                if riddleAnswered == False:
                    stage = 5
            if pygame.Rect.colliderect(player1.baseRect, main_deck.boundary01):
                player1.baseRect.update(130, 200, 50, 50)
                stage = 3
                transition.play()
                
        if stage == 3: # under-deck with barrel
            SCR_WID, SCR_HEI = 550, 750
            screen = pygame.display.set_mode((SCR_WID, SCR_HEI), 0, 32)
            pygame.display.set_caption('ShipRekt!')
            crewmate3.baseRect.update(140, 475, 50, 50)
            below_deck.draw(screen)
            player1.movement(event, SCR_HEI, SCR_WID, 2)
            crewmate1.draw(screen)
            crewmate3.draw(screen)
            player1.draw(screen)
            screen.blit(inventory, (SCR_WID-151, 0))
            if barrelSearched == False:
                screen.blit(crewmate1.fitTextbox3, (200, 500))
            if pygame.Rect.colliderect(player1.baseRect, below_deck.boundary03):
                player1.baseRect.left += player1.MOVESPEED
            if pygame.Rect.colliderect(player1.baseRect, below_deck.boundary04):
                player1.baseRect.left -= player1.MOVESPEED
            if pygame.Rect.colliderect(player1.baseRect, below_deck.boundary05):
                player1.baseRect.top += player1.MOVESPEED
            if pygame.Rect.colliderect(player1.baseRect, below_deck.boundary06):
                player1.baseRect.top -= player1.MOVESPEED
            
            if pygame.Rect.colliderect(player1.baseRect, below_deck.boundary01):
                player1.baseRect.update(390,520, 50, 50)
                stage = 2
            if pygame.Rect.colliderect(player1.baseRect, below_deck.boundary02):
                player1.baseRect.update(300, 260, 50, 50)
                transition.play()
                stage = 4
            if pygame.Rect.colliderect(player1.baseRect, below_deck.boundary07):
                if barrelSearched == False:
                    if froggy == False:
                        if riddleAnswered == True:
                            inventory = pygame.image.load('invhn.png')
                        elif riddleAnswered == False:
                            inventory = pygame.image.load('invnails.png')
                    elif froggy == True:
                        if riddleAnswered == False:
                            inventory = pygame.image.load('invwn.png')
                        elif riddleAnswered == True:
                            inventory = pygame.image.load('fullinv.png')
                            
                    barrelSearched = True
                screen.blit(nailsFound, (0,0))
                

        if stage == 4: # flooded portion
            SCR_WID, SCR_HEI = 600, 480
            screen = pygame.display.set_mode((SCR_WID, SCR_HEI), 0, 32)
            pygame.display.set_caption('ShipRekt!')
            flooded_deck.draw(screen)
            player1.movement(event, SCR_HEI, SCR_WID, 2)
            player1.draw(screen)
            screen.blit(inventory, ((SCR_WID - 151, 0)))
            if pygame.Rect.colliderect(player1.baseRect, flooded_deck.boundary02):
                screen.blit(woodFound, (0,0))
                if froggy == False:
                    if barrelSearched:
                        if riddleAnswered:
                            inventory = pygame.image.load('fullinv.png')
                        else:
                            inventory = pygame.image.load('invwn.png')
                    else:
                        if riddleAnswered:
                            inventory = pygame.image.load('invwh.png')
                        else:
                            inventory = pygame.image.load('invwood.png')
                    froggy = True
            if pygame.Rect.colliderect(player1.baseRect, flooded_deck.boundary01) :
                player1.baseRect.update(325, 260, 50, 50)
                transition.play()
                stage = 3

            if pygame.Rect.colliderect(player1.baseRect, flooded_deck.boundary03):
                if riddleAnswered and barrelSearched and froggy:
                    screen.blit(congrats, (0,0))
                    pygame.display.update()
                    time.sleep(4)
                    player1.baseRect.update(240, 310, 50, 50)
                    stage = 6
                else:
                    stage = 4
                
        if stage == 5: # answer the riddle
            SCR_WID, SCR_HEI = 550, 750
            screen = pygame.display.set_mode((SCR_WID, SCR_HEI), 0, 32)
            pygame.display.set_caption('ShipRekt!')
            main_deck.draw(screen)
            drunkard.draw(screen)
            player1.draw(screen)
            screen.blit(drunkard.riddle, (20, 25))
            pygame.display.update()
            while riddleAnswered == False:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_1 or event.key == K_KP1:
                                riddleAnswered = True
                                screen.blit(drunkard.correct, (20, 25))
                                pygame.display.update()
                                time.sleep(2)
                                screen.blit(drunkard.gift, (20, 25))
                                if froggy == False:
                                    if barrelSearched == False:
                                        inventory = pygame.image.load('invh.png')
                                    elif barrelSearched == True:
                                        inventory = pygame.image.load('invhn.png')
                                if froggy == True:
                                    if barrelSearched == False:
                                        inventory = pygame.image.load('invwh.png')
                                    elif barrelSearched == True:
                                        inventory = pygame.image.load('fullinv.png')
                        else:
                            riddleAnswered == False
            if riddleAnswered == True:
                stage = 2
                
        if stage == 6:
            SCR_WID, SCR_HEI = 550, 480
            screen = pygame.display.set_mode((SCR_WID, SCR_HEI), 0, 32)
            pygame.display.set_caption('ShipRekt!')
            victory_deck.draw(screen)
            screen.blit(thanks, (0,0))
            player1.draw(screen)
            pygame.display.update()
            

        if stage == 7:
            SCR_WID, SCR_HEI = 550, 480
            screen = pygame.display.set_mode((SCR_WID, SCR_HEI), 0, 32)
            pygame.display.set_caption('ShipRekt!')
            capsized_deck.draw(screen)
            screen.blit(failure, (SCR_WID/8, (SCR_HEI/2)-120))
            
        print(int(seconds))
        pygame.display.update()
        mainClock.tick(60)        
main()
