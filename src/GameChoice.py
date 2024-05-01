import pygame
from pygame.locals import *
from MountainGuesser import MountainGuesser

MS1 = MountainGuesser()

class GameChoice:

  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((1600, 800))
    self.clock = pygame.time.Clock()
    self.running = True

    # Initialize font
    self.font1 = pygame.font.Font(None, 100)
    self.font2 = pygame.font.Font(None, 75)
    self.font3 = pygame.font.SysFont('Arial', 65)
    

    # Render the "hello" text
    self.hello_text = self.font3.render("Choose Your Game!", True,
                                        (225, 224, 222))
    self.MountainChoice_text = self.font3.render("Mountain Guesser", True,
                                          (225, 224, 222))
    self.CityChoice_text = self.font3.render("City Guesser", True,
                                          (225, 224, 222))
    self.LakeChoice_text = self.font3.render("Lake Guesser", True,
                                          (225, 224, 222))
    self.CountryChoice_text = self.font3.render("Country Guesser", True,
                                          (225, 224, 222))

    # Get the rectangle of the rendered text
    self.hello_rect = self.hello_text.get_rect(
        center=(self.screen.get_width() // 2, 100))
    self.MountainChoice_rect = self.MountainChoice_text.get_rect(
        center=(self.screen.get_width() // 6, 250))
    self.CityChoice_rect = self.CityChoice_text.get_rect(
        center=(self.screen.get_width() // 2, 250))
    self.LakeChoice_rect = self.LakeChoice_text.get_rect(
        center=((self.screen.get_width() // 1)-300, 250))
    self.CountryChoice_rect = self.CountryChoice_text.get_rect(
        center=(self.screen.get_width() // 2, 450))

    # Define button rectangles
    self.MountainButton_rect = pygame.Rect((self.screen.get_width() // 6)-150, 290, 300, 100)
    self.CityButton_rect = pygame.Rect((self.screen.get_width() // 2)-150, 290, 300, 100)
    self.LakeButton_rect = pygame.Rect((self.screen.get_width() // 1)-450, 290, 300, 100)
    self.CountryButton_rect = pygame.Rect((self.screen.get_width() // 2)-150, 490, 300, 100)
    self.QuitButton_rect = pygame.Rect(1540, 10, 20, 20)

  def Choice(self):
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            if self.MountainButton_rect.collidepoint(event.pos):
              print("Mountain Clicked")
              MS1.RunMountain()
            elif self.CityButton_rect.collidepoint(event.pos):
              print("City Clicked")
            elif self.LakeButton_rect.collidepoint(event.pos):
              print("Lake Clicked")
            elif self.CountryButton_rect.collidepoint(event.pos):
              print("Country Clicked")
            elif self.QuitButton_rect.collidepoint(event.pos):
              self.running = False

      self.screen.fill((40,40,40))

      # Render your game here
      pygame.draw.rect(self.screen, (115, 177, 244),
                       self.MountainButton_rect)  # Draw the button rectangle
      pygame.draw.rect(self.screen, (115, 177, 244),
                       self.CityButton_rect)  # Draw the button rectangle
      pygame.draw.rect(self.screen, (115, 177, 244),
                       self.LakeButton_rect)  # Draw the button rectangle
      pygame.draw.rect(self.screen, (115, 177, 244),
                       self.CountryButton_rect)  # Draw the button rectangle
      pygame.draw.rect(self.screen, (251, 109, 81),
                       self.QuitButton_rect)  # Draw the button rectangle

      # Display the "hello" text
      self.screen.blit(self.hello_text, self.hello_rect)
      self.screen.blit(self.MountainChoice_text, self.MountainChoice_rect)
      self.screen.blit(self.CityChoice_text, self.CityChoice_rect)
      self.screen.blit(self.LakeChoice_text, self.LakeChoice_rect)
      self.screen.blit(self.CountryChoice_text, self.CountryChoice_rect)

      pygame.display.flip()
      self.clock.tick(60)

    pygame.quit()
