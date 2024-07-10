# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# 56.00

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total=0
    ele=0
    for i in student_marks[query_name]:
        ele=ele+1
        total=total+i
    avg=total/ele
    print('%.2f' % avg)