checker_list=input().split(", ")
second_list=input().split(", ")
founded_words=[checker for checker in checker_list for words in second_list if checker in words]

print(sorted(set(founded_words), key=founded_words.index))