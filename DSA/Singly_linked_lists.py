class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        
    
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)
node6 = Node(20)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
# node5.next = None # na dileo None hobe

# print(node1.next.next.data)# 3

def traverseAndPrint(head):
    currentNode = head
    
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("Null")
    
traverseAndPrint(node1)

def DeleteSpecificNode(head , nodeToDelete):
    if head == nodeToDelete:
        return head.next  
    
    currentNode = head
    while currentNode.next and currentNode.next != nodeToDelete:
        currentNode = currentNode.next 
    
    if currentNode.next is None:
        return head
    
    currentNode.next = currentNode.next.next
    return head
## Alternative---->
# def DeleteSpecificNode(head , nodeToDelete):
#     if head == nodeToDelete:
#         return head.next  
    
#     currentNode = head
#     while currentNode:
#         if currentNode.next == nodeToDelete:
#             currentNode.next = currentNode.next.next 
#             break
#         currentNode = currentNode.next     
        
#     # currentNode.next = currentNode.next.next
#     return head

node1 = DeleteSpecificNode(node1, node4)

print("After delation node")
traverseAndPrint(node1)

def insertNodeAtPosition(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode
    currentNode = head
    
    for _ in range(position -2):
        if currentNode is None:
            break
        currentNode = currentNode.next 
    
    newNode.next = currentNode.next 
    # print(newNode.next.data)# 9
    currentNode.next = newNode
    # print(currentNode.data)# 3
    return head
     

newNode = Node(97)
Node1 = insertNodeAtPosition(node1, newNode, 4)
print("After Insertion : ")
traverseAndPrint(Node1) 

def findLowestValue(head):
    minValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data 
        currentNode = currentNode.next 
    
    return minValue

lowestValue = findLowestValue(node1)
print(f"lowest value in the linkedlist: {lowestValue}")
