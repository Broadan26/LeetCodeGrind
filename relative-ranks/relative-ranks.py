class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Sort initial list descending
        sorted_scores = sorted(score, reverse = True)
        
        # Create a mapping for medal names
        awards = ['Gold Medal', 'Silver Medal', 'Bronze Medal'] + [str(i) for i in range(4, len(score)+1)]
        
        #Map sorted scores to medal names
        score_awards = {score: award for score, award in zip(sorted_scores, awards)}
        
        # Return the mapped list
        return [score_awards[sc] for sc in score]