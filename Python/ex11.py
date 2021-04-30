def count_letter(word,letter):
    count=0
    for l in word:
        if l==letter:
            count=count+1
    return count
word=input('Enter a word: ')
letter=input('Enter a letter in word: ')
count=count_letter(word,letter)
print(count)
