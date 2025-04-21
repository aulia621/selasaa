# main.py

from stack import Stack

def MainMenu():
    s = Stack()
    pilih = "y"
    while (pilih == "y"):
        print("|Menu Aplikasi Stack|")
        print("1. Push Object")
        print("2. Pop Object")
        print("3. Cek Empty")
        print("4. Tampil Objek Terakhir")
        print("5. Panjang Dari Stack")
        print("=====================")

        pilihan = str(input("Masukkan pilihan: "))
        if pilihan == "1":
            obj = str(input("Objek yang ingin ditambahkan: "))
            s.Push(obj)
            print("Objek " + obj + " telah ditambahkan")
        elif pilihan == "2":
            if not s.IsEmpty():
                print("Objek " + s.Pop() + " dihapus")
            else:
                print("Stack kosong, tidak ada objek yang dihapus.")
        elif pilihan == "3":
            print("Apakah stack kosong? " + str(s.IsEmpty()))
        elif pilihan == "4":
            if not s.IsEmpty():
                print("Objek terakhir: " + s.Peek())
            else:
                print("Stack kosong, tidak ada objek terakhir.")
        elif pilihan == "5":
            print("Panjang dari Stack adalah: " + str(s.Size()))
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

        pilih = str(input("Apakah Anda ingin melanjutkan? (y/n): "))

if __name__ == "__main__":
    MainMenu()