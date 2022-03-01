# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        numsList = []
        while head: 
            numsList.append(head.val)
            head = head.next
        
        numsList=list(set(numsList))
        numsList.sort()
        
        #newNode = ListNode()
        
        
        newNode = ListNode()
        for i in reversed(numsList):
            newNode.val = i 
            temp = ListNode()
            temp.next = newNode
            newNode = temp
        return newNode.next
                
        