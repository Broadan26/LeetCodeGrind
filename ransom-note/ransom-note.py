class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        Determines if the first string is a subset of the second string
        Returns True if it is a subset, False otherwise
        '''
        if len(ransomNote) <= len(magazine):
            ransomDict = {}
            magazineDict = {}
            for c in ransomNote: #Hash the ransomNote
                if c not in ransomDict:
                    ransomDict[c] = 1
                else:
                    ransomDict[c] += 1
            for c in magazine: #Hash the magazine
                if c not in magazineDict:
                    magazineDict[c] = 1
                else:
                    magazineDict[c] += 1
            for key in ransomDict: #Ensure ransomNote is a subset of magazine
                if key not in magazineDict or ransomDict[key] > magazineDict[key]:
                    return False
            return True
        return False