class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # this is 40 ms

        # hash Table approach
        
        # search and insert
        hash_set = set()
        for i in nums:
            if i in hash_set:
                return True
            hash_set.add(i)
        return False
        '''
        debug output
        nums:  [1,2,3,1]
        when: i = 1 at index 0
        hash_set: {1}
        i: 1 
        when: i = 1 at index 3, skip duplicate
        hash_set: {1, 2, 3} 
        i: 1 
        '''
    
        
        '''
        # this is 55 ms
        sorting and searching algorithm

        # sorting
        nums = sorted(nums)

        # searching
        for i in range(len(nums)):
            if nums[i] == nums[i + 1]:
                return True
            else:
                return False
        '''