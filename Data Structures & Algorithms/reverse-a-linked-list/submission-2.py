# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            print(curr.val)
            temp = curr.next
            if temp:
                print(temp.val)
            else:
                print('n')
            curr.next = prev
            print(curr.val)
            prev = curr
            print(prev.val)
            curr = temp
            if curr:
                print(curr.val)
            else:
                print('n')
            print()
        return prev