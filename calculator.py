import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 475, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Create Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Calculator")

# Fonts
font = pygame.font.Font(None, 36)

# Calculator buttons
buttons = [
    ("C", 50, 120), ("AC", 150, 120), 
    ("7", 50, 210), ("8", 150, 210), ("9", 250, 210), ("/", 350, 210),
    ("4", 50, 300), ("5", 150, 300), ("6", 250, 300), ("*", 350, 300),
    ("1", 50, 390), ("2", 150, 390), ("3", 250, 390), ("-", 350, 390),
    ("0", 50, 480), (".", 150, 480), ("=", 250, 480), ("+", 350, 480),
]

# Calculator state
expression = ""

# Main function
def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(event.pos)

        screen.fill(WHITE)

        draw_buttons()
        draw_display()

        pygame.display.update()
        clock.tick(FPS)

# Function to handle button clicks
def handle_click(pos):
    global expression

    for button, x, y in buttons:
        button_rect = pygame.Rect(x, y, 80, 80)
        if button_rect.collidepoint(pos):
            if button == "=":
                try:
                    expression = str(eval(expression))
                except:
                    expression = "Error"
            elif button == "C":
                expression = expression[:-1]
            elif button == "AC":
                expression = ""
            else:
                expression += button

# Function to draw calculator buttons
def draw_buttons():
    for button, x, y in buttons:
        button_rect = pygame.Rect(x, y, 80, 80)
        pygame.draw.rect(screen, GRAY, button_rect)
        pygame.draw.rect(screen, BLACK, button_rect, 2)
        draw_text(button, x + 40, y + 40)

# Function to draw the calculator display
def draw_display():
    display_rect = pygame.Rect(50, 30, 320, 70)
    pygame.draw.rect(screen, GRAY, display_rect)
    pygame.draw.rect(screen, BLACK, display_rect, 2)
    draw_text(expression, 210, 65)

# Function to draw text on the screen
def draw_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

if __name__ == "__main__":
    main()
