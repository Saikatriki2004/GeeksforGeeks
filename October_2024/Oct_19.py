class Solution:
    def roundToNearest (self, str) : 
        #Complete the function
        n = len(str)
        s = list(str)
        c = s.copy()

        if (c[n - 1] == '0'):
            return ("".join(s))
            
        elif (c[n - 1] >= '1' and c[n - 1] <= '5'):
            c[n - 1] = '0'
            return ("".join(c))

        else:
            c[n - 1] = '0'
            for i in range(n - 2, -1, -1):
                if (c[i] == '9'):
                    c[i] = '0'
                else:
                    t = ord(c[i]) - ord('0') + 1
                    c[i] = chr(48 + t)
                    break
                
        s1 = "".join(c)
        if (str[0] == '9' and s1[0] == '0'):
            s1 = "1" + s1
            
        return s1