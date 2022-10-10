class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:


        def buildGraphDict(edges):
            graph_dict = {}
            for start, end in edges:
                if start not in graph_dict:
                    graph_dict[start] = []
                if end not in graph_dict:
                    graph_dict[end] = []

                graph_dict[start].append(end)
                graph_dict[end].append(start)

            return graph_dict


        def has_path(graph, src, dst, visited):
            if src == dst:
                return True

            if src in visited:
                return False

            visited.add(src)

            for neighbour in graph[src]:
                if neighbour not in visited:
                    if (has_path(graph, neighbour, dst, visited) == True):
                        return True

            return False
        
        graph = buildGraphDict(edges)
        return has_path(graph, source, destination, set())
        



        
        
        
# 0 : [1, 2]
# 1 : [0, 2]
# 2 : [1, 0]
    
