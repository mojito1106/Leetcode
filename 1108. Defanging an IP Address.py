#py
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".","[.]")


//c
char * defangIPaddr(char * address){
    
   
    int i,j,k;
    j=strlen(address);
    char *result=malloc(sizeof(char)*30);
    i=0;
    k=0;
    while(i<j){
        
        if(address[i]=='.'){
            /*
            j+=2;
            for(k=j-1;k>i+2;k--){
                result[k]=address[k-2];
             */
            result[i+2*k]='[';
            result[i+2*k+1]='.';
            result[i+2*k+2]=']';
            
            i++;
            k++;
        }
            
            
           
            
        
        else {
            result[i+2*k]=address[i];
            i++;
        }
   
    }
    result[i+2*k]='\0';
     return result;
     
}
