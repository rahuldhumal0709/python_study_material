# remove last item of list

lst = [10,20,30,40,50]
lst = lst[:-1]
print(lst)

# remove a specific item using index

lst = [10,20,30,40,50]
n = int(input(f'Which item you want to delete using index(0-{len(lst)-1}) : '))
lst = lst[:n] + lst[n+1:]
print(lst)