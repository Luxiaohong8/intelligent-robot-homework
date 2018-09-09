import numpy as np
import matplotlib.pyplot as plt

#A* algorithm (in case heuristic is not 0)
def run_path_planning(occ_map, start, goal):
  plot_map(occ_map, start, goal)

  # cost values for each cell, filled incrementally. 
  # Initialize with infinity
  costs = np.ones(occ_map.shape) * np.inf
  
  # cells that have already been visited
  closed_flags = np.zeros(occ_map.shape)
  
  # store predecessors for each visited cell 
  predecessors = -np.ones(occ_map.shape + (2,), dtype=np.int)

  # heuristic for A*
  heuristic = np.zeros(occ_map.shape)
  for x in range(occ_map.shape[0]):
    for y in range(occ_map.shape[1]):
      heuristic[x, y] = get_heuristic([x, y], goal)

  parent = start
  costs[start[0], start[1]] = 0

  # loop until goal is found
  while not np.array_equal(parent, goal):
    
    open_costs = np.where(closed_flags==1, np.inf, costs) + heuristic

    x, y = np.unravel_index(open_costs.argmin(), open_costs.shape)
    
    if open_costs[x, y] == np.inf:
      break
    parent = np.array([x, y])
    closed_flags[x, y] = 1;
    
    neighbors=get_neighborhood(parent,occ_map.shape)
    for child in neighbors:
      child_cost=costs[x,y]+get_edge_cost(parent,child,occ_map)
      if child_cost<costs[child]:
        costs[child]=child_cost
        predecessors[child]=parent

    plot_expanded(parent, start, goal)

  if np.array_equal(parent, goal):
    path_length = 0
    while predecessors[parent[0], parent[1]][0] >= 0:
      plot_path(parent, goal)
      predecessor = predecessors[parent[0], parent[1]]
      path_length += np.linalg.norm(parent - predecessor)
      parent = predecessor
  plt.waitforbuttonpress()

def get_neighborhood(cell, occ_map_shape):
  neighbors = []
  for i in [-1,0,1]:
    for j in [-1,0,1]:
      x=cell[0]+i
      y=cell[1]+j
      if x<0 or x>=occ_map_shape[0]:continue
      if y<0 or y>=occ_map_shape[1]:continue
      if i==0 and j==0:continue
      neighbors.append((x,y))
  return neighbors

#  Calculate cost for moving from parent to child.
def get_edge_cost(parent, child, occ_map):
  occ = occ_map[child[0], child[1]]
  edge_cost = np.linalg.norm(parent-child)
  edge_cost+=10*occ
  if occ>=0.5:
    edge_cost=np.inf
  return edge_cost

def get_heuristic(cell, goal):
  heuristic = 0
  cost=1*np.linalg.norm(cell-goal)
  return cost

def plot_map(occ_map, start, goal):
  plt.imshow(occ_map.T, cmap=plt.cm.gray)
  plt.plot([start[0]], [start[1]], 'ro')
  plt.plot([goal[0]], [goal[1]], 'go')
  plt.axis([0, occ_map.shape[0]-1, 0, occ_map.shape[1]-1])
  plt.xlabel('x')
  plt.ylabel('y')

def plot_expanded(expanded, start, goal):
  if np.array_equal(expanded, start) or np.array_equal(expanded, goal):
    return
  plt.plot([expanded[0]], [expanded[1]], 'y+')
  plt.pause(1e-10)

def plot_path(path, goal):
  if np.array_equal(path, goal):
    return
  plt.plot([path[0]], [path[1]], 'bo')
  plt.pause(1e-6)

occ_map = np.loadtxt('mymap.txt')
start = np.array([20, 2])
goal = np.array([2, 5])
run_path_planning(occ_map, start, goal)

