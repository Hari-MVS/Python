class node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class llinked:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print('Linked List is Empty')
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    
    def add_elem(self,data):
        new = node(data)
        new.ref = self.head
        self.head = new

l = llinked()
l.add_elem(10)
l.add_elem(20)
l.add_elem(30)
l.display()

