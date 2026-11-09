from pico2d import (clear_canvas, update_canvas, get_events, SDL_QUIT,
                    SDL_KEYDOWN, SDLK_ESCAPE, SDLK_i, SDLK_0, SDLK_1, SDLK_2,
                    SDLK_p)
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
paused = False


def init():
    global boy, grass, item_mode, paused
    grass = Grass()
    game_world.add_oject(grass, 0)

    boy = Boy()
    game_world.add_oject(boy, 1)
    item_mode = ItemMode()
    paused = False


def finish():
    global boy, grass, item_mode, paused
    game_world.clear()
    boy = None
    grass = None
    item_mode = None
    paused = False


def handle_events():
    global paused
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            item_mode.toggle()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            paused = not paused
            if paused:
                boy.pause_movement()
        elif paused:
            continue
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_0 and
              item_mode.active):
            boy.clear_ball()
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_1 and
              item_mode.active):
            boy.select_ball(Ball.SMALL)
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_2 and
              item_mode.active):
            boy.select_ball(Ball.LARGE)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)  # 2. quit 대신 title_mode로 전환
        else:
            boy.handle_event(event)


def update():
    if not paused:
        game_world.update()


def render():
    clear_canvas()
    game_world.render()
    item_mode.draw()
    update_canvas()


def pause():
    pass


def resume():
    pass