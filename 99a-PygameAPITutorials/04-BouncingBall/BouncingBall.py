import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

# DONE: Create a Ball class.
class Ball:
    def __init__(self, screen, x, y, radius, color):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = random.randint(1, 5)
        self.speed_y = random.randint(1, 5)

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        if self.x - self.radius < 0 or self.x + self.radius > self.screen.get_width():
            self.speed_x = -1*self.speed_x
        if self.y - self.radius < 0 or self.y + self.radius > self.screen.get_height():
            self.speed_y = -1*self.speed_y
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y

# DONE: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# DONE: Methods: __init__, draw, move


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # DONE: Create an instance of the Ball class called ball1
    # ball1 = Ball(screen, 55, 55, 7, 'red')
    # ball2 = Ball(screen, 20, 40, 7, 'green')
    # ball3 = Ball(screen, 40, 30, 7, 'blue')

    balls = []

    for k in range(100):
        x = random.randint(5, screen.get_width())
        y = random.randint(5, screen.get_height())
        color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        balls.append(Ball(screen, x, y, 7, color))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # DONE: Move the ball
        for ball in balls:
            ball.move()
            ball.draw()
        # ball1.move()
        # ball2.move()
        # ball3.move()
        # DONE: Draw the ball
        # ball1.draw()
        # ball2.draw()
        # ball3.draw()

        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
