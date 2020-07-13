

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* smallerNumbersThanCurrent(int* nums, int numsSize, int* returnSize){
     // faster than 87.4%
    *returnSize = numsSize; 
    int* result=malloc(sizeof(int)*numsSize);
    int i,j,k,a ;
    int aarary[101];
    for(a=0;a<101;a++){
        aarary[a]=0; //要初始化,不然只會是記憶體的一塊空間，有可能上面會有值
    }
    
    for(i=0;i<numsSize;i++){
        aarary[nums[i]]++;
        result[i]=0;//要記得給他初始化一下
    }
    for(j=0;j<numsSize;j++){
        for(k=0;k<nums[j];k++){
            result[j]+=aarary[k];
        }
    }
    return result;
    /* faster than 55%
    *returnSize = numsSize; //*表取出該returnSize的值
    int* result=malloc(sizeof(int)*numsSize);
    int i,j;
    int count;
    for(i=0;i<numsSize;i++){
        count=0;
        for(j=0;j<numsSize;j++){
            if (nums[i]>nums[j]) count++;
        }
        result[i]=count;
    }
    return result;
    */
}
