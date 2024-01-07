class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1
    
    def print_list(self):
        temp = self.head
        data = "*"
        while temp != None:
            print(f"*{temp.value}*", end=", ")
            temp =temp.next
        print()

    def append(self, value):
        new_node = Node(value)
        if self.lenght == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght += 1
    
    def insert(self, index, value):
        if 0 < index < self.lenght:
            new_node  = Node(value)
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        elif index == 0:
            self.prepend(value)
        else:
            raise IndexError("Wrong indexing")
        
    def pop(self):
        temp = self.head
        pretemp = self.head

        if self.lenght == 0:
            return None
        
        for i in range(self.lenght-1):
            pretemp = temp
            temp = temp.next
        
        pretemp.next = None
        self.tail = pretemp
        self.lenght -= 1 
        if self.lenght == 0:
            self.tail = None
            self.head = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.lenght == 0:
            self.head = new_node 
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.lenght += 1

    def pop_first(self):
        if self.lenght == 0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.lenght -= 1

        if self.lenght == 1:
            self.head = None
            self.tail = None

        return temp
    
    def get(self, index):

        if 0 <= index <= self.lenght-1:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        
        elif self.lenght == 0:
            return None
        
        else:
            raise IndexError("Out of Index")

    def set_value(self, index, value):
        temp_var = self.get(index)
        temp_var.value = value

    
    def remove(self, index ):

        if self.lenght == 0 :
            return None
        
        elif index == 0:
            return self.pop_first()

        elif index == self.lenght-1:
            return self.pop()
        else:
            pre = self.get(index-1)
            temp = pre.next
            pre.next = temp.next
            temp.next = None
            return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = self.temp
        after = temp.next
        before = None
        for _ in range(self.lenght):
            after = temp.next
            temp.next = before 
            before = temp
            temp = after

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None



