def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for roll in range(len(game)):
        if game[roll] == '/':
            result += 10 - get_value(game[roll-1])
        else:
            result += get_value(game[roll])

        if frame < 10 and get_value(game[roll]) == 10:

            if game[roll] == '/':
                result += get_value(game[roll+1])

            elif game[roll] in ['X', 'x']:
                result += get_value(game[roll+1])

                if game[roll+2] == '/':
                    result += 10 - get_value(game[roll+1])
                else:
                    result += get_value(game[roll+2])
        if not in_first_half or game[roll] in ['X', 'x']:
            in_first_half = True
            frame += 1
        else:
            in_first_half = False
    return result


def get_value(char):
    if char in [str(num) for num in range(1, 11)]:
        return int(char)
    elif char in ['X', 'x', '/']:
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
