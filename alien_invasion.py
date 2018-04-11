import pygame
from settings import Settings
from ship import Ship
import games_functions as gf
def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    settins=Settings()
    screen=pygame.display.set_mode((settins.screen_width,settins.screen_height))
    ship=Ship(screen,settins)
    pygame.display.set_caption("Alien Invasion")
    #游戏主体循环
    while True:
        gf.check_events(ship)
        ship.update()
        #让最近绘制的屏幕可见
        screen.fill(settins.bg_color)
        ship.blitme()
        pygame.display.flip()

run_game()