<c++>
/*
integer x cannot use sizeof(x), it will turn out to be a memory size, not how many digits x has!!
sizeof can be use to count an array size!
any number bigger than 0 is standardized for "true"
*/

class Solution {
public:
    bool isPalindrome(int x) {
        
        if (x < 0) return false;
        if (x == 0) return true;
        else{
            int count = 0;
            int a = x;
            while(a>0){
                a = a/10;
                count ++;
            }
            int c[count] ;
            int b = x;
            for(int i = count-1; i > -1; i--)
            {
                c[i] = b%10;
                b = b/10;
                
            }
            for(int j = 0; j<count/2; j++)
            {
                if(c[j] != c[count-1-j]) return false;
            }
            return true;
        }
             
    }
};
