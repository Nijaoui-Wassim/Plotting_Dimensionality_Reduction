import math
import pygame
import random
import numpy as np
from plotting_tools import *

shift_xis = 0
shift_yis = 0
shift_angle = 0
scale_input = 1
shift_step = np.pi / 15
step = 1
navigation_step = 50
navigation_shift_x,navigation_shift_y = 0,0
axis_angle = 0
num_random_points = 3
radius = 100
index = 0

def generate_points(num_random_points, num_d, radius, cls):
    random_points, classes, header = [], [], []
    header = ["D "+str(i+1) for i in range(num_d)]
    for i in range(num_random_points):
        for j in range(cls):
            random_point = np.random.randint(0, abs(radius), size = num_d)
            random_points.append(random_point)
            classes.append(j)
    return random_points , classes, header

def plot_array(random_points, classes, num_d, header):   
    global navigate_up,navigate_down,navigate_right,navigate_left,move_up,move_down,move_right,move_left,show_final_points,zoom_in, zoom_out, reset_vue,hide_lines,go_dim_up, go_dim_down,running, shift_angle_up, shift_angle_down, radius, step, navigation_step, navigation_shift_x,navigation_shift_y, axis_angle, num_random_points, shift_step, scale_input, shift_angle, shift_xis, shift_yis, index
    #variables
    class_color = [(0, 0, 0), (255, 102, 102), (255, 179, 102), (255, 255, 102), (179, 255, 102), (102, 255, 140), (102, 255, 255), (102, 140, 255), (140, 102, 255), (217, 102, 255), (255, 102, 179), (0, 255, 0), (255, 0, 0),(0, 0, 255)]
    created_classes = np.unique(classes)
    axis_angle = 2*np.pi/num_d + shift_angle
    #maximum_per_dimension = [0 for i in range(num_d)]
    score_value = update_score(num_d)
    if len(created_classes) > 13:
        for j in range(len(created_classes)-13):
            color = ((np.random.randint(0, 255, size = 1))[0], (np.random.randint(0, 255, size = 1))[0], (np.random.randint(0, 255, size = 1))[0])
            class_color.append(color)
    # Create a unique color to each different class 
    for i in range(len(classes)):
        for j in range(len(created_classes)):
            if classes[i] == created_classes[j]:
                points_color.append(class_color[j])
                break 
            
    # Make all classes visible
    show_class = [True for i in range(len(classes))]
    while running:
        if hide_lines == False: 
            screen.blit(bg, (0, 0))
        else:
            screen.fill((255,255,255)) #change background color - white
        for event in pygame.event.get():      #get all user events
            try:
                running, move_up, move_down, move_right, move_left, reset_vue, zoom_in, zoom_out, go_dim_up, go_dim_down, hide_lines, navigate_up, navigate_down, navigate_right, navigate_left, show_class, shift_angle_up, shift_angle_down, show_final_points, scale_input , index = get_user_input(event, running, move_up, move_down, move_right, move_left, reset_vue, zoom_in, zoom_out, go_dim_up, go_dim_down, hide_lines, navigate_up, navigate_down, navigate_right, navigate_left, show_class, shift_angle_up, shift_angle_down, show_final_points, scale_input, created_classes, classes, index)
            except Exception as e:
                print(e)
        if move_up:
            shift_yis -= step
        if move_down:
            shift_yis += step
        if move_right:
            shift_xis += step
        if move_left:
            shift_xis -= step
        if shift_angle_up: #shift_angle_up, shift_angle_down
            shift_angle += shift_step
        elif shift_angle_down:
            shift_angle -= shift_step
        if go_dim_up:
            num_d += 1
            axis_angle = 2*np.pi/num_d + shift_angle
            score_value = update_score(num_d)
            #maximum_per_dimension = [0 for i in range(num_d)]
            go_dim_up = False
        if go_dim_down:
            num_d -= 1
            axis_angle = 2*np.pi/num_d + shift_angle
            score_value = update_score(num_d)
            #maximum_per_dimension = [0 for i in range(num_d)]
            go_dim_down = False
        if zoom_in:
            radius += step
        elif zoom_out:
            radius -= step
        if reset_vue:
            shift_angle = 0
            shift_xis = 0
            shift_yis = 0 
            radius = 100
            #scale_input = 1
            navigation_shift_x,navigation_shift_y = 0,0
        if navigate_up:
            navigation_shift_y += navigation_step
        if navigate_down:
            navigation_shift_y -= navigation_step
        if navigate_right:
            navigation_shift_x -= navigation_step
        if navigate_left:
            navigation_shift_x += navigation_step
        random_points = np.array(random_points) * scale_input
        #maximum_per_dimension = update_maximum_dimensions(maximum_per_dimension, num_d, random_points)
    #try:
        axis_x = [np.cos(shift_angle) * radius + origin_x]
        axis_y = [-np.sin(shift_angle) * radius + origin_y]
        axis_ang = [shift_angle]
        for i in range(1,num_d):
            if radius < step+1:
                radius = step+2
            x = np.cos((axis_angle) * i+ shift_angle) * radius
            y = np.sin((axis_angle) * i+ shift_angle) * radius
            #y = math.sin(math.radians(axis_angle * i)) * radius
            axis_x.append(x + origin_x)
            axis_y.append(-y + origin_y)
            axis_ang.append((axis_angle) * i+ shift_angle)
            x,y = 0,0
        #show scare
        if hide_lines == False:
            show_score(TextX, TextY, score_value)
        if hide_lines == False and (num_d<50): 
            if ((abs(navigation_shift_x)< screen_w)or(abs(navigation_shift_y)< screen_h)):
                for i in range(len(axis_x)):
                    pygame.draw.line(screen, (0,0,0),(int(origin_x+shift_xis+navigation_shift_x), int(origin_y+shift_yis+navigation_shift_y)),(int(axis_x[i]+navigation_shift_x), int(axis_y[i]+navigation_shift_y)))
                    draw_points(axis_x[i]+navigation_shift_x,axis_y[i]+navigation_shift_y, shift_x = 0, shift_y = 0)
                draw_points(origin_x+navigation_shift_x ,origin_y+navigation_shift_y ,shift_x = shift_xis, shift_y = shift_yis)
                # connect end of axis together optionnal
                conect_points(np.array(axis_x)+navigation_shift_x, np.array(axis_y)+navigation_shift_y, COLOR = (10,255,255))
        for i in range(len(axis_x)):
            spacing_x, spacing_y = 0, 0
            if(num_d<20): 
                if axis_x[i] > origin_x :
                    spacing_x = 10
                else:
                    spacing_x = -100
                if axis_y[i] > origin_y :
                    spacing_y = 10
                else:
                    spacing_y = -50
                show_score(int(axis_x[i]+navigation_shift_x+spacing_x), int(axis_y[i]+navigation_shift_y+spacing_y),header[i],18)
            elif i%(int(num_d*0.1)) == 0:
                if axis_x[i] > origin_x :
                    spacing_x = 10
                else:
                    spacing_x = -100
                if axis_y[i] > origin_y :
                    spacing_y = 10
                else:
                    spacing_y = -50
                show_score(int(axis_x[i]+navigation_shift_x+spacing_x), int(axis_y[i]+navigation_shift_y+spacing_y),header[i],18)                
        final_point_x = 0 # origin_x + shift_xis 
        final_point_y = 0 # origin_y + shift_yis
        point_x, point_y,final_point_x,final_point_y = ditribute_points(random_points, classes, num_d, radius, step, axis_ang, origin_x, origin_y, shift_xis, shift_yis, points_color, hide_lines, final_point_x, final_point_y, navigation_shift_x,navigation_shift_y, show_class,  show_final_points, scale_input)
        #show legend
        legend_x ,legend_y = 50, 50
        legend_step = 50
        #rates = return_rates_for_test_point(train_set,test_point,classes)
        for i in range(len(created_classes)):
            draw_points(legend_x ,legend_y , shift_x = 0, shift_y = 0,  COLOR = class_color[i], r = 20)
            show_score((legend_x+30), (legend_y), created_classes[i] ,18) 
            legend_y += legend_step
        pygame.display.update()   #to update screen
        #except Exception as e:
        #    print(e)
