class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistry = 0

        left = 0
        right = len(skill) - 1
        comp = skill[left] + skill[right]

        while left <= right:
            if skill[left] + skill[right] == comp:
                chemistry += skill[left] * skill[right]
                left += 1
                right -= 1
            else:
                return -1

        return chemistry
