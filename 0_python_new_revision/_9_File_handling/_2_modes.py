# r - read mode(allows to read the data from file), bydefault mode, it doesnot create the file if it doesn't exist.

# file = open('//home//nexgensis//rahul//self_learning//python_study_material//Atm_statement.txt')
# data = file.read()
# print(data)
# file.close()

# with open('//home//nexgensis//rahul//self_learning//python_study_material//Atm_statement1.txt',mode='r') as file:
#     data = file.read()
#     print(data)
# is_closed = file.closed
# print("Is close : ",is_closed)

with open('//home//nexgensis//rahul//self_learning//python_study_material//demo55.txt',mode='a+') as file:
    # data = file.write('Demo file')
    current_position1 = file.tell()
    print(current_position1)
    data1 = file.write("Hello India")
    current_position = file.tell()
    print(current_position)
    file.seek(current_position1,0)
    current_position = file.tell()
    print(current_position)
    data = file.read()
    print(data)
    # print(data)