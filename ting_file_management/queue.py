from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        value = self.data[0]
        self.data = self.data[1:]
        return value

    def search(self, index):
        if 0 <= index <= len(self.data) - 1:
            return self.data[index]
        else:
            raise IndexError("Índice Inválido ou Inexistente")
