#Joshua Cordero 
#Simple Space invadors game using the pygame library

import pygame
import math
import random
import os
pygame.init()


fileDir = os.path.dirname(os.path.realpath('__file__'))
fileName = os.path.join(fileDir, "SpaceInvadersSound/fastinvader1.wav")
music = pygame.mixer.Sound(fileName)
#pygame.mixer.music.play(-1)
shoot = pygame.mixer.Sound(os.path.join(fileDir, "SpaceInvadersSound/shoot.wav"))
shoot.set_volume(0.1)
explosion = pygame.mixer.Sound(os.path.join(fileDir, "SpaceInvadersSound/explosion.wav"))
explosion.set_volume(0.1)


class player(object):
	global playerr

	def __init__(self, x, y, width, height, vel):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = vel
		self.lives = 3
		self.beginX = x
		self.beginY = y
		self.beginWidth = width
		self.beginHeight = height
		self.beginVel = vel
		self.hitbox = (self.x - 1, self.y+5, self.width, self.height)


	def draw(self, win):
		self.move()
		self.hitbox = (self.x - 1, self.y+5, self.width, self.height)
		#print(self.hitbox)
		win.blit(playerr, (self.x, self.y))
		#pygame.draw.rect(win, (0,200,0), self.hitbox, 2)
		# Draw the amount of lives left
		pimage = pygame.image.load('player1-1.png')
		pimage = pygame.transform.scale(pimage, (21, 21))
		if self.lives >= 1:
			win.blit(pimage, (20,480))
			#pygame.draw.rect(win, (0,200,0), (20, 485, 20, 10))
		if self.lives >= 2:
			win.blit(pimage, (45,480))
			#pygame.draw.rect(win, (0,200,0), (45, 485, 20, 10))
		if self.lives >= 3:
			win.blit(pimage, (70,480))
			#pygame.draw.rect(win, (0,200,0), (70, 485, 20, 10))


	def move(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_LEFT] and self.x > 5:
			self.x -= self.vel
		elif keys[pygame.K_RIGHT] and self.x + self.width < 495:
			self.x += self.vel


	def hit(self):

		self.x = self.beginX
		self.y = self.beginY
		self.lives -= 1
		i = 0
		while i < 250:
			pygame.time.delay(10)
			i += 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					i = 301
					pygame.quit()


	def reset(self):

		font1 = pygame.font.SysFont('comicsans', 100)
		text = font1.render('You lost',1, (255,0,0))
		win.blit(text, (250 - (text.get_width()/2), 200))
		pygame.display.update()
		i = 0
		while i < 300:
			pygame.time.delay(10)
			i += 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					i = 301
					pygame.quit()

	def nextLevel(self, level):
		self.level = level
		font = pygame.font.SysFont('comicsans', 100)
		text = "Level " + str(self.level)
		text = font.render(text,1, (255,255,255))
		win.blit(text, (250 - (text.get_width()/2), 200))
		pygame.display.update()
		i = 0
		while i < 300:
			pygame.time.delay(10)
			i += 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					i = 301
					pygame.quit()
		self.x = self.beginX
		
		'''
		self.x = self.beginX
		self.y = self.beginY
		self.width = self.beginWidth
		self.height = self.beginHeight
		self.vel = self.beginVel
		self.lives = 3

		'''



class enemy(object):
	def __init__(self, x, y, width, height, vel, point, image,column = 0, color = (255, 255, 255)):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = vel
		self.color = color
		self.beginX = x
		self.end = 0
		self.point = point
		self.image = image
		self.hitbox = (self.x-1, self.y+5, self.width, self.height+8)
		self.hitbox2 = (self.x, self.y, self.width, self.height)
		self.image_count = 0
		self.image_delay = 0
		self.column = column
		self.movePoint = x
		self.moveWidth = 45
		#self.keepVel = self.vel


	def draw(self, win):
		self.move()
		self.hitbox = (self.x-1, self.y+5, self.width, self.height+8)
		win.blit(self.image[self.image_count], (self.x, self.y))
		
		if self.image_delay == 10:
			if self.image_count == 0:
				self.image_count = 1
			elif self.image_count == 1:
				self.image_count = 0
			self.image_delay = 0

		self.image_delay += 1
		#pygame.draw.rect(win, (self.color), self.hitbox, 2)

	def move(self):
		if abs(self.movePoint - self.x) < self.moveWidth:
			self.x += self.vel

		#if self.x - self.beginX < 45:
		#	self.x += self.vel
		#elif self.x - self.beginX < -45:
		#	self.x += self.vel


		else:
			self.vel = -self.vel
			self.x += self.vel
			self.end += 1
			if self.end > 2:
				self.vel *= 1.05

			self.moveDown()

	def moveDown(self):
		self.y += 15


	def draw2(self, win):
		self.move2()
		self.hitbox2 = (self.x-1, self.y+5, self.width, self.height+8)
		win.blit(self.image, (self.x, self.y))
		#pygame.draw.rect(win, (self.color), self.hitbox2, 2)
	
	def move2(self):
		self.x -= self.vel

class projectile(object):
	def __init__(self, x, y, direction, vel=2, radius = 5,color = (255, 255, 255)):
		self.x = x
		self.y = y
		self.direction = direction
		self.radius = radius
		self.color = color
		self.vel = vel


	def draw(self, win):
		self.move()
		pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

	def move(self):
		self.y = self.y + (self.vel * self.direction)


class shield(object):
	def __init__(self, x, y, width, height, color = (0,255,0)):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))


def redrawGameWindow():
	global defender, enemys, bullets, enemybullets, barricades, score, flybye, high_Score, win
	win.fill((0,0,0))

	defender.draw(win)
	for enemy in enemys:
		enemy.draw(win)
	for bullet in bullets:
		bullet.draw(win)
	for ebullet in enemybullets:
		ebullet.draw(win)
	for barricade in barricades:
		barricade.draw(win)

	if flybye != 1:
		flybye.draw2(win)

	font = pygame.font.SysFont('comicsans', 30)
	text = font.render('Score: ' + str(score), 1, (255,0,0))
	win.blit(text, (380, 480))

	text2 = font.render('HighScore: ' + str(high_Score), 1, (255,0,0))
	win.blit(text2, (200, 480))

	pygame.display.update()
'''
def setupEnemys():
	global enemys, points, enemy12, enemy22, enemy32
	points = 4
	#x = 57.5
	x = 59.5
	y = 60
	count = 0
	image_count = 0
	image = enemy12
	column = 1
	for i in range(0,32):
		enemys.append(enemy(x,y,35,20,1, points, image, column))
		x = x + 50
		count += 1
		column += 1
		if count == 8:
			y = y + 30
			x = 59.5
			points -= 1
			count = 0
			column = 1
			if image_count == 0:
				image = enemy22
			elif image_count == 1:
				image = enemy32
			if image_count < 2:
				image_count += 1
			else:
				image_count = 0
	#print(enemys[0].x)
'''

def setupEnemys():
	global enemys, points, enemy12, enemy22, enemy32
	points = 4
	x = 59.5
	y = 60
	count = 0
	image_count = 0
	image = enemy12
	column = 1
	for i in range(0,32):
		enemys.append(enemy(x,y,35,20,0.5, points, image, column))
		y += 30
		count += 1
		image_count += 1
		points -= 1
		if image_count == 0:
			image = enemy12
		elif image_count == 1:
			image = enemy22
		else:
			image = enemy32
		if count == 4:
			y = 60
			x += 50
			image_count = 0
			points = 4
			column += 1
			count = 0



def destroyBullet():
	global bullets, enemys, enemybullets, defender, barricades, score
	for bullet in bullets:
		if bullet.y < 0:
			bullets.pop(bullets.index(bullet))

		for enemy in enemys:
			if abs(enemy.hitbox[0] + (enemy.hitbox[2]//2) - bullet.x) < enemy.hitbox[2]//2  and abs(enemy.hitbox[1] + enemy.hitbox[3]//2 - bullet.y) < enemy.hitbox[3]//2:
				score += enemys[enemys.index(enemy)].point
				bullets.pop(bullets.index(bullet))
				enemys.pop(enemys.index(enemy))
				explosion.play()

	for ebullet in enemybullets:
		if ebullet.y > 500:
			enemybullets.pop(enemybullets.index(ebullet))

		if abs(defender.hitbox[0] + (defender.hitbox[2]//2) - ebullet.x) < defender.hitbox[2]//2 and abs(defender.hitbox[1] + defender.hitbox[3]//2 - ebullet.y) < defender.hitbox[3]//2:
			enemybullets.pop(enemybullets.index(ebullet))
			defender.hit()


def checkIfatEnd():
	global enemys, defender
	for enemy in enemys:
		if enemy.y > 400 - enemy.height:
			defender.lives = 0

def randomEnemyBullet():
	if len(enemys) > 0:
		r = random.randrange(len(enemys))
		x = enemys[r].hitbox[0]
		y = enemys[r].hitbox[1]
		x = x + enemys[r].hitbox[2]//2
		x = int(round(x))
		y = int(round(y))
		#print(x,y)
		enemybullets.append(projectile(x,y,1, 10))


def baricadeSetup():
	global barricades
	x = 45
	y = 410
	x2 = x
	width = 5
	height = 5
	loop = 0
	#barricades.append(shield(x,y,width,height))
	for i in range(0,4):
		for i in range(0,30):
			barricades.append(shield(x,y,width,height))
			loop += 1
			x += 5
			if loop >= 10:
				loop = 0
				x = x2
				y += 5
		x2 += 125
		x = x2
		y = 410
		loop = 0

'''
def hitbaricade():
	global bullets, barricades, enemybullets
	for bullet in bullets:
		for barricade in barricades:
			if abs(barricade.x + (barricade.width//2) - bullet.x) < barricade.width//2 + 2 and abs(barricade.y + barricade.height//2 - bullet.y) < barricade.height//2 + 2:
				bullets.pop(bullets.index(bullet)) #this one breaks
				barricades.pop(barricades.index(barricade)) #this one works

	
	for ebullet in enemybullets:
		for barricade in barricades:
			if abs(barricade.x + (barricade.width//2) - ebullet.x) < barricade.width//2 + 5 and abs(barricade.y + barricade.height - ebullet.y) < defender.height:
				enemybullets.pop(enemybullets.index(ebullet)) #this one breaks
				barricades.pop(barricades.index(barricade)) #this one works
				#print(type(barricades))
'''
def hitbaricade():
    global bullets, barricades, enemybullets
    bullets_removed = set()
    barricades_removed = set()
    for bullet in bullets:
        for barricade in barricades:
            if abs(barricade.x + (barricade.width//2) - bullet.x) < barricade.width//2 + 5 and abs(barricade.y + barricade.height//2 - bullet.y) < barricade.height//2 + 5:
                bullets_removed.add(bullet)
                barricades_removed.add(barricade)
    bullets = [bullet for bullet in bullets if bullet not in bullets_removed]
    barricades = [barricade for barricade in barricades if barricade not in barricades_removed]

    ebullets_removed = set()
    barricades_removed = set()
    for ebullet in enemybullets:
        for barricade in barricades:
            if abs(barricade.x + (barricade.width//2) - ebullet.x) < barricade.width//2 + 5 and abs(barricade.y + barricade.height - ebullet.y) < barricade.height + 5:
                ebullets_removed.add(ebullet)
                barricades_removed.add(barricade)
    enemybullets = [ebullet for ebullet in enemybullets if ebullet not in ebullets_removed]
    barricades = [barricade for barricade in barricades if barricade not in barricades_removed]


def checkchangeLevel():
   	global enemys, defender, barricades, level, bullets, enemybullets, enemyBeginVel
   	if len(enemys) <= 0:
   		level += 1
   		enemys = []
   		barricades = []
   		defender.nextLevel(level)
   		setupEnemys()
   		baricadeSetup()
   		edge_setup()
   		for enemy in enemys:
   			if level > 1:
   				enemy.vel = enemyBeginVel * level/1.9 * 1.1
   			else:
   				enemy.vel = enemyBeginVel * 1.1

   		bullets = []
   		enemybullets = []

def flyby():
	global flybye, enemy42
	x = 500
	y = 20
	pointsworth = random.randrange(100,350)
	image = enemy42[0]
	flybye = enemy(x, y, 35, 20, 4, pointsworth, image)


def checkflybyehit():
	global bullets, score, flybye
	if flybye != 1:

		for bullet in bullets:
			if flybye != 1:
				if abs(flybye.x + (flybye.width//2) - bullet.x) < flybye.width//2 + 5  and abs(flybye.y + flybye.height//2 - bullet.y) < flybye.height//2:
					bullets.pop(bullets.index(bullet))
					score += flybye.point
					flybye = 1

def highScore():
	global score, high_Score
	doc = open("spaceInvadersHighScore.txt", "a")
	doc.close()
	doc = open("spaceInvadersHighScore.txt", "r")
	high_Score = doc.read()
	try:
		high_Score = int(high_Score)
		if high_Score > score:
			pass
		elif high_Score <= score:
			high_Score = score
			doc.close()
			doc = open("spaceInvadersHighScore.txt", "w")
			doc.write(str(high_Score))
			doc.close()


	except ValueError as e:
		doc.close()
		doc = open("spaceInvadersHighScore.txt", "w")
		doc.write("0")
		doc.close()


def edge_setup():
	global enemys, edges
	edges = []
	for i in range(len(enemys)//4):
		edges.append(i+1)
	#print(edges)

def adjust_enemy_rows(center, movementSpan):
	global enemys
	for enemy in enemys:
		enemy.movePoint -= center
		enemy.moveWidth += movementSpan


def adjust_column(adjustmentAmount):
	global enemys
	for enemy in enemys:
		enemy.column += adjustmentAmount

def enemysToEdge():
	global enemys, edges
	#print(enemys[0].column, enemys[-1].column)
	#print (edges)
	if len(enemys) > 0:
		if enemys[0].column != edges[0]:
			adjust_enemy_rows(22.5, 22.5)
			#print("reee")
			edges.pop(0)
			#print(edges)
		elif enemys[-1].column != edges[-1]:
			adjust_enemy_rows(-22.5, 22.5)
			#print("yee")
			edges.pop(-1)
		




	


def initialize():
	global win, enemy12, enemy22, enemy32, enemy42, clock, playerr
	screen_width = 500
	screen_height = 500
	win = pygame.display.set_mode((screen_width, screen_height))

	clock = pygame.time.Clock()

	playerr = pygame.image.load('player1-1.png')
	playerr = pygame.transform.scale(playerr, (30 * screen_width//500, 30 * screen_height//500))

	enemy1 = [pygame.image.load('enemy1-1.png'), pygame.image.load('enemy1-2.png')]
	enemy12 = []
	for image in enemy1:
		image = pygame.transform.scale(image, (35 * screen_width//500, 35 * screen_height//500))
		enemy12.append(image)
	enemy2 = [pygame.image.load('enemy2-1.png'), pygame.image.load('enemy2-2.png')]
	enemy22 = []
	for image in enemy2:
		image = pygame.transform.scale(image, (30 * screen_width//500, 30 * screen_height//500))
		enemy22.append(image)
	enemy3 = [pygame.image.load('enemy3-1.png'), pygame.image.load('enemy3-2.png')]
	enemy32 = []
	for image in enemy3:
		image = pygame.transform.scale(image, (30 * screen_width//500, 30 * screen_height//500))
		enemy32.append(image)
	enemy4 = [pygame.image.load('enemy4-1.png')]
	enemy42 = []
	for image in enemy4:
		image = pygame.transform.scale(image, (30 * screen_width//500, 30 * screen_height//500))
		enemy42.append(image)



def main():
	try:
		global enemys, bullets, enemybullets, defender, run, barricades, level, enemyBeginVel, score, flybye, clock
		initialize()
		win = pygame.display.set_mode((500, 500))
		bulletDelay = 0
		ebulletDelay = 0
		flybyeDelay = 0
		run = True
		defender = player(250, 450, 35, 20, 5)
		enemys = []
		bullets = []
		enemybullets = []
		barricades = []
		level = 1
		score = 0
		flybye = 1
		#enemys.append(enemy(250, 250, 35, 20, 5))
		setupEnemys()
		baricadeSetup()
		edge_setup()

		enemyBeginVel = enemys[0].vel

		while run:
			clock.tick(27)
			bulletDelay += 1
			ebulletDelay += 1
			flybyeDelay += 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

			keys = pygame.key.get_pressed()

			if keys[pygame.K_SPACE] and bulletDelay > 10 and len(bullets) < 1:
				bullets.append(projectile(defender.hitbox[0] + (defender.hitbox[2]//2), 460, -1, 10))
				bulletDelay = 0
				shoot.play()

			#if keys[pygame.K_r]:
			#	bullets.append(projectile(defender.hitbox[0] + (defender.hitbox[2]//2), 460, -1, 10))
			if len(enemybullets) < 3 and ebulletDelay > 20:
				randomEnemyBullet()
				ebulletDelay = 0

			if flybyeDelay > random.randrange(200, 1000) and flybye == 1:
				flyby()
				flybyeDelay = 0

			if flybye != 1:
				if flybye.x + flybye.width < 0:
					flybye = 1


			destroyBullet()
			hitbaricade()
			checkIfatEnd()
			checkchangeLevel()
			checkflybyehit()
			highScore()
			enemysToEdge()
			#print (enemys[-1].row)

			if defender.lives <= 0:
				defender.reset()
				bulletDelay = 0
				ebulletDelay = 0
				flybyeDelay = 0
				defender = player(250, 450, 35, 20, 5)
				enemys = []
				bullets = []
				enemybullets = []
				barricades = []
				level = 0
				score = 0
				flybye = 1
				setupEnemys()
				baricadeSetup()

			redrawGameWindow()
		pygame.quit()
	except pygame.error as e:
		run = True

	#pygame.quit()
if __name__ == '__main__':
	main()