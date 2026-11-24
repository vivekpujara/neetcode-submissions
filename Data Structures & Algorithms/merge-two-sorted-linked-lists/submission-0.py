# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # stays null at beginning of new sorted merged llist
        tail = dummy

        # remember here: list1 and list2 are the HEAD NODES of the input LLs
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # if one input llist's chain still extends, can just attach that whole remaining chain
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next  # returns new llist head node (one step ahead of the null val)
                           # and as a result, because this is llist, it returns the 
                           # whole new llist

"""
brute force
output must be sorted as well
two pointers (1 on each input ll)
use while loop?
need tmp vars to store connections, or just construct new ll?
handle duplicates, include them as well
T: O(n^2)?
S: O(n)

optimized
binary search on l1 and l2? to find the next element to add to the new ll?
T: O(nlogn)?
S; O(1)? if we just use vars, instead of instantiating a new ll

first attempt logic (close, but revise syntax for ll)
l1curr = 0
        l2curr = 0
        newll = ListNode()

        while l1curr and l2curr:
            if list1[l1curr] <= list2[l2curr]:
                newll.append(list1[l1curr])
                if list1[l1curr] == list2[l2curr]:
                    newll.append(list2[l2curr])
                l1curr += 1
                l2curr += 1
        
        return newll  # or return head of newll
"""