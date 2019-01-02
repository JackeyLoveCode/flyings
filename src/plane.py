'''英雄机'''
import pygame
from src.bullet import Bullet

class OurPlane(pygame.sprite.Sprite):
    energy = 100
    def __init__(self,bg_size):
        super(OurPlane, self).__init__()
        self.image_one = pygame.image.load("../material/image/hero1.png")
        self.image_two = pygame.image.load("../material/image/hero2.png")
        # 获取我方飞机的位置
        self.rect = self.image_one.get_rect()
        # 本地背景的大小
        self.width, self.height =  bg_size[0], bg_size[1]
        # 定义飞机的初始化位置
        self.rect.left,self.rect.top = \
            ((self.width - self.rect.width)) // 2,(self.height - self.rect.height) - 200
        # 获取飞机图片的掩模，用来进行精准碰撞检测
        self.mask = pygame.mask.from_surface(self.image_one)
        # 设置飞机的生命状态  True活的，false死的
        self.active = True
        #子弹集合
        self.bullets = []
        # 设置飞机的移动速度
        self.speed = 10
        #生命值
        self.energy = OurPlane.energy
        # 加载飞机损毁状态
        self.destroy_images = []
        self.destroy_images.extend([pygame.image.load("../material/image/hero_blowup_n1.png")
                                    ,pygame.image.load("../material/image/hero_blowup_n2.png")
                                    ,pygame.image.load("../material/image/hero_blowup_n3.png")
                                    ,pygame.image.load("../material/image/hero_blowup_n4.png")])

    #发射子弹方法
    def shoot(self):
        self.createBullets()
    #创建子弹集合
    def createBullets(self,rect,num,bg_size):
        for index in range(0,num):
            bullet = Bullet(rect,bg_size)
            self.bullets.append(bullet)
        return self.bullets
    # 飞机的移动方法（向上）
    def move_up(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else :
            self.rect.top = 0

    def move_down(self):
        if self.rect.bottom < self.height:
            self.rect.top += self.speed
        else :
            self.rect.top = self.height

    def move_left(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else :
            self.rect.left = 0

    def move_right(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
           self.rect.left = self.width

    # 复位功能
    def reset(self):
        self.rect.left, self.rect.top = \
            ((self.width - self.rect.width)) // 2, (self.height - self.rect.height) - 20
        self.active = True
