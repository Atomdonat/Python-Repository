def dec_to_text(arr):
    x = ""
    for i in arr:
        if i == 1:
            x += "a"
        elif i == 2:
            x += "b"
        elif i == 3:
            x += "c"
        elif i == 4:
            x += "d"
        elif i == 5:
            x += "e"
        elif i == 6:
            x += "f"
        elif i == 7:
            x += "g"
        elif i == 8:
            x += "h"
        elif i == 9:
            x += "i"
        elif i == 10:
            x += "j"
        elif i == 11:
            x += "k"
        elif i == 12:
            x += "l"
        elif i == 13:
            x += "m"
        elif i == 14:
            x += "n"
        elif i == 15:
            x += "o"
        elif i == 16:
            x += "p"
        elif i == 17:
            x += "q"
        elif i == 18:
            x += "r"
        elif i == 19:
            x += "s"
        elif i == 20:
            x += "t"
        elif i == 21:
            x += "u"
        elif i == 22:
            x += "v"
        elif i == 23:
            x += "w"
        elif i == 24:
            x += "x"
        elif i == 25:
            x += "y"
        elif i == 26:
            x += "z"
        elif i == 27:
            x += "ä"
        elif i == 28:
            x += "ö"
        elif i == 29:
            x += "ü"
        elif i == 30:
            x += "ß"
        elif i == 31:
            x += " "
        elif i == 32:
            x += "!"
        elif i == 33:
            x += "?"
        elif i == 34:
            x += "."
        elif i == 35:
            x += ","
        elif i == 36:
            x += ";"
        elif i == 37:
            x += "1"
        elif i == 38:
            x += "2"
        elif i == 39:
            x += "3"
        elif i == 40:
            x += "4"
    return x

arr_x = [18,18,18,7,35,4,23,11,29,37,34,27,29,28]
print(dec_to_text(arr_x))
        
        