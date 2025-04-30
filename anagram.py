a = input("Enter a word 1: ")
b = input("Enter a word 2: ")
if len(a) != len(b):
    print("Given word is  NOT anagram")
else:
    a = sorted(a.lower())
    b = sorted(b.lower())
    if a ==b:
        print("Given words are anagrams")
    else:
        print("NO")