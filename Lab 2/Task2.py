input_str = input("IN : ")

char_counts = {}

for char in input_str:
    
    
    if char in char_counts:
        
        char_counts[char] = char_counts[char] + 1
    else:
        
        char_counts[char] = 1


result = ""
for char in char_counts:
   
    result = result + char + ":" + str(char_counts[char]) + ", "


print("OUT :", result[:-2])