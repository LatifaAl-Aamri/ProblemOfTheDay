#problem of the day
"""
Given a linked list and a number k , you have to revers
first part of linked list with k nodes and the second
part with n-k nodes .
input : 1--> 2--> 3--> 4--> 5
        k = 2
output: 2 --> 1--> 5--> 4--> 3
Explanation:
As k =2 so the first part 2 nodes : 1-->2 and
second part with 3 nodes: 3--> 4--> 5
now after reversing the first part: 2-->1 and
second part  5--> 4--> 3
so the output is: 2--> 1--> 5--> 4--> 3
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def reverse_linked_list_parts(head, k):
    if not head or k <= 0:
        return head
    
    # Traverse to the kth node
    current = head
    for _ in range(k - 1):
        if current:
            current = current.next
        else:
            return head  # Less than k nodes, no need to reverse
    
    # Reverse the first part
    first_part_end = current
    next_part_start = current.next
    first_part_end.next = None
    new_first_part_start = reverse_linked_list(head)
    
    # Traverse to the end of the second part
    current = next_part_start
    while current and current.next:
        current = current.next
    
    # Reverse the second part
    if current:
        current.next = reverse_linked_list(next_part_start)
    
    # Return the merged linked list
    if new_first_part_start:
        return new_first_part_start
    return head

# Helper function to print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" --> ")
        current = current.next
    print("None")

# Test the code
if __name__ == "__main__":
    # Create the linked list: 1 --> 2 --> 3 --> 4 --> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    print("Original linked list:")
    print_linked_list(head)
    
    k = 2
    new_head = reverse_linked_list_parts(head, k)
    
    print("\nLinked list after reversing parts:")
    print_linked_list(new_head)