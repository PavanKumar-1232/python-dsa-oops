##################################################sliding window##############################################
#Maximum Sum Subarray of Size K
"""class solution:
    def max_sum(arr,k):
        n=len(arr)
        k = 3
        l=0
        temp=0
        ans=float("-inf")
        for r in range(n):
            temp+=arr[r]
            if r-l+1>k:
                temp-=arr[l]
                l+=1
            if r-l+1==k:
                ans=max(ans,temp)
        return ans
print(solution.max_sum([2,1,5,1,3,2],3))"""
#First Negative Integer in Every Window of Size K
#nums = [12,-1,-7,8,-15,30,16,28]
"""class solution:
    def first_neg(arr,k):
        n=len(arr)
        l=0
        ans=[]
        che=[]
        for r in range (n):
            if arr[r]<0:
                che.append(arr[r])
            if r-l+1==k:
                if che:
                    ans.append(che[0])
                else:
                    ans.append(0)
                if che and arr[l]==che[0]:
                    che.pop(0)
                l+=1
        return ans            
print(solution.first_neg([12,-1,-7,8,-15,30,16,28],3))"""
#count distinct elements in every window of size k
"""class solution:
    def distint_ele(arr,k):
        n=len(arr)
        l=0
        ans=[]
        freq={}
        for r in range(n):
            freq[arr[r]]=freq.get(arr[r],0)+1
            if r-l+1>k:
                freq[arr[l]]-=1
                if freq[arr[l]]==0:
                    del freq[arr[l]]
                l+=1
            if r-l+1==k:
                ans.append(len(freq))
        return ans   
print(solution.distint_ele([1,2,1,3,4,2,3],4))    """      
#maximum num of vowels in a substring of given length k
"""class solution:
    def max_vowles(s,k):
        n=len(s)
        vowles=set("aeiou")
        ans=0
        l=0
        count=0
        for r in range(n):
            if s[r] in vowles:
                count+=1
            if r-l+1>k:
                if s[l] in vowles:
                    count-=1
                l+=1
            if r-l+1==k:
                ans=max(ans,count)
        return ans      
print(solution.max_vowles("abciiidef",3))"""
#avg of all subarrays of size k
"""class solution:
    def avg_sub(arr,k):
        n=len(arr)
        l=0
        temp=0
        ans=[]
        for r in range(n):
            temp+=arr[r]
            if r-l+1>k:
                temp-=arr[l]
                l+=1
            if r-l+1==k:
                ans.append(temp/k)
            return ans
print(solution.avg_sub([1,3,2,6,-1,4,1,8,2],5)) """                 
#minimum size subarray sum
"""class solution:
    def min_size(arr,target):
        n=len(arr)
        l=0
        ans=float("inf")
        temp=0
        for r in range(n):
            temp+=arr[r]
            while temp>=target:
                ans=min(temp,r-l+l)
                temp-=arr[l]
                l+=1
            if ans==float("inf"):
                return 0
        return ans   
print(solution.min_size([2,3,1,2,4,3],7))   
"""
#longest substring without repeating characters
"""class solutions:
    def longest_substring(arr):
        n=len(arr)
        l=0
        seen=set()
        ans=0
        for r in range(n):
            ch=arr[r]
            if ch not in seen:
                seen.add(ch)
            else:
                while ch in seen:
                    seen.remove(ch)
                    l+=1
                seen.add(ch)
            ans=max(ans,r-l+1)
        return ans            
print(solutions.longest_substring("abcabcbb")   )"""
#3sum
"""def three_sum(arr,target):
    res=[]
    for i in range(len(arr)-2):
        l,r=i+1,len(arr)-1
        while l<r:
            currsum=arr[i]+arr[l]+arr[r]
            
            if currsum==target:
                res.append((arr[i],arr[l],arr[r]))
                l+=1
                r-=1
            elif currsum<target:

                l+=1
            else:
                r-=1
    return res                    
print(three_sum([-1,0,1,2,-1,-4],0))"""
#max sum of any sub array of size k arr=[1,2,1,3,4,2,3] k=2
"""def max_size(arr,k):
    n=len(arr)
    l=0
    ans=float("-inf")
    temp=0
    for r in range(n):
        temp+=arr[r]
        if r-l+1>k:
            temp-=arr[l]
            l+=1
        if r-l+1==k:
            ans=max(ans,temp)    
    return ans 
max_size(arr=[1,2,1,3,4,2,3],k=2)       """
#max sum of dist ele of arr in size k

"""def max_dist(arr,k):
    n=len(arr)
    l=0
    ans=float("-inf")
    temp=0
    seen={}
    for r in range(n):
        seen[arr[r]]=seen.get(arr[r],0)+1
        temp+=arr[r]
        while seen[arr[r]]>1 or r-l+1>k:
            seen[arr[l]]-=1
            temp-=arr[l]
            if seen[arr[l]]==0:
                del seen[arr[l]]
            l+=1
        if r-l+1==k:
            ans=max(ans,temp)
    return ans
print(max_dist(arr=[1,2,1,3,4,2,3],k=2))"""
#longest substring with at most k zeroes
"""def at_most(arr,k):
    n=len(arr)
    l=0     
    temp=0
    target=0
    ans=0
    for r in range(n):
        if arr[r]==0:
            temp+=1
        target+=arr[r]    
        while temp>k:
            if arr[l]==0:
                temp-=1
            target-=arr[l]
            l+=1
        ans=max(ans,r-l+1)
    return ans  
print(at_most(arr=[1,0,1,0,1],k=1))         
"""
#excat k even numbers nums=[1,2,1,3,4,2,3] k=2
"""def excat_k_even(arr,k):
    def excat_even(arr,k):
        n=len(arr) 
        l=0
        temp=0
        ans=0
        for r in range(n):
            if arr[r]%2==0:
                temp+=1
            while temp>k:
                if arr[l]%2==0:
                    temp-=1
                l+=1
            ans=r-l+1
        return ans
    return excat_even(arr,k)-excat_even(arr,k-1)
print(excat_k_even(arr=[1,2,1,3,4,2,3],k=2))  """           
#min subarray with atleast 2 vowles and 1 consonant
"""def sub_arr(s):
    n=len(s)
    l=0
    vowles=set("aeiou")
    contants=set("bcdfghjklmnpqrstvwxtz")
    vowl_count=0
    cont_count=0
    ans=float("inf")
    for r in range(n):
        if s[r] in vowles:
            vowl_count+=1
        if s[r] in contants:
            cont_count+=1
        while vowl_count>=2 and cont_count>=1:
            ans=min(ans,r-l+1) 
            if s[l] in vowles:
                vowl_count-=1
            if s[l] in contants:
                cont_count-=1
            l+=1
    return ans if ans!=float("inf") else 0
print(sub_arr("aeiobcdfg")) """                             
#product range subaray between 2 numbers
"""import re
def product_range(arr,l,r):
    def product_blw(arr,l,r):
        n=len(arr)
        i=0
        ans=0
        temp=1
        for j in range(n):
            temp*=arr[j]
            while temp>=l and i<=j:
                if temp<=r:
                    ans+=j-i+1
                temp//=arr[i]
                i+=1    
        return ans
    return product_blw(arr,l,r)-product_blw(arr,l-1,r)
print(product_range(arr=[10,5,2,6],l=100,r=1000))  """                   
#hashmap and hashset
#twosum
"""def two_sum(arr,target):
    seen={}
    result=[]
    for num in arr:
        diff=target-num
        if diff in seen:
            result.append((diff,num))
        seen[num]=seen.get(num,0)+1
    return result       
print(two_sum([2,7,11,15],9))
"""
#valid anagram
"""def is_anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    freq={}
    for ch in s1:
        freq[ch]=freq.get(ch,0)+1
        for ch in s2:
            if ch not in freq:
                return False
            
    return True
print(is_anagram("listen","silent"))"""