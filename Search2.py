def A_Search(agent, target):
    
    start = agent.rect
    goal = target.rect
    
    prio = PriorityQueue()
    visited = set()
    pathway = dict()
    distance = {start: 0}
    prio.add(start)
    
    while prio:
        node = prio.pop()
        if node in visited:
            continue
        if node == target.rect:
            return path(pathway, start, node)
        visited.add(node)
        for successor in succesor_function(node):
            prio.add(
                successor,
                priority = distance[node] + 1 + heuristic(successor)
            )
   
    return #not really done, trying different approach