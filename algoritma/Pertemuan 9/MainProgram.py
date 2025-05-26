import ClassBubble
from ClassBubble import BubbleSorting

def GenerateElement():
    size = int(input("Masukkan jumlah elemen array: "))
    dataelement = []
    for i in range(size):
        dataelement.append(ClassBubble.randint(1, 100))
    return dataelement

def MainMenu():
    element = GenerateElement()
    print("Data array sebelum sorting: ", element)
    
    pilih = "y"
    while (pilih == "y"):
        print("Main Aplikasi Sorting Data!")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("--------------------")
        
        pilihan = int(input("Masukkan pilihan: "))
        
        if pilihan == 1:
            Bubble = BubbleSorting()
            sorted_array = Bubble.ProsesBubble(element.copy())  # copy untuk tidak mengubah original
            print("Data array setelah sorting menggunakan Bubble Sort:", sorted_array)
        else:
            print("Main sorting belum lengkap...")
        
        pilih = input("Lanjut? (y/n): ")

if __name__ == "__main__":
    MainMenu()