class Node:
    def __init__(self,co_ords):
        self.neighbours = []
        self.links = []
        self.co_ordinates = co_ords

class Graph:
    def __init__(self):
        self.nodes = []

    def get_nodes(self,side,size):
        for x in range (0,side,size):
            for y in range(0,side,size):
                pt = (x,y)
                new_node = Node(pt)
                self.nodes.append(new_node)

    def set_start(self,co_ord):
        for node in self.nodes:
            if node.co_ordinates == co_ord:
                self.start_node = node
        return self.start_node

    def set_end(self,co_ord):
        for node in self.nodes:
            if node.co_ordinates == co_ord:
                self.end_node = node
        return self.end_node

    def set_blocked(self,co_ord):
        for node in self.nodes:
            if node.co_ordinates == co_ord:
                self.nodes.remove(node)

    def set_neighbours(self,node):
        co_ord = node.co_ordinates

        if co_ord[0] - 25 >= 0:  #for left neighbour
            pt = (co_ord[0] -25 , co_ord[1])
            l_neigh = self.find_node(pt)
            if l_neigh != None:
                node.neighbours.append(l_neigh)
                node.links.append(10)

        if co_ord[0] - 25 >= 0 and co_ord[1] - 25 >=0: # for left top neighbour
            pt = (co_ord[0] -25, co_ord[1] - 25)
            lt_neigh = self.find_node(pt)
            if lt_neigh != None:
                node.neighbours.append(lt_neigh)
                node.links.append(14)

        if co_ord[0] + 25 <= 475 and co_ord[1] - 25 >= 0: # for right top neighbour
            pt = (co_ord[0] + 25, co_ord[1] - 25)
            rt_neigh = self.find_node(pt)
            if rt_neigh != None:
                node.neighbours.append(rt_neigh)
                node.links.append(14)

        if co_ord[0] - 25 >= 0 and co_ord[1] +25 <= 475: #for left bottom neighbour
            pt = (co_ord[0] - 25, co_ord[1] + 25)
            lb_neigh = self.find_node(pt)
            if lb_neigh != None:
                node.neighbours.append(lb_neigh)
                node.links.append(14)

        if co_ord[0] + 25 <= 475 and co_ord[1] + 25 <= 475: #for right bottom neighbour
            pt = (co_ord[0] + 25, co_ord[1] + 25)
            rb_neigh = self.find_node(pt)
            if rb_neigh != None:
                node.neighbours.append(rb_neigh)
                node.links.append(14)

        if co_ord[0] + 25 <= 475: #for right neighbour
            pt = (co_ord[0] + 25, co_ord[1])
            r_neigh = self.find_node(pt)
            if r_neigh != None:
                node.neighbours.append(r_neigh)
                node.links.append(10)

        if co_ord[1] - 25 >= 0: #for top neighbour
            pt = (co_ord[0] , co_ord[1] - 25)
            t_neigh = self.find_node(pt)
            if t_neigh != None:
                node.neighbours.append(t_neigh)
                node.links.append(10)

        if co_ord[1] + 25 <= 475: #for bottom neighbour
            pt = (co_ord[0], co_ord[1] + 25)
            b_neigh = self.find_node(pt)
            if b_neigh != None:
                node.neighbours.append(b_neigh)
                node.links.append(10)

    def find_node(self,co_ords):
        for node in self.nodes:
            if node.co_ordinates == co_ords:
                return node
        return None