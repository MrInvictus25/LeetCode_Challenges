"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following
the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
"""

# To detect if a list is cyclic, we can check whether a node had been visited before. A natural way is to use a hash table.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodesVisited = set()  # Creating an empty set to store visited nodes
        current = head  # Starting with the head of the linked list

        while current is not None:  # Traverse the linked list
            if current in nodesVisited:  # Check if the current node is already in the set
                return True  # If it is, there is a cycle
            nodesVisited.add(current)  # Adding the current node to the set
            current = current.next  # Moving to the next node

        return False  # If we reach the end of the list, there is no cycle


def build_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head # Initializing current to point to the head node.

    for value in values[1:]: # Iterating through the remaining values in the values list.
        current.next = ListNode(value) # For each value, creating a new node and setting it as the next node of current.
        current = current.next  # Moving current to point to the newly created node.


    # Returning the head in this helper functions because the head is the starting point of the linked list. After performing
    # operations like building the linked list or creating a cycle, we need to retain a reference to the start of the
    # list to perform further operations or checks on the entire list. After constructing the linked list by linking all
    # nodes, returning the head allows other parts of the code to access and manipulate the entire list.
    # Without returning head, the reference to the start of the list would be lost, making it impossible to traverse the
    # list from the beginning.

    return head

# This function introduces a cycle in the linked list by connecting the tail to a node at a specified position.
def create_cycle(head, pos):
    if pos == -1:
        return head

    cycleEntry = None # cycleEntry will store the node where the cycle should start.
    current = head # current is used to traverse the list.
    index = 0  # index keeps track of the current position in the list.

    while current.next:
        if index == pos:
            cycle_entry = current
        current = current.next
        index += 1

    current.next = cycle_entry # Setting the next pointer of the last node to cycle_entry, creating a cycle.

    return head


# Main code
if __name__ == "__main__":
    values = [3, 2, 0, -4]
    pos = 1
    head = build_linked_list(values)
    head = create_cycle(head, pos)

    solution = Solution()
    print(solution.hasCycle(head))
