from vertexv1 import Vertex
class Graph:

    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self,n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def addEdge(self,from_vertex,to_vertex,weight =0):
        if from_vertex not in self.vert_list:
            nv = self.add_vertex(from_vertex)
        if to_vertex not in self.vert_list:
            nv