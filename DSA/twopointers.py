############################################################two pointers#########################################################
#swaping array
"""def rotate(arr):
    l,r=0,len(arr)-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr"""
#check palindrome string
"""def ispalindrome(s):
    s=s.strip().lower()
    l,r=0,len(s)-1
    while l<r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True    """
#remove duplicates from sorted array
"""import re


def remove_dup(arr):
    if len(arr)<=1:
        return arr
    j=0
    for i in range(len(arr)-1):
        if arr[i]!=arr[i+1]:
            arr[j]=arr[i]
            j+=1
    return arr[:j]    
print(remove_dup([1,1,2,2,3,4,4,5]))"""
#remove an given element
"""def remove_ele(arr,ele):
    j=0
    for i in range(len(arr)-1):
        if arr[i]!=ele:
            arr[j]=arr[i]
            j+=1
    return arr[:j]    
print(remove_ele([1,2,3,4,2,5],2))
    """
#move all zeros to an end
"""def move_zeros(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[j]=arr[i]
            j+=1
    for i in range(j,len(arr)):
        arr[i]=0
    return arr    
print(move_zeros([0,1,0,3,12,0,5]))    """  
#check subsequence
"""def is_subsequence(s1,s2):
    l1=len(s1)
    l2=len(s2)
    i,j=0,0
    while i<l1 and j<l2:
        if s1[i]==s2[j]:
            i+=1
            j+=1
        else:
            j+=1    
    return i==l1
print(is_subsequence("abc","ahbgdc"))     """      
#pair with given sum
"""def pair_sum(arr,target):
    l,r=0,len(arr)-1
    while l<r:
        currsum=arr[l]+arr[r]
        if currsum==target:
            return True
        elif currsum<target:
            l+=1
        else:
            r-=1
    return False
print(pair_sum([1,2,3,4,5,6],10))    """        
#container with most water
"""def conatiner(arr):
    j=len(arr)-1
    for i in range(len(arr)-1):
        if arr[i]<=arr[j]:
            area=arr[i]*(j-i)
        else:
            area=arr[j]*(j-i)
        j-=1
    return area
print(conatiner([1,8,6,2,5,4,8,3,7])) """   
#triple with zerosum
"""def three_zero(arr):
    res=[]
    arr.sort()
    for i in range(len(arr)-2):
        l,r=i+1,len(arr)-1
        while l<r:
            currsum=arr[i]+arr[l]+arr[r]
            if currsum==0:
                res.append([arr[i],arr[l],arr[r]])
                l+=1
                r-=1
            elif currsum<0:
                l+=1
            else:
                r-=1
    return res"""