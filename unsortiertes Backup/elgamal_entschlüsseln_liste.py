def elgamal_decode_dic(arr_y, k_m_inv, mod):
    dic_x = {}
    for i in range(len(arr_y)):
        dic_x[str(arr_y[i])] = arr_y[i] * k_m_inv % mod
    return dic_x

def elgamal_decode_arr(arr_y, k_m_inv, mod):
    arr_x = []
    for i in arr_y:
        arr_x.append(i * k_m_inv % mod)
    return arr_x

mod = 41#int(input("Gruppenindex: "))
arr_len = 14#int(input("Anzahl y: "))
arr = [18,18,18,7,35,4,23,11,29,37,34,27,29,28]
# for i in range(arr_len):
#     arr.append(int(input("y: ")))
print("Gruppenindex: 41")
print("Anzahl y: 14")
print("y:", str(arr))
k_m_inv = int(input("inverse von K_m: "))
print("y: x")
print(elgamal_decode_arr(arr, k_m_inv, mod))