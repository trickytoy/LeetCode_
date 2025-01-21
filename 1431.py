def kidsWithCandies(candies, extraCandies):
    curr_max = max(candies)
    bool_array = []

    for i in candies:
        curr_total = i+extraCandies
        print(curr_total)
        if (i+extraCandies > curr_max):
            bool_array.append(True)
        else:
            bool_array.append(False)

    return bool_array

print(kidsWithCandies([2,3,5,1,3], 3))