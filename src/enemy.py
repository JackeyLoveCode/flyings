'''敌机'''
import pygame
from random import randint
class SmallEnemy(pygame.sprite.Sprite):
    energy = 4
    def __init__(self,bg_size):
        super(SmallEnemy, self).__init__()
        self.image = pygame.image.load("../material/image/enemy1.png")
        # 获取敌方飞机的位置
        self.rect = self.image.get_rect()
        # 本地背景的大小
        self.width, self.height = bg_size[0], bg_size[1]
        # 定义飞机的初始化位置
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width)) // 2, 0
        #定义飞机的血槽
        self.energy = SmallEnemy.energy
        # 获取敌方飞机图片的掩模，用来进行精准碰撞检测
        self.mask = pygame.mask.from_surface(self.image)
        # 设置飞机的生命状态  True活的，false死的
        self.active = True
        # 设置飞机的移动速度
        self.speed = 6
        # 加载飞机损毁状态
        self.destroy_images = []
        self.destroy_images.extend([pygame.image.load("../material/image/enemy1_down1.png")
                                       , pygame.image.load("../material/image/enemy1_down2.png")
                                       , pygame.image.load("../material/image/enemy1_down3.png")
                                       , pygame.image.load("../material/image/enemy1_down4.png")])

    # 飞机的移动方法 （向下）
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False
            self.kill()


class MiddleEnemy(pygame.sprite.Sprite):
    energy = 16

    def __init__(self,bg_size):
        super(MiddleEnemy, self).__init__()
        self.image = pygame.image.load("../material/image/enemy2.png")
        # 本地背景的大小
        self.width, self.height = bg_size[0], bg_size[1]
        # 获取敌方飞机的位置
        self.rect = self.image.get_rect()
        # 定义飞机的初始化位置
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width)) // 2, 0
        #定义飞机的血槽
        self.energy = MiddleEnemy.energy
        # 获取敌方飞机图片的掩模，用来进行精准碰撞检测
        self.mask = pygame.mask.from_surface(self.image)
        # 设置飞机的生命状态  True活的，false死的
        self.active = True
        # 设置飞机的移动速度
        self.speed = 2
        # 加载飞机损毁状态
        self.destroy_images = []
        self.destroy_images.extend([pygame.image.load("../material/image/enemy2_down1.png")
                                       , pygame.image.load("../material/image/enemy2_down2.png")
                                       , pygame.image.load("../material/image/enemy2_down3.png")
                                       , pygame.image.load("../material/image/enemy2_down4.png")])

    # 飞机的移动方法 （向上）
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.kill()


class LargeEnemy(pygame.sprite.Sprite):
    energy = 100

    def __init__(self,bg_size):
        super(LargeEnemy, self).__init__()
        self.image_one = pygame.image.load("../material/image/enemy3_n1.png")
        #图片
        self.images = []
        self.images.extend([pygame.image.load("../material/image/enemy3_n1.png"),
                            pygame.image.load("../material/image/enemy3_n2.png")])
        # 获取大型飞机的位置
        self.rect = self.image_one.get_rect()
        #背景
        self.width,self.height = bg_size[0],bg_size[1]
        # 定义飞机的初始化位置
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width)) // 2, -255
        #定义飞机的血槽
        self.energy = LargeEnemy.energy
        # 本地背景的大小
        self.width, self.height = bg_size[0], bg_size[1]
        # 获取敌方飞机图片的掩模，用来进行精准碰撞检测
        self.mask = pygame.mask.from_surface(self.image_one)
        # 设置飞机的生命状态  True活的，false死的
        self.active = True
        # 设置飞机的移动速度
        self.speed = 1
        # 加载飞机损毁状态
        self.destroy_images = []
        self.destroy_images.extend([pygame.image.load("../material/image/enemy3_down1.png")
                                       , pygame.image.load("../material/image/enemy3_down2.png")
                                       , pygame.image.load("../material/image/enemy3_down3.png")
                                       , pygame.image.load("../material/image/enemy3_down4.png")
                                       , pygame.image.load("../material/image/enemy3_down5.png")
                                        , pygame.image.load("../material/image/enemy3_down6.png")
                                    ])

    # 飞机的移动方法 （向上）
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.kill()
