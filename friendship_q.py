Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#word from the first friend
word =input("Enter the word: ")
word=word.lower()

#inputting the meaningful word with the exact same letters
test_word = input("Enter a new meaningful word using the exact same letters to test your friendship: ")
test_word=test_word.lower()

#defining the dictionary
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count
#shopkeeper input to verify the word's meaning
def userinput():
    if count_in_dict(word) != count_in_dict(test_word):
        print("The letters aren't exact, friendship is fake")
        return
    ans = input("Does the word makes sense?(y or n): ")

    if ans == 'y':
        print("The friends pass the friendship test")
    elif ans == 'n':
        print("The word doesn't have a meaning, friendship is fake")
    else:
        print("Invalid input,try again with y or n")
        userinput()
userinput()