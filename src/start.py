import pygame
from pygame.locals import *

class start:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True

        # Initialize font
        self.font1 = pygame.font.Font(None, 100)

        # Render the "hello" text
        self.hello_text = self.font1.render("Welcome to World Guesser!", True, (255, 255, 255))

        # Get the rectangle of the rendered text
        self.hello_rect = self.hello_text.get_rect(center=(self.screen.get_width() // 2, 100))

        # Define button rectangles
        self.button1_rect = pygame.Rect((self.screen.get_width() // 2)-300, self.screen.get_height() // 4, 600, 150)

    def start_test(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:  
                    if event.button == 1:  
                        if self.button1_rect.collidepoint(event.pos):
                            print("hello") 

            self.screen.fill((50, 0, 200)) 

            # Render your game here
            pygame.draw.rect(self.screen, (0, 0, 255), self.button1_rect)  # Draw the button rectangle

            # Display the "hello" text
            self.screen.blit(self.hello_text, self.hello_rect)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

# Create an instance of the StartScreen class and run the start_test method
if __name__ == "__main__":
    start_screen = StartScreen()
    start_screen.start_test()
