class Graph:
    def __init__(self, edges):
        self.edges=edges
        self.graph_dict={ }
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        print("Graph ", self.graph_dict)

    def get_paths(self, start ,end, path=[]):
        path=path+[start]
        if start==end:
            return [path]
        if start not in self.graph_dict:
            return []

        paths=[]
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths= self.get_paths(node , end , path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end , path=[]):
        path = path + [start]
        if start==end:
            return path
        if start not in self.graph_dict:
            return []
        shortest_path= None
        for node in self.graph_dict[start]:
            if node not in path:
                new_path= self.get_shortest_path(node , end , path)
                if new_path:
                    if shortest_path is None or len(new_path)<len(shortest_path):
                        shortest_path=new_path

        return shortest_path

if __name__=='__main__':

    routes=[
        ('mombai', 'paris'),
        ('mombai','dubai'),
        ('paris','dubai'),
        ('paris', 'newYork'),
        ('dubai','newYork' ),
        ('newYork','toronto')
    ]
    routes_graph= Graph(routes)
    start="mombai"
    end="newYork"
    print(f"Paths between {start} to {end} :", routes_graph.get_paths(start, end))
    print(f"Shortest path between {start} and {end} : ", routes_graph.get_shortest_path(start,end))
