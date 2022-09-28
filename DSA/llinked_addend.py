
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
                print(n.data,'****',end=' ')
                n = n.ref
    def add_item(self,data):
        new =node(data)
        new.ref = self.head
        self.head =  new
    def add_end(self,data):
        new = node(data)
        if self.head is  None:
            self.head = new
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new
l = llinked()
l.add_item(20)
l.add_end(40)
l.add_end(30)
l.add_item(60)
l.display()



                
