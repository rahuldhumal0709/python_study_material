# WAP to print the number of occurrences of a specified element in a MyList.
MyList1=[10,20,10,40,50]
ele=10
count=0
for i in MyList1:
    if (i==ele):
        count=count+1
print('{} has occurred {} times'.format(ele,count))