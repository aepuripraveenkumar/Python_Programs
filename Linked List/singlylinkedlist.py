# insert(data): insert data at the head of the list
# print(): print the whole LinkedList, throw ValueError if data not found
# size(): return the number of nodes in the list
# search(data): return the node that has the data, returns None if not found
# delete(data): delete a node with the data, return the node if found, None if not found


class Node(object):
    def __init__(self,data=None):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_next(self,new_next):
        self.next = new_next

class LinkedList():
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        '''It adds element at beginning of the list '''
        
        new_node = Node(data)
        #new_node.next = self.head
        new_node.set_next(self.head)
        self.head = new_node
    
    def printList(self):
            current = self.head
            lst = []
            while current:
                #print current.data,
                lst.append(str(current.get_data()))
                #current = current.next
                current = current.get_next()
            print('->'.join(lst))
    
#---------------------------------------------------
#     def printList(self):
#             current = self.head
#             while current:
#                 #print current.data,
#                 print current.get_data()
#                 #current = current.next
#                 current = current.get_next()
#---------------------------------------------------
            
    def size(self):
            count = 0
            current = self.head
            while current:
                count += 1
                #current = current.next
                current = current.get_next()
            return count

    def search(self, data):
        current = self.head
        location = 0
        while current:
            if current.get_data() == data:
                print data,"is found in the list at location", location
                return True
            else:
                current = current.get_next()
                location += 1
        print data,"is not found in the list"
        return False
    
    def delete(self,data):
        current = self.head
        prev = None
        
        while current:
            if current.get_data() == data:
                if current == self.head:
                    self.head = current.get_next()
                else:
                    prev.set_next(current.get_next())
                print data,"is deleted from the list"
                return True
            
            prev = current    
            current = current.get_next()      
        print data,"is not present in the list to delete"
        return False
        
if __name__ == "__main__":
    lst = LinkedList()
    
    lst.insert(1)
    lst.insert(2)
    lst.insert(3)
    lst.insert(4)
    lst.insert(5)
     
    lst.printList()
    
    print "Size of the List:",lst.size()
    
    lst.search(1)
    lst.search(6)
    
    lst.delete(6)
    lst.delete(1)
    lst.printList()
    lst.delete(5)
    lst.printList()
    lst.delete(3)
    lst.printList()
