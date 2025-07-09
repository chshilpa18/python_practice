def raise_to_power(base_num, pow_num):
    res = 1;
    for index in range(pow_num):
        res = res * base_num
    print(res)



raise_to_power(3, 3)