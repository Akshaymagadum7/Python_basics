class unionFind:
    def __init__(self, n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*(n)
    
    def find(self, x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
        
    def union(self, v1, v2):
        v1_parent=self.find(v1)
        v2_parent=self.find(v2)
        
        if v1_parent==v2_parent:
            return True
        
        if self.rank[v1_parent]>self.rank[v2_parent]:
            self.parent[v2_parent]=v1_parent
            
        if self.rank[v1_parent]<self.rank[v2_parent]:
            self.parent[v1_parent]=v2_parent
            
        else:
            self.parent[v1_parent]=v2_parent
            self.rank[v2_parent]+=1
            
            
class Solution:
    def detectCycle(self, v, adj):
        uf=unionFind(v)
        
        for v1 in range(v):
            for v2 in adj[v1]:
                if v1<v2:
                    
                    v1_parent=uf.find(v1)
                    v2_parent=uf.find(v2)
                    print(v1_parent,v2_parent)
                    
                    if v1_parent==v2_parent:
                        return 1
                    uf.union(v1, v2)
	                
        return 0 #False


s=Solution()
v=5
adj=[[2,3,4], [3], [0,4], [1,0], [0,2]]
ans=s.detectCycle(v, adj)
print(ans)