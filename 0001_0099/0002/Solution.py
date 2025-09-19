from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    See: https://leetcode.cn/problems/add-two-numbers/description/
    """

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        _dummy = ListNode()
        _carry = 0
        i, j, k = l1, l2, _dummy

        while i or j:
            _i = i.val if i else 0
            _j = j.val if j else 0
            _sum = _i + _j + _carry

            if _sum >= 10:
                _carry = 1
                _sum -= 10
            else:
                _carry = 0
            k.next = ListNode(_sum)
            k = k.next
            i = i.next if i else None
            j = j.next if j else None

        if _carry:
            k.next = ListNode(_carry)

        return _dummy.next
