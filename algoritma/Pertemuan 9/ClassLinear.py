class LinearSearching:
    
    def ProsesLinear(self, array, key):
        # Metode 1: Sederhana dan efisien
        for i in range(0, len(array)):
            if (array[i] == key):
                return i
            else: 
                print("Data pada indeks ke-",i, "(", array[i],") Tidak sama dengan ", key);
        return -1
    
