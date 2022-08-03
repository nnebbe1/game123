


    def A_Search(start, goal):
    
    
        open_lst = {start}
        closed_lst = {}
    
        dists = {}
        dists[start] = 0
    
        path = {}
        path[start] = start
    
        while open_lst: 
            n = None
        
            for v in open_lst:
                if n == None or dists[v] + self.h(v) < dists[n] + self.h(n):
                    n = v
                
            if n == None:
                return None
        
        
            if n == goal:
                reconst_path = []
            
                while path[n] != n:
                    reconst_path.append(n)
                    n = path[n]
                
                reconst_path.append(start)
            
                reconst_path.reverse()
            
                return reconst_path
            
            for m in self.get_neighbors(n):
          # if the current node is not presentin both open_lst and closed_lst
            # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    path[m] = n
                    dists[m] = dists[n] + 1
 
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if dists[m] > dists[n] + 1:
                        dists[m] = dists[n] + 1
                        path[m] = n
 
                    if m in closed_lst:
                        closed_lst.remove(m)
                        open_lst.add(m)
 
            open_lst.remove(n)
            closed_lst.add(n)
        
        return None
                
                
                
                
                
                
                
