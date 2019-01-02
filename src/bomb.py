import pygame

#炮弹
class Bomb(pygame.sprite.Sprite):

    def __init__(self, rect,bg_size):
        super(Bomb, self).__init__()
        self.image = pygame.image.load("../material/image/bomb.png")
        #是否被发射
        self.shootStatus = False
        # 获取炮弹的位置
        self.rect = self.image.get_rect()
        #本地背景的位置
        self.width,self.height = bg_size[0],bg_size[1]
        # 定义炮弹的初始化位置<165*255>
        self.rect.left,self.rect.top = rect[0] + 165 // 2,rect[1] + 255
        # 本地背景的大小
        self.width, self.height = bg_size[0], bg_size[1]
        # 获取炮弹图片的掩模，用来进行精准碰撞检测
        self.mask = pygame.mask.from_surface(self.image)
        # 设置子弹的移动速度
        self.speed = 10
        #设置炮弹的生存状态
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

