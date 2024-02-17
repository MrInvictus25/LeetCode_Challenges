# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val,
# and return the new head.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head

        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return sentinel.next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to display a linked list
def display_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
input_values = [1, 2, 6, 3, 4, 5, 6]
linked_list = create_linked_list(input_values)

solution_instance = Solution()
result = solution_instance.removeElements(linked_list, 6)

print("Input linked list:")
display_linked_list(linked_list)

print("Output linked list after removal:")
display_linked_list(result)
# example = Solution()
# print(example.removeElements([1,2,6,3,4,5,6], 6))
