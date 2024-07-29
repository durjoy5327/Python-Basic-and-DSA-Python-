class Graph:
    def __init__(self, edges):
        self.edges=edges
        self.graph_dict={ }
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=end
        print("Graph ", self.graph_dict)





if __name__=='main':

    routes=[
        ('mombai', 'paris'),
        ('mombai','dubai'),
        ('paris','dubai'),
        ('paris', 'newwork'),
        ('dubai','newwork' ),
        ('newwork','toronto')
    ]
    routes_graph= Graph(routes)