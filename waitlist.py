class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.name = initdata.first + " " + initdata.last
        self.sid = initdata.sid
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def pop_left(self):
        if not self.head:
            return None
        current_head = self.head
        self.head = self.head.next
        self.size -= 1
        print(f'{current_head.name} ID: {current_head.sid} has been moved off the waitlist')
        print(f'Waitlist size: {self.size}')

    def add(self,item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                if not current.next:
                    break
                current = current.next
            current.next = new_node
        self.size += 1

    def is_empty(self):
        if not self.head:
            return True
        else:
            return False

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def __repr__(self):
        return_str = "Waitlist status: "
        for node in self:
            return_str = return_str + node.name
            if node.next:
                return_str = return_str + " -- "
        if self.is_empty():
            return "Waitlist status: Is empty"
        return return_str

    def __str__(self):
        return_str = "Waitlist status"
        prints = self.head
        while prints:
            return_str = return_str + " " + prints.name
            prints = prints.next
        return return_str


import random

class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.sid = random.randint(1000,9999)

    def __str__(self):
        return_str = f'Firstname:{self.first}, Lastname:{self.last}, StudentID = {self.sid}'
        return return_str

if __name__ == '__main__' :
    Ateh = Student('Ateh', 'Nji-Tanji')
    Safi = Student('Safi','Shrestha')
    Nche = Student('Nche', 'Nji-Tanji')
    waitlist = Queue()
    waitlist.add(Ateh)
    waitlist.add(Safi)
    waitlist.add(Nche)
    print(repr(waitlist))
    waitlist.pop_left()
    print(repr(waitlist))
    waitlist.pop_left()
    print(repr(waitlist))
    waitlist.pop_left()
    print(repr(waitlist))


