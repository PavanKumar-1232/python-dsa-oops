#############################################################recursion#############################
#fibonacci num
"""def fibbo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibbo(n-1)+fibbo(n-2)
print(fibbo(10)) """
#climbing staris
"""def climbing_stairs(n):
    if n==0:
        return 0
    if n==1:
        return 1
    prev,curr=1,1
    for i in range(2,n+1):
        prev,curr=curr,prev+curr
    return curr
print(climbing_stairs(5))"""
#power(x,n)
"""def pow(x,n):
    if n==0:
        return 1
    if n<0:
        x=1/x
        n=-n
    if n%2==0:
        half=pow(x,n//2)
        return half*half
    else:
        half=pow(x,n//2)
        return half*half*x
print(pow(2,10))"""
#reverse string
"""def reverse(s):
    if len(s)==0:
        return ""
    return s[-1]+reverse(s[:-1])
print(reverse("pavan"))"""
#maximum depth of binary tree
"""def max_depth(root):
    if root is None:
        return 0
    left_depth=max_depth(root.left)
    right_depth=max_depth(root.right)
    return max(left_depth,right_depth)+1
print(max_depth([3,9,20,None,None,15,7]))"""
#check if array is sorted
"""def is_sorted(arr):
    if len(arr)<=1:
        return True
    if arr[0]>arr[1]:
        return False
    return is_sorted(arr[1:])
print(is_sorted([1,2,3,4,5]))"""
#count occurences of a given element in array
"""def count_ele(arr,ele):
    if len(arr)==0:
        return 0
    count=1 if arr[0]==ele else 0
    return count + count_ele(arr[1:],ele)
print(count_ele([1,2,3,2,4,2],2))"""
#product of an array
"""def product_arr(arr):
    if len(arr)==0:
        return 1
    if len(arr)==1:
        return arr[0]
    return arr[0]*product_arr(arr[1:])
print(product_arr([1,2,3,4]))"""
#find max num in arr
"""def max_ele(arr):
    if len(arr)==1:
        return arr[0]
    mid=len(arr)//2
    left_max=max_ele(arr[:mid]) 
    right_max=max_ele(arr[mid:])
    return max(left_max,right_max)
print(max_ele([1,5,3,9,2]))"""
#find first occurence of an element in arr
"""def first_orr(arr,tar,idx):
    if idx==len(arr):
        return -1
    if arr[idx]==tar:
        return idx
    return first_orr(arr,tar,idx+1)
print(first_orr([1,2,3,4,2,5],2,0))
"""