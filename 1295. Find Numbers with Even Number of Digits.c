

int findNumbers(int* nums, int numsSize){
    
    int num;
    int result=0;
    for(int i=0; i<numsSize; i++){
        int count = 0;
        num=nums[i];
        while(num!=0){
            num/=10;
            count++;
        }
        if(count%2==0) result++;
        
    }
    return result;
}
