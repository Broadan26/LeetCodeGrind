class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: # Nothing to do
            return '0'
        
        hex_map = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        answer = ''
        if num < 0: # Flip the number
            num += 2 ** 32
        while num > 0: # Map each 4 bits to a spot in the hex map
            answer = hex_map[(num & 15)] + answer
            num = num >> 4 # Shift 16 over
        return answer