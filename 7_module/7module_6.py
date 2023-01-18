def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if riddle.find(start_letter)==-1:
        return None
    first_index=riddle.find(start_letter)
    word=riddle[first_index:first_index+word_length]
    if reverse==True:
        word=riddle[first_index:first_index-word_length:-1]
    return word



riddle='riddle'
word_length=4
start_letter='l'
print(solve_riddle(riddle, word_length, start_letter, reverse=True))
