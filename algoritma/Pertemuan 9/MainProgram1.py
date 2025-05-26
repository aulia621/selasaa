import ClassLinear
from ClassLinear import LinearSearch  # Sesuaikan dengan nama class yang benar
from ClassBubble import BubbleSorting

def GenerateElement():
    """Generate random array untuk testing searching"""
    size = int(input("Masukkan jumlah elemen array: "))
    element = []
    for i in range(size):
        element.append(ClassLinear.radint(1, 100))
    return element

def MainMenu():
    element = GenerateElement()
    print("Data array: ", element)
    
    pilih = "y"
    while (pilih == "y"):
        print("Main Aplikasi Searching Data!")
        print("1. Linear Search")
        print("2. Binary Search")
        print("3. Recursive Binary Search")
        print("=" * 20)
        
        pilihan = int(input("Masukkan pilihan: "))
        cariData = int(input("Masukkan data yang ingin dicari: "))
        
        if pilihan == 1:
            Linear = LinearSearch()
            result = Linear.ProsesLinear(element, cariData)
            if(result != -1):
                print("Data", cariData, "ditemukan pada indeks ke-", result)
            else:
                print("Data tidak ditemukan")
        else:
            print("Menu searching belum lengkap...")
            
        pilih = input("Lanjut? (y/n): ")

if __name__ == "__main__":
    # SortingBubble = BubbleSorting()  # Tidak diperlukan di sini
    MainMenu()