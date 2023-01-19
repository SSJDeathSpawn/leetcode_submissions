from typing import Optional
import time
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        if self.next == None:
            return str(self.val)
        return str(self.val) + "->" + self.next.__repr__()

def make_linked_list(val: int) -> Optional[ListNode]:
    val = int(str(val)[::-1])
    p_prev = None
    while val > 0:
        p = ListNode(val%10, p_prev)
        val //= 10
        p_prev = p
    return p_prev

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    val = 0
    while l1 != None or l2 != None:
        time.sleep(1)
        temp = 0
        if l1: temp += l1.val
        if l2: temp += l2.val
        if temp < 10: val *= 10
        val += temp
        if l1: l1 = l1.next
        if l2: l2 = l2.next
        print(val, l1, l2, sep="\n")
    return make_linked_list(val)

print(addTwoNumbers(make_linked_list(9999999),make_linked_list(9999)))
