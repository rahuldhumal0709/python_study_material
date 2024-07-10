def letter(cls,input1):
    arr = [0]*26
    arr[1] = 1
    for i in range(2,26):
        arr[i] += arr[i-1]+arr[i-2]
    
    ans =0
    for i in input1:
        a = ord(i) - 65
        ans += arr[a]
    
    return ans