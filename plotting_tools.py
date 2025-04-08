# Title 
import pygame
import numpy as np

the_rs = []
#initializing pygame
pygame.init()

font = pygame.font.Font("assets//Sportive-Regular.ttf", 32)
font2 = pygame.font.Font("assets//font2.otf", 100)

#Load background image
bg = pygame.image.load("assets//background.png")

#creating game window
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# put it not fullscreen
screen = pygame.display.set_mode((800, 600))

#font size
TextX = 200
TextY = 100
#screen width and height
# get real screen width and height
infoObject = pygame.display.Info()
screen_w = infoObject.current_w
screen_h = infoObject.current_h

point_x = []
point_y = []

points_color = []

class_one_color = (173, 49, 192)
class_two_color = (226, 181, 55)

class_one_color_with_alpha = (173, 49, 192, 100)
class_two_color_with_alpha = (226, 181, 55, 100)

origin_x = screen_w/2
origin_y = screen_h/2

navigate_up,navigate_down,navigate_right,navigate_left = False,False,False,False
move_up,move_down,move_right,move_left,show_final_points = False,False,False,False,False
shift_angle_up, shift_angle_down = False, False
zoom_in, zoom_out, reset_vue = False,False,False
hide_lines,go_dim_up, go_dim_down,running = False, False, False, True

#navigate_up,navigate_down,navigate_right,navigate_left,move_up,move_down,move_right,move_left,show_final_points,zoom_in, zoom_out, reset_vue,hide_lines,go_dim_up, go_dim_down,running, show_all_classes, show_class_one, show_class_two, shift_angle_up, shift_angle_down

#change title
pygame.display.set_caption("Plotting in the nth Dimension")

#change icon
icon = pygame.image.load("assets//icon.png") #define icon
pygame.display.set_icon(icon)             #set the icon

#Load background image
bg = pygame.image.load("assets//background.png")
       
def update_score(num_d = 3):
    if num_d == 1:
        score_value = "Plotting in the 1st Dimession"
    elif num_d ==2:
        score_value = "Plotting in the 2nd Dimession"
    elif num_d ==3:
        score_value = "Plotting in the 3rd Dimession"
    else:
        score_value = "Plotting in the "+ str(num_d)+"th Dimession"
    return score_value

def fill_shape(origin_x, origin_y, list_x, list_y, navigation_shift, COLOR = (150,150,22), thickness = 3):
    for i in range(len(list_x)-1):
        pygame.draw.polygon(screen, COLOR, [[origin_x + navigation_shift, origin_y + navigation_shift], [list_x[i] + navigation_shift, list_y[i] + navigation_shift], [list_x[i+1] + navigation_shift, list_y[i+1] + navigation_shift]], thickness)
    pygame.draw.polygon(screen, COLOR, [[origin_x + navigation_shift, origin_y + navigation_shift], [list_x[0] + navigation_shift, list_y[0] + navigation_shift], [list_x[-1] + navigation_shift, list_y[-1] + navigation_shift]], thickness)

def ditribute_points(random_points, classes, num_d, radius, step, axis_ang, origin_x, origin_y, shift_xis, shift_yis, points_color, hide_lines, final_point_x, final_point_y, navigation_shift_x,navigation_shift_y, show_class,  show_final_points, scale_input): 
    temp_x, temp_y = 0, 0
    for k in range(len(random_points)):
        point_x_class, point_y_class=[], []
        final_point_x, final_point_y = 0, 0
        for i in range(num_d):
            mycolor = (0,0,0)
            if radius < step+1:
                radius = step+2              
            r = 1-((random_points[k][i] )/(radius)) #maximum_per_dimension[i]
            x = np.cos(axis_ang[i]) * random_points[k][i] + origin_x + shift_xis*r
            y = -np.sin(axis_ang[i]) * random_points[k][i] + origin_y + shift_yis*r
            point_x.append(x)
            point_y.append(y)
            point_x_class.append(x)
            point_y_class.append(y)
            if show_final_points and (show_class[k]):
                temp_x, temp_y = final_point_x, final_point_y
                final_point_x +=  np.cos(axis_ang[i]) * random_points[k][i]  + shift_xis*r - shift_xis
                final_point_y +=  -np.sin(axis_ang[i]) * random_points[k][i] + shift_yis*r - shift_yis #y - (origin_y + shift_yis*r)
            try:
                ind = classes.index(classes[k])
            except:
                ind = list(classes).index(classes[k])
            if (show_class[ind]):
                #try:
                draw_points(x + navigation_shift_x,y + navigation_shift_y, 0, 0 ,COLOR = points_color[k]) 
                if hide_lines == False: #connect other points to it
                    if i == num_d-1:
                        conect_points(np.array(point_x_class) + navigation_shift_x, np.array(point_y_class) + navigation_shift_y, COLOR = points_color[k]) #show connection
            #draw fnal point
            #if show_final_points and (show_class[k]):
                #draw_points(final_point_x* scale_input+origin_x+ navigation_shift_x+ shift_xis,final_point_y* scale_input+ navigation_shift_y+origin_y+ shift_yis, 0, 0 ,COLOR = points_color[k] ,r=3)
                #pygame.draw.line(screen, points_color[k],(final_point_x* scale_input+origin_x+ navigation_shift_x+ shift_xis,final_point_y* scale_input+ navigation_shift_y+origin_y+ shift_yis),(temp_x+origin_x+ navigation_shift_x+ shift_xis,temp_y+ navigation_shift_y+origin_y+ shift_yis))
#===============================

        if show_final_points and (show_class[k]):
            draw_points(final_point_x* scale_input+origin_x+ navigation_shift_x+ shift_xis,final_point_y* scale_input+ navigation_shift_y+origin_y+ shift_yis, 0, 0 ,COLOR = points_color[k] ,r=10)

    return point_x, point_y,final_point_x* scale_input,final_point_y* scale_input
                

def show_score(x,y,score_value, fonrt_size = 32):
    if fonrt_size == 32:
        score = font.render(str(score_value),True, (0, 0, 0))
    else:
        font1 = pygame.font.Font("assets//Sportive-Regular.ttf", fonrt_size)
        score = font1.render(str(score_value),True, (0, 0, 0))
    screen.blit(score, (x, y))

def draw_points(x,y, shift_x, shift_y,width = screen_w, height = screen_h ,  COLOR = (255,0,0), r = 5):
    if len(COLOR) == 4:
        surface = pygame.Surface((width,height), pygame.SRCALPHA)
        pygame.draw.circle(surface,COLOR,(int(x+shift_x), int(y+shift_y)),r)
        screen.blit(surface, (0,0))
    else:
        pygame.draw.circle(screen, COLOR, [int(x+shift_x), int(y+shift_y)], r)

def conect_points(list_of_points_x, list_of_points_y, COLOR = (0,0,0)):
    for i in range(len(list_of_points_x)-1):
        try:
            pygame.draw.line(screen, COLOR,(int(list_of_points_x[i]), int(list_of_points_y[i])),(int(list_of_points_x[i+1]), int(list_of_points_y[i+1])))
        except:
            pygame.draw.line(screen, COLOR,(int(list_of_points_x[i]), int(list_of_points_y[i])),(int(list_of_points_x[i+1])+5, int(list_of_points_y[i+1])+5))

    pygame.draw.line(screen, COLOR,(int(list_of_points_x[0]), int(list_of_points_y[0])),(int(list_of_points_x[-1]), int(list_of_points_y[-1])))

def get_line_X_y(minimum, maximum, slope = 1, b = 0, step = 1):
    X = [int(i) for i in range(minimum, maximum, step)]
    y = []
    for x in X:
        y.append(-slope*x+b)
    return X, y

def line_len(x1,y1,x2,y2):
    D = np.sqrt(math.pow((x1-x2),2)+math.pow((y1+y2),2))
    return D

def update_maximum_dimensions(num_d, random_points):
    maximum_per_dimension = [0 for i in range(num_d)]
    for i in range(len(random_points)):
        for j in range(num_d):
            if maximum_per_dimension[j] < random_points[i][j]:
                maximum_per_dimension[j] = random_points[i][j]
    return maximum_per_dimension

def predict(X_train,y_train,X_test,y_test, eps = 10, show_details = False):
    correct_pred, rst, conf_rates = 0, 0, []
    for i in range(len(X_test)):
        point_rate, conf_rates = return_rates_for_test_points(X_train,X_test[i],y_train, eps,conf_rates)
        ind = point_rate.index(max(point_rate))
        if sum(point_rate) != 0:
            confidence = round(point_rate[ind] / sum(point_rate) , 3)
        else:
            confidence = 0
        if show_details:
            print("ground_truth: ",y_test[i], "predicted: ",ind,"confidance: ", confidence)
        if y_test[i] == ind:
            correct_pred+= 1
    if len(X_test) == 0:
        rst = round(correct_pred/ len(X_test),3)
    else:
        rst = round(correct_pred/ len(y_test),3)
    if show_details:
        print("accuracy : ",rst)
    return rst

def return_rates_for_test_points(train_set,test_point,classes, eps = 10, conf_rates=[]):
    created_classes = np.unique(classes)
    epsilone = np.array(update_maximum_dimensions(len(train_set[0]), train_set))
    epsilone = epsilone / eps
    rows, cols = (len(train_set[0]), len(created_classes)) 
    rates = [[0 for i in range(cols)] for j in range(rows)] 
    final_rates = [0 for j in range(rows)] 
    if conf_rates == []:
        conf_rates = [[1 for i in range(cols)] for j in range(rows)] 
    for i in range(len(train_set)):
        for j in range(len(test_point)):
            if ((train_set[i][j] < test_point[j]+epsilone[j])and(train_set[i][j] > test_point[j]-epsilone[j])):
                try:
                    ind = int(created_classes.index(classes[i]))
                except:
                    ind = int(list(created_classes).index(classes[i]))
                rates[j][ind] = rates[j][ind] + 1 *conf_rates[j][ind] 
    final_rates = [0 for i in range(len(rates[0]))]
    for i in range(len(rates[0])):
        for j in range(len(rates)):
            final_rates[i]+= rates[j][i]
    inde = final_rates.index(max(final_rates))
    for i in range(len(rates[0])):
        for j in range(len(rates)):
            if classes[i] == inde:
                conf_rates[j][i]+= 0.1
            #else:
            #    conf_rates[j][i]-= 0.1
            
    return final_rates, conf_rates

def get_user_input(event, running, move_up, move_down, move_right, move_left, reset_vue, zoom_in, zoom_out, go_dim_up, go_dim_down, hide_lines, navigate_up, navigate_down, navigate_right, navigate_left, show_class, shift_angle_up, shift_angle_down, show_final_points, scale_input, created_classes, classes, index):
    if event.type == pygame.QUIT:     # pressing the close button = Pygame.Quit
        running = False               #quit the window
        pygame.display.quit()
        pygame.quit()
    #get keyboard input
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            move_up = True
        if event.key == pygame.K_DOWN:
            move_down = True
        if event.key == pygame.K_RIGHT:
            move_right = True
        if event.key == pygame.K_LEFT:
            move_left = True
        if event.key == pygame.K_r:
            reset_vue = True
        if event.key == pygame.K_q: #zoom_in, zoom_out, reset_vue
            zoom_in = True
        if event.key == pygame.K_e:
            zoom_out = True
        if event.key == pygame.K_u:    
            go_dim_up = True
        if event.key == pygame.K_i:    
            go_dim_down = True
        if event.key == pygame.K_w:
            navigate_up= True
        if event.key == pygame.K_s:
            navigate_down= True
        if event.key == pygame.K_a:
            navigate_left= True
        if event.key == pygame.K_g:
            shift_angle_up = True
        if event.key == pygame.K_f:
            shift_angle_down = True
        if event.key == pygame.K_d:
            navigate_right= True
        if event.key == pygame.K_p:
            scale_input += 0.01
        if event.key == pygame.K_l:
            scale_input -= 0.01
        if event.key == pygame.K_c: #show_all_classes, show_class_one, show_class_two = True, False, False              
            if index >= len(created_classes):
                for i in range(len(classes)):
                    show_class[i] = True 
                    index = 0
            else:
                index += 1
                for i in range(len(classes)):
                    if classes[i] == created_classes[index-1]:
                        show_class[i] = True
                    else:
                        show_class[i] = False
                

        if event.key == pygame.K_h:
            if hide_lines:
                hide_lines = False
            else:
                hide_lines = True
        if event.key == pygame.K_x:
            if show_final_points:
                show_final_points = False
            else:
                show_final_points = True
    elif(event.type == pygame.KEYUP):
        if event.key == pygame.K_UP:
            move_up = False
        if event.key == pygame.K_DOWN:
            move_down = False
        if event.key == pygame.K_RIGHT:
            move_right = False
        if event.key == pygame.K_LEFT:
            move_left = False
        if event.key == pygame.K_r:
            reset_vue = False
        if event.key == pygame.K_q: #zoom_in, zoom_out, reset_vue
            zoom_in = False
        if event.key == pygame.K_e:
            zoom_out = False
        if event.key == pygame.K_w:
            navigate_up= False
        if event.key == pygame.K_s:
            navigate_down= False
        if event.key == pygame.K_a:
            navigate_left= False
        if event.key == pygame.K_d:
            navigate_right= False
        if event.key == pygame.K_g:
            shift_angle_up = False
        if event.key == pygame.K_f:
            shift_angle_down = False
    return running, move_up, move_down, move_right, move_left, reset_vue, zoom_in, zoom_out, go_dim_up, go_dim_down, hide_lines, navigate_up , navigate_down, navigate_right, navigate_left, show_class, shift_angle_up, shift_angle_down, show_final_points, scale_input, index
def fill_shape_with_alpha(x,y,w,h, COLOR = (0,0,0,128)):
    s = pygame.Surface((w,h), pygame.SRCALPHA)   # per-pixel alpha
    s.fill(COLOR)                         # notice the alpha value in the color
    screen.blit(s, (x,y))
