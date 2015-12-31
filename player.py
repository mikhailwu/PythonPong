import pygame

class player:	
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
	def drawToScreen(screen, color):
		pygame.draw.rect(screen, color, pygame.Rect(self.x, self.y, self.width, self.height))
	def reflectBall(ball):
		
	
