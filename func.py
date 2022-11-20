
def sum_list(my_list):
    sum_num = 0
    for n in my_list:
        sum_num += n
    return sum_num


if __name__=="__main__":
    lis = [4, 6, 7, 8, 3, 89, 90]

    print(sum_list(lis))
