class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        #print(current)
        print(head)
        while current != None and current.next != None:
            print('current.val: ', current.val)
            print('=' * 50)
            print('current.next: ', current.next)
            print('=' * 50)
            print('current.next.val: ', current.next.val)
            print('=' * 50)
            print('current.next.next: ', current.next.next)
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

example = Solution()

new_head = example.deleteDuplicates(head)
print('==================')
print(new_head)
