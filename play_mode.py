from pico2d import (clear_canvas, update_canvas, get_events, SDL_QUIT,
                    SDL_KEYDOWN, SDLK_ESCAPE, SDLK_i, SDLK_0)
import game_framework
import game_world
import title_mode  # 1. title_mode 모듈 임포트
from grass import Grass
from boy import Boy
from ball import Ball
from item_mode import ItemMode

boy = None
grass = None
item_mode = None


def init():
    global boy, grass, item_mode
    grass = Grass()
    game_world.add_oject(grass, 0)

    boy = Boy()
    game_world.add_oject(boy, 1)
    item_mode = ItemMode()


def finish():
    game_world.clear()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            item_mode.toggle()
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_0 and
              item_mode.active):
            boy.clear_ball()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)  # 2. quit 대신 title_mode로 전환
        else:
            boy.handle_event(event)


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass