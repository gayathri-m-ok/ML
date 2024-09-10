def count_pairs_with_sum(arr, t_sum):
    count = 0
    seen = set()
    
    for number in arr:
        complement = t_sum - number
        if complement in seen:
            count += 1
        seen.add(number)
    
    return count

arr = [2, 7, 4, 1, 3, 6]
t_sum = 10


result = count_pairs_with_sum(arr, t_sum)
print("Number of pairs with sum equal to 10:", result)
