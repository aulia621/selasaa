class BubbleSorting:
    
    def ProsesBubble(self, array):
        temp = 0
        for i in range(len(array)):
            swapped = False
            for j in range(0, len(array)-i-1):
                if array[j] > array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
                    swapped = True
            if not swapped:
                break;
            # Hapus baris break yang tidak diperlukan di sini
            print("Proses Array iterasi ke-", (i+1), ":", array)
        
        return array;