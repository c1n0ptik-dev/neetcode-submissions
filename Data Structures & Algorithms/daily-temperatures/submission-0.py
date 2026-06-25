class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                index, value = stack.pop()
                answer[index] = (i - index)


            stack.append([i, temperatures[i]])

        return answer


        

