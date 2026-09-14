number=[2,3,4,5,6,7,8,9]
small=number[0]
large=number[0]
for i in number:
    if(i<small):small=i
    if(i>large): large=i

print(small)
print(large)
