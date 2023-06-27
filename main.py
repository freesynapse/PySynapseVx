#!/usr/bin/python3


from settings import *
import moderngl as mgl
import os
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'   # hide pygame welcome message
import pygame as pg
import sys
# PySynapse modules
from scene import Scene
from shader_manager import ShaderManager
from player import Player


#
class PyVxEngine:
    def __init__(self):
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)
        
        pg.display.set_mode(glm.ivec2(WIN_RES), flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()
        
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = 'auto'
        
        self.clock = pg.time.Clock()
        self.dt = 0
        self.time = 0
        
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        
        self.is_running = True
        self.on_init()
        
    def on_init(self):
        self.player = Player(self)
        self.shader_manager = ShaderManager(self)
        self.scene = Scene(self)
    
    def update(self):
        self.player.update()
        self.shader_manager.update()
        self.scene.update()
        
        self.dt = self.clock.tick()
        self.time = pg.time.get_ticks() * 0.001
        pg.display.set_caption(f'{self.clock.get_fps():.1f} fps')
    
    def render(self):
        self.ctx.clear(color=BG_COLOR)
        self.scene.render()
        pg.display.flip()
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False
    
    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit()
    
    
if __name__ == '__main__':
    app = PyVxEngine()
    app.run()







