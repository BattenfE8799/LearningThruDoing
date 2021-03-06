# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:06:38 2021

@author: Engineer Man Youtube tutorial
"""

import random
import curses

#uses curses to initialize the screen
s = curses.initscr()
#sets curser to 0 so it doesn't show up on the screen
curses.curs_set(0)
#getting width and height 
sh, sw = s.getmaxyx()
#create a new window using height and width and starting at top left corner
w = curses.newwin(sh, sw, 0, 0)
#sets so it accepts keypad input
w.keypad(1)
#refreshes the screen every 100 milseconds
w.timeout(100)

#creates snakes initial positions (Left Centered)
snk_x = sw/4
snk_y = sh/2
#creates initial snake body parts
snake = [
    [snk_y, snk_x], #first snake body part
    [snk_y, snk_x-1], #1 left from head
    [snk_y, snk_x-2] #2 left from head
]

#creating food 
food = [sh/2, sw/2] # starting place for food as the center of the screen
#adds that food to the screen
w.addch(int(food[0]), int(food[1]), curses.ACS_PI) 
#tells snake where they're going initially
key = curses.KEY_RIGHT

#start an infinite loop for every movement of the snake
while True:
    next_key = w.getch() #see what the next key is
    key = key if next_key == -1 else next_key #sets the key 
  
    #check to see if user lost game
    #loses game if the y position is at the top/height of screen or if x position is either to the left or width of screen
    # or can loose if the snake is in itself
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
      curses.endwin() #kills the window
      quit() #quits
    
    #determine what the new head of the snake will be
    new_head = [snake[0][0], snake[0][1]] #start by taking old head of the snake as our starting point
    #figure out what key is being clicked 
    if key == curses.KEY_DOWN:
        new_head[0] += 1  # 1 on y axis
    if key == curses.KEY_UP:
        new_head[0] -= 1  # -1 on y axis
    if key == curses.KEY_LEFT:
        new_head[1] -= 1  # -1 on x axis
    if key == curses.KEY_RIGHT:
        new_head[1] += 1  # 1 on x axis
    
    #insert new head of the snake
    snake.insert(0, new_head)
    
    #determines if snake has run into the food
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1), #height -1
                random.randint(1, sw-1)  #width -1
            ]
            food = nf if nf not in snake else None # if no food has been eaten, the loop goes again
        #adds food, pi
        w.addch(food[0], food[1], curses.ACS_PI) 
    else:
        tail = snake.pop() #pops the tail off the snake...
        #add a space where the tail piece was
        w.addch(int(tail[0]), int(tail[1]), ' ')
      
    #adding head of the snake to the screen
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

  
  
  





