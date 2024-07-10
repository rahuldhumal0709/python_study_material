def CountSwap(s, n):
    s = list(s)
    count = 0
    ans = True
    for i in range(n // 2):
	    left = i
	    right = n - left - 1
	    while left < right:
	        if s[left] == s[right]:
                break
            else:
                right -= 1
    if left == right:
        ans = False
        break
    else:
        for j in range(right, n - left - 1):
            (s[j], s[j + 1]) = (s[j + 1], s[j])
            count += 1
    if ans:
        return (count)
    else:
        return -1
s = input()
n = len(s)
ans1 = CountSwap(s, n)
ans2 = CountSwap(s[::-1], n)
print(max(ans1, ans2))

	

