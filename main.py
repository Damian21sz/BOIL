# coding=utf-8
# Copyright 2023 Dawid Skora, Wojciech Sadzik, Damian Szelag
# LICENCE MIT

import graphviz
from datetime import date
from gui import Gui
import os

dot = graphviz.Digraph(comment='BOiL')

class Action:
    def __init__(self, name, duration):
        self.name = str(name)
        self.backwards = []
        self.forwards = []

    def add_backward(self, backward):
        self.backwards.append(backward)

    def add_forward(self, forward):
        self.forwards.append(forward)

class Node:
    def __init__(self, name):
        self.name = name
        self.min_duration = float('inf')
        self.max_duration = 0
        self.luz = 0

actions_arr = ["A", "B", "C"]
durations_arr = ["3", "3", "3"]
orders_arr = ["1-2","2-3", "1-3"]

actions_nr = int(orders_arr[-1].split("-")[1])

actions_obj = []
nodes = []

dot.node("legenda", label="{ " + "nr zdarzenia" + "|{" + "maksymalny czas" + "|" + "minimalny czas" + "}|" + "luz" + "}", shape='record')
dot.node("legenda2", label="czerwona -> ścieżka krytyczna", fontcolor="red")
dot.node("legenda3", label="czarna -> czynność")

for i, a in enumerate(actions_arr):
    obj = Action(a, durations_arr[i])
    actions_obj.append(obj)

for a in range(actions_nr):
    nodes.append(Node(a + 1))

for i, o in enumerate(orders_arr):
    order = o.split("-")
    first = int(order[0]) - 1
    second = int(order[1]) - 1

    actions_obj[first].add_forward(second)
    actions_obj[second].add_backward(first)

for i, a in enumerate(actions_arr):
    order = orders_arr[i].split("-")
    first = int(order[0]) - 1
    second = int(order[1]) - 1
    duration = durations_arr[i]

    sum_duration = nodes[first].max_duration + int(duration)
    
    if sum_duration > nodes[second].max_duration:
        nodes[second].max_duration = sum_duration
        
nodes[-1].min_duration = nodes[-1].max_duration

for i, a in reversed(list(enumerate(actions_arr))):
    order = orders_arr[i].split("-")
    first = int(order[0]) - 1
    second = int(order[1]) - 1
    duration = durations_arr[i]

    sum_duration = nodes[second].min_duration - int(duration)
    
    if sum_duration < nodes[first].min_duration:
        nodes[first].min_duration = sum_duration
    
for n in nodes:
    n.luz = n.min_duration - n.max_duration
    
for n in nodes:
    dot.node(str(n.name), label="{ " + str(n.name) + "|{" + str(n.min_duration) + "|" + str(n.max_duration) + "}|" + str(n.luz) + "}", shape='record')

# ==============================================================================================

def calc_critical_path(origin, obj, duration):
    path = []
    
    if len(obj.forwards) == 0:
        path.append(actions_nr)
        return path
    
    for i in obj.forwards:
        node = nodes[i]
        dur = find_duration(origin, node.name)

        if node.luz == 0 and duration + int(dur) == node.max_duration:
            next_node = calc_critical_path(int(node.name), actions_obj[i], node.max_duration)

            if next_node != None:
                for n in next_node:
                    path.append(n)

                path.append(origin)
            
    return path
        
def find_duration(first, second):
    o = str(first) + "-" + str(second)
    i = 0
    for order in orders_arr:
        if order == o:
            return durations_arr[i]
        
        i += 1
            
path = calc_critical_path(1, actions_obj[0], 0)
path.reverse()

i = 0
for o in orders_arr:
    order = o.split("-")
    first = int(order[0]) - 1
    second = int(order[1]) - 1
    
    in_critical_path = 0
    for p in range(len(path) - 1):
        if (first + 1) == path[p] and (second + 1) == path[p + 1]:
            in_critical_path = 1
            break

    if in_critical_path == 1:
        dot.edge(str(first + 1), str(second + 1), label=actions_obj[i].name+durations_arr[i], color="red")
    else:
        dot.edge(str(first + 1), str(second + 1), label=actions_obj[i].name+durations_arr[i])
    
    i += 1

# ==============================================================================================

# def calc_critical_path(origin, obj, duration):
#     critical_path = []
    
#     if len(obj.forwards) == 0:
#         critical_path.append(actions_nr)
#         return critical_path
    
#     critical_path.append(origin)
    
#     for f in obj.forwards:
#         critical_path = critical_path + calc_critical_path(f + 1, actions_obj[f], duration + int(durations_arr[f]))
        
#     return critical_path

# def draw_path(critical_path):
#     for i in range(len(critical_path) - 1):
#         dot.edge(str(critical_path[i]), str(critical_path[i + 1]), color='red')
#     dot.edge(str(critical_path[-1]), str(critical_path[-1]), color='red')


# for a in actions_obj:
#     if len(a.forwards) == 0:
#         draw_path(calc_critical_path(a.name, a, int(durations_arr[actions_arr.index(a.name)])))

today = date.today()
file_name = "test-output/round-table" + str(today) + ".gv"
print("Program was started")
#dot.render(file_name, view=True)
#gui = Gui()
#gui.start()
