class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #writing my own sort function; increases time complexity to O(n*k^2)
        def insertion_sort(arr):
            arr = list(arr)
            n = len(arr)
            for i in range(n-1):
                for j in range(i+1, 0, -1):
                    if arr[j] < arr[j-1]:
                        arr[j], arr[j-1] = arr[j-1], arr[j]
                    else:
                        break
            return ''.join(arr)
            
        hashMap = { }
        ans = [ ]
        
        for word in strs:
            sorted_word = "".join(insertion_sort(word))
            if sorted_word not in hashMap:
                hashMap[sorted_word] = []
            hashMap[sorted_word].append(word)
  
        for item in hashMap:
            ans.append(hashMap[item])
        return ans

"""
time: O(n*klogk), where n = length of array, k = length of the longest string
space: O(m), where m = number of groups
"""     
