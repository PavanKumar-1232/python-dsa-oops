####################################graph###########################
"""class Graph:
     def __init__(self,no_city):
         self.dic = {"S":0 ,"P":1,"C":2,"T":3, "M":4, "G":5,"B":6,"K":7}
         self.no_city = no_city
         self.matrix = [[0] * 8 for i in range(8)]

     def insert(self,s,d):
             row = self.dic[s]
             col = self.dic[d]
             self.matrix[row][col] = 1
             self.matrix[col][row] = 1



 city_graph = Graph(8)
 data = [("S","P"),("S","T"),("P","C"),("C","K"),("C","G"),("G","B")]

 for s,d in data:
     city_graph.insert(s,d)


 for i in city_graph.matrix:
     print(i)    """
#list
"""class Graph:
    def __init__(self):
        self.dic = {}

    def insert(self,s,d):
        for i in range(2):
            if s in self.dic:
                self.dic[s].append(d)
            else:
                self.dic[s] = [d]
            s , d = d,s
city_graph = Graph()
data = [("S","P"),("S","T"),("P","C"),("C","K"),("C","G"),("G","B")]
for s,d in data:
    city_graph.insert(s,d)
print(city_graph.dic)
"""