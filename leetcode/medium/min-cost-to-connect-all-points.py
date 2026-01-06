class Solution:
    def find(self,i):
        if self.components[i]==i:
            return i
        self.components[i] = self.find(self.components[i])
        return self.components[i]

    def union(self,i,parent):
        if self.components[i]==i:
            self.components[i] = parent
        else:
            self.union(self.components[i],parent)
            self.components[i] = parent

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i,point1 in enumerate(points):
            for j,point2 in enumerate(points):
                if i!=j:
                    
edges.append([abs(point1[0]-point2[0])+abs(point1[1]-point2[1]),i,j])
        edges = sorted(edges)
        cost = 0
        self.components = [i for i in range(len(points))]
        n_connected_edges = 0
        for edge in edges:
            if n_connected_edges==len(points)-1:
                break
            parent_edge_1 = self.find(edge[1])
            parent_edge_2 = self.find(edge[2])
            if parent_edge_1!=parent_edge_2:
                cost+=edge[0]
                self.union(edge[1],parent_edge_2)
                n_connected_edges+=1
        return cost
            





        
