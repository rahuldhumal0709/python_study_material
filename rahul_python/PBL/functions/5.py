# Write a function to print the even numbers from a given list.List is passed as an argument to the function.
def evennumbers(lst):
    for i in lst:
        if i%2 == 0:
            print(i, end = " ")
        else:
            continue
MyList = [5,8,7,10,48]
evennumbers(MyList)