import pygame
class Ship():
    def __init__(self,screen,settings):
        """初始化飞船并设置其初始位置"""
        self.screen=screen

        #加载飞船图像并获取其外接矩形
        self.image =  pygame.transform.scale(pygame.image.load('images/rocket-2442125_640.png'), (50, 70))
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.moving_right=False
        self.moving_left=False
        #将毎搜飞船放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom



    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx+=2
        if self.moving_left and self.rect.left>self.screen_rect.left:
            self.rect.centerx-=2