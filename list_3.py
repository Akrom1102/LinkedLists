class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


    def push(self, new_data):
        # listning boshiga element qo'shish
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def insert(self, prev_node, new_data):
        # listning ixtiyoriy nuqtasiga element qo'shish
        if prev_node is None:
            print("Error")
        # yangi element qo'shamiz
        new_node = Node(new_data)
        # yangi tugunni keyingi elementga bog'laymiz
        new_node.next = prev_node.next
        # avvalgi tugunni yangi elementga bog'laymiz
        prev_node.next = new_node


    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

# tugun valuelari
a = Node("Ot 🐴")
b = Node("Kuchuk 🐶")
c = Node("Mushuk 🐈")
d = Node("Maymun 🐒")
e = Node("Qo'y 🐑")
f = Node("Tovuq 🐔")
ll = LinkedList()
ll.head = a
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# push
# ______________________________________________________________________________________________________________________
ll.push("Bo'ri 🐺")
ll.push("Sher 🦁")
ll.push("Jirafa 🦒")
ll.push("Ayiq 🐻")
ll.push("Yo'lbars 🐯")

#
print("2-tugun")
print("Push faqat boshidagi 5 tasi 👇 (yovvoyi hayvonlar)")
ll.printList()
print("__________")


# ______________________________________________________________________________________________________________________
# push tugadi


# insert

# ______________________________________________________________________________________________________________________
# 1
insert_1 = Node("Akrom")
ll.insert(insert_1, "Abdumannobov")
ll1 = LinkedList()
ll1.head = insert_1

# 2
insert_2 = Node("Kamron")
ll.insert(insert_2, "Aliyev")
ll2 = LinkedList()
ll2.head = insert_2

# 3
insert_3 = Node("Aziz")
ll.insert(insert_3, "Esonboyev")
ll3 = LinkedList()
ll3.head = insert_3

# 4
insert_4 = Node("Bilol")
ll.insert(insert_4, "Abdug'aniyev")
ll4 = LinkedList()
ll4.head = insert_4

# 5
insert_5 = Node("Muhammadamin")
ll.insert(insert_5, "Alisherov")
ll5 = LinkedList()
ll5.head = insert_5


print("Insert 👇")
ll1.printList()
ll2.printList()
ll3.printList()
ll4.printList()
ll5.printList()
print("Insert tugadi 👆")
print("_________")
# insert tugadi

# ______________________________________________________________________________________________________________________


# append

# ______________________________________________________________________________________________________________________
append_1 = LinkedList()
append_1.append(1)
append_1.append(2)
append_1.append(3)
append_1.append(4)
append_1.append(5)

print("Append 👇")
append_1.printList()
print("Append tugadi 👆")

# ______________________________________________________________________________________________________________________
