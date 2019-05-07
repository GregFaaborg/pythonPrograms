'''
Greg Faaborg
HW 5

usage
python -i hw5.py
>>> list(males)
['Joe', 'Bill', 'Paul', 'Mike', 'Adam']
>>> list(females)
['Marie', 'Helen', 'Miranda']
>>> list(parent_of("Joe"))
['Helen', 'Bill']
>>> list(parent_of("Marie"))
['Helen', 'Bill']
>>> list(parent_of("Bill"))
['Mike']
>>> list(parent_of("Miranda"))
['Mike']
>>> list(sibling_of("Joe"))
['Marie']
>>> list(sister_of("Bill"))
['Miranda']
>>> list(brother_of("Bill"))
[]
>>> >>> list(brother_of("Marie"))
['Joe']
>>> list(mother_of("Marie"))
['Helen']
>>> list(father_of("Joe"))
['Bill']
>>> list(gp_of("Marie"))
[['Mike'], ['Adam']]
>>> list(gp_of("Joe"))
[['Mike'], ['Adam']]
>>> list(cousin_of("Marie"))
['Paul']
>>> list(cousin_of("Joe"))
['Paul']
>>> list(cousin_of("Paul"))
['Joe', 'Marie']
'''

males = []
females = []

males = ["Joe","Bill","Paul","Mike","Adam"]
females = ["Marie","Helen","Miranda"]


parents = {}
parents["Joe"] = ["Helen","Bill"]
parents["Marie"] = ["Helen","Bill"]
parents["Bill"] = ["Mike"]
parents["Helen"] = ["Adam"]
parents["Paul"] = ["Miranda"]
parents["Miranda"] = ["Mike"]


def parent_of(child):
    
    if child not in parents:
        return []
    else:
        return parents.get(child)

def sibling_of(person):
    return [k for k,v in parents.items() if v == parents.get(person) and k != person]

def brother_of(person):
    results = (sibling_of(person))
    return [elem for elem in results if elem in males]

def sister_of(person):
    results = (sibling_of(person))
    return [elem for elem in results if elem in females]

def mother_of(person):
    results = (parent_of(person))
    return [elem for elem in results if elem in females]

def father_of(person):
    results = (parent_of(person))
    return [elem for elem in results if elem in males]

#grandparents
def gp_of(person):
    results = (parent_of(person))
    gp1 = parent_of(results[0])
    length = len(results)
    if length == 2:
        gp2 = parent_of(results[1])
        yield [elem for elem in gp2]
    yield [elem for elem in gp1] 

def cousin_of(person):
    res1 = parent_of(person)

    if len(res1) == 2:
        res2 = sibling_of(res1[1])
        res3 = sibling_of(res1[0])
        yield [k for k, v in parents.items() if v == res2 or v == res3]
    else:
        res4 = sibling_of(res1[0]);
       
        if set(res4).issubset(parents):
            for child,parent in parents.items():
                if set(res4).issubset(parent):
                    yield child








