# This program implements magical forest journey using linked list
# It allows the user(operator) to perform operations like remove,traverse,print based on the energy_scroll given
#Time complexity worst case - O(n)
#                best case - O(1)
#INPUT : Takes energy_scroll as the input
#OUTPUT : Returns the modified linked list after performing operations
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class SinglyLinkedList:
    def __init__(self):
        self.head=None

    def iinsert(self,data,index):
        itr=self.head
        if(index<0 or index>self.counts()):
            raise Exception("INVALID INDEX")
        count=0
        if(index==0):
            node=Node(data,self.head)
            self.head=node
        if(index==self.counts()):
            node=Node(data,None)
            while(itr.next):
                itr=itr.next
            itr.next=node
    
    def counts(self):
        itr=self.head
        c=0
        while itr:
            itr=itr.next
            c=c+1
        return c
    
    def print_list(self):
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+" "
            itr=itr.next
        print(llstr)

    def traverse(self,times):
        itr=self.head
        c=0
        while itr:
            if(c==times):
                break
            itr=itr.next
            c=c+1
        self.head=itr

    def insertatindex(self,data,index):
        itr=self.head
        c=0
        while itr:
            if(c==index-1):
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            c=c+1

    def remove(self):
        self.head=self.head.next


    def create_alphabet_trail():
        temp=SinglyLinkedList()
        i=65
        j=0
        while(j<26):
            temp.iinsert(chr(i),j)
            i=i+1
            j=j+1
        return temp
    

    def chirpy_journey(self,energy_scroll):
        for i in energy_scroll:
            for j in range(i):
                self.remove()
            self.traverse(i)


if __name__ == "__main__":
    print("=== Chirpy's Trail – The Vanishing Forest ===")
    forest = SinglyLinkedList.create_alphabet_trail()
    print("\nInitial Trail:")
    forest.print_list()
    # Ask user for energy scroll
    user_input = input("\nEnter energy values separated by spaces (e.g., 3 5 2): ").strip()
    if user_input:
        try:
            energy_scroll = [int(x) for x in user_input.split()]
        except ValueError:
            print("Invalid input. Using default energy scroll [3, 5, 2].")
            energy_scroll = [3, 5, 2]
    else:
        print("No input provided. Using default energy scroll [3, 5, 2].")
        energy_scroll = [3, 5, 2]
    print(f"\nEnergy Scroll: {energy_scroll}")
    forest.chirpy_journey(energy_scroll)
    print("\nFinal Trail:")
    forest.print_list()
    