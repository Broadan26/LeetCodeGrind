class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        length = len(deck)
        index = [i for i in range(length)] # Create index copy of deck
        answer = [None] * length # Create new deck to slot into
        deck.sort() # Sort deck to mirror index copy
        
        for card in deck:
            answer[index.pop(0)] = card # Pop in order
            if index: # Move new first element to back
                index.append(index.pop(0))
        return answer