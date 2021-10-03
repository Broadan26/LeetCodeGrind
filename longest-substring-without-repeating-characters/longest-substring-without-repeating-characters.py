class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {} # Keep track of seen chars
        max_length = 0
        start = 0 # Start of window
        for end_ch in range(len(s)): # Move end of window
            if s[end_ch] in last_seen and start <= last_seen[s[end_ch]]: # Shift the start
                start = last_seen[s[end_ch]] + 1
            else: # Update the frequency list
                max_length = max(max_length, end_ch - start + 1)
            last_seen[s[end_ch]] = end_ch
        return max_length