class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id

    def display_info(self):
        return f"{self.title}\n{self.author}\n{self.item_id}\n"

class Book(LibraryItem):
    def __init__(self, title, author, item_id, pages):
        super().__init__(title, author, item_id)
        self.pages = pages
    def display_info(self):
        info = super().display_info() + f"{self.pages}\n" 
        return info

class DVD(LibraryItem):
    def __init__(self, title, author, item_id, duration):
        super().__init__(title, author, item_id)
        self.duration = duration
    def display_info(self):
        info = super().display_info() + f"{self.duration}\n"
        return info     

class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number):
        super().__init__(title, author, item_id)  
        self.issue_number = issue_number
    def display_info(self):
        info =  super().display_info() + f"{self.issue_number}\n"
        return info  

class Library:
    def __init__(self):
        self.itms = []

    def add_item(self, item):
        self.itms.append(item)

    def remove_item(self, item_id):
        self.itms = [item for item in self.itms if item.item_id != item_id]
   
    def display_all_items(self):
        for item in self.itms:
            print(item.display_info())

l = Library()
a = DVD("dghgh", "tgara", 1568, 65)
b = Book("dsgf", "fdgsf", 1523, 25)
c = Magazine("dgsgsd", "dsgsd", 1566, 667)
l.add_item(a)
l.add_item(b)
l.add_item(c)
l.display_all_items()
l.remove_item(1568)
l.remove_item(1566)
l.display_all_items()