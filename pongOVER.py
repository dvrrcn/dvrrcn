########################
## Darren Cronover
## Project 2 Part 2:
##     Make 3 Changes
## 13 April 2021
## 
########################
########################

# 4/13/2021 - 3 Changes:
#
# 1: Add a Background & change after certain score.
## ✓ Background changes when either player gets to 5 points

# 2: Add sound to the game and have the sound change based upon the score
## ✓ Sound of ball hitting paddle changes when either player exceeds 5 points

# 3: Add a random ball spawning
## ✓ ball2.methods utilized after score reaches random.randint(1,9)

import pygame, random

SCR_WID, SCR_HEI = 600, 480

class Player():
        
        def __init__(self, name):
                if name == 1:
                        self.x, self.y = 8, SCR_HEI/2
                        
                else:
                        self.x, self.y = SCR_WID-16, SCR_HEI/2
                        
                self.speed = 5
                self.padWid, self.padHei = 8, 64
                self.score = 0
                self.scoreFont = pygame.font.Font("imagine_font.ttf", 64)

        def scoring(self, screen, enemy):
                scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
                screen.blit(scoreBlit, (32, 16))
                scoreBlit2 = enemy.scoreFont.render(str(enemy.score), 1, (255, 255, 255))
                screen.blit(scoreBlit2, (SCR_HEI+92, 16))
                    
                if self.score == 10:
                        print ("player 1 wins!")
                        exit()
                
                if enemy.score == 10:
                        print ("Player 2 wins!")
                        exit()

        def movement(self, enemy):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                        self.y -= self.speed
                elif keys[pygame.K_s]:
                        self.y += self.speed
       
                if self.y <= 0:
                        self.y = 0
                elif self.y >= SCR_HEI-64:
                        self.y = SCR_HEI-64
                        
                if keys[pygame.K_UP]:
                        enemy.y -= enemy.speed
                elif keys[pygame.K_DOWN]:
                        enemy.y += enemy.speed
       
                if enemy.y <= 0:
                        enemy.y = 0
                elif enemy.y >= SCR_HEI-64:
                        enemy.y = SCR_HEI-64
       
        def draw(self, screen, enemy):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))
                pygame.draw.rect(screen, (255, 255, 255), (enemy.x, enemy.y, enemy.padWid, enemy.padHei))
 
##class Enemy():
##        def __init__(self):
##                self.x, self.y = SCR_WID-16, SCR_HEI/2
##                self.speed = 3
##                self.padWid, self.padHei = 8, 64
##                self.score = 0
##                self.scoreFont = pygame.font.Font("imagine_font.ttf", 64)
##       
##        def scoring(self):
##                scoreBlit2 = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
##                screen.blit(scoreBlit2, (SCR_HEI+92, 16))
##                if self.score == 10:
##                        print ("Player 2 wins!")
##                        exit()
##       
##        def movement(self):
##                keys = pygame.key.get_pressed()
##                if keys[pygame.K_UP]:
##                        self.y -= self.speed
##                elif keys[pygame.K_DOWN]:
##                        self.y += self.speed
##       
##                if self.y <= 0:
##                        self.y = 0
##                elif self.y >= SCR_HEI-64:
##                        self.y = SCR_HEI-64
##       
##        def draw(self):
##                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))
 
class Ball():
    
        def __init__(self, name):
                self.speed_x = -3
                self.speed_y = 3
                self.size = 8
                self.name = name
                if name == 1:
                    self.x, self.y = SCR_WID/2, SCR_HEI/2
                else:
                    self.x, self.y = SCR_WID/2, (SCR_HEI/2)+75
                    
        def movement(self, player, enemy, noise1, noise2):
                self.x += self.speed_x
                self.y += self.speed_y
                #wall col
                if self.y <= 0:
                        self.speed_y *= -1
                elif self.y >= SCR_HEI-self.size:
                        self.speed_y *= -1
 
                if self.x <= 0:
                        self.__init__(self.name)
                        enemy.score += 1
                elif self.x >= SCR_WID-self.size:
                        self.__init__(self.name)
                        self.speed_x = 3
                        player.score += 1
                ##wall col
                #paddle col
                #player
                for n in range(-self.size, player.padHei):
                        if self.y == player.y + n:
                                if self.x <= player.x + player.padWid:
                                    if player.score < 5 and enemy.score < 5:
                                        noise1.play()
                                    else:
                                        noise2.play()
                                    self.speed_x *= -1
                                    break
                        n += 1
                #enemy
                for n in range(-self.size, enemy.padHei):
                        if self.y == enemy.y + n:
                                if self.x >= enemy.x - enemy.padWid:
                                    if player.score < 5 and enemy.score < 5:
                                        noise1.play()
                                    else:
                                        noise2.play()
                                        
                                    self.speed_x *= -1
                                    break
                        n += 1
                ##paddle col
 
        def draw(self, screen):
            pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 8, 8))
            
def main():

        pygame.init()
        screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
        pygame.display.set_caption("PONG: Project 2 Part 2")
        pygame.font.init()
        clock = pygame.time.Clock()
        FPS = 60
        bg2 = pygame.image.load('pong_bg2.png')
        bg1 = pygame.image.load('pong_bg1.png')
        rand_num = random.randint(1,8)
        player1 = Player(1) 
        player2 = Player(2)
        ball = Ball(1)
        ball2 = Ball(2)
        
        #set up music
        Bounce1 = pygame.mixer.Sound('pong_bounce_1.wav')
        Bounce2 = pygame.mixer.Sound('pong_bounce_2.wav')
        pygame.mixer.music.load('pong_bg_music2.wav')
        pygame.mixer.music.play(-1,0.0)
        pygame.mixer.music.set_volume(0.2)

        try:
            while True:
                    
                    #process
                    for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    print ("Game exited by user")
                                    exit()


                    #logic
                    ball.movement(player1, player2, Bounce1, Bounce2)
                    player1.movement(player2)
                    #draw
                    screen.fill((0,0,0))
                    ##background put here
                    screen.blit(bg1, (0,0))
                    if player1.score >= 5 or player2.score >= 5:
                        screen.blit(bg2, (0,0))
                    ball.draw(screen)
                    if player1.score > rand_num or player2.score > rand_num:
                        ball2.movement(player1, player2, Bounce1, Bounce2)
                        ball2.draw(screen)
                    player1.draw(screen, player2)
                    player1.scoring(screen, player2)
                    ##draw
                    #_______
                    pygame.display.flip()
                    clock.tick(FPS)
        except:
            print("Game over!")

main()
