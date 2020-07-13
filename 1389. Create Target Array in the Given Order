

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* createTargetArray(int* nums, int numsSize, int* index, int indexSize, int* returnSize){
    
    int i,j;
    int* result = malloc(sizeof(int)*numsSize);
    
    for(i=0;i<indexSize;i++){
        
        if(index[i]!= i){
            
            int tmp=nums[i]; //先保留,為了要讓其他職等下往後移
            for(j=index[i];j<i;j++){
                index[j]+=1; //index值順移
                //nums[i]=nums[i-1];
                //nums[index[i]]=tmp;
                //i--;
                
            }
                       
        }
        result = nums ;
               
    }
    return result;
    
    /*解法一
    int i,j;
    *returnSize =numsSize;
    int* result = malloc(sizeof(int)*numsSize);
    
    for(i = 0; i < indexSize; i++){
        
        if(index[i] < returnSize-1){
            for(j=*returnSize-1;j>index[i];j--){   //順移 //回傳直要加*才是整數
                result[j]=result[j-1];
            }
                   
        }
        result[index[i]] = nums[i];
           
    }
    return result;
    */
    
}
