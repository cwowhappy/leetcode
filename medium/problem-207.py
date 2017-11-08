import queue


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :param numCourses:
        :param prerequisites:
        :return:
        """
        adjacentMatrix = [[] for column in range(numCourses)]
        for prerequisite in prerequisites:
            adjacentMatrix[prerequisite[1]].append(prerequisite[0])

        inDegrees = [0 for i in range(numCourses)]
        for index in range(numCourses):
            for i in adjacentMatrix[index]:
                inDegrees[i] += 1
        visitingQueue = queue.Queue()
        for index in range(numCourses):
            if inDegrees[index] == 0:
                visitingQueue.put(index)
        while not visitingQueue.empty():
            index = visitingQueue.get()
            inDegrees[index] = -1
            for i in adjacentMatrix[index]:
                inDegrees[i] -= 1
                if inDegrees[i] == 0:
                    visitingQueue.put(i)

        return sum(inDegrees) == -numCourses
