#py
class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        while(num != 0): 
            if(num % 2 == 0):
                num /= 2
                count += 1
            else:
                num -= 1
                count += 1
        return count
//
int numberOfSteps (int num){
    
    int n=num;
    int i=0;
    while(n>0){
        if(n%2==0) {
            n=n/2;
            i++;
        }
        else{
            n--;
            i++;
        }
        
    }
    return i;
}
