class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Linked_List:
    def __init__(self, array):
        self.root = ListNode(array[0])
        cur = self.root
        for el in array[1:]:
            cur.next = ListNode(el)
            cur = cur.next


class Solution:
    def addTwoNumbers(self, l1, l2):
        l3 = ListNode(0)
        s = l3
        while l1 or l2:
            if not l1:
                l1 = ListNode(0)
            elif not l2:
                l2 = ListNode(0)
            s.val += (l1.val + l2.val)
            if s.val // 10:
                s.next = ListNode(s.val // 10)
                s.val = s.val % 10
                s = s.next
            elif l1.next or l2.next:
                s.next = ListNode(0)
                s = s.next
            l1 = l1.next
            l2 = l2.next
        return l3

# Testbed
l1 = Linked_List([1])
l2 = Linked_List([9, 9])
s = Solution()
s.addTwoNumbers(l1.root, l2.root)