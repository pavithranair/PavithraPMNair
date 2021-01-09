def near_square(num):
    if num < 0:
        return 0
    else:
        for i in range(num, 0, -1):
            print(i)
            if i*i <= num:
                return(i*i)
near_square(5)
