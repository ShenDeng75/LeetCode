
n, dist = map(int, input().split())
nums = list(map(int, input().split()))

res = 0
left = 0
right = 2

while left < n - 2:
    while right < n and nums[right] - nums[left] <= dist:
        right += 1
    if right - 1 - left >= 2:
        num = right - left - 1
        res += num * (num - 1) // 2
    left += 1

print(res % 99997867)
