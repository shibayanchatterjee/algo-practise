import os
os.system('clear')

class Node():
    def __init__(self, val) -> None:
        self.val=val
        self.next=None

class LinkedList():
    def __init__(self) -> None:
        self.head=None
        self.tail=None

    def createlinkedlist(self, arr):
        for k in arr:
            n=Node(k)
            if self.head is None:
                self.head=n
                self.tail=n
            else:
                self.tail.next=n
                self.tail=n
        return

    def printlinkedlist(self):
        tmp=self.head
        l=[]
        while tmp:
            l.append(tmp.val)
            tmp=tmp.next
        line='->'.join(str(k) for k in l)
        print(line)
        return

    def removeduplicates(self):
        '''
        Solution to remove duplicates without buffer.
        Time=O(n^2)
        Space=O(1)
        where n is the size of linked list.
        '''
        dup, ptr1, ptr2=None, None, None
        ptr1=self.head
        while ptr1 and ptr1.next:
            ptr2=ptr1
            while ptr2.next:
                if ptr1.val==ptr2.next.val:
                    dup=ptr2.next
                    ptr2.next=ptr2.next.next
                else:
                    ptr2=ptr2.next
            ptr1=ptr1.next
        return

    def removeduplicateswithbuffer(self):
        '''
        Solution to remove duplicates with buffer
        Time=O(n)
        Space=O(n)
        where n is the size of linked list
        '''
        prev=None
        curr=self.head
        s=set()
        while curr:
            if curr.val in s:
                prev.next=curr.next
            else:
                s.add(curr.val)
                prev=curr
            curr=prev.next
        return
    
    def findkthtolast(self, k):
        '''
        Solution to find kth element to last
        in a linked list.
        We use two pointers spaced at k interval,
        the one that is in front, when it reaches
        the end will have the other pointer at kth
        point.
        Time=O(n)
        Space=O(1)
        where n is the length of linked list
        '''
        if not self.head:
            return -1
        l=0
        ptr=self.head
        while ptr:
            l+=1
            ptr=ptr.next
        if k > l:
            return -1
        ptr1, ptr2=self.head, self.head
        while k>=0:
            ptr2=ptr2.next
            k-=1
        while ptr2:
            ptr1=ptr1.next
            ptr2=ptr2.next
        return ptr1.val

    def deletemiddlenode(self):
        '''
        Solution to delete middle node in a
        linked list. It's necessary to have 
        two pointers, one slow and other fast.
        When fast pointer hits the end of linked
        list the slow pointer will be at the mid.
        Traverse again to delete the node.
        '''
        fast=self.head
        slow=self.head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        print('Middle node: ', slow.val, slow)
        fast=self.head
        while fast.next:
            if fast.next==slow:
                fast.next=fast.next.next
                break
            fast=fast.next
        return

    def partitionlist(self, x):
        '''
        Solution to partition a linked list
        around a value x, s.t. all nodes less
        than x comes before x, and all nodes
        more than that after x.
        '''
        '''
        ptr=self.head
        newhead=ptr
        newtail=ptr
        ptr=ptr.next
        while ptr:
            if ptr.val<x:
                ptr.next=newhead
                newhead=ptr
            elif ptr.val>=x:
        '''
        return

    def addlinkedlistrevorder(self):
        '''
        Solution to add two linked lists
        present in reverse order, and provide
        sum result in reverse order.
        '''
        ptr1=self.head1
        ptr2=self.head2
        count, val1, val2=0, 0, 0
        while ptr1:
            val1+=ptr1.val*(10**count)
            count+=1
            ptr1=ptr1.next
        while ptr2:
            val2+=ptr2.val*(10**count)
            count+=1
            ptr2=ptr2.next
        sumv=val1+val2
        newhead, newtail=None, None
        while sumv>0:
            rem=sumv%10
            n=Node(rem)
            if not newhead:
                newhead=n
                newtail=n
            else:
                newtail.next=n
                newtail=n
            sumv=sumv//10
        return newhead

    def addlinkedlistforwardorder(self):
        revhead1=self.reverselinkedlist(self.head1)
        revhead2=self.reverselinkedlist(self.head2)
        # Do the summation
        # Build linked list in reverse order
        return

    def reverselinkedlist(self):
        next, prev=None, None
        curr=self.head
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
        return

    def checkpalindrome(self):
        '''
        Solution to check if a linked list
        is palindrome. Reverse the linked
        list, and check if the reversed list
        and the original list are same.
        '''
        revhead=self.reverselinkedlist()
        ptr1=self.head
        ptr2=revhead
        while ptr1 and ptr2:
            if ptr1.val!=ptr2.val:
                return False
            ptr1=ptr1.next
            ptr2=ptr2.next
        return True
    
    def checkintersection(self):
        l1, l2=0, 0
        ptr1=self.head1
        ptr2=self.head2
        while ptr1:
            l1+=1
            ptr1=ptr1.next
        while ptr2:
            l2+=1
            ptr2=ptr2.next
        diff=abs(l1-l2)
        if l1>l2:
            while diff>=0:
                ptr1=ptr1.next
                diff-=1
        if l2>l1:
            while diff>=0:
                ptr2=ptr2.next
                diff-=1
        while ptr1 and ptr2:
            if ptr1==ptr2:
                return (True, ptr1)
            ptr1=ptr1.next
            ptr2=ptr2.next
        return False

    def checkloopdetection(self):
        fast, slow=None, None
        fast=self.head
        slow=self.head
        flag=False
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                flag=True
                break
        if flag:
            fast=self.head
            while fast!=slow:
                if fast==slow:
                    node=fast
                    break
                fast=fast.next
            return (flag, node.val)
        return flag

obj=LinkedList()
#arr=[2, 3, 6, 7, 7, 6, 6, 6, 15, 20, 15, 22]
#obj.createlinkedlist(arr)
#obj.printlinkedlist()

# Problem-2.1
#obj.removeduplicates()
#obj.removeduplicateswithbuffer()
#obj.printlinkedlist()

# Problem-2.2
#e=obj.findkthtolast(2)
#print('kth to last: ', e)

# Problem-2.3
#arr=[2, 3, 1]
#obj.createlinkedlist(arr)
#obj.printlinkedlist()
#obj.deletemiddlenode()
#obj.printlinkedlist()

# Problem-2.5
arr1=[2, 3, 1]
arr2=[5, 9, 2]
obj.createlinkedlist(arr1)
obj.createlinkedlist(arr2)
obj.printlinkedlist(arr1)
obj.printlinkedlist(arr2)
obj.addlinkedlistforwardorder()
obj.addlinkedlistrevorder()

# Reverse linked list
arr=[2, 3, 1]
obj.createlinkedlist(arr)
obj.printlinkedlist()
obj.reverselinkedlist()
obj.printlinkedlist()

# Problem-2.6
obj.checkpalindrome()

# Problem-2.7
obj.checkintersectionlist()

# Problem-2.8
obj.checkloopdetection()