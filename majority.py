def majority(nums) :
    a = None
    count =0
    for i in nums:
        if count ==0:
            a=i
        elif a==i:
            count+=1
        else:
            -1
    
    return a if nums.count(a)>len(nums) //2 else None
nums = [2,3,2,2,4,7]
print(majority(nums))
