list1 = [23,24,25,26,27,28,100]
print("Original List : ",list1)

sum = 0
for i in list1:
    sum += i

avg = sum / len(list1)
print("Sum : ", sum)
print("Average : ", avg)

print("Max Number : ",max(list1))
print("Min Number : ",min(list1))

list1.sort()
print("Smallest using sort : ", list1[0])
print("Largest using sort : ", list1[-1])