class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map_ = {}
        nextGreater = []
        stack = []
        
        for i in range(len(nums2)):
            while stack and  nums2[i] > stack[-1]:
                map_[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
        
        for i in range(len(nums1)):
            nums1[i] = map_.get(nums1[i]) or -1
        
        return nums1