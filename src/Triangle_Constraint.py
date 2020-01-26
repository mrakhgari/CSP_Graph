from Constraint import Constraint
from itertools import product

class Triangle_Constraint(Constraint):
    def __init__(self, center, adjs):
        super(Triangle_Constraint, self).__init__(center, adjs)

    def constraint_method(self):
        x = []
        temp_list = []
        for adj in self.__adjs:
            if len(adj.__domain) == 0: return False
            x = list(product(x, adj.__domian))  
        for y in x:
            res = 1
            for i in y:
                res *= i
            if int(str(i)[:1]) in self.__center.__domain:
                temp_list.append(y)
                temp_center.append(int(str(i)[:1]))
        print(x)
        return True
