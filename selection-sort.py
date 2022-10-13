#User function Template for python3

class Solution: 
  
    def select(self, arr, i):
        for i in range(len(arr)):
            small = i
            for j in range(i+1,len(arr)):
                if arr[small] > arr[j]:
                    small = j
        return arr[small]
    
    def selectionSort(self, arr,n):
        for i in range(n):
            small = i
            for j in range(i+1,n):
                if arr[small] > arr[j]: 
                    small = j
   
            (arr[i],arr[small])= (arr[small],arr[i])
                    
       
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
