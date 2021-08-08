class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        '''
        Splits n people into the group sizes provided by the list groupSizes
        Returns the groups as a nested list of ints
        '''
        if len(groupSizes) == 0:
            return None
        dict = {}
        for person, group in enumerate(groupSizes): #Run through groupsize and organize into buckets
            if group not in dict: #No entry for groupsize
                dict[group] = [person]
            else: #Groupsize exists so append
                dict[group].append(person)
        new_groups = []
        for index in dict: #Run through the buckets
            if len(dict[index]) != index: #Members greater than group size
                for j in range(0, len(dict[index]), index):
                    new_groups.append(dict[index][j:j+index])
            else: #Group size is same as members, easy case
                new_groups.append(dict[index])
        return new_groups