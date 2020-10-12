'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    input_len = len(word)
    target_len = 2
    target_phr = 'th'
    
    # Base Case definition:
    if input_len == 0 or input_len < target_len:
        return 0

    # Recursive Case
    # Check if the first two letters match and increment by one.
    if word[0 : target_len] == target_phr:
        return count_th(word[target_len - 1:]) + 1

    # Second case is count from the remaining index.
    return count_th(word[target_len - 1:])
