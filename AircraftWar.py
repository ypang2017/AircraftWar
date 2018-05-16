# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *
import time


class BasePlane:
    def __init__(self, screen_tmp, x, y, image_name):
        self.x = x
        self.y = y
        self.screen = screen_tmp
        self.image = pygame.image.load(image_name)
        self.bullets = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullets.remove(bullet)


class HeroPlane(BasePlane):
    def __init__(self, screen_tmp):
        super().__init__(screen_tmp, 210, 650, "./picture/hero1.png")

    def display(self):
        super().display()

    def move_left(self):
        if self.x > 0:
            self.x -= 10

    def move_right(self):
        if self.x < 380:
            self.x += 10

    def fire(self):
        self.bullets.append(Bullet(self.screen, self.x + 40, self.y - 10))


class EnemyPlane(BasePlane):
    def __init__(self, screen_tmp):
        super().__init__(screen_tmp, 0, 0, "./picture/enemy0.png")
        self.direction = "right"

    def display(self):
        super().display()
        self.move()

    def move(self):
        if self.direction == "right":
            if self.x < 430:
                self.x += 2
            else:
                self.direction = "left"
        elif self.direction == "left":
            if self.x > 0:
                self.x -= 2
            else:
                self.direction = "right"

class Bullet:
    def __init__(self, screen_tmp, x, y):
        self.x = x
        self.y = y
        self.screen = screen_tmp
        self.image = pygame.image.load("./picture/bullet.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 5

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


def key_control(hero_tmp):
    # 获取事件，比如按键等
    for event in pygame.event.get():

        # 判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left,向左移动
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_tmp.move_left()
            # 检测按键是否是d或者right，向右移动
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_tmp.move_right()
            # 检测按键是否是空格键，发射子弹
            elif event.key == K_SPACE:
                print('space')
                hero_tmp.fire()

def main():
    # 1. 创建窗口
    screen = pygame.display.set_mode((480, 780), 0, 32)

    # 2. 创建背景图片
    background = pygame.image.load("./picture/background.png")

    # 3. 创建一个英雄飞机对象
    hero = HeroPlane(screen)

    # 4. 创建一个敌人飞机对象
    enemy = EnemyPlane(screen)

    while True:
        screen.blit(background, (0, 0))
        hero.display()
        enemy.display()
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)


if __name__ == "__main__":
    main()
