'''子弹'''
import pygame


class Bullet(pygame.sprite.Sprite):
    plane_left = plane_top = 0
    def __init__(self, rect,bg_size):
        super(Bullet, self).__init__()
        self.image = pygame.image.load("../material/image/bullet1.png")
        #飞机的位置
        self.plane_left,self.plane_top = rect.left,rect.top
        #是否被发射
        self.shootStatus = False
        # 获取子弹的位置
        self.rect = self.image.get_rect()
        #本地背景的位置
        self.width,self.height = bg_size[0],bg_size[1]
        # 定义子弹的初始化位置
        self.rect.left,self.rect.top = rect[0] + 45,rect[1]
        # 本地背景的大小
        self.width, self.height = bg_size[0], bg_size[1]
        # 获取子弹图片的掩模，用来进行精准碰撞检测
        self.mask = pygame.mask.from_surface(self.image)
        # 设置子弹的移动速度
        self.speed = 10
        #设置子弹的生存状态
        self.active = True


    # 子弹的移动方法 （向上）
    def move(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.active = False
            self.kill()

    def update(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
            # print(self.rect.top,self.speed)
        else:
            self.kill()
            # self.rect.bottom = self.height
            # self.active = False


#敌机子弹
class EnemyBullet(pygame.sprite.Sprite):
    plane_left = plane_top = 0
    def __init__(self, rect,bg_size):
        super(EnemyBullet, self).__init__()
        self.image = pygame.image.load("../material/image/bullet2.png")
        #飞机的位置
        self.plane_left,self.plane_top = rect.left,rect.top
        #是否被发射
        self.shootStatus = False
        # 获取子弹的位置
        self.rect = self.image.get_rect()
        #本地背景的位置
        self.width,self.height = bg_size[0],bg_size[1]
        # 定义子弹的初始化位置
        self.rect.left,self.rect.top = rect[0] + 20,rect[1] + 30
        # 本地背景的大小
        self.width, self.height = bg_size[0], bg_size[1]
        # 获取子弹图片的掩模，用来进行精准碰撞检测
        self.mask = pygame.mask.from_surface(self.image)
        # 设置子弹的移动速度
        self.speed = 10
        #设置子弹的生存状态
        self.active = True


    # 子弹的移动方法 （向下）
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False
            self.kill()

    def update(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
            # print(self.rect.top,self.speed)
        else:
            self.kill()
            # self.rect.bottom = self.height
            # self.active = False


    # 复位功能
    def reset(self):
        self.rect.left, self.rect.top = self.plane_left + self.rect.width,self.plane_top - 20
        self.active = True