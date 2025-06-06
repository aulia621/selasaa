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


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)


def main():
    queue = Queue()
    stack = Stack()
    
    while True:
        print("|Menu Aplikasi|")
        print("1. Queue")
        print("2. Stack")
        print("===========================")
        
        try:
            pilihan = int(input("Masukkan pilihan: "))
            if pilihan == 1:
                while True:
                    print("|Menu Aplikasi Queue|")
                    print("1. Enqueue Object")
                    print("2. Dequeue Object")
                    print("3. Cek Empty")
                    print("4. Tampilkan Objek Terdepan")
                    print("5. Panjang Dari Queue")
                    print("6. Kembali ke Menu Utama")
                    print("===========================")

                    sub_pilihan = int(input("Masukkan pilihan: "))
                    if sub_pilihan == 1:
                        obj = input("Objek yang ingin ditambahkan: ")
                        queue.enqueue(obj)
                        print(f'Objek "{obj}" berhasil ditambahkan.')
                    elif sub_pilihan == 2:
                        obj = queue.dequeue()
                        print(f'Objek "{obj}" berhasil dikeluarkan.')
                    elif sub_pilihan == 3:
                        if queue.is_empty():
                            print("Queue kosong.")
                        else:
                            print("Queue tidak kosong.")
                    elif sub_pilihan == 4:
                        try:
                            obj = queue.peek()
                            print(f'Objek terdepan: "{obj}"')
                        except IndexError as e:
                            print(e)
                    elif sub_pilihan == 5:
                        print(f'Panjang Queue: {queue.size()}')
                    elif sub_pilihan == 6:
                        break
                    else:
                        print("Pilihan tidak valid. Silakan coba lagi.")
        
            elif pilihan == 2:
                while True:
                    print("|Menu Aplikasi Stack|")
                    print("1. Push Object")
                    print("2. Pop Object")
                    print("3. Cek Empty")
                    print("4. Tampilkan Objek Teratas")
                    print("5. Panjang Dari Stack")
                    print("6. Kembali ke Menu Utama")
                    print("===========================")

                    sub_pilihan = int(input("Masukkan pilihan: "))
                    if sub_pilihan == 1:
                        obj = input("Objek yang ingin ditambahkan: ")
                        stack.push(obj)
                        print(f'Objek "{obj}" berhasil ditambahkan.')
                    elif sub_pilihan == 2:
                        obj = stack.pop()
                        print(f'Objek "{obj}" berhasil dikeluarkan.')
                    elif sub_pilihan == 3:
                        if stack.is_empty():
                            print("Stack kosong.")
                        else:
                            print("Stack tidak kosong.")
                    elif sub_pilihan == 4:
                        try:
                            obj = stack.peek()
                            print(f'Objek teratas: "{obj}"')
                        except IndexError as e:
                            print(e)
                    elif sub_pilihan == 5:
                        print(f'Panjang Stack: {stack.size()}')
                    elif sub_pilihan == 6:
                        break
                    else:
                        print("Pilihan tidak valid. Silakan coba lagi.")
        
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
        except IndexError as e:
            print(e)

# Menjalankan program
if __name__ == "__main__":
    main()