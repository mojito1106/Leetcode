

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* decompressRLElist(int* nums, int numsSize, int* returnSize){
    
    int i,j=0;
    *returnSize = 0;
    int* result=malloc(sizeof(int)*5000);
    for(i=0;i<numsSize;i++){
        if (i%2==1){
            for(; j<(*returnSize)+nums[i-1]; j++){
                 result[j] = nums[i];
            }
            
            *returnSize=j;
        }
    }
    return result;
}
