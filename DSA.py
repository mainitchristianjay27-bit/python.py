class Node:

    def __init__(self, data):
        self.data = data         
        self.prev = None         
        self.next = None         

class DoublyLinkedList:
    
    def __init__(self):
        self.head = None        

    def insert_beginning(self, data):
        
        new_node = Node(data)
        
        if self.head is None:     
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node      

    def insert_end(self, data):
        new_node = Node(data)
        
        if self.head is None:    
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def delete(self, key):
      
        current = self.head
        
        while current is not None:
            if current.data == key:
                
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                
                    else:
                        current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                
                return True   
            current = current.next
        
        return False  

    def display_forward(self):
        if self.head is None:
            print("List is empty!")
            return
        
        current = self.head
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")  

    def display_backward(self):
        if self.head is None:
            print("List is empty!")
            return
        current = self.head
        while current.next is not None:
            current = current.next
        
        
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

def main():
    dll = DoublyLinkedList()
    print(" Doubly Linked List Program")
    print("Group Activity!\n")
    
    while True:
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Delete a value")
        print("4. Display Forward (Head → Tail)")
        print("5. Display Backward (Tail → Head)")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            data = input("Enter value to insert at beginning: ")
            dll.insert_beginning(data)
            print(f" '{data}' inserted at the beginning.")
        
        elif choice == "2":
            data = input("Enter value to insert at end: ")
            dll.insert_end(data)
            print(f"'{data}' inserted at the end.")
        
        elif choice == "3":
            data = input("Enter value to delete: ")
            if dll.delete(data):
                print(f"'{data}' was deleted.")
            else:
                print(f"'{data}' not found in the list.")
        
        elif choice == "4":
            print(" List (Forward):")
            dll.display_forward()
        
        elif choice == "5":
            print("= List (Backward):")
            dll.display_backward()
        
        elif choice == "6":
            print("Thank you! Program ended.")
            break
        else:
            print("Invalid choice! Please enter 1-6.")

if __name__ == "__main__":
    main()