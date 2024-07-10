# str1="this is a string"
# # split_demo=str1.split(" ")
# replace_demo = str1.replace(" ","-")
# print("Replace : ",replace_demo)
# print(replace_demo)

#correct
# def mutate_string(string, position, character):
#     l=list(s)
#     l[int(i)]=c
#     return ''.join(l)
# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

# ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']
# 3 s
# O/P : abrscadabra
string = "abracadabra"
l = list(string)
print(l)
i, c = input().split()
l[int(i)] = c
string = ''.join(l)
print (string)