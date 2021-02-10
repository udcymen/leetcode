class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]
        
        degrees = [0 for _ in range(numCourses)]
        edges = [[] for _ in range(numCourses)]
        
        for course, preCourse in prerequisites:
            degrees[course] += 1
            edges[preCourse].append(course)
            
        result = []
        q = []
        
        for index, degree in enumerate(degrees):
            if degree == 0:
                result.append(index)
                q.append(index)
                
        while q:
            course = q.pop()
            
            for nextCourse in edges[course]:
                degrees[nextCourse] -= 1
                
                if degrees[nextCourse] == 0:
                    result.append(nextCourse)
                    q.append(nextCourse)
                    
        for degree in degrees:
            if degree != 0:
                return []
                    
        return result