import glfw
import numpy as np
 
from OpenGL.GL import *
from math import sin, cos


if not glfw.init():
    raise Exception("glfw can not be initialized!")


window = glfw.create_window(1280, 720,
                            'My OpenGL Window',
                            None,
                            None)


if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")


glfw.set_window_pos(window, 400, 200)
glfw.make_context_current(window)


# vertex of triangle - X, Y, Z 
vertices = [-0.5, -0.5, 0.0,
             0.5, -0.5, 0.0,
             0.0,  0.5, 0.0]


# color of triangle - RGB, (1 - red, 2 - gren, 3 - blue)
colors = [1.0, 0.0, 0.0,
          0.0, 1.0, 0.0,
          0.0, 0.0, 1.0]


# matrix of vertices cast to array a float32
vertices = np.array(vertices, dtype=np.float32)

# matrix of color cast to array a float32
colors = np.array(colors, dtype=np.float32)


glEnableClientState(GL_VERTEX_ARRAY)
glVertexPointer(3, GL_FLOAT, 0, vertices) # size, type, stride, pointers*

glEnableClientState(GL_COLOR_ARRAY)
glColorPointer(3, GL_FLOAT, 0, colors) # size, type, stride, pointers*

glClearColor(0, 0.1, 0.1, 1)


while not glfw.window_should_close(window):
    glfw.poll_events()
    
    glClear(GL_COLOR_BUFFER_BIT)
    glDrawArrays(GL_TRIANGLES, 0, 3) # we drawing triangle in current window

    glfw.swap_buffers(window)


glfw.terminate()
