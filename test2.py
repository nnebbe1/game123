import math 

def heuristic_function(grid_node:tuple)->int:
        x_coord, y_coord = grid_node
        x_distance = int(abs(x_coord - 10))+1
        y_distance = int(abs(y_coord - 10))+1
        return int(math.sqrt(x_distance*x_distance + y_distance*y_distance))

print(heuristic_function((5,5)))