import pygame
from djkstras2 import Node
from djkstras2 import Graph
import time
from tkinter import messagebox
from tkinter import *

pygame.init()
pygame.display.set_caption("Djkstras Algorithm Visualiser")
window_size = (500,500)
screen = pygame.display.set_mode(window_size)
done = False

graph = Graph()
graph.get_nodes(500,25)

weights = {} #{node:weight}
shortest_paths = {}
visited = []
not_visited = graph.nodes.copy()

def display_result():
    Tk().wm_withdraw()
    res = shortest_paths[graph.end_node]
    if res >= 1000000000:
        res = "No Path Found!"
    result = "Shortest Distance: ",res
    messagebox.showinfo("Result",result)
    sys.exit()
    #print(len(visited))

def color_current_node(current_node):
    if current_node != graph.end_node and current_node != graph.start_node:
        pink = (255,192,203)
        pygame.draw.rect(screen, pink, (current_node.co_ordinates[0], current_node.co_ordinates[1], 25, 25), 0)
        pygame.display.update()
        time.sleep(0.05)

def initialise_weights(graph):
    for node in graph.nodes:
        if node == graph.start_node:
            weights[node] = 0
        else:
            weights[node] = 1000000000

def djkstras(graph):
    initialise_weights(graph)

    global shortest_paths
    global weights
    shortest_paths = weights.copy()
    current_node = min(weights.keys(), key=(lambda k: weights[k]))
    while not_visited and current_node!=graph.end_node:
        try:
            current_node = min(weights.keys(), key=(lambda k: weights[k]))
        except:
            break
        if current_node in visited:
            del weights[current_node]
            continue
        visited.append(current_node)
        not_visited.remove(current_node)

        for x in range (0,len(current_node.neighbours)):
            node = current_node.neighbours[x]
            if node in visited:
                continue
            current_wt = shortest_paths[node]
            if current_wt == 1000000000:# make this the same as the elif
                shortest_paths[node] = current_node.links[x] + shortest_paths[current_node]
            elif current_node.links[x] + shortest_paths[current_node] < current_wt:
                shortest_paths[node] = current_node.links[x]+shortest_paths[current_node]
        color_current_node(current_node)
        weights = shortest_paths.copy()
        del weights[current_node]
    #print(shortest_paths)
    display_result()

def draw_grid(offset,grid_size):
    blue = (0,0,255)
    for y in range (offset,501,grid_size):
        for x in range(offset,501,grid_size):
            pygame.draw.rect(screen,blue,(x,y,25,25),1)
        pygame.display.update()


def on_grid_click(x_click,y_click,color,count):
    x_click = (int)(x_click / 25) * 25
    y_click = (int)(y_click / 25) * 25
    if count == 0:
        graph.set_start((x_click,y_click))
    elif count == 1:
        graph.set_end((x_click,y_click))
    else:
        graph.set_blocked((x_click,y_click))

    pygame.draw.rect(screen, color , (x_click, y_click, 25, 25), 0)
    pygame.display.update()
    return x_click,y_click

draw_grid(0,25)
count = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and count >= 1:
            if event.key == pygame.K_RETURN:
                for node in graph.nodes:
                    graph.set_neighbours(node)
                djkstras(graph)
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_click , y_click = pygame.mouse.get_pos()
            if count == 0:
                point = on_grid_click(x_click, y_click, (0, 128, 0),count)
                count = 1
            elif count == 1:
                point = on_grid_click(x_click,y_click,(255,0,0),count)
                count = 2
            else:
                point = on_grid_click(x_click,y_click,(255,255,255),count)
                count = 3
pygame.quit()
