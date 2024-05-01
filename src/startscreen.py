import pygame
from pygame.locals import *
from GameChoice import GameChoice

Start1 = GameChoice()

class startscreen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1600, 800))
        self.clock = pygame.time.Clock()
        self.running = True

        # Initialize font
        self.font1 = pygame.font.Font(None, 100)

        # Render the "hello" text
        self.hello_text = self.font1.render("Welcome to World Guesser!", True, (225, 224, 222))

        # Get the rectangle of the rendered text
        self.hello_rect = self.hello_text.get_rect(center=(self.screen.get_width() // 2, 100))

        # Define button rectangles
        self.button1_rect = pygame.Rect((self.screen.get_width() // 2)-300, self.screen.get_height() // 4, 600, 150)

    def ChangeStart(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:  
                    if event.button == 1:  
                        if self.button1_rect.collidepoint(event.pos):
                            Start1.Choice()
                            

            self.screen.fill((40, 40, 40)) 

            # Render your game here
            pygame.draw.rect(self.screen, (115, 177, 244), self.button1_rect)  # Draw the button rectangle

            # Display the "hello" text
            self.screen.blit(self.hello_text, self.hello_rect)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
