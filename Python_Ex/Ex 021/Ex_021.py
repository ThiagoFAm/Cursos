import pygame

pygame.init()
pygame.mixer.music.load("/Users/thiagoamaral/Documents/Curso_Python/Python_Ex/Ex 021/Mario.mp3")
pygame.mixer.music.play()
pygame.event.wait()