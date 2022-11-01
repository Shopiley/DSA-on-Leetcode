class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # giving connected components
        if image[sr][sc] == color:
            return image

        visited = set()
        self.explore(image, sr, sc, visited, color, image[sr][sc])
        return image
        
        
    def explore(self, image, sr, sc, visited, color, current):
        start = sr, sc
        
        if sr not in range(len(image)) or sc not in range(len(image[0])):
            return 
        
        # if image[sr][sc] == 0:
        #     return False
        
        if current != image[sr][sc]:
            return 
        
        if start in visited:
            return False
        visited.add(start)
        
        image[sr][sc] = color
        self.explore(image, sr, sc+1, visited, color, current)
        self.explore(image, sr, sc-1, visited, color, current)
        self.explore(image, sr+1, sc, visited, color, current)
        self.explore(image, sr-1, sc, visited, color, current)
        
        
        
        
                
        