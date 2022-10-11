from collections import deque
def solve(n, nums, target):
    l,h=0,n-1
    while l<=h:
        i=l+(h-l)//2
        if nums[i]==target:
            return i
        if nums[i]>target:
            h=i-1
        else:
            l=i+1
    return -1

if __name__ == '__main__':
	n = int(input())
	nums = list(map(int, input().split()))
	target = int(input())
	out = solve(n, nums, target)
	print(out)
