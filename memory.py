# memory.py

class Memory:
    def __init__(self):
        self.data = None

    def save(self, data):
        self.data = data
        print("Data saved to memory.")

    def retrieve(self):
        print("Data retrieved from memory.")
        return self.data
