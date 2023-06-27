from settings import *
from mesh.base_mesh import BaseMesh


class QuadMesh(BaseMesh):
    def __init__(self, app):
        super().__init__()
        
        self.app = app
        self.ctx = app.ctx
        self.program = app.shader_manager.quad
        
        self.vbo_format = '3f 3f'
        self.attrs = ('a_position', 'a_color')
        self.vao = self.get_vao()
        
    def get_vertex_data(self):
        vertices = [
            (0.5, 0.5, 0.0), (-0.5, 0.5, 0.0), (-0.5, -0.5, 0.0),
            (0.5, 0.5, 0.0), (-0.5, -0.5, 0.0), (0.5, -0.5, 0.0),
        ]
        colors = [
            (0, 1, 0), (1, 0, 0), (1, 1, 0),
            (0, 1, 0), (1, 1, 0), (0, 0, 1)
        ]
        vertex_data = np.hstack([np.array(vertices, dtype='float32'), 
                                 np.array(colors, dtype='float32')])
        return vertex_data

