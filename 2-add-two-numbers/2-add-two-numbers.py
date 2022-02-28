# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_int = ''
        seccond_int = ''
        while l1 or l2 :
             
            if l1 is not None:    
                first_int += str(l1.val)
                l1 = l1.next

            if l2 is not None:
                seccond_int += str(l2.val)
                l2 = l2.next
        total = str(int(first_int[::-1])+int(seccond_int[::-1]))
       
        newNode = ListNode()
        for i in total:
            newNode.val = i 
            temp = ListNode()
            temp.next = newNode
            newNode = temp
        return newNode.next
           
           
            
        