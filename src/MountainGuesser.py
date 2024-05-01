import pygame
from pygame.locals import *
import random


class MountainGuesser:

  def __init__(self):
    # Same Variable
    pygame.init()
    self.screen = pygame.display.set_mode((1600, 800))
    self.clock = pygame.time.Clock()
    self.running = True
    self.MountRandom = 1

    #Specific Variable
    self.CorrectMountain = 0
    self.IncorrectMountain = 0
    self.HintCountMountain = ""
    self.MountainHint = False 
    self.Mountain = ""
    self.MountainGuess = ""
    self.DifficultyMountain = ""
    self.HintCountOver = ""
    self.BlueColor = (86,142,166)
    self.RedColor = (251,109,81)
    self.MountainStart = False
    self.TestNum = 0

        # Initialize font
    self.font1 = pygame.font.Font(None, 100)
    self.font2 = pygame.font.Font(None, 75)
    self.font3 = pygame.font.SysFont('Arial', 65)
    self.font4 = pygame.font.SysFont('Arial', 40)

    #Images
    #WorldImg = pygame.image.load('WorldImage.png')
    #Fuji = pygame.image.load('MountFuji.jpg')

    #Create Text
    self.hello_text = self.font3.render("Choose:", True,
                                        (225, 224, 222))
    self.MountDiff_text = self.font3.render("Choose Your Difficulty:", True,
                                        (225, 224, 222))
    self.MountEasyText_text = self.font4.render("Easy", True,
                                        (225, 224, 222))
    self.MountMediumText_text = self.font4.render("Medium", True,
                                        (225, 224, 222))
    self.MountHardText_text = self.font4.render("Hard", True,
                                        (225, 224, 222))
    self.MountStartText_text = self.font3.render("Start", True,
                                        (225, 224, 222))
    self.MountGuessText_text = self.font3.render("Where is this?", True,
                                        (225, 224, 222))


    # Mountain Create Text
    self.MountFujiText_text = self.font4.render("Mount Fuji", True,
                                        (225, 224, 222))
    self.MountKilimanjaroText_text = self.font4.render("Mount Kilimanjaro", True,
                                        (225, 224, 222))
    self.MountRainierText_text = self.font4.render("Mount Rainier", True,
                                        (225, 224, 222))
    self.MountMayonText_text = self.font4.render("Mount Mayon", True,
                                        (225, 224, 222))
    self.MountK2Text_text = self.font4.render("K2", True,
                                        (225, 224, 222))
    self.MountDenaliText_text = self.font4.render("Mount Denali", True,
                                        (225, 224, 222))
    self.MountEverestText_text = self.font4.render("Mount Everest", True,
                                        (225, 224, 222))
    self.MountLoganText_text = self.font4.render("Mount Logan", True,
                                        (225, 224, 222))
    self.MountMatterhornText_text = self.font4.render("Matterhorn", True,
                                        (225, 224, 222))
    self.MountHalfDomeText_text = self.font4.render("Half Dome", True,
                                        (225, 224, 222))

    #Rectangle Of Text
    self.hello_rect = self.hello_text.get_rect(
        center=(self.screen.get_width() // 2, 100))
    self.MountDiff_rect = self.MountDiff_text.get_rect(
        center=(self.screen.get_width() //4, 250))
    self.MountEasyText_rect = self.MountEasyText_text.get_rect(
        center=((self.screen.get_width() //4)+ 425, 255))
    self.MountMediumText_rect = self.MountMediumText_text.get_rect(
        center=((self.screen.get_width() //4)+ 725, 255))
    self.MountHardText_rect = self.MountHardText_text.get_rect(
        center=((self.screen.get_width() //4)+ 1025, 255))
    self.MountStartText_rect = self.MountStartText_text.get_rect(
        center=((self.screen.get_width() //2), 495))
    self.MountGuessText_rect = self.MountGuessText_text.get_rect(
        center=(1305, 75))


    # Mountain Text Rect 200
    self.MountFujiText_rect = self.MountFujiText_text.get_rect(
        center=(1305, 200))
    self.MountDenaliText_rect = self.MountDenaliText_text.get_rect(
        center=(1305, 200))

    # Mountain Text Rect 350
    self.MountKilimanjaroText_rect = self.MountKilimanjaroText_text.get_rect(
        center=(1305, 350))
    self.MountLoganText_rect = self.MountLoganText_text.get_rect(
        center=(1305, 350))
    self.MountMatterhornText_rect = self.MountMatterhornText_text.get_rect(
        center=(1305, 350))
    
    # Mountain Text Rect 500
    self.MountRainierText_rect = self.MountRainierText_text.get_rect(
        center=(1305, 500))
    self.MountK2Text_rect = self.MountK2Text_text.get_rect(
        center=(1305, 500))
    self.MountHalfDomeText_rect = self.MountHalfDomeText_text.get_rect(
        center=(1305, 500))
    # Mountain Text Rect 650
    self.MountMayonText_rect = self.MountMayonText_text.get_rect(
        center=(1305, 650))
    self.MountEverestText_rect = self.MountEverestText_text.get_rect(
        center=(1305, 650))

    
    # Define button rectangles
    self.QuitButton_rect = pygame.Rect(1540, 10, 20, 20)
    self.MountHardButton_rect = pygame.Rect((self.screen.get_width() // 4) + 950, 220, 150, 75)
    self.MountMediumButton_rect = pygame.Rect((self.screen.get_width() // 4) + 650, 220, 150, 75)
    self.MountEasyButton_rect = pygame.Rect((self.screen.get_width() // 4) + 350, 220, 150, 75)
    self.MountStartButton_rect = pygame.Rect((self.screen.get_width() // 2)-150, 450, 300, 100)
    self.MountGuess1Button_rect = pygame.Rect(1130, 150, 350, 100)
    self.MountGuess2Button_rect = pygame.Rect(1130, 300, 350, 100)
    self.MountGuess3Button_rect = pygame.Rect(1130, 450, 350, 100)
    self.MountGuess4Button_rect = pygame.Rect(1130, 600, 350, 100)
    


  def RunMountain(self):
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            if self.QuitButton_rect.collidepoint(event.pos):
              self.running = False
            elif self.MountHardButton_rect.collidepoint(event.pos):
              print("Mountain Hard")
              self.DifficultyMountain = "3"
            elif self.MountEasyButton_rect.collidepoint(event.pos):
              print("Mountain Easy")
              self.DifficultyMountain = "1"
            elif self.MountMediumButton_rect.collidepoint(event.pos):
              print("Mountain Medium")
              self.DifficultyMountain = "2"
            elif self.MountStartButton_rect.collidepoint(event.pos):
              print("Mountain Start")
              self.MountainStart = True
              if self.DifficultyMountain == "1" and self.MountainStart == True:
                self.EasyMountain()
              elif self.DifficultyMountain == "2" and self.MountainStart == True:
                self.MediumMountain()
              elif self.DifficultyMountain == "3" and self.MountainStart == True:
                self.HardMountain()

            

      self.screen.fill((48,95,114))

      # Render your Button here
      if self.DifficultyMountain == "":
        pygame.draw.rect(self.screen, (251, 109, 81),
                         self.QuitButton_rect)  # Draw the button rectangle
        pygame.draw.rect(self.screen, (self.RedColor),
                         self.MountHardButton_rect)
        pygame.draw.rect(self.screen, (251, 109, 81),
                         self.MountMediumButton_rect)
        pygame.draw.rect(self.screen, (251, 109, 81),
                         self.MountEasyButton_rect)
        pygame.draw.rect(self.screen, (251, 109, 81),
                         self.MountStartButton_rect)
      elif self.DifficultyMountain == "1":
        pygame.draw.rect(self.screen, (251, 109, 81),
                         self.QuitButton_rect)  # Draw the button rectangle
        pygame.draw.rect(self.screen, (self.RedColor),
                         self.MountHardButton_rect)
        pygame.draw.rect(self.screen, (self.RedColor),
                         self.MountMediumButton_rect)
        pygame.draw.rect(self.screen, (self.BlueColor),
                         self.MountEasyButton_rect)
        pygame.draw.rect(self.screen, (251, 109, 81),
                         self.MountStartButton_rect)
      elif self.DifficultyMountain == "2":
        pygame.draw.rect(self.screen, (251, 109, 81),
                         self.QuitButton_rect)  # Draw the button rectangle
        pygame.draw.rect(self.screen, (self.RedColor),
                         self.MountHardButton_rect)
        pygame.draw.rect(self.screen, (self.BlueColor),
                         self.MountMediumButton_rect)
        pygame.draw.rect(self.screen, (251, 109, 81),
                         self.MountEasyButton_rect)
        pygame.draw.rect(self.screen, (251, 109, 81),
                         self.MountStartButton_rect)
      elif self.DifficultyMountain == "3":
        pygame.draw.rect(self.screen, (251, 109, 81),
                         self.QuitButton_rect)  # Draw the button rectangle
        pygame.draw.rect(self.screen, (self.BlueColor),
                         self.MountHardButton_rect)
        pygame.draw.rect(self.screen, (self.RedColor),
                         self.MountMediumButton_rect)
        pygame.draw.rect(self.screen, (251, 109, 81),
                         self.MountEasyButton_rect)
        pygame.draw.rect(self.screen, (251, 109, 81),
                         self.MountStartButton_rect)

      # Display the text
      self.screen.blit(self.hello_text, self.hello_rect)
      self.screen.blit(self.MountDiff_text, self.MountDiff_rect)
      self.screen.blit(self.MountEasyText_text, self.MountEasyText_rect)
      self.screen.blit(self.MountMediumText_text, self.MountMediumText_rect)
      self.screen.blit(self.MountHardText_text, self.MountHardText_rect)
      self.screen.blit(self.MountStartText_text, self.MountStartText_rect)


      pygame.display.flip()
      self.clock.tick(60)

    pygame.quit()
  def MountainName(self):
    print("PlaceHolder")
  
  def UserGuessMountain(self):
    print("Placeholder")
  
  def CorrectGuessMountain(self):
    print("Placeholder")
  
  def IncorrectGuessMountain(self):
    print("Placeholder")
  
  def HintMountain(self):
    print("Placeholder")

  def EasyMountain(self):
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            if self.QuitButton_rect.collidepoint(event.pos):
              self.running = False


      self.screen.fill((131,128,179))

      # Render your Button here
      pygame.draw.rect(self.screen, (251, 109, 81),
                         self.QuitButton_rect)  # Draw the button rectangle

      if self.MountRandom == 1:
        map_image1 = pygame.image.load("Images/MountFuji.jpg")
        self.screen.blit(self.MountGuessText_text, self.MountGuessText_rect)
        pygame.draw.rect(self.screen, (251, 109, 81),
                             self.MountGuess1Button_rect)
        pygame.draw.rect(self.screen, (251, 109, 81),
                             self.MountGuess2Button_rect)
        pygame.draw.rect(self.screen, (251, 109, 81),
                             self.MountGuess3Button_rect)
        pygame.draw.rect(self.screen, (251, 109, 81),
                             self.MountGuess4Button_rect)
        self.screen.blit(self.MountFujiText_text, self.MountFujiText_rect)
        self.screen.blit(self.MountKilimanjaroText_text, self.MountKilimanjaroText_rect)
        self.screen.blit(self.MountRainierText_text, self.MountRainierText_rect)
        self.screen.blit(self.MountMayonText_text, self.MountMayonText_rect)

        map_image1 = pygame.transform.scale(map_image1, (1000,750))
        map_rect = map_image1.get_rect()
        self.screen.blit(map_image1, (10,25))
        
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.MountGuess1Button_rect.collidepoint(event.pos):
                        self.MountRandom = self.MountRandom + 1
                        self.CorrectMountain = self.CorrectMountain + 1
                    elif self.MountGuess2Button_rect.collidepoint(event.pos) or self.MountGuess3Button_rect.collidepoint(event.pos) or self.MountGuess4Button_rect.collidepoint(event.pos):
                        self.MountRandom = self.MountRandom + 1
                        self.IncorrectMountain = self.IncorrectMountain + 1
      elif self.MountRandom == 2:
        map_image1 = pygame.image.load("Images/K2Image.jpg")
        self.screen.blit(self.MountGuessText_text, self.MountGuessText_rect)
        pygame.draw.rect(self.screen, (251, 109, 81),
                             self.MountGuess1Button_rect)
        pygame.draw.rect(self.screen, (251, 109, 81),
                             self.MountGuess2Button_rect)
        pygame.draw.rect(self.screen, (251, 109, 81),
                             self.MountGuess3Button_rect)
        pygame.draw.rect(self.screen, (251, 109, 81),
                             self.MountGuess4Button_rect)

        self.screen.blit(self.MountLoganText_text, self.MountLoganText_rect)
        self.screen.blit(self.MountEverestText_text, self.MountEverestText_rect)
        self.screen.blit(self.MountDenaliText_text, self.MountDenaliText_rect)
        self.screen.blit(self.MountK2Text_text, self.MountK2Text_rect)

        map_image1 = pygame.transform.scale(map_image1, (1000,750))
        map_rect = map_image1.get_rect()
        self.screen.blit(map_image1, (10,25))
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.MountGuess3Button_rect.collidepoint(event.pos):
                        self.MountRandom = self.MountRandom + 1
                        self.CorrectMountain = self.CorrectMountain + 1
                    elif self.MountGuess2Button_rect.collidepoint(event.pos) or self.MountGuess1Button_rect.collidepoint(event.pos) or self.MountGuess4Button_rect.collidepoint(event.pos):
                        self.MountRandom = self.MountRandom + 1
                        self.IncorrectMountain = self.IncorrectMountain + 1
      elif self.MountRandom == 3:
        map_image1 = pygame.image.load("Images/Matterhorn.jpg")
        self.screen.blit(self.MountGuessText_text, self.MountGuessText_rect)
        pygame.draw.rect(self.screen, (251, 109, 81),
                             self.MountGuess1Button_rect)
        pygame.draw.rect(self.screen, (251, 109, 81),
                             self.MountGuess2Button_rect)
        pygame.draw.rect(self.screen, (251, 109, 81),
                             self.MountGuess3Button_rect)
        pygame.draw.rect(self.screen, (251, 109, 81),
                             self.MountGuess4Button_rect)

        self.screen.blit(self.MountMatterhornText_text, self.MountMatterhornText_rect) #2
        self.screen.blit(self.MountEverestText_text, self.MountEverestText_rect)
        self.screen.blit(self.MountDenaliText_text, self.MountDenaliText_rect)
        self.screen.blit(self.MountK2Text_text, self.MountK2Text_rect)

        map_image1 = pygame.transform.scale(map_image1, (1000,750))
        map_rect = map_image1.get_rect()
        self.screen.blit(map_image1, (10,25))
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.MountGuess2Button_rect.collidepoint(event.pos):
                        self.MountRandom = self.MountRandom + 1
                        self.CorrectMountain = self.CorrectMountain + 1
                    elif self.MountGuess3Button_rect.collidepoint(event.pos) or self.MountGuess1Button_rect.collidepoint(event.pos) or self.MountGuess4Button_rect.collidepoint(event.pos):
                        self.MountRandom = self.MountRandom + 1
                        self.IncorrectMountain = self.IncorrectMountain + 1
      elif self.MountRandom == 4:
        
        self.MountCorrectText_text = self.font3.render(str(self.CorrectMountain), True,
                                        (225, 224, 222))
        self.MountIncorrectText_text = self.font3.render(str(self.IncorrectMountain), True,
                                        (225, 224, 222))
        self.MountCorrectText_rect = self.MountCorrectText_text.get_rect(
        center=(1305, 75))
        self.MountIncorrectText_rect = self.MountIncorrectText_text.get_rect(
        center=(1400, 75))
        
        self.screen.blit(self.MountCorrectText_text, self.MountCorrectText_rect)
        self.screen.blit(self.MountIncorrectText_text, self.MountIncorrectText_rect)



      

     

      pygame.display.flip()
      self.clock.tick(60)

    pygame.quit()

  def MediumMountain(self):
    print("Placeholder")
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            if self.QuitButton_rect.collidepoint(event.pos):
              self.running = False
            

      self.screen.fill((131,128,179))

      # Render your Button here
     
      pygame.draw.rect(self.screen, (251, 109, 81),
                         self.QuitButton_rect)  # Draw the button rectangle

      # Display the text



      pygame.display.flip()
      self.clock.tick(60)

    pygame.quit()


  def HardMountain(self):
    print("Placeholder")
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            if self.QuitButton_rect.collidepoint(event.pos):
              self.running = False
            

      self.screen.fill((131,128,179))

      # Render your Button here
     
      pygame.draw.rect(self.screen, (251, 109, 81),
                         self.QuitButton_rect)  # Draw the button rectangle

      # Display the text



      pygame.display.flip()
      self.clock.tick(60)

    pygame.quit()



    pygame.quit()

  
  
