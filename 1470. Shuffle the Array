class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        
        
        
        """O(n)
        count = 0;
        result = [0]*len(nums); //Initialization(given the size of array) 
        for i in range(n):
            result[count] = nums[i]; //also can use result.append(nums[i) with the initialization result[]
            count += 1;
            result[count] = nums[i+n];
            count += 1;
        return result; """
        
        
        
        """O(n^2)
        count = 0;
        j_start = n;
        result = [0]*len(nums);
        for i in range(n):
            result[count] = nums[i];
            count += 1;
            for j in range(j_start,2*n):
                result[count] = nums[j];
                count += 1;
                if count % 2 == 0:
                    break;
            j_start += 1;
        return result; """
