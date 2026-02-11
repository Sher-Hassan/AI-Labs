original_string = input("Enter original string: ")
sub_string = input("Enter sub-string: ")

count = 0
sub_length = len(sub_string)


for i in range(len(original_string)):
    
    
    chunk = original_string[i : i + sub_length]
    
    
    if chunk == sub_string:
        count = count + 1

print(count)