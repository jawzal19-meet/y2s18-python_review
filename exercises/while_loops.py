# Write your solution for 1.3 here!

# sum=0
# add=1
# c=0
# while (sum<=10000):
#     sum=sum+add
#     add=add+1
# print (sum)
# print(add)


sum=0
add=1
c=0
while(sum<=10000):
    if add%2==0:
        sum=sum+add
    add=add+1
print(sum)
print(add)
