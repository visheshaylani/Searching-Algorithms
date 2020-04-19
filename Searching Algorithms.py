import queue as q
from queue import LifoQueue 

# Breadth First Search
def bfs(graph, source, dest):    
    if source not in graph:
        print('%s is not found in the graph' %(source))
        return 
    if dest not in graph:
        print('%s is not found in the graph' %(dest))
        return
    if source == dest:
        return
    
    flag = 0
    visited_cost = 0
    cost = 0
    parent = {}
    queue = q.Queue()
    queue.put((0,source))
    parent[source] = {source: 0}
    visited = []
    visited.append(source)
    
    while queue.empty() == 0:
        node = queue.get()
        current_node = str(node[1])
        
        for neighbor in graph[current_node]:
            
            if neighbor not in parent:
                queue.put((cost + graph[current_node][neighbor] , neighbor))
                parent[neighbor] = (graph[current_node][neighbor] , current_node)   # (cost , node)
                visited.append(neighbor)
                visited_cost += graph[current_node][neighbor]   # visited cost
                
            if neighbor == dest: # if destination found.
                flag += 1
                queue.put((cost + graph[current_node][neighbor] , neighbor))
                parent[neighbor] = (graph[current_node][neighbor] , current_node)           
                path = [dest]
                
                if flag == 1:
                    while dest != source:
                        t1 = dest
                        dest = parent[dest][1]  # retreive parent from parent{} which is at the 1 index of every node.
                        t2 = dest
                        cost += graph[t1][t2]   # retreive cost from the graph
                        path.insert(0,dest)     # put at the 0 index in the path[]
                    print("Visited: %s, cost = %s" %(str(visited), str(visited_cost)))
                    print()
                    print("Path: %s, cost = %s" %(str(path), str(cost)))
    return

# Uniform Cost Search
def UCS(graph, source, dest):
    if source not in graph:
        print('%s is not found in the graph' %(source))
        return 
    if dest not in graph:
        print('%s is not found in the graph' %(dest))
        return
    if source == dest:
        return
    
    Q = q.PriorityQueue()
    Q.put((0, [source]))    # source has 0 cost to reach itself
    visited = []
    visited.append(source)
    visited_cost = 0
    
    while Q.empty() == 0:
        node = Q.get()
#        print('Node: ', node)
        current_node = str(node[1][len(node[1]) -1])
#        print("Current Node: ", current_node)
        if dest in node[1]:
            print('Visited: %s, cost = %s' %(str(visited), str(visited_cost)) )
            print()
            print('Path: %s, cost = %s' %(str(node[1]), str(node[0])) )
            break
        cost = node[0]
        
        for neighbor in graph[current_node]:
            t = node[1][:]
#            print('Tmep: ', t)
            t.append(neighbor)
#            print('Append: ', t)
            Q.put((cost + graph[current_node][neighbor], t))
            
            if neighbor not in visited:
                visited.append(neighbor)
                visited_cost += graph[current_node][neighbor]                
    return

# Greedy Best First Search
def GreedyDFS(graph, source, dest, heuristics):    
    if source not in graph:
        print('%s is not found in the graph' %(source))
        return 
    if dest not in graph:
        print('%s is not found in the graph' %(dest))
        return
    if source == dest:
        return
    
    flag = 0
    cost = 0
    parent = {}
    queue = q.PriorityQueue()
    queue.put((0,source))
    parent[source] = {source: 0}
    visited = []
    visited.append(source)
    visited_cost = 0
    
    while queue.empty() == 0:
        node = queue.get()
        
        while(queue.empty() == 0): # doing Priority list empty after selecting the node with min heuristic
            queue.get()
            
        current_node = str(node[1])
            
        for neighbor in graph[current_node]:
            if neighbor not in parent:
                queue.put((int(heuristics[neighbor]) , neighbor))   # put (heuristic, node) in the priority Queue. 
                parent[neighbor] = (graph[current_node][neighbor] , current_node)
                visited.append(neighbor)
                visited_cost += graph[current_node][neighbor]
                
            if neighbor == dest: # if destination found.
                flag += 1
                queue.put((int(heuristics[neighbor]) , neighbor))
                parent[neighbor] = (graph[current_node][neighbor] , current_node)              
                path = [dest]
                
                if flag == 1:
                    while dest != source:
                        t1 = dest
                        dest = parent[dest][1]
                        t2 = dest
                        cost += graph[t1][t2]
                        path.insert(0,dest)
                    print("Visited: %s, cost = %s" %(str(visited), str(visited_cost)))
                    print()                        
                    print("Path: %s, cost = %s" %(str(path), str(cost)))
                
    if flag == 0:
        print("DESTINATION NOT FOUND")
    return

# Depth Limited Search
def DLS(graph, source, dest, depth):
   stack = LifoQueue()
   parent = {}
   visited = []
   cost = 0
   stack.put((0 , source))
   parent[source] = {source : 0}
   visited.append(source)
   visited_cost = 0
   flag = 0
   limit = 0
   
   while stack.empty() == 0:
       if limit <= depth:
           node = stack.get()
           limit -= 1
           current_node = str(node[1])
           
           for neighbor in graph[current_node]:
               
               if neighbor not in parent:
#                   print(neighbor)
                   visited.append(neighbor)
                   visited_cost += graph[current_node][neighbor]
                   stack.put((graph[current_node][neighbor] , neighbor))
                   parent[neighbor] = (graph[current_node][neighbor] , current_node)
                   limit += 1
                   
                   if neighbor == dest: # if destination found.
                       flag += 1
                       stack.put((graph[current_node][neighbor] , neighbor))
                       parent[neighbor] = (graph[current_node][neighbor] , current_node)                    
                       path = [dest]
                       
                       if flag == 1:
                           while dest != source:
                               t1 = dest
                               dest = parent[dest][1]
                               t2 = dest
                               cost += graph[t1][t2]
                               path.insert(0,dest)
                           print("Visited: %s, cost = %s" %(str(visited), str(visited_cost)))
                           print()                               
                           print("Path: %s, cost = %s" %(str(path), str(cost)))   
#                           print('Limit: ', limit) 
                       return True                
       if limit >= depth:
           return False                  
   return

# Iterative Deepening Depth First Search
def IDDFS(graph, source, dest, depth):
    for i in range(depth):
        if DLS(graph, source, dest, i) == True:
#            print('IDDFS: ', i)
            return True
    print('DESTINATION NOT FOUND WITHIN MAX DEPTH')    
    return False

    
# Main
if __name__ == '__main__':
    source = 'Arad'
    dest = 'Bucharest'
    
    graph = {
     'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140}, 
     'Zerind': {'Oradea': 71, 'Arad': 75}, 
     'Timisoara': {'Arad': 118, 'Lugoj': 111}, 
     'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'RimnicuVilcea': 80}, 
     'Oradea': {'Zerind': 71, 'Sibiu': 151}, 
     'Lugoj': {'Timisoara': 111, 'Mehadia': 70}, 
     'RimnicuVilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146}, 
     'Mehadia': {'Lugoj': 70, 'Dobreta': 75}, 
     'Craiova': {'Dobreta': 120, 'RimnicuVilcea': 146, 'Pitesti': 138}, 
     'Pitesti': {'RimnicuVilcea': 97, 'Craiova': 138, 'Bucharest': 101}, 
     'Fagaras': {'Sibiu': 99, 'Bucharest': 211}, 
     'Dobreta': {'Mehadia': 75, 'Craiova': 120}, 
     'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85}, 
     'Giurgiu': {'Bucharest': 90}, 'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98}, 
     'Vaslui': {'Urziceni': 142, 'Iasi': 92}, 
     'Hirsova': {'Urziceni': 98, 'Eforie': 86}, 
     'Iasi': {'Vaslui': 92, 'Neamt': 87}, 
     'Eforie': {'Hirsova': 86}, 
     'Neamt': {'Iasi': 87}
     }
    
    heuristics = {
            'Arad': '366', 'Bucharest': '0', 'Craiova': '160', 'Dobreta': '242', 
            'Eforie': '161', 'Fagaras': '178', 'Giurgiu': '77', 'Hirsova': '151', 
            'Iasi': '226', 'Lugoj': '244', 'Mehadia': '241', 'Neamt': '234', 
            'Oradea': '380', 'Pitesti': '98', 'RimnicuVilcea': '193', 'Sibiu': '253', 
            'Timisoara': '329', 'Urziceni': '80', 'Vaslui': '199', 'Zerind': '374'
            }
    
    print()
    print('********************Breath First Search********************')
    print()
    bfs(graph, source, dest)
    print()
    
    print('********************Unifrom Cost Search********************')
    print()
    UCS(graph, source, dest)
    print()
    
    print('********************Gready Breath First Search********************')
    print()
    GreedyDFS(graph, source, dest, heuristics)
    print()
    
    print('********************Iterative Deepening DFS********************')
    print()
    IDDFS(graph, source, dest, 10)
    print()    