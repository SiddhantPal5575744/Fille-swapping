def swap():
    with open("test1.txt",'r') as a:
        data_a=a.read()
    with open("test2.txt",'r') as b:
        data_b=b.read()
    with open("test1.txt",'w') as a:
        a.write(data_b)
    with open("test2.txt",'w') as b:
        b.write(data_a)

    print(data_a)
    print(data_b)
swap()