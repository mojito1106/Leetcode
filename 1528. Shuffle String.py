#python3
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        
        value = ''
        #dict_list = {key:value for key,value in zip(s,indices)}
        #print (list(zip(s,indices)))
        dict_list = {indices[i]:s[i] for i in range(len(indices))}
        new_dict_list = sorted(dict_list.items())
        #print(type(new_dict_list))
        print (new_dict_list)
       
        for i in range(len(indices)):
            value += new_dict_list[i][1]
        return value

"""
#python
class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        #print (indices)
        #print (s)
        self.s = s
        self.t = s
        new_s = ''
        
        for i in range(len(indices)):
            for j in range(len(indices)):
                if i == indices[j]:
                    new_s += self.s[j]
        return new_s"""
