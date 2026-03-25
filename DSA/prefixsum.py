##########################################prefix sum ############################
#running total difference
"""def running_total(nums):
    n=len(nums)
    pre_sum=0
    ans=[]
    tot_sum=sum(nums)
    for i in range(n):
        pre_sum+=nums[i]
        right_sum=tot_sum-pre_sum+nums[i]
        ans.append(abs(pre_sum-right_sum))
    return ans    
print(running_total([10,4,8,3]))"""
#range query counter
"""def range_query(arr,query):
    n=len(arr)
    pre_sum=[0]*n
    pre_sum[0]=arr[0]
    for i in range(1,n):
        pre_sum[i]=pre_sum[i-1]+arr[i]
    ans=[]
    for l,r in query:
        if l==0:
            ans.append(pre_sum[r])    
        else:
            ans.append(pre_sum[r]-pre_sum[l-1])    
    return ans
print(range_query(arr=[1,2,3,4,5],query=[[0,2],[1,3],[0,4]]))"""
#count zero sum subarrays
"""def sum_zero(arr):
    n=len(arr)
    pre_sum=0
    freq={}
    ans=0
    for i in range(n):
        pre_sum+=arr[i]
        if pre_sum==0:
            ans+1
        if pre_sum in freq:
            ans+=freq[pre_sum]
        freq[pre_sum]=freq.get(pre_sum,0)+1
    return ans
print(sum_zero([1,-1,2,-2,3,-3,4]))    """
#longest balanced subarrayof 1 and -1
"""def longest_balance(arr):
    n=len(arr)
    pre_sum=0
    freq={}
    ans=0
    for i in range(n):
        pre_sum+=arr[i]
        if pre_sum in freq:
            ans=max(ans,i-freq[pre_sum])
        else:
            freq[pre_sum]=i 

    return ans
print(longest_balance([1,-1,1,1,-1,-1,1,-1]))"""