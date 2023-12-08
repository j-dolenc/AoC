import math
import numpy as np
f = open("day8.txt", "r")

lines = [line.replace("\n","") for line in f if line != "\n"]

commands = lines[0]
lines.pop(0)
lines =[[line.split(" = ")[0],line.split(" = ")[1].split(", ")[0].replace("(",""),line.split(" = ")[1].split(", ")[1].replace(")","")] for line in lines]

class Node:
    def __init__(self, name:str, left= None,right = None):
        self.name = name
        self.left = left
        self.right = right
    
    def __str__(self):
        return self.name

root = Node(lines[0][0])
node_list = [root]
node_names = [lines[0][0]]

for line in lines:
    if line[0] not in node_names:
        #create new node and append it to node_list
        new_node = Node(line[0])
        node_list.append(new_node)
        node_names.append(line[0])
        if(line[1] not in node_names):
            new_node.left = Node(line[1])
            node_names.append(line[1])
            node_list.append(new_node.left)
        else:
            for node in node_list:
                if node.name == line[1]:
                    new_node.left = node
                    break
        if(line[2] not in node_names):
            new_node.right = Node(line[2])
            node_names.append(line[2])
            node_list.append(new_node.right)
        else:
            for node in node_list:
                if node.name == line[2]:
                    new_node.right = node
                    break
    else:
        for node in node_list:
            #find node with same name
            if node.name == line[0]:
                #check if left  is in list
                if(line[1] not in node_names):
                    node.left = Node(line[1])
                    node_names.append(line[1])
                    node_list.append(node.left)
                else:
                    for node2 in node_list:
                        if node2.name == line[1]:
                            node.left = node2
                            break
                #check if right is in list
                if(line[2] not in node_names):
                    node.right = Node(line[2])
                    node_names.append(line[2])
                    node_list.append(node.right)
                else:
                    for node2 in node_list:
                        if node2.name == line[2]:
                            node.right = node2
                            break
                break

current_nodes = []
current_names = []
for node in node_list:
    if node.name[2] == "A":
        current_nodes.append(node)
        current_names.append(node.name)
#print(current_names)

sol_lens = [0 for _ in range(len(current_nodes))]
sol_index = 0
for node in current_nodes:
    i = 0
    current_node = node
    steps = 0
    while i <len(commands):
        if(current_node.name[2] == "Z"):
            break
        if(current_node != None):
            if(commands[i] == "L"):
                current_node = current_node.left
                steps+=1
            else:
                current_node = current_node.right
                steps+=1

        if(i  == len(commands)-1):
            i = 0
        else:
            i+=1
    sol_lens[sol_index] = steps
    sol_index+=1
#print(sol_lens)

def lcm(a,b):
    return a*b // math.gcd(a,b)

part = 1

for sol in sol_lens:
    part = lcm(part,sol)
print("Part 2: ", part)
