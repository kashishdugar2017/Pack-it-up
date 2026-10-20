import tkinter as tk

def packed_popup(name):
    popup = tk.Toplevel()
    popup.title("Packed!")
    popup.geometry("300x100")
    popup.configure(bg="#F4C2E1")
    msg = tk.Label(popup, text=f"You Packed:\n{name}!",
                   font=("Georgia", 16, "bold"),
                   bg="#F4C2E1", fg="#5B3A6B")
    msg.pack(expand=True)

class PackableThing():
    def __init__(self,name,color,size):
        self.name = name
        self.color = color
        self.size = size

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Container(PackableThing):
    def __init__(self, name, color, size):
        super().__init__(name, color, size)
        self.contents = []

    def add_item(self, item):
        self.contents.append(item)

    def remove_item(self, item):
        self.contents.remove(item)

    def count(self):
        return len(self.contents)

class Item(PackableThing):
    def __init__(self, name, color, size):
        super().__init__(name, color, size)

class Orginizer(Container):
    def __init__(self, name, color, size):
        super().__init__(name, color, size)

class Bag(Container):
    def __init__(self, name, color, size):
        super().__init__(name, color, size)