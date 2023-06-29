from mesh.base_mesh import BaseMesh
from mesh.chunk_mesh_builder import build_chunk_mesh


class ChunkMesh(BaseMesh):
    def __init__(self, chunk):
        super().__init__()
        self.app = chunk.app
        self.chunk = chunk
        self.ctx = self.app.ctx
        self.program = self.app.shader_manager.chunk
        
        self.vbo_format = '3u1 1u1 1u1 1u1 1u1'
        self.format_size = sum(int(fmt[:1]) for fmt in self.vbo_format.split())
        self.attrs = ['a_position', 'a_voxel_id', 'a_face_id', 'a_ao_id', 'a_flip_id']
        self.vao = self.get_vao()
    
    def get_vertex_data(self):
        mesh = build_chunk_mesh(
            chunk_voxels=self.chunk.voxels,
            format_size=self.format_size,
            chunk_pos=self.chunk.position,
            world_voxels=self.chunk.world.voxels
        )
        return mesh