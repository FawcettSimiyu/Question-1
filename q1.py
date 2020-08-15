email = 'example_key'

def cat(password, limit):

    num_incorrect = 0
    index = 0
    def attempt(digit):
        nonlocal num_incorrect
        nonlocal index
        if (num_incorrect >= limit):
            return 'The safe is now inaccessible!'
        if (password[index] == digit):
            index += 1
            if (index == len(password)):
                return 'Successfully unlocked!'
        else:
            num_incorrect += 1
    return attempt#     return ______
