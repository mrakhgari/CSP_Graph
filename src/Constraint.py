class Constraint:
    def __init__(self, center, adjs):
        self.__center = center
        self.__adjs = []
        self.set_adjs(adjs)
    
    def set_adjs(self, adjs):
        for edge in adjs:
            self.__adjs.append(edge[0])

    def __str__(self):
        return str(self.__center) + str(self.__adjs) 

    def __repr__(self):
        return str(self)

    def __contains__(self, key):
        print(' contains ? ')
        return key == self.__center or key in self.__adjs        