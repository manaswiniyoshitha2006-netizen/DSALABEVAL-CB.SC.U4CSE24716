# This program implements a Ride manager System for a giant carnival ride using linked list
# It allows the user(operator) to perform operations like include,remove,remove alternate,print and occupancy of the visitors
#Time complexity worst case - O(n)
#                best case - O(1)
#INPUT : visitor details and ride type and command
#OUTPUT : performs operation and gives output based on given command
class Node:
    def __init__(self,visitor_id=None,name=None,ride_type=None,next=None):
        self.next=next
        self.visitor_id=visitor_id
        self.name=name
        self.ride_type=ride_type
    
class CarnivalRide:
    def __init__(self):
        self.head=None
    
    def add_visitor(self,visitor_id,name,ride_type):
        itr=self.head
        count=0
        if(self.head is None):
            node=Node(visitor_id,name,ride_type,None)
            self.head=node
        else:
            node=Node(visitor_id,name,ride_type,None)
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
    
    def print_occupancy(self):
        itr=self.head
        c=0
        while itr:
            itr=itr.next
            c=c+1
        print("OCCUPANCY : ",c)
    
    def remove_visitor(self,id):
        itr=self.head
        c=0
        tem=self.head
        t=0
        while itr:
            if(itr.visitor_id==id):
                break
            c=c+1
            itr=itr.next
        
        if(c==0):
            self.head=self.head.next

        while tem:
            if(t==c-1):
                tem.next=tem.next.next
                break
            t=t+1
            tem=tem.next

    def print_alphabetical(self):
        itr=self.head
        while itr:
            print("ID : ",itr.visitor_id," Name : ",itr.name," Type : ",itr.ride_type)
            itr=itr.next

if __name__ == "__main__":
    ride = CarnivalRide()
    index=0
    while True:
        print("ENTER COMMAND : ")
        command = input().strip()
        parts = command.split()
        if(len(parts)<4):
            raise Exception("ALL INPUTS ARE NOT GIVEN")
        if(len(parts)>4):
            raise Exception("MORE NUMBER OF INPUTS ARE GIVEN")
        if not command:
            continue

        if command[0] == 'A':
            parts = command.split()
            visitor_id, name, ride_type = int(parts[1]), parts[2], parts[3]
            ride.add_visitor(visitor_id,name,ride_type)
        elif command[0] == 'R':
            _, visitor_id = command.split()
            ride.remove_visitor(int(visitor_id))
        elif command == 'P':
            ride.print_alphabetical()
        elif command == 'O':
            ride.print_occupancy()
        elif command == 'ALT':
            ride.alternate_exit()
        elif command == 'END':
            break
        else:
            print("Invalid Command")
            break