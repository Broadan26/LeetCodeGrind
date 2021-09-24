class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n+1):
            to_append = ''
            if i % 15 == 0:
                to_append = 'FizzBuzz'
            elif i % 5 == 0:
                to_append = 'Buzz'
            elif i % 3 == 0:
                to_append = 'Fizz'
            else:
                to_append = str(i)
            answer.append(to_append)
        return answer