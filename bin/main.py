'''程序入口'''
import pygame, sys
from src.plane import OurPlane
from src.enemy import SmallEnemy
from src.enemy import MiddleEnemy
from src.enemy import LargeEnemy
from src.bullet import Bullet
from src.bullet import EnemyBullet
from src.button import Button
from src.bomb import Bomb
pygame.init()
bg_size = (480, 700)
screen = pygame.display.set_mode(bg_size)
logo = pygame.image.load('../material/image/shoot_copyright.png').convert_alpha()
pygame.display.set_caption("飞机大战")
background_image_path = "../material/image/background.png"
background = pygame.image.load(background_image_path).convert()
# 游戏结束背景图
gameover_image = pygame.image.load("../material/image/game_over.png")
# 绘制矩形
# pygame.draw.rect(background, (0,0,255), (0, 0, 480, 100),2)
# 绘制Money文本
text = str(0)
lives_text = str(3)
money_font = pygame.font.SysFont('simsunnsimsun', 20)
money_number_surface = money_font.render("获得金钱:" + text, True, (0, 0, 0), None)
lives_number_surface = money_font.render("剩余生命:" + lives_text, True, (0, 0, 0), None)
# 自定义生成小型敌机事件
GENERATORSMALLENEMYEVENT = pygame.USEREVENT + 1
pygame.time.set_timer(GENERATORSMALLENEMYEVENT, 2000)
# 自定义生成中型敌机事件
GENERATORMIDDLEENEMYEVENT = pygame.USEREVENT + 2
pygame.time.set_timer(GENERATORMIDDLEENEMYEVENT, 10000)
# 自定义生成大型敌机事件
GENERATORLARGEENEMYEVENT = pygame.USEREVENT + 3
pygame.time.set_timer(GENERATORLARGEENEMYEVENT, 30000)
# 自定义生成英雄子弹事件
GENERATORBULLETEVENT = pygame.USEREVENT + 4
pygame.time.set_timer(GENERATORBULLETEVENT, 500)
# 自定义生成敌机子弹事件
GENERATORENEMYBULLETEVENT = pygame.USEREVENT + 5
pygame.time.set_timer(GENERATORENEMYBULLETEVENT, 2000)
#自定义生成炮弹对象
GENERATORBOMBEVENT = pygame.USEREVENT + 6
pygame.time.set_timer(GENERATORBOMBEVENT, 5000)
# 创建OurPlane的对象
ourplane = OurPlane(bg_size)
# 定义四种血槽颜色
color_black = (0, 0, 0)
color_green = (0, 255, 0)
color_red = (255, 0, 0)
color_white = (255, 255, 255)
# 最高分数
maxScore = 0


def showWelcome(gameStart, gameOver):
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if gameStart.is_over():
                return False
            elif gameOver.is_over():
                pygame.quit()
                exit()
    screen.blit(background, (0, 0))
    screen.blit(logo, ((bg_size[0] - logo.get_width()) / 2, 100))
    gameStart.render(screen)
    gameOver.render(screen)
    return True


def run():
    global text
    global lives_text
    global money_font
    global money_number_surface
    global lives_number_surface
    global maxScore
    # 英雄机生命数
    ourplane_lives = 3

    # 游戏是否结束
    game_over = False
    # 是否运行
    running = True
    y = 0
    # 图片切换变量
    switch_image = True
    # 设置图片切换变量的参数
    delay = 60
    # 生成存储小型敌机的小组group
    small_enemies = pygame.sprite.Group()
    # 生成存储中型敌机的小组group
    middle_enemies = pygame.sprite.Group()
    # 生成存储大型敌机的小组group
    large_enemies = pygame.sprite.Group()
    # 生成子弹
    bulls = pygame.sprite.Group()
    # 生成子弹
    enemy_bulls = pygame.sprite.Group()
    # 所有敌机
    enemies = pygame.sprite.Group()
    #所有炮弹
    bombs = pygame.sprite.Group()
    # 游戏开始按钮
    gameStart = Button('../material/image/game_resume_nor.png', '../material/image/game_resume_pressed.png',
                       (bg_size[0] / 2, bg_size[1] * 8 / 12))
    while running:
        delay -= 1
        if delay == 0:
            delay = 60
        # if delay % 3:
        #     switch_image  = not switch_image
        # 绘制背景
        screen.blit(background, (0, 0))
        # 绘制金钱文本
        screen.blit(money_number_surface, (350, 20))
        # 绘制生命数文本
        screen.blit(lives_number_surface, (250, 20))
        # screen.blit(background, (0, -bg_size[1] + y))
        clock = pygame.time.Clock()
        clock.tick(20)
        if not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # 生成子弹
                if event.type == GENERATORBULLETEVENT:
                    bull = Bullet(ourplane.rect, bg_size)
                    bulls.add(bull)
                # 生成敌机子弹
                if event.type == GENERATORENEMYBULLETEVENT:
                    for enemy in enemies:
                        if enemy.active:
                            enemy_bull = EnemyBullet(enemy.rect, bg_size)
                            enemy_bulls.add(enemy_bull)
                # 生成小型敌机
                if event.type == GENERATORSMALLENEMYEVENT and large_enemies.__len__() <= 0:
                    small_enemy = SmallEnemy(bg_size)
                    small_enemies.add(small_enemy)
                    enemies.add(small_enemy)
                # 生成中型敌机
                if event.type == GENERATORMIDDLEENEMYEVENT and large_enemies.__len__() <= 0:
                    middle_enemy = MiddleEnemy(bg_size)
                    middle_enemies.add(middle_enemy)
                    enemies.add(middle_enemy)
                # 生成大型敌机
                if event.type == GENERATORLARGEENEMYEVENT and large_enemies.__len__() == 0:
                    large_enemy = LargeEnemy(bg_size)
                    large_enemies.add(large_enemy)
                    enemies.add(large_enemy)
                if event.type == GENERATORBOMBEVENT and large_enemies.__len__() > 0:
                    for large_enemy in large_enemies:
                        bomb = Bomb(large_enemy.rect,bg_size)
                        bombs.add(bomb)
            # 绘制小型敌机
            for each in small_enemies:
                if each.active:
                    screen.blit(each.image, each.rect)
                    each.move()
                    pygame.draw.line(screen, color_black, (each.rect.left, each.rect.top - 5),
                                     (each.rect.right, each.rect.top - 5), 3)
                    energy_remain = each.energy / SmallEnemy.energy
                    # 生命槽颜色
                    #print(energy_remain)
                    if energy_remain > 0.2:
                        energy_color = color_green
                        pygame.draw.line(screen, energy_color, (each.rect.left, each.rect.top - 5),
                                         (each.rect.right, each.rect.top - 5), 3)
                    elif energy_remain < 0.2 and energy_remain > 0:
                        energy_color = color_red
                        pygame.draw.line(screen, energy_color, (each.rect.left, each.rect.top - 5),
                                         (each.rect.right, each.rect.top - 5), 3)
                    elif energy_remain <= 0:
                        each.active = False
                        # 绘制Money文本,金钱增加10
                        text = str(int(text) + 10)
                        money_font = pygame.font.SysFont('simsunnsimsun', 20)
                        money_number_surface = money_font.render("获得金钱:" + text, True, (0, 0, 0), None)
                        screen.blit(money_number_surface, (350, 20))
                        # 绘制死亡状态下的敌机图片
                        for i in range(4):
                            screen.blit(each.destroy_images[i], each.rect)
                        small_enemies.remove(each)
                        enemies.remove(small_enemy)
                        # small_enemies.remove(each)
            # 绘制中型敌机
            for each in middle_enemies:
                if each.active:
                    screen.blit(each.image, each.rect)
                    each.move()
                    energy_remain = each.energy / MiddleEnemy.energy
                    # 生命槽颜色
                    #print(energy_remain)
                    if energy_remain > 0.2:
                        pygame.draw.line(screen, color_black, (each.rect.left, each.rect.top + 100),
                                         (each.rect.right, each.rect.top + 100), 3)
                        energy_color = color_green
                        pygame.draw.line(screen, energy_color, (each.rect.left, each.rect.top + 100),
                                         (each.rect.left + (each.rect.right - each.rect.left) * energy_remain, each.rect.top + 100), 3)
                    elif energy_remain < 0.2 and energy_remain > 0:
                        pygame.draw.line(screen, color_black, (each.rect.left, each.rect.top + 100),
                                         (each.rect.right, each.rect.top + 100), 3)
                        energy_color = color_red
                        pygame.draw.line(screen, energy_color, (each.rect.left, each.rect.top + 100),
                                         (each.rect.left + (each.rect.right - each.rect.left) * energy_remain, each.rect.top + 100), 3)
                    elif energy_remain <= 0:
                        each.active = False
                        # 绘制Money文本,金钱增加50
                        text = str(int(text) + 50)
                        money_font = pygame.font.SysFont('simsunnsimsun', 20)
                        money_number_surface = money_font.render("获得金钱:" + text, True, (0, 0, 0), None)
                        screen.blit(money_number_surface, (350, 20))
                        # 绘制死亡状态下的敌机图片
                        for i in range(4):
                            screen.blit(each.destroy_images[i], each.rect)
                        middle_enemies.remove(each)
                        enemies.remove(middle_enemy)
            # 绘制大型敌机
            for each in large_enemies:
                print(each.active)
                if each.active:
                    screen.blit(each.image_one, each.rect)
                    each.move()
                    # 绘制血槽
                    energy_remain = each.energy / LargeEnemy.energy
                    # 生命槽颜色
                    print(energy_remain)
                    if energy_remain >= 0.2:
                        pygame.draw.line(screen, color_black, (each.rect.left, each.rect.top + 260),
                                         (each.rect.right, each.rect.top + 260), 3)
                        energy_color = color_green
                        pygame.draw.line(screen, energy_color, (each.rect.left, each.rect.top + 260),
                                         (each.rect.left + (each.rect.right - each.rect.left) * energy_remain,
                                          each.rect.top + 260), 3)
                    elif energy_remain < 0.2 and energy_remain > 0:
                        pygame.draw.line(screen, color_black, (each.rect.left, each.rect.top + 260),
                                         (each.rect.right, each.rect.top + 260), 3)
                        energy_color = color_red
                        pygame.draw.line(screen, energy_color, (each.rect.left, each.rect.top + 260),
                                         (each.rect.left + (each.rect.right - each.rect.left) * energy_remain,
                                           each.rect.top + 260), 3)
                    elif energy_remain <= 0:
                        each.active = False
                        # 绘制Money文本,金钱增加100
                        text = str(int(text) + 100)
                        money_font = pygame.font.SysFont('simsunnsimsun', 20)
                        money_number_surface = money_font.render("获得金钱:" + text, True, (0, 0, 0), None)
                        screen.blit(money_number_surface, (350, 20))
                        for i in range(6):
                            screen.blit(each.destroy_images[i], each.rect)
                        large_enemies.remove(each)
                        enemies.remove(large_enemy)
                        game_over = True
                else:
                    pass
            # 绘制英雄机的图片
            if ourplane.active and ourplane_lives != 0:
                if switch_image:
                    energy_remain = ourplane.energy / OurPlane.energy
                    print(energy_remain)
                    if energy_remain > 0.2:
                        pygame.draw.line(screen, color_black, (ourplane.rect.left, ourplane.rect.top + 130),
                                         (ourplane.rect.right, ourplane.rect.top + 130), 3)
                        # 绘制血槽
                        pygame.draw.line(screen, color_green, (ourplane.rect.left, ourplane.rect.top + 130),(ourplane.rect.left + (ourplane.rect.right - ourplane.rect.left) * energy_remain,
                                           ourplane.rect.top + 130), 3)
                        screen.blit(ourplane.image_one, ourplane.rect)
                    elif energy_remain <= 0.2 and energy_remain > 0:
                        pygame.draw.line(screen, color_black, (ourplane.rect.left, ourplane.rect.top + 130),
                                         (ourplane.rect.right, ourplane.rect.top + 130), 3)
                        # 绘制血槽
                        pygame.draw.line(screen, color_red, (ourplane.rect.left, ourplane.rect.top + 130),
                                         (ourplane.rect.left + (ourplane.rect.right - ourplane.rect.left) * energy_remain, ourplane.rect.top + 130), 3)
                        screen.blit(ourplane.image_one, ourplane.rect)
                    elif energy_remain <= 0:
                        ourplane_lives -= 1
                        lives_text = int(lives_text) - 1
                        lives_number_surface = money_font.render("剩余生命:" + str(lives_text), True, (0, 0, 0), None)
                        screen.blit(lives_number_surface, (250, 20))
                        # 绘制死亡状态下的英雄机图片
                        for i in range(4):
                            screen.blit(ourplane.destroy_images[i], ourplane.rect)
                        ourplane.energy = 100
                        ourplane.active = True
                        # screen.blit(ourplane.image_one,ourplane.rect)
                        # ourplane.reset()
                else:
                    screen.blit(ourplane.image_two, ourplane.rect)
            else:
                game_over = True
            # 绘制子弹
            for bull in bulls:
                screen.blit(bull.image, bull.rect)
                bull.move()
            # 绘制敌机子弹
            for bull in enemy_bulls:
                screen.blit(bull.image, bull.rect)
                bull.move()
            # 绘制炮弹
            for bomb in bombs:
                screen.blit(bomb.image, bomb.rect)
                bomb.move()
            # 子弹和小型飞机碰撞
            for bull in bulls:
                for enemy in small_enemies:
                    if pygame.sprite.collide_mask(bull, enemy):
                        if enemy.energy > 0:
                            enemy.energy -= 2
                        bull.kill()
                        bulls.remove(bull)
            # 子弹和中型飞机碰撞
            for bull in bulls:
                for enemy in middle_enemies:
                    if pygame.sprite.collide_mask(bull, enemy):
                        if enemy.energy > 0:
                            enemy.energy -= 2
                        bull.kill()
                        bulls.remove(bull)
            # 子弹和大型飞机碰撞
            for bull in bulls:
                for enemy in large_enemies:
                    if pygame.sprite.collide_mask(bull, enemy):
                        if enemy.energy > 0:
                            enemy.energy -= 2
                        bull.kill()
                        bulls.remove(bull)
            # 敌方子弹和英雄飞机碰撞
            for enemy_bull in enemy_bulls:
                if pygame.sprite.collide_mask(enemy_bull, ourplane):
                    ourplane.energy -= 10
                    enemy_bull.kill()
                    enemy_bulls.remove(enemy_bull)
            # 敌方飞机和英雄飞机碰撞
            for enemy in enemies:
                if ourplane.active and enemy.active:
                    if pygame.sprite.collide_mask(enemy, ourplane):
                        ourplane.energy -= 1
            #炮弹和英雄飞机碰撞
            for bomb in bombs:
                if pygame.sprite.collide_mask(bomb, ourplane):
                    ourplane.energy -= 5
            # 控制英雄机移动
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
                ourplane.move_up()
            elif key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
                ourplane.move_down()
            elif key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
                ourplane.move_left()
            elif key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
                ourplane.move_right()
            # ourplane.move_down()
            y += 1
            if bg_size[1] == y:
                y = 0
                # 绘制英雄飞机
                # screen.blit(ourplane.image_one,ourplane.rect)

        elif game_over:
            score = int(text)
            if score > maxScore:
                maxScore = score
            Score = money_font.render(str(score), True, (0, 0, 0), None)
            mScore = money_font.render(str(maxScore), True, (0, 0, 0), None)
            screen.blit(gameover_image, (0, 0))
            screen.blit(mScore, (150, 40))
            screen.blit(Score, (240 - Score.get_width() / 2, 375))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    run()
