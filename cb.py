class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

def main():
    queue = Queue()
    
    while True:
        print("|Menu Aplikasi Queue|")
        print("1. Enqueue Object")
        print("2. Dequeue Object")
        print("3. Cek Empty")
        print("4. Tampilkan Objek Terdepan")
        print("5. Panjang Dari Queue")
        print("===========================")
        
        try:
            pilihan = int(input("Masukkan pilihan: "))
            if pilihan == 1:
                obj = input("Objek yang ingin ditambahkan: ")
                queue.enqueue(obj)
                print(f'Objek "{obj}" berhasil ditambahkan.')
            elif pilihan == 2:
                obj = queue.dequeue()
                print(f'Objek "{obj}" berhasil dikeluarkan.')
            elif pilihan == 3:
                if queue.is_empty():
                    print("Queue kosong.")
                else:
                    print("Queue tidak kosong.")
            elif pilihan == 4:
                try:
                    obj = queue.peek()
                    print(f'Objek terdepan: "{obj}"')
                except IndexError as e:
                    print(e)
            elif pilihan == 5:
                print(f'Panjang Queue: {queue.size()}')
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
        except IndexError as e:
            print(e)

# Menjalankan program
if __name__ == "__main__":
    main()
    