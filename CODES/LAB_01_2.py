def calculate_range(num):
    if len(num) < 3:
        return "Range determination not possible"
    else:
        return max(num) - min(num)


num = [5, 3, 8, 1, 0, 4]


res = calculate_range(num)
print("The range is:", res)
