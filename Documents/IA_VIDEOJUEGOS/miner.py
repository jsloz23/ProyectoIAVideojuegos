# =================INIT====================
import pygame, sys, os.path
from pygame.locals import *
pygame.init()

# =================DIMENSIONES DEL TABLERO====================
mazeWidth = 22
mazeHeight = 18
u = pixelUnit = 30
windowWidth = mazeWidth * pixelUnit
windowHeight = mazeHeight * pixelUnit
whiteColor = pygame.Color(255,255,255)
blackColor = pygame.Color(0,0,0)
maze = {}
player= pygame.image.load("sprites/player.png")
posX=30
posY=30


# ================= PYGAME WINDOWS====================
windowSurfaceObj = pygame.display.set_mode((windowWidth,windowHeight))

def drawSquare(x,y,c):
	global u
	pygame.draw.rect(windowSurfaceObj, c, (x*u, y*u, u, u))


def isBorder(x,y):
	if x == 0 and (y>=0 and y < mazeHeight):
		return True
	if x == (mazeWidth-1) and (y>=0 and y < mazeHeight):
		return True
	if y == 0 and (x>=0 and x < mazeWidth):
		return True
	if y == mazeHeight-1 and (x>=0 and x < mazeWidth):
		return True
	return False

def drawMaze():
	for x in range(0, mazeWidth):
		for y in range(0, mazeHeight):
			if maze[x,y] == 1:
				drawSquare(x,y,blackColor)


def generateScene():
	for x in range(0, mazeWidth):
		for y in range(0, mazeHeight):
			maze[x,y] = 0
			if isBorder(x,y):
				maze[x,y] = 1
	windowSurfaceObj.fill(whiteColor)
	drawMaze()	
	


def drawScene():
	windowSurfaceObj.fill(whiteColor)
	drawMaze()
	pygame.draw.rect(windowSurfaceObj,whiteColor, pygame.Rect(posX,posY,60,80))
	windowSurfaceObj.blit(player,(posX,posY))
	pygame.display.update()
	

def movement(mov):
	global posX, posY
	if mov==0:
		posX+=pixelUnit
	elif mov==1:
		posY+=pixelUnit	
	elif mov==2:
		posX-=pixelUnit
	elif mov==3:
		posY-=pixelUnit

generateScene()
while True:
	pygame.draw.rect(windowSurfaceObj,whiteColor, pygame.Rect(posY,posY,60,80))
	windowSurfaceObj.blit(player,(posX,posY))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_RIGHT:
					movement(0)				
			if event.key == K_DOWN:
					movement(1)
			if event.key == K_LEFT:
				movement(2)
			if event.key == K_UP:
				movement(3)

	drawScene()