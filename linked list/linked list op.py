# ds-journey
class node:
    def _init_(self,val):
        self.value=value
        self.next=None
class CSLL:
    def _init_(self):
        self.head=None
    def add(self,val):
        if self.empty() is True:
            self.head=node(val)
            self.head.next=self.head
            print("head node created")
            return
        opt=int(input("enter 1 to add at beginning\nenter 2 to add at end\nenter 3 to add at middle::"))
        if opt==1:
            a=node(val)
            a.next=self.head
            n=self.head
            while n.next is not self.head:
                n=n.next
            n.next=a
            self.head=a
        elif opt==2:
            i=self.head
            while i.next is not self.head:
                i=i.next
                i.next=node(val)
                i.next.next=self.head
        elif op==3:
            pos=int(input("enter position"))
            i=1 
            n=self.head
            f=n.next
            flag=0
            while f is not self.head:
                if i==pos:
                    flag=1 
                    break
                f=f.next
                n=n.next
                i=i+1 
            if flag==1:
                n.next=node(val)
                n.next.next=f 
            else:
                print("position not found")
    def delete(self):
        if self.empty() is True:
            print("linked list is empty")
            return
        elif self.head.next is self.head:
            self.head=None
            return
        opt=int(input("enter 1 to delete at beginning\nenter 2 toi delete at end\nenter 3 to delete at position::"))
        if opt==1 :
            n=self.head
            while n.next is not self.head:
                n=n.next
            n.next=self.head.next
            self.head=self.head.next
        elif opt==2:
            n=self.head
            while n.next.next is not self.head:
                n=n.next
            n.next=self.head
        else:
            opt=int(input("enter 1 to delete by position\nenter 2 to delete by value::"))
            if opt==1:
                pos=int(input("enter position::"))
                i=1 
                n=self.head
                f=self.head.next
                flag=0
                while f.next is not self.head:
                    if i==pos:
                        flag=1 
                        break
                    i=i+1 
                    n=n.next
                    f=f.next
                if flag==1:
                    n.next=f.next
                else:
                    print("position not found")
                    return
            else:
                val=int(input("enter the value"))
                n=self.head
                f=self.head.next
                flag=0
                while f.next is not self.head:
                    if f.value==val:
                        flag=1 
                        break
                    f=f.next
                    n=n.next
                if flag==1:
                    n.next=f.next
                else:
                    print("value not found")
                    return
    def clear(self):
        self.head=None
        print("linked list is cleared")
    def empty(self):
        if self.head is None:
            return True
        else:
            return False
    def display(self):
        if self.empty() is True:
            print("list empty")
            return
        print("the linked list is")
        print(self.head.value,"<==HEAD")
        n=self.head.next
        while n is not self.head:
            print(n.value)
            n=n.next
        print("list ends")
LL=CSLL()
while True:
    option=int(input("enter 1 to add an element\nenter 2 to delete an element\nenter 3 to clear thge list\nenter 4 to display the list\nenter 5 to exit th elist::"))
    if option==1:
        value=int(input("enter value"))
        LL.add(value)
        continue
    elif option==2:
        LL.delete()
        continue
    elif option==3:
        LL.clear()
        continue
    elif option==4:
        LL.display()
        continue
    elif option==5:
        print("exit")
        break
    elif option==6:
        print(LL.empty())
    else:
        print("wrong option"
