def highest_occurrence(input_string):
    
    cleaned_string = ''.join(filter(str.isalpha, input_string)).lower()
    
    
    char_count = {}
    
    for char in cleaned_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
   
    max_char = max(char_count, key=char_count.get)
    max_count = char_count[max_char]
    
    return max_char, max_count

input_string = "PARROT"


max_char, max_count = highest_occurrence(input_string)
print(f"The highest occurring character is '{max_char}' with a count of {max_count}.")
