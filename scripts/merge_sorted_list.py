from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)

        current = head

        while list1 and list2:
            if list1.value <= list2.value:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

            current.next = list1 if list1 else list2
        return head.next


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

s = Solution()
merged = s.mergeTwoLists(list1, list2)

while merged:
    print(merged.value)
    merged = merged.next


