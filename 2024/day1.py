

f = open("day1.txt", encoding="utf8")
nums1 = []
nums2 = []
for line in f:
    nums1.append(int(line.split()[0]))
    nums2.append(int(line.split()[1]))
print(nums1)
print(nums2)

#sort arrays
nums1.sort()
nums2.sort()

#for each element sum the differences
sum = 0

for i in range(len(nums1)):
    occurences = 0
    for j in range(len(nums2)):
        if(nums1[i] == nums2[j]):
            occurences+=1
    sum+=occurences* nums1[i]
print(sum)

