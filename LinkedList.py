# A simple implementation of a linked list
import sys # Used for exit()
class ListNode(object):
    data = 0
    prevNode = 0
    nextNode = 0

    def __init__(self, data, prevNode, nextNode):
        self.data = data
        self.prevNode = prevNode
        self.nextNode = nextNode

def main():
    # head = make_listnode(0, 0, 0)
    head = 0
    lastNode = 0
    while 1==1:
        print("1. Add ListNode\n2. Print list\n3. Remove ListNode\n4. Exit")
        choice = int(input())
        if choice > 4 or choice < 1:
            print("Invalid choice")
            continue
        if choice == 1:  # Add ListNode
            print("Data to put into ListNode?")
            data = input()
            if head == 0:
                # Create the head
                head = ListNode(data, 0, 0)
                lastNode = head
            else:
                # Head exists
                newNode = ListNode(data, lastNode, 0)
                lastNode.nextNode = newNode
                lastNode = newNode
        if choice == 2:  # Print List
            current = head
            while current.nextNode != 0:
                print(str(current.data))
                current = current.nextNode
            print(str(current.data))
        if choice == 3:  # Remove ListNode
            current = head
            print("What data to remove?")
            data = input()
            while current.nextNode != 0:
                if current.data == data:  # Remove Node
                    current.prevNode.nextNode = current.nextNode
                    current.nextNode.prevNode = current.prevNode
                    lastNode = current.prevNode
                    break
                current = current.nextNode
            if current.data == data:  # Remove Node (Last Node)
                current.prevNode.nextNode = 0
                lastNode = current.prevNode
            else:
                print("Data not found")
        if choice == 4:
            sys.exit()  # End program
main()
