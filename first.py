# goal is to check each position of the strings for common letters then remember these occurences so as to easily find a pair of strings with a common letter in the same position.

def solution(S):
    #step 1: initialize a dictionary to store occurences of letters in specific positions
    letter_positions = {}

    #step 2: populate the dictionary
    for i, string in enumerate(S):
        for pos , letter in enumerate(string):
            if (letter, pos) not in letter_positions:
                letter_positions[(letter, pos)] = [i]
            else:
                letter_positions[(letter, pos)].append(i) 
    
    #step 3: find a pair of strings with a common letter in the same position
    for (letter, pos), indexes in letter_positions.items():
        if len(indexes) > 1:
            #found a pair of strings, return their indexes and the position
            return [indexes[0], indexes[1], pos]
        
    #step 4: if no such pair is found, return an empty list
    return[]

example1 = ['abc', 'bca','dbe']
print(solution(example1))

# create a data structure to store letter positions
# populate the data structure
# find a pair of strings with a common letter in the same position
# return result 