from vertex import Vertex
class Graph:

    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self,key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

