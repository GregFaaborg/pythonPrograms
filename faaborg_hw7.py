'''
Greg Faaborg
Prog Lang Assignment 7
dictionary class
'''

class mdict :
    def __init__(self):
        self.d = dict()
    

    def memb(self,k,v) :
        vs = self.d.get(k)
        if not vs or not v in vs : return False
        else : return True 

    def __getitem__(self,k) :
        return self.d[k]

    def __contains__(self,k) :
        return k in self.d
    def __repr__(self) :
        return self.d.__repr__()

    '''
    above are Dr. Taraus methods
    below are my own method implementations
    '''

    def add(self,k,v):
        self.d.setdefault(k,[]).append(v)
    

    def del_certain_value(self,k,v):
        self.d[k].remove(v)
        print("Removed", v ,"in key", k) 

    def clear_dict(self):
        self.d.clear()
        print("Dictionary Cleared")

    def print_key_values(self):
        if(len(self.d) == 0):
            print("Nothing in Dictionary")
        else:
            for k,v in self.d.items():
                print(k,v)


    def del_key_and_values(self,k):
        del self.d[k]
        print("Deleted key", k, "and all its values")


    
if __name__ == "__main__":

    mydict = mdict()

    for i in range(5):
        for x in range(8):
            mydict.add(i,x)
    

    print("2:",mydict.__getitem__(2))
    print("Is 3 in dictionary:",mydict.__contains__(3))
    print("Is key 2 with the value 4 in the dictionary:",mydict.memb(2,4))

    mydict.print_key_values()
    print()
    mydict.del_certain_value(2,4)
    mydict.print_key_values()
    print()
    mydict.del_key_and_values(1)
    mydict.print_key_values()
    print()
    mydict.clear_dict()
    mydict.print_key_values()

    for i in range(6):
        for x in range(7):
            mydict.add(i,x)

    print("New dicitonary set\n")
    print("4:",mydict.__getitem__(4))
    print("Is 6 in dictionary:",mydict.__contains__(6))
    print("Is key 8 with the value 8 in the dictionary:",mydict.memb(8,8))
    mydict.print_key_values()
    print()
    mydict.del_certain_value(5,2)
    mydict.print_key_values()
    print()
    mydict.del_key_and_values(4)
    mydict.print_key_values()
    print()
    mydict.clear_dict()
    mydict.print_key_values()

    print()
    for i in range(3):
        for x in range(20):
            mydict.add(i,x)

    print("New dicitonary set\n")
    print("1:",mydict.__getitem__(1))
    print("Is 0 in dictionary:",mydict.__contains__(0))
    print("Is key 2 with the value 4 in the dictionary:",mydict.memb(2,4))
    mydict.print_key_values()
    print()
    mydict.del_certain_value(0,17)
    mydict.print_key_values()
    print()
    mydict.del_key_and_values(2)
    mydict.print_key_values()
    print()
    mydict.clear_dict()
    mydict.print_key_values()

    
    






