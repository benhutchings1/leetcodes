import math
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"Val: {self.val} Next: {self.next}"

l1 = ListNode(5, next=ListNode(6, next=ListNode(4)))

l2 = ListNode(2, next=ListNode(4, next=ListNode(3, next=ListNode(5))))

# 465 + 342

def add_numbers(l1,l2):
    out = 0
    overflow = 0
    digit = 1
    while l1 is not None and l2 is not None:
        # Get digit sum
        x = l1.val + l2.val      

        # Add to output in digit place
        out += x * digit

        l1 = l1.next if l1.next is not None else None
        l2 = l2.next if l2.next is not None else None
        digit *= 10
    
    unfinished = l1 if l1 is not None else l2
    
    while unfinished is not None:
        out += unfinished.val * digit
        digit *= 10
        unfinished = unfinished.next

    return [int(i) for str(out).split()]
    
print(123.split())
