def replace_char_code(word:str):
    ch_code_str=''
    new_word=[]
    for ch in word:
        if ch.isnumeric():
            ch_code_str+=ch
        else:
            new_word.append(ch)
    ch_at_beginning = chr(int(ch_code_str))

    new_word.insert(0,ch_at_beginning)
    return new_word
def decifher_word(word:str):
    new_word=replace_char_code(word)
    new_word[1],new_word[-1]=new_word[-1], new_word[1]
    return "".join(new_word)
words=input().split()
decifher_words=[]
for word in words:
    decifher_words.append(decifher_word(word))
print(' '.join(decifher_words))

