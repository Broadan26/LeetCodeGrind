class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s) # Make string mutable
        for idx in range(0, len(s_list), 2*k): # Start at 0, iterate string, increment by 2k
            s_list[idx:idx+k] = reversed(s_list[idx:idx+k]) #Reverse idx to k every 2k
        return ''.join(s_list) # Convert back to string