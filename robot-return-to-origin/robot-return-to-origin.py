class Solution:
    def judgeCircle(self, moves: str) -> bool:
        from collections import Counter
        move_dict = Counter(moves)
        return move_dict['U'] == move_dict['D'] and move_dict['L'] == move_dict['R']