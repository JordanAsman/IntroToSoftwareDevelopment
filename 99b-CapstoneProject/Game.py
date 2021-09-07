import pygame, sys, random, time

class Villain():
    def __init__(self, screen, level, x, y, width):
        self.screen = screen
        self.level = level
        self.speed = 2
        self.width = width
        self.is_dead = False
        self.image_string = "pirate{}.png".format(self.level)
        self.image = pygame.image.load(self.image_string)
        self.image = pygame.transform.scale(self.image, (200, 250))
        self.image.set_colorkey((255, 255, 255))
        self.x = x
        self.x_orig = x
        self.y = y - self.image.get_height()
        self.scrolling = False

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    # moves the pirate in a designated range if the screen is not scrolling
    def move(self):
        if not self.scrolling:
            if self.x == self.x_orig + 50 or self.x < self.x_orig - 50:
                self.speed = - self.speed
                self.image = pygame.transform.flip(self.image, True, False)
                self.image.set_colorkey((255, 255, 255))
            self.x += self.speed

    # checks if the pirate was hit by a weapon
    def hit_by(self, weapon):
        hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        return hitbox.collidepoint(weapon.x, weapon.y)


class Hero():
    def __init__(self, screen, level, width, score):
        self.screen = screen
        self.level = level
        self.width = width
        self.is_dead = False
        self.image_string = "hero{}.png".format(self.level)
        self.image = pygame.image.load(self.image_string)
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.image_right = pygame.transform.scale(self.image, (100, 150))
        self.image_left = pygame.transform.flip(self.image, True, False)
        self.image.set_colorkey((255, 255, 255))
        self.image_left.set_colorkey((255, 255, 255))
        self.image_right.set_colorkey((255, 255, 255))
        self.x = 0
        self.speed = 2
        self.y = self.screen.get_height() - self.image.get_height()
        self.y_acc = 0.2
        self.y_speed = 0
        self.weapons = []
        self.keys = []
        self.can_jump = True
        self.left_press = False
        self.right_press = False
        self.jump_height = 61
        self.bump_left = False
        self.bump_right = False
        self.ground = self.screen.get_height()
        self.on_box = False
        self.keys_collected = 0
        self.score = score
        self.win = False
        self.recent_dir = 'right'

    # Moves the hero left or right
    def move(self):
        if self.x < 0:
            self.x = 0
        if self.x + self.image.get_width() > self.screen.get_width() - 1:
            self.x = self.screen.get_width() - 1 - self.image.get_width()

        change_x = 0

        if self.left_press and not self.right_press:
            change_x = - self.speed
            self.image = self.image_left
            self.recent_dir = 'left'
        elif self.right_press and not self.left_press:
            change_x = self.speed
            self.image = self.image_right
            self.recent_dir = 'right'
        self.x += change_x

    # Draws the hero on the screen
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    # Creates a gravity factor - makes the Hero fall if in the air
    def update(self):
        self.y_speed += self.y_acc

        on_ground = self.y + self.image.get_height() > self.screen.get_height() - 1

        if on_ground and self.y_speed > 0:
            self.y_speed = 0
        if self.on_box and self.y_speed > 0:
            self.y_speed = 0

        self.y += self.y_speed

    # Checks if the hero can jump
    def jump(self):
        self.can_jump = self.y + self.image.get_height() > self.screen.get_height() - 1
        self.can_jump |= self.on_box
        if self.can_jump:
            self.y_speed = -5

    # Adds a weapon to the hero's weapons and moves it across the screen
    def throw(self):
        weapon = Weapon(self.screen, self.x + 3*self.image.get_width()/4, self.y + self.image.get_height()/4, self.recent_dir)
        self.weapons.append(weapon)

    # Remove weapons that hit the villains
    def remove_used_weapons(self):
        for k in range(len(self.weapons) - 1, -1, -1):
            if self.weapons[k].has_exploded or self.weapons[k].y < 0:
                del self.weapons[k]

    # Checks if hero is bumping into a crate on the left or right
    def bump(self, crate, background):
        hero_hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        crate_hitbox = pygame.Rect(crate.x, crate.y, crate.image.get_width(), crate.image.get_height())
        if hero_hitbox.colliderect(crate_hitbox):
            for k in range(int(crate.y+10), int(crate.y+crate.image.get_height())):
                if hero_hitbox.collidepoint(crate.x, k):
                    self.bump_left = True
                    background.can_scroll = False
                if hero_hitbox.collidepoint(crate.x + crate.image.get_width(), k):
                    self.bump_right = True
                    background.can_scroll = False
        if self.bump_left:
            self.x = crate.x - self.image.get_width()
            self.bump_left = False
        if self.bump_right:
            self.x = crate.x + crate.image.get_width()
            self.bump_right = False
        if self.bump_left and self.y + self.image.get_height() == crate.y:
            self.bump_left = False
        if self.bump_right and self.y + self.image.get_height() == crate.y:
            self.bump_right = False

    # Check if hero has landed on a crate
    def land(self, crate, background):
        hero_hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        crate_hitbox = pygame.Rect(crate.x, crate.y, crate.image.get_width(), crate.image.get_height())
        if hero_hitbox.colliderect(crate_hitbox):
            for k in range(int(crate.x+10), int(crate.x+crate.image.get_width()-10)):
                if hero_hitbox.collidepoint(k, crate.y):
                    self.on_box = True
                    background.can_scroll = True


class Weapon():
    def __init__(self, screen, x, y, dir):
        self.screen = screen
        self.x = x
        self.y = y
        self.direction = dir
        self.has_exploded = False
        self.image = pygame.image.load('rock.jpeg')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.image.set_colorkey((255, 255, 255))
        self.sound = pygame.mixer.Sound('rock.wav')

    # Moves the weapon based on the direction the hero was last going
    def move(self):
        if self.direction == 'right':
            self.x += 5
        if self.direction == 'left':
            self.x -= 5

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


class Crate():
    def __init__(self, x, screen):
        self.screen = screen
        self.image = pygame.image.load('crate.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        # self.width = width
        # self.x = random.randint(100, self.width)
        self.x = x
        self.y = self.screen.get_height() - self.image.get_height()
        self.speed = 2

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


class Key():
    def __init__(self, screen, crate):
        self.screen = screen
        self.image = pygame.image.load('key.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.x = crate.x + crate.image.get_width() / 2 - self.image.get_width() / 2
        self.y = self.screen.get_height() - self.image.get_height() - crate.image.get_height()
        self.is_collected = False

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    # Checks if the key has been hit by the hero
    def hit_by(self, hero):
        key_hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        hero_hitbox = pygame.Rect(hero.x, hero.y, hero.image.get_width(), hero.image.get_height())
        if hero_hitbox.colliderect(key_hitbox) and not self.is_collected:
            hero.keys.append(self)
            hero.keys_collected += 1
            self.is_collected = True
            hero.score += 100
            return True
        return False


class Background():
    def __init__(self, screen, level, hero, width):
        self.screen = screen
        self.level = level
        self.hero = hero
        self.width = width
        self.image_string = "background{}.jpg".format(self.level)
        self.image = pygame.image.load(self.image_string)
        self.image = pygame.transform.scale(self.image, (self.width, self.screen.get_height()))
        self.x = 0
        self.y = 0
        self.speed = 2
        self.can_scroll = True

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    # Scrolls the background image, the crates, the keys, and the pirates
    def scroll(self, crates, keys, pirates):
        if self.hero.x > 10:
            if self.hero.right_press:
                if self.x >= -(self.image.get_width() - self.screen.get_width()):
                    self.x -= self.speed
                    for crate in crates:
                        crate.x -= self.speed
                    for key in keys:
                        key.x -= self.speed
                    for villian in pirates:
                        villian.scrolling = True
                        villian.x -= self.speed
                        villian.x_orig = villian.x
                else:
                    for villian in pirates:
                        villian.scrolling = False
            elif self.hero.left_press:
                if self.x <= 0:
                    self.x += self.speed
                    for crate in crates:
                        crate.x += self.speed
                    for key in keys:
                        key.x += self.speed
                    for villian in pirates:
                        villian.scrolling = True
                        villian.x -= self.speed
                        villian.x_orig = villian.x
            else:
                for villian in pirates:
                    villian.scrolling = False
        else:
            for villian in pirates:
                villian.scrolling = False


def instructions():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Instructions")
    HEIGHT = 600
    screen = pygame.display.set_mode((640, HEIGHT))
    instruction_image = pygame.image.load('howToPlay.PNG')
    instruction_image = pygame.transform.scale(instruction_image, (640, HEIGHT))
    instruction_image.set_colorkey((255, 255, 255))
    color = (255, 255, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    width = screen.get_width()
    height = screen.get_height()
    smallfont = pygame.font.SysFont(None, 35)
    text = smallfont.render('Back', True, color)

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width / 2 - 75 <= mouse[0] <= width / 2 + 75 and height - 75 <= mouse[1] <= height - 35:
                    start()
        screen.blit(instruction_image, (0, 0))

        mouse = pygame.mouse.get_pos()
        if width / 2 - 75 <= mouse[0] <= width / 2 + 75 and height - 75 <= mouse[1] <= height - 35:
            pygame.draw.rect(screen, color_light, [width / 2 - 75, height / 2 + 225, 140, 40])

        else:
            pygame.draw.rect(screen, color_dark, [width / 2 - 75, height / 2 + 225, 140, 40])

        screen.blit(text, (width / 2 - 33, height / 2 + 233))

        pygame.display.update()
        clock.tick(15)


def start():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Lost in Neverland!")
    HEIGHT = 600
    screen = pygame.display.set_mode((640, HEIGHT))
    start_image = pygame.image.load('win_back.png')
    start_image = pygame.transform.scale(start_image, (640, HEIGHT))
    color = (255, 255, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    width = screen.get_width()
    height = screen.get_height()
    smallfont = pygame.font.SysFont(None, 35)
    text_start = smallfont.render('Start', True, color)
    text_instructions = smallfont.render('How to Play', True, color)
    start_sound = pygame.mixer.Sound('start.wav')
    rect_width = 150
    rect_height = 20

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width / 2 - rect_width - 50 <= mouse[0] <= width / 2 - 50 and height - 75 <= mouse[1] <= height - 35:
                    start_sound.play()
                    time.sleep(7)
                    main()
                if width / 2 + rect_width/4 <= mouse[0] <= width / 2 + rect_width + rect_width/4 and height - 75 <= mouse[1] <= height - 35:
                    instructions()

        screen.blit(start_image, (0, 0))

        # Makes buttons, changes color if the mouse hovers over the button
        mouse = pygame.mouse.get_pos()
        if width / 2 - rect_width - 50 <= mouse[0] <= width / 2 - 50 and height - 75 <= mouse[1] <= height - 35:
            pygame.draw.rect(screen, color_light, [width / 2 - rect_width - 50, height / 2 + 225, rect_width, 40])

        else:
            pygame.draw.rect(screen, color_dark, [width / 2 - rect_width - 50, height / 2 + 225, rect_width, 40])

        if width / 2 + rect_width/4 <= mouse[0] <= width / 2 + rect_width + rect_width/4 and height - 75 <= mouse[1] <= height - 35:
            pygame.draw.rect(screen, color_light, [width / 2 + rect_width/4, height / 2 + 225, rect_width, 40])

        else:
            pygame.draw.rect(screen, color_dark, [width / 2 + rect_width/4, height / 2 + 225, rect_width, 40])

        screen.blit(text_start, (width / 2 - rect_width, height / 2 + 234))
        screen.blit(text_instructions, (width / 2 + rect_width/4 + 5, height / 2 + 234))

        pygame.display.update()
        clock.tick(15)


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Lost in Neverland!")
    HEIGHT = 600
    WIDTH = 2000
    screen = pygame.display.set_mode((640, HEIGHT))
    level = 1
    game_over_image = pygame.image.load('lose.png')
    game_over_image = pygame.transform.scale(game_over_image, (640, HEIGHT))
    win_background = pygame.image.load('win_back.png')
    win_background = pygame.transform.scale(win_background, (640, HEIGHT))
    win_image = pygame.image.load("win.png")
    win_image = pygame.transform.scale(win_image, (200, 250))
    win_image.set_colorkey((255, 255, 255))
    level_change = False

    quit = pygame.mixer.Sound('quit.wav')
    lose = pygame.mixer.Sound('lose.wav')
    win = pygame.mixer.Sound('win.wav')
    play_win = True
    play_lose = True
    can_throw = True

    # Create hero
    hero = Hero(screen, level, WIDTH, 0)

    # Creates the villains
    pirates = []
    count = 1
    num = random.randint(200, int((WIDTH - 100) / 3))
    for villian in range(3):
        villian = Villain(screen, level, num * count, screen.get_height(), WIDTH)
        pirates.append(villian)
        count += 1

    # Creates the background
    background = Background(screen, level, hero, WIDTH)

    # Creates the crates and keys
    crates = []
    keys = []
    count = 1
    num = random.randint(100, int((WIDTH - 120)/3))
    for crate in range(3):
        crate = Crate(num * count, screen)
        key = Key(screen, crate)
        crates.append(crate)
        keys.append(key)
        count += 1

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN and pressed_keys[pygame.K_SPACE]:
                for villian in pirates:
                    if villian.x - hero.x + hero.image.get_width() <= 500 and can_throw:
                        can_throw = False
                        hero.throw()
            if event.type == pygame.KEYDOWN and pressed_keys[pygame.K_RETURN]:
                main()
            if event.type == pygame.QUIT:
                quit.play()
                time.sleep(10)
                sys.exit()
        if level_change:
            time.sleep(2)

        # Advances level
        if len(pirates) == 0 and hero.keys_collected == 3 and hero.x + hero.image.get_width() >= screen.get_width() - 2:
            if level >= 9:
                hero.win = True
            else:
                level += 1
                level_change = True
                score = hero.score
                hero = Hero(screen, level, WIDTH, score)
                pirates = []
                count = 1
                num = random.randint(100, int((WIDTH - 100) / 3))
                for villian in range(3):
                    villian = Villain(screen, level, num * count, screen.get_height(), WIDTH)
                    pirates.append(villian)
                    count += 1
                background = Background(screen, level, hero, WIDTH)
                hero.keys_collected = 0
                crates = []
                keys = []
                count = 1
                num = random.randint(100, int((WIDTH - 120)/ 3))
                for crate in range(3):
                    crate = Crate(num * count, screen)
                    key = Key(screen, crate)
                    crates.append(crate)
                    keys.append(key)
                    count += 1
                hero.is_dead = False
                if level >= 5:
                    sound_string = "sound{}.wav".format(level)
                    sound = pygame.mixer.Sound(sound_string)
                    sound.play()
        else:
            level_change = False

        # Check if you won
        if hero.win:
            background = win_background
            screen.blit(background, (0, 0))
            screen.blit(win_image, (
                                   (screen.get_width() - win_image.get_width()) / 2,
                                   (screen.get_height() - win_image.get_height()) / 2))
            font = pygame.font.Font(None, 85)
            win_string = "You Won!! Score: {}".format(hero.score)
            win_string_image = font.render(win_string, True, (255, 255, 255))
            screen.blit(win_string_image, (15, 50))
            if play_win:
                play_win = False
                win.play()
            pygame.display.update()
            continue

        # Check if you lost
        if hero.is_dead:
            screen.blit(game_over_image, (0, 0))
            hero.score = 0
            if play_lose:
                play_lose = False
                lose.play()
            pygame.display.update()
            continue

        hero_hitbox = pygame.Rect(hero.x, hero.y, hero.image.get_width(), hero.image.get_height())

        pressed_keys = pygame.key.get_pressed()

        # Check for collision with crates before moving
        hero.on_box = False
        for crate in crates:
            hero.bump(crate, background)
            if not hero.bump_right and not hero.bump_left:
                if pressed_keys[pygame.K_LEFT]:
                    hero.left_press = True
                    hero.move()
                if pressed_keys[pygame.K_RIGHT]:
                    hero.right_press = True
                    hero.move()
            hero.land(crate, background)

        # Checks if player wants hero to jump
        if pressed_keys[pygame.K_UP]:
            hero.jump()

        # Constant gravity factor to make hero fall when in air
        hero.update()

        # Scrolls the background image, crate, keys, and pirates
        background.scroll(crates, keys, pirates)


        # Draws background
        background.draw()

        # Draws crates and keys
        for crate in crates:
            crate.draw()
        for key in keys:
            key.draw()

        # Draw hero
        hero.draw()

        # Draw pirates
        for villian in pirates:
            villian.draw()

        # Draws weapons
        for weapon in hero.weapons:
            weapon.draw()

        # Resetting variables
        hero.left_press = False
        hero.right_press = False

        # Move the villains
        for villian in pirates:
            villian.move()

        # Moves weapons hero throws
        for weapon in hero.weapons:
            weapon.move()

        for weapon in hero.weapons:
            if weapon.direction == 'left':
                can_throw = True

        # Check for pirate hit by weapon, advance level if all defeated
        for villian in pirates:
            for weapon in hero.weapons:
                if villian.hit_by(weapon):
                    weapon.sound.play()
                    can_throw = True
                    villian.is_dead = True
                    weapon.has_exploded = True

        # Check for key collected
        for k in range(len(keys) - 1, -1, -1):
            if keys[k].hit_by(hero):
                del keys[k]

        # Removes used weapons
        hero.remove_used_weapons()

        # Removes dead pirates
        for k in range(len(pirates) - 1, -1, -1):
            if pirates[k].is_dead:
                del pirates[k]

        # Check for hero killed
        for villian in pirates:
            villian_hitbox = pygame.Rect(villian.x, villian.y, villian.image.get_width(), villian.image.get_height())
            if villian_hitbox.colliderect(hero_hitbox):
                hero.is_dead = True

        # Scoreboard
        font = pygame.font.Font(None, 30)
        score_string = "Score: {}".format(hero.score)
        score_image = font.render(score_string, True, (255, 255, 255))
        screen.blit(score_image, (5, 5))

        pygame.display.update()

start()