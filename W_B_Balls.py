white = int(input("Enter the number of white balls: "))
black = int(input("Enter the number of black balls: "))

i = 1  

while True:
    if i % 2 != 0:  #odd row,white balls
        if white >= i:
            white -= i
        else:
            break
    else:  #even row, black balls
        if black >= i:
            black -= i
        else:
            break
    i += 1

print("The height of Balls Triangle:", i - 1)
