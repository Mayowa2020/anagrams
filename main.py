# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):

    # remove all spaces between characters and convert the characters to lowercase
    word = word.replace(" ", "").lower()
    anagram = anagram.replace(" ", "").lower()

    # create a dictionary
    di = {}

    if len(word) != len(anagram):  
        return False

    for i in word:
        if i in di:
            di[i] += 1
        else: 
            di[i] = 1

    for i in anagram:
        if i in di:
            di[i] -= 1   
        else:
            di[i] = 1

    for i in di:
        if di[i] != 0:        
            return False
    return True             


print(find_anagram("fairy tales", "rail safety"))

print(find_anagram("hello", "check"))


