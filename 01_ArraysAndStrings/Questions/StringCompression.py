# String Compression: 
# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. 
# If the "compressed" string would not become smaller than the original string, 
# your method should return the original string. You can assume the string has 
# only uppercase and lowercase letters (a - z)

# Solution: We can have two pointer. Frist one and Second one will point to current
# element and the next element to check if they are equal, write new string accordingly.


def find_string_compression(input):
    compressed = ""
    count = 1
    for i in range(len(input)):
        runnerup = i + 1
        if runnerup == len(input):
            compressed += (input[i] + str(count))
            break
        if input[i] != input[runnerup]:
            compressed += (input[i] + str(count))
            count = 1
        else: 
            count += 1

    if len(compressed) >= len(input):
        compressed = input
    return compressed
