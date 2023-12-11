# mengubah string ke kode biner
def konvertBiner(uji):
    # list berisi kode biner per karakter
    binary_list = []
    
    # pengubahan per karakter
    for char in uji:
        binary_list.append(bin(ord(char))[2:].zfill(8))
         
    return ''.join(binary_list)
 

if __name__ == "__main__":
    uji = input("Masukkan string yang ingin diubah : ")
    print()
    print(f"Panjang binernya adalah : {len(konvertBiner(uji))}")
    print()
    print(f"Kode binernya adalah : ")
    print(konvertBiner(uji))