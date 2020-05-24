from stack_array import *  # Needed for Depth First Search
from queue_array import *  # Needed for Breadth First Search


# Change to an adjacency list representation (from dictionary back to list

class Vertex:
    '''Add additional helper methods if necessary.'''

    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = {}
        # self.adjacent_to = []
        self.color = 'white'

    def addNeighbor(self, nbr, weight=0):
        self.adjacent_to[nbr] = weight

    def setColor(self, color):
        self.color = color

    def getConnections(self):
        return self.adjacent_to.keys()

    def getId(self):
        return self.id

    def getColor(self):
        return self.color

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.adjacent_to])


class Graph:
    '''Add additional helper methods if necessary.'''

    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        self.vertList = {}
        self.numVertices = 0

        with open(str(filename), 'r') as file:
            chars = file.read()
        file.close()
        connections = chars.split("\n")
        for connection_pair in connections:
            if connection_pair != '':
                connection_pair = connection_pair.split(' ')
                vertex0 = connection_pair[0]
                vertex1 = connection_pair[1]
                if vertex0 not in self.vertList:
                    vertex0 = self.add_vertex(vertex0)
                else:
                    vertex0 = self.vertList[vertex0]
                if vertex1 not in self.vertList:
                    vertex1 = self.add_vertex(vertex1)
                else:
                    vertex1 = self.vertList[vertex1]
                self.vertList[vertex0.getId()].addNeighbor(vertex1)
                self.vertList[vertex1.getId()].addNeighbor(vertex0)

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if key not in self.vertList.keys():
            self.numVertices = self.numVertices + 1
            newVertex = Vertex(key)
            self.vertList[key] = newVertex
            return newVertex

    def __contains__(self, key):
        return key in self.vertList

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.vertList[v1].addNeighbor(self.vertList[v2])
        self.vertList[v2].addNeighbor(self.vertList[v1])

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        return sorted(list(self.vertList.keys()))

    def conn_components(self):
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        final_list = []
        # print(self.vertList.keys())
        # print(self.get_vertices())
        # vertices = self.get_vertices()
        for v in self.get_vertices():
            # print(v)
            # print(self.vertList[v])
            temp = self.vertList[v].getConnections()
            temp_list = [None] * (len(temp) + 1)
            temp_list[0] = v
            for count, i in enumerate(temp):
                temp_list[count + 1] = i.getId()
            # print(temp_list)
            final_list.append(temp_list)
        # print(final_list)
        for count, i in enumerate(final_list):
            # print("guess: "+str(i))
            if i == [-1]:
                pass
            else:
                for count2 in range(count + 1, len(final_list)):
                    # print("i: "+str(i))
                    # print("j: " + str(final_list[count2]))
                    if len(i) > 1:
                        for k in i:
                            if k in final_list[count2]:
                                final_list[count].extend(final_list[count2])
                                final_list[count2] = [-1]
        # print(final_list)
        while [-1] in final_list:
            final_list.remove([-1])
        # print(final_list)
        for count, i in enumerate(final_list):
            final_list[count] = sorted(list(set(i)))
        # print(final_list)
        final_list.sort(key=lambda x: x[0])
        # print(final_list)
        return final_list

    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        # print(self.get_vertices())
        # print(self.get_vertices()[0])
        v = self.get_vertices()[0]
        start = self.vertList[v]
        pass
        vertQueue = Queue(10000)
        vertQueue.enqueue(start)
        while vertQueue.size() > 0:
            currentVert = vertQueue.dequeue()
            for nbr in currentVert.getConnections():
                if currentVert.getColor() == 'white':
                    if nbr.getColor() == 'white':
                        nbr.setColor('gray')
                        vertQueue.enqueue(nbr)
                    elif nbr.getColor() == 'gray':
                        pass
                else:
                    if nbr.getColor() == 'white':
                        pass
                    elif nbr.getColor() == 'gray':
                        return False
        return True
