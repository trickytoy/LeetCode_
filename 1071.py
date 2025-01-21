def gcdOfStrings(str1, str2):
    curr_GCD = ""
    for i in range(len(str1)):
        if ((len(str1) % (i+1) == 0) and (len(str2) % (i+1) == 0)):
            str1_divisor =  int(len(str1)/(i+1))
            str2_divisor = int(len(str2)/(i+1))
            if ((str1[:(i+1)] * str1_divisor == str1) and (str1[:(i+1)] * str2_divisor == str2)):
                curr_GCD = str1[:(i+1)]

    return (curr_GCD)

print(gcdOfStrings("ABCABC", "ABC"))