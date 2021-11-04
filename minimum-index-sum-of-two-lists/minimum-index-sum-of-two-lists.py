class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list_dict1 = {}
        list_dict2 = {}
        for i in range(0, len(list1)):
            if list1[i] not in list_dict1:
                list_dict1[list1[i]] = i
        for i in range(0, len(list2)):
            if list2[i] not in list_dict2:
                list_dict2[list2[i]] = i
                
        answer = []
        min_index = float('inf')
        for key, val in list_dict1.items():
            if key not in list_dict2:
                continue
            elif list_dict1[key] + list_dict2[key] < min_index:
                answer = []
                answer.append(key)
                min_index = list_dict1[key] + list_dict2[key]
            elif min_index == list_dict1[key] + list_dict2[key]:
                answer.append(key)
        return answer