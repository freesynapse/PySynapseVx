import pygame as pg
from settings import *
from camera import Camera


class Player(Camera):
    def __init__(self, app, position=PLAYER_POS, yaw=-90, pitch=0):
        self.app = app
        super().__init__(position, yaw, pitch)
        
    def keyboard_control(self):
        keys_state = pg.key.get_pressed()
        vel = PLAYER_SPEED * self.app.dt
        if keys_state[pg.K_w]:
            self.move_forward(vel)
        if keys_state[pg.K_s]:
            self.move_back(vel)
        if keys_state[pg.K_a]:
            self.move_left(vel)
        if keys_state[pg.K_d]:
            self.move_right(vel)
        if keys_state[pg.K_SPACE]:
            self.move_up(vel)
        if keys_state[pg.K_LSHIFT]:
            self.move_down(vel)
        
    def mouse_control(self):
        dx, dy = pg.mouse.get_rel()
        if dx:
            self.rotate_yaw(dx * MOUSE_SENSITIVITY)
        if dy:
            self.rotate_pitch(dy * MOUSE_SENSITIVITY)
    
    def update(self):
        self.keyboard_control()
        self.mouse_control()
        super().update()