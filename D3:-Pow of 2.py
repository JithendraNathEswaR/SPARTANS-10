for m in range(2):
    x = int(input( ))
    if bin(x).count('1') == 1:
        print("Given num is power of 2")
    else:
        print("Given num is not power of 2")
