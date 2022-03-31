def word_break(dictionary, word):
    #print(word)
    if word in dictionary:
        return True
        
    for i in range(1,len(word)):
        if word[:i] in dictionary:
            if word_break(dictionary, word[i:]):
                return True
            
    return False


n = input() 
dictionary = input()
word = input()
if word_break(dictionary, word):
    print(1)
else:
    print(0)