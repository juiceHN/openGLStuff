import pygame
import numpy
import OpenGL.GL as gl
import OpenGL.GL.shaders as shaders

WHITE = (255, 255, 255)
pygame.init()
window = pygame.display.set_mode((800, 800), pygame.OPENGL)
done = False
x, y = 50, 50

vertex_Shader = '''
#version 330
in vec4 position;

void main(){
    gl_Position = position;
}
'''

fragment_Shader = '''
#version 330
void main(){
    gl_FragColor = vec4(0.0f, 1.0f, 0.0f, 1.0f);
}
'''

shader = shaders.compileProgram(
    shaders.compileShader(vertex_Shader, gl.GL_VERTEX_SHADER),
    shaders.compileShader(fragment_Shader, gl.GL_FRAGMENT_SHADER))

vertex_data = numpy.array(
    [0.0, 0.5, 0.0, 0.5, -0.5, 0.0, -0.5, -0.5, 0.0], dtype=numpy.float32)

vertex_Buffer_Object = gl.glGenBuffers(1)
gl.glBindBuffer(gl.GL_ARRAY_BUFFER, vertex_Buffer_Object)
gl.glBufferData(gl.GL_ARRAY_BUFFER, 9 * 4, vertex_data, gl.GL_STATIC_DRAW)

vertex_array_object = gl.glGenVertexArrays(1)
gl.glBindVertexArray(vertex_array_object)

# shaders
position = gl.glGetAttribLocation(shader, 'position')
gl.glEnableVertexAttribArray(position)
# 3 = take vertex in 3 numbers
gl.glVertexAttribPointer(position, 3, gl.GL_FLOAT, False, 0, None)


while not done:

    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glDrawArrays(gl.GL_TRIANGLES, 0, 3)
    gl.glUseProgram(shader)
    # pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            x += 10
        if pressed[pygame.K_LEFT]:
            x = x - 10
        if pressed[pygame.K_DOWN]:
            y = y + 10
        if pressed[pygame.K_UP]:
            y = y - 10
