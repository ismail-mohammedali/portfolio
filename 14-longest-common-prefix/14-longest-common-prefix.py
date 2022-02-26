class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common_string =''
        temp_string = ''
        
        if len(strs)==0:
            return common_string
        for letter in strs[0]:
            temp_string += letter
            for string in strs: 
                if temp_string != string[0:len(temp_string)]: 
                    return common_string
                elif temp_string != string[0] and  len(temp_string)==1:
                    return common_string
            common_string = temp_string
        return common_string
            
        
        
                        
                    
            
       
            