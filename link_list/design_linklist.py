class Node():
    def __init__(self,data=None,next = None) -> None:
        self.data = data 
        self.next = next
    
class Linklist():

    def __init__(self):
        # self.head is storing an object so either None or Node 
        # It should store the object and that of Node only 
        self.head = Node()
        self.cnt = 0 

    def add_at_begining(self,data):
        # You can insert something at begining with 2 conditions 
        #1. when an array is empty like this [] - simple allocate that data to head 
        #2. when an array is having elements like this [1,2,3] -> [4,1,2,3] - Approach you just have to replace the head but carfull with 
        # the idea of not forgeting that head as next pointer to new head
        new_head = Node(data)
        if self.head  == None :
            self.head = new_head
        else:
            new_head.next = self.head
            self.head = new_head 
        self.cnt += 1
        # print("After inserting at begining ",self.display())
    
    def insert_begining(self,data):
        new_node = Node(data)
        old_first_element = self.head.next
        new_node.next = old_first_element
        self.head.next = new_node
    
        print("After inserting at begining ",self.display())


    def insert_end(self,data):
        # You have to iterate till the you don't find a node whose adjascent node is not None
        # i.e 1->2->->4 iterate till the node where adjacent node is available and once that condition breaks 
        # you assign the new node tho that existing node's pointer 
        new_node = Node(data)
        curr_node = self.head 
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node
        self.cnt += 1
    
    def delete_node(self,index):
        # delete node by index 
        # 1 .check if that index exist 
        # 2. if index exists then do the same connection as we do in adding at begining or at the end 
        curr_node = self.head
        prev_node = None
        cnt = 0 
        if index == 0 :
            self.head = self.head.next
        else:
            while curr_node:
                if cnt == index:
                    
                    # new_node.next = curr_node
                    # prev_node.next = new_node

                    prev_node.next = curr_node.next
                    curr_node = None
                    break
                prev_node = curr_node 
                curr_node = curr_node.next
        self.cnt -= 1


    def insert_inbetween(self,data,index):
        #TODO by yourself
        new_node = Node(data)
        if index == 0:
            self.insert_begining(data)
            return None
        elif index == self.cnt - 1:
            self.insert_end(data)
            return None
        else:
            curr_node = self.head
            prev_node = None
            cnt = 0 
            while curr_node:
                if cnt == index:
                    new_node.next = curr_node
                    prev_node.next = new_node
                    break
                prev_node = curr_node 
                curr_node = curr_node.next
                cnt += 1
            self.cnt += 1
        return None 
                
    def append(self,data):
        #TODO by yourself 
        # same as array 
        # new_node = Node(data)       
        # curr_node = self.head 
        # while curr_node.next:
        #     curr_node = curr_node.next
        # curr_node.next = new_node
        self.insert_end(data)

    def length(self,)->int:
        #TODO find total elements in linked list 
        cnt  = 0 
        curr_node = self.head
        while curr_node:
            curr_node = curr_node.next
            cnt += 1
        return cnt 
        # or else direct return self.cnt

    def display(self,):
        #TODO print all the elements of linked list 
        curr_node = self.head 
        arr = []
        #This is called traversing in Linked list (Most important thing in link list is traversing)
        while curr_node.next:
            # print(curr_node.data)
            curr_node = curr_node.next
            arr.append(curr_node.data)
            
        print("element display",arr)
        return arr
        
    def get_data(self,index)-> int :
        # get_data is just a new operator like insert but the traversing remained same 
        curr_node = self.head 
        cnt = 0
        if index == 0:
            return self.head.data
        else:
            while curr_node:
                if index == cnt: 
                    return curr_node.data
                curr_node = curr_node.next 
                cnt += 1

        return -1 




        

if __name__=="__main__":
    #Purpose of main???

    my_linklist= Linklist()
    my_linklist.display()
    my_linklist.append(1)
    my_linklist.display()
    my_linklist.append(2)
    my_linklist.append(3)
    my_linklist.append(4)
    my_linklist.append(5)
    my_linklist.display()
    print("append test completed successfully")
    print(my_linklist.get_data(4))
    my_linklist.insert_begining(8)
    my_linklist.display()
    my_linklist.insert_inbetween(34,6)
    my_linklist.display()
  
        

    






'''

b = you don't know the data type of data 
c = index is also a variagble
a + b*c
first_elements' pointer + memeoryof that data type(2 byte,4 byte etc)*(index on which we want to get value)        

'''