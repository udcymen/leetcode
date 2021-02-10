class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        degrees = [0 for _ in range(numCourses)]
        edges = [[] for _ in range(numCourses)]
        
        for course, preCourse in prerequisites:
            degrees[course] += 1
            edges[preCourse].append(course)
            
        q = []
        
        for index, degree in enumerate(degrees):
            if degree == 0:
                q.append(index)
        
        while q:
            course = q.pop()
            for nextCourse in edges[course]:
                degrees[nextCourse] -= 1
                
                if degrees[nextCourse] == 0:
                    q.append(nextCourse)
        
        for degree in degrees:
            if degree != 0:
                return False
            
        return True