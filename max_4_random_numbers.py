import random

print("This program generates 4 random numbers than prints the biggest one")
a = random.random() * 100
b = random.random() * 100
c = random.random() * 100
d = random.random() * 100

print("I have generated these numbers: %.2f %.2f %.2f %.2f" % (a, b, c, d))
if a >= b and a >= c and a >= d:
    print("The biggest number is %.2f" % a)
elif b >= a and b >= c and b >= d:
    print("The biggest number is %.2f" % b)
elif c >= a and c >= b and c >= d:
    print("The biggest number is %.2f" % c)
else:
    print("The biggest number is %.2f" % d)


# determine the second largest number
def biggest(a=0, b=0, c=0, d=0):
    if a >= b and a >= c and a >= d:
        return a
    elif b >= a and b >= c and b >= d:
        return b
    elif c >= a and c >= b and c >= d:
        return c
    return d


nums = [a, b, c, d]

r = biggest(nums[0], nums[1], nums[2], nums[3])
print("The biggest number is %.2f" % r)
nums.remove(r)
r = biggest(nums[0], nums[1], nums[2])
print("The seconds biggest number is %.2f" % r)
nums.remove(r)
r = biggest(nums[0], nums[1])
print("The third biggest number is %.2f" % biggest(nums[0], nums[1]))
nums.remove(r)
r = biggest(nums[0])
print("The smallest number is %.2f" % nums[0])
