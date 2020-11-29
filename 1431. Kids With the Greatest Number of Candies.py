#py
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        big = max(candies)
        res = [[0]*1 for _ in range(len(candies))]
        for i in range(len(candies)):
            if(candies[i] + extraCandies) < big:
                res[i] = False  #capital
            else:
                res[i] = True
        return res

//c 
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize){
    int max=0;
    int i,j;
    //bool* returnSize=malloc(sizeof(bool) * candiesSize);
    *returnSize = candiesSize; //*表示拿出該指標位置的value
    bool *result =  malloc(sizeof(bool) * candiesSize); //題目求的是回傳bool值
    for(i=0;i<candiesSize;i++){
        if (candies[i]>max) max=candies[i];
    }
    for(j=0;j<candiesSize;j++){
        if((candies[j]+extraCandies)>=max) result[j]=true; 
        else result[j]=false;
        //true,false不用加雙引號,不然會變成字串
    }
    
    return result;
    
}
