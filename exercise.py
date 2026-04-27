moves = "UD"
move = list(moves)
i , j = 0 , 0
for x in move:
    if x == "L":
        i += 1
    elif x == "R":
        i -= 1
    elif x == "U":
        j += 1
    elif x == "D":
        j -= 1
if i == 0 and j == 0:
    return True
else:
    return False
