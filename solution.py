#User function Template for python3
from itertools import combinations 
class Solution:
    def subsets(self, A):
        #code here
        n = len(A)
        res = []
        for i in range(1 << n):
            sub = []
            for j in range(n):
                if i & (1 << j):
                    sub += [A[j]]
            res.append(sub)
        return sorted(res)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        A = list(map(int,input().strip().split()))
        
        ob=Solution()
        result =ob.subsets(A)
        
        for i in range(len(result)):
            for j in range(len(result[i])):
                print(result[i][j],end=" ")
                
            print()
            
            

# } Driver Code Ends
