class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        for a,b in prerequisites:
            graph[a].append(b)

        def dfs(node, visiting, visited):
            if node in visiting:
                return False
            if node in visited:
                return True

            visiting.add(node)

            for neighbor in graph[node]:
                if not dfs(neighbor, visiting, visited):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            
            return True

        visiting = set()
        visited = set()

        for course in range(numCourses):
            if not dfs(course, visiting, visited):
                return False

        return True