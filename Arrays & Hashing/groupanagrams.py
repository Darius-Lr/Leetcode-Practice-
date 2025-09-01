class Solution:

    def groupAnagrams(self, strs):
        listtotal=[]
        used=[False]*len(strs)
        for i in range(len(strs)):
            if used[i] == True:
                continue
            formlist = [strs[i]]
            used[i] = True
            for  j in range(i+1,len(strs)):
                self.a=strs[i]
                self.b=strs[j]
                if self.isBool() == True:
                    formlist.append(strs[j])
                    used[j]=True
            listtotal.append(formlist)
        return listtotal




    def isBool(self):
        if len(self.a)!=len(self.b):
            return False
        for x in self.a:
            if self.a.count(x)!=self.b.count(x):
                return False
        return True


x=Solution()
print(x.groupAnagrams(["","b"]))
