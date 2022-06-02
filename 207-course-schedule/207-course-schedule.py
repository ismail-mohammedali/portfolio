class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i:[] for i in range(numCourses)}
        for req, pre in prerequisites:
            preMap[pre].append(req)
        
        
        visit_set = set()
        
        def dfs ( crs):
            if crs in visit_set: 
                return False
            if preMap[crs]==[]:
                return True
            
            visit_set.add(crs)
            
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visit_set.remove(crs)
            preMap[crs]=[]
            return True
        for crs in range(numCourses):
            
            if not dfs(crs): return False
        return True
        
        