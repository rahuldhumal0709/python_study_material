def largestSubarray(cls,input1,input2):
    one =0
    zero =0
    ans =0
    for i in input2:
        if(i == 1):
            one +=1
        else:
            zero +=1
        ans = min(one,zero)
    return ans**2