class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        leftptr = 0
        rightptr = len(people) - 1
        boatNum = 0
        
        while leftptr < rightptr:
            if people[leftptr] + people[rightptr] <= limit:
                leftptr += 1
    
            rightptr -= 1    
            boatNum += 1
        if leftptr == rightptr:
            boatNum += 1
            
        return boatNum