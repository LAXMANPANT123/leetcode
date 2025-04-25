
class Solution(object):
    def swapPairs(self, head):

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        ret = dummy

        while head and head.next:
            firstNode = head
            secondNode = head.next

            prev.next = secondNode
            nextTemp = secondNode.next
            secondNode.next = firstNode
            firstNode.next = nextTemp
             
             #updating previous node
            prev = firstNode
             
             #moving the pointer too the first node
            head = firstNode.next

        return ret.next
        