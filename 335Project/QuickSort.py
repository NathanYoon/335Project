# Quick Sort by Elnathan Yoon
import pygame, sys, random

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# screen dimensions
WIDTH = 400
HEIGHT = 500
window_size = (WIDTH, HEIGHT)

# intializing pygame
pygame.init()

# initializing screen
window = pygame.display.set_mode(window_size)

# title 
pygame.display.set_caption('Quick Sort Visualization')

clock = pygame.time.Clock()
width_of_bars = 1
range_of_bars = int(WIDTH/width_of_bars)

# initializing lists with random integers
list_of_ints = list(range(1,400)) # list of integers from 1 to 400
random.shuffle(list_of_ints) # shuffling integers
# intializing lists for keeping track of state of integers
state = []
for i in range(range_of_bars):
    state.append(1)


# This function takes last element as pivot, places the pivot element at its correct position in the sorted array
# and places all smaller elements (smaller than pivot) to left of pivot and all greater elements to right of pivot
def partition(arr, low, high):
    for i in range(low, high):
        state[i] = 0
    i = low        
    pivot = arr[high] 
    state[low] = 0

    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            state[i] += 1
            i+= 1
            state[i] = 0

    arr[i], arr[high] = arr[high], arr[i]
    return i

high = len(list_of_ints) - 1
low = 0
size = high - low + 1
stack = [0] * (size)

top = 0
stack[top] = 0
top += 1
stack[top] = high

j = 0

# Game Loop
while True:
    window.fill((10, 10, 10))

    # Quick Sort Implementation 
    if top >= 0:
        high = stack[top]
        top -= 1
        low = stack[top]
        top -= 1

        p = partition(list_of_ints, low, high)

        state[p] = 1
        if p-1 > low:
            top += 1
            stack[top] = low
            top += 1
            stack[top] = p - 1

        if p+1 < high:
            top += 1
            stack[top] = p+1
            top += 1
            stack[top] = high

    else:
        if j < len(list_of_ints):
            state[j] = 2
            j+=1

    # Changing color of sorted ints in display
    for i in range(len(list_of_ints)):
        if state[i] == 0:
            color = RED
        elif state[i] == 2:
            color = GREEN
        else:
            color = WHITE
        pygame.draw.rect(window, color, pygame.Rect(int(i*width_of_bars), (HEIGHT - list_of_ints[i]), width_of_bars, list_of_ints[i]))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(40) # runs program at 40 frames per second
    pygame.display.flip() # updates the entire display