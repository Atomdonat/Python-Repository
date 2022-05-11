def str_to_bin(text):
    return str(bin(int(str(text).encode('utf-8').hex(),16)))[2:].zfill(8)
    


