'''
Greg Faaborg
CSCE 4430 HW2
This Python program given a lambda term in de Bruijn notation displays it
as a horizontal tree.
'''

#Below are the given functions that convert a string into a tuple 
#as given by Dr. Tarau in the assignment
def l(x) : return ('l',x)
def a(x,y) : return ('a',x,y)

#global count variable used to indicate whether we are at the root of the tree
count = 0

#prints the internal nodes and the root of the tree
def print_remain(level, node):
    global count

    #if we are not at the root
    if count > 0:
        print('   ' * (level-1) + '^==' + node[0])
    #at root
    else: 
        print(node[0])
        count = count + 1


#prints the leaves of the tree
def print_final(level, node):
    print('   ' * level + '^==' + str(node))


#searches the nested tuples and calls their corresponding functions
def make_tree(expr, level=0):

    print_remain(level,expr[0])

    #search next tuple recursively
    for tup in expr[1:]:
        if isinstance(tup,tuple):
            make_tree(tup, level+1)
        else:
            print_final(level, tup)

if __name__ == "__main__":

    #asks the user for input and evaluates the expression using the functions given in the assignment
    expression = eval(input("Enter Lambda Expression:"))
    print("The evaluated expression is:")
    print(expression)
    print("The corresponding tree for the expression is below:")
    make_tree(expression)

    
    print("*" * 50 + "\nThe ^ points to the nodes parent and if there a multiple children \nthe first indented child indicates that it is the left child \n and the second one is the right child.")
    print("""For example, 
    a
    ^==b <- left child of a, parent of c and e
    ---^==c <-left child of b
    ------^==d <-only child of c
    ---^==e <- right child of b
    ^==f <- right child of a        
    """)





