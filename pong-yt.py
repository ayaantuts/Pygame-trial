import pygame
import random

# initialize pygame
pygame.init()

# initials
WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong game but better")
run = True
direction = [0, 1]
angle = [0, 1, 2]

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# ball
radius = 15
ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
speed = .75
ball_vel_x, ball_vel_y = speed, speed

# paddle
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT / 2 - paddle_height / 2
left_paddle_x, right_paddle_x = 100 - \
	paddle_width / 2, WIDTH - (100 - paddle_width / 2)
left_paddle_vel = right_paddle_vel = 0

# main loop
while run:
	wn.fill(BLACK)
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			run = False
		elif i.type == pygame.KEYDOWN:
			if i.key == pygame.K_UP:
				left_paddle_vel -= .9
			if i.key == pygame.K_DOWN:
				left_paddle_vel += .9

		elif i.type == pygame.KEYUP:
			right_paddle_vel = left_paddle_vel = 0

	# ball movement
	ball_x += ball_vel_x
	ball_y += ball_vel_y

	# ball's movement controls
	if ball_y >= HEIGHT - radius or ball_y <= 0 + radius:
		ball_vel_y *= -1

	if ball_x >= WIDTH - radius:
		ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
		dir = random.choice(direction)
		ang = random.choice(angle)
		if dir == 0:
			if ang == 0:
				ball_vel_y, ball_vel_x = -2 * speed, speed
			elif ang == 1:
				ball_vel_y, ball_vel_x = -speed, speed
			else:
				ball_vel_y, ball_vel_x = -speed, 2 * speed

		if dir == 1:
			if ang == 0:
				ball_vel_y, ball_vel_x = 2 * speed, speed
			elif ang == 1:
				ball_vel_y, ball_vel_x = speed, speed
			else:
				ball_vel_y, ball_vel_x = speed, 2 * speed
		ball_vel_x *= -1

	if ball_x <= 0 + radius:
		ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
		if dir == 0:
			if ang == 0:
				ball_vel_y, ball_vel_x = -2 * speed, speed
			elif ang == 1:
				ball_vel_y, ball_vel_x = -speed, speed
			else:
				ball_vel_y, ball_vel_x = -speed, 2 * speed

		if dir == 1:
			if ang == 0:
				ball_vel_y, ball_vel_x = 2 * speed, speed
			elif ang == 1:
				ball_vel_y, ball_vel_x = speed, speed
			else:
				ball_vel_y, ball_vel_x = speed, 2 * speed

	# paddle movement
	left_paddle_y += left_paddle_vel

	# move left paddle based on ball position
	if ball_x < WIDTH / 4 and ball_vel_x < 0:
		left_paddle_center = left_paddle_y + paddle_height / 2
		if ball_y < left_paddle_center:
			left_paddle_vel = -abs(left_paddle_center - ball_y) / 30
		elif ball_y > left_paddle_center:
			left_paddle_vel = abs(left_paddle_center - ball_y) / 30
		else:
			left_paddle_vel = 0

		left_paddle_y += left_paddle_vel

	# move right paddle based on ball position
	if ball_x > 3 * WIDTH / 4 and ball_vel_x > 0:
		right_paddle_center = right_paddle_y + paddle_height / 2
		if ball_y < right_paddle_center:
			right_paddle_vel = -abs(right_paddle_center - ball_y) / 30
		elif ball_y > right_paddle_center:
			right_paddle_vel = abs(right_paddle_center - ball_y) / 30
		else:
			right_paddle_vel = 0

		right_paddle_y += right_paddle_vel

	# paddle's movement controls
	if left_paddle_y <= 0:
		left_paddle_y = 0
	elif left_paddle_y >= HEIGHT - paddle_height:
		left_paddle_y = HEIGHT - paddle_height

	if right_paddle_y <= 0:
		right_paddle_y = 0
	elif right_paddle_y >= HEIGHT - paddle_height:
		right_paddle_y = HEIGHT - paddle_height

	# if ball_x >= WIDTH - radius or ball_x <= 0 + radius:
	#     ball_vel_x *= -1

	# collision
	if left_paddle_x <= ball_x <= left_paddle_x + paddle_width and left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
		ball_x = left_paddle_x + paddle_width
		ball_vel_x *= -1
	elif right_paddle_x <= ball_x <= right_paddle_x + paddle_width and right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
		ball_x = right_paddle_x
		ball_vel_x *= -1

	# Objects
	pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)
	pygame.draw.rect(wn, RED, pygame.Rect(
		left_paddle_x, left_paddle_y, paddle_width, paddle_height))
	pygame.draw.rect(wn, RED, pygame.Rect(
		right_paddle_x, right_paddle_y, paddle_width, paddle_height))

	pygame.display.update()
