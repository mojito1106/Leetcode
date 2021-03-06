//py
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum_list = [[0]*1 for _ in range(len(nums))] #一定要先定義list的長度
        sum_list[0] = nums[0]
        for i in range(1,len(nums)):
            sum_list[i] = sum_list[i-1] + nums[i]
        return sum_list
        
        ''' append的速度會慢很多
        sum_list = []
        #sum_list = [nums[0]]
        for i in range(1,len(nums)):
            sum_list.append(sum(nums[:i+1]))
        return sum_list
        '''

//c++
class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> wade(nums.size());
        wade[0] = nums[0];
        for(int i=1; i < nums.size(); i++) {
            wade[i] = nums[i];
            wade[i] += wade[i-1];
        }
        return wade;
    }
};
