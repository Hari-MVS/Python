class node:
    def __init__(self,data):
        self.data =data
        self.ref = None

class llinked:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print('Linked list is Empty')
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

l = llinked()

l.display()
