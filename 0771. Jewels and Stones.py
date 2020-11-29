#py
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        """
        count = 0
        for i in range(len(S)):
            for j in range(len(J)):
                if S[i] == J[j]:
                    count += 1
        return count"""
        count=0
        for x in J:
            count += S.count(x)
        return count
        
//c
int numJewelsInStones(char * J, char * S){
    
    int i,k,jj,count;
    
    count=0;
    for(i=0;i<strlen(J);i++){
        jj=J[i];
        for(k=0;k<strlen(S);k++){
            if (jj==S[k]) count++;
        }
    }
    return count;
}
