f = open("day8.txt", "r")

lines = [line.replace("\n","") for line in f if line != "\n"]

commands = lines[0]
lines.pop(0)
lines =[[line.split(" = ")[0],line.split(" = ")[1].split(", ")[0].replace("(",""),line.split(" = ")[1].split(", ")[1].replace(")","")] for line in lines]
#print(lines)
# for line in lines:
#     print(line)
class Node:
    def __init__(self, name:str, left= None,right = None):
        self.name = name
        self.left = left
        self.right = right
    
    def __str__(self):
        return self.name




root = Node("AAA")
node_list = [root]
node_names = ["AAA"]
# node_list = []
# find = ["",""]
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

root = node_list[0]

i = 0
current_node = root
steps = 0
while i <len(commands):
    if(current_node.name == "ZZZ"):
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
print("Part 1: ", steps)



    
    

