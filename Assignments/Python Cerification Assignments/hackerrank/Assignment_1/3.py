if __name__ == '__main__':
    main_lst=[]
    for i in range(int(input())):
        lst=[]
        name = input()
        lst.append(name)
        score = float(input())
        lst.append(score)
        main_lst.append(lst)
    print(main_lst)
        