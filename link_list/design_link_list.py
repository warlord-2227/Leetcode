import os 
import sys 

class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None

class SingleLinkList():
    def __init__(self):
        # What happens if we initialize as None??
        self.head = Node()
    
    def append(self,data):
        # Find the complexity of append method
        curr_node = self.head
        subject_node = Node(data)
        while curr_node.next != None:
            curr_node = curr_node.next        
        curr_node.next = subject_node
    
    def length(self,):
        # Should we consider head as part of length or not??
        cnt = 0 
        curr_node = self.head
        while curr_node.next != None:
            cnt += 1
            curr_node = curr_node.next
        print("length",cnt)
        return cnt
    
    def display(self,):
        # what is the philosophy of this method? 
        elements = []
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
            elements.append(curr_node.data)
        return elements
    
    def insert_begining(self,data):
        # difference between add at begining and insert at begining 
        new_node = Node(data)
        old_first_element = self.head.next
        new_node.next = old_first_element
        self.head.next = new_node
        print(self.display())

    def insert_inbetween(self,data,index):
        new_node = Node(data)
        if index > self.length():
            print("The index is more than it's existing length")
            return None
        elif index < 0:
            print("Negative index is prohibited")
            return None
        else:
            cnt = 0
            curr_node = self.head
            while cnt+1 != index:
                cnt += 1
                curr_node = curr_node.next
            temp_node = curr_node.next
            curr_node.next = new_node
            new_node.next = temp_node
        return 0
    
    def get_data(self,index):
        #if present at begining
        #if present in between/end
        
        if index > self.length()-1 :
            print("Length of linklist is shorter than index")
            # What should be the return statement here
            return None
        elif index < 0:
            print("Negative index doesn't exist")
            #what should be the return statement here 
            return None
        else:
            curr_node = self.head
            cnt = 0 
            while cnt!= index:
                cnt += 1
                curr_node = curr_node.next

        return curr_node.data
    



if __name__=="__main__":
    #Purpose of main???
    pass



        













    # def add_node_begining(self,data):
    #     if not self.head:
    #         self.head = Node(data)
    #     else:
    #         subject_node = Node(data)
    #         temp_ptr = self.head.next
    #         subject_node.next = temp_ptr
    #         self.head = subject_node

if __name__=="__main__":
    s_l = SingleLinkList()
    s_l.add_node_begining(2)
    s_l.add_node_begining(3)
    s_l.add_node_begining(45)
    s_l.display()

    # print(s_l.head.next)
    print("run")




        
        