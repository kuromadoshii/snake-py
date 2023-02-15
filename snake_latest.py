import pygame as pg
from random import randint

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
CINZA = (128, 128, 128)
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)

def main():

	def morte():
		r = 0
		ani = True
		screen.fill(PRETO)
		pg.mixer.music.stop()
		som_morte.play()
		
		while ani:
			screen.blit(pg.transform.scale(im, (rh, rv)), (0, 0))
			screen.blit(im3, rect)
			clock.tick(25)
			pg.display.flip()
			
			for ev in pg.event.get():
				if ev.type == pg.QUIT:
					ani = False
					
			tecla = pg.key.get_pressed()

			if tecla[pg.K_ESCAPE]:
				ani = False

			if tecla[pg.K_RETURN]:
				ani = False
				r = 1

			screen.blit(pg.transform.scale(im2, (rh, rv)), (0, 0))
			screen.blit(im3, rect)
			clock.tick(25)
			pg.display.flip()
			
		return r
	
	# colisão com o alimento
	def colisao(snake1, ali1, aum1):
		if snake1[0][0] >= ali1[1] - 10 and snake1[0][0] <= ali1[1] + 10 and \
		snake1[0][1] >= ali1[2] - 10 and snake1[0][1] <= ali1[2] + 10:
			if ali1[0] == 0:
				aum1 += 10
				t = 0
	
			elif ali1[0] == 1:
				aum1 += 20
				t = 1

			else:
				aum1 += 30
				t = 2

			a1 = (t, randint(32, rh - 32), randint(32, rv - 32)) #
			#som_alim.play()

			return a1, aum1

		else:
			return False

	def des_alim(alimento):
			sombra = alimento[1] + 3, alimento[2] + 4
			

			pg.draw.circle(screen, PRETO, sombra, 8)
			if alimento[0] == 0:
				pg.draw.circle(screen, AMARELO, (alimento[1], alimento[2]), 8)
			if alimento[0] == 1:
				pg.draw.circle(screen, VERDE, (alimento[1], alimento[2]), 8)
			if alimento[0] == 2:
				pg.draw.circle(screen, VERMELHO, (alimento[1], alimento[2]), 8)

	pg.init()
	clock = pg.time.Clock()
	
	#pg.display.set_caption("Snake") titulo da janela(somente no modo janela)
	pg.mouse.set_visible(False)
	im = pg.image.load("img/jeff_im1.png")
	im2 = pg.image.load("img/jeff_im2.png")
	im3 = pg.image.load("img/you_dead.png")

	
	#informações tela
	scrinfo = pg.display.Info()
	rh, rv = scrinfo.current_w, scrinfo.current_h
	screen = pg.display.set_mode((rh, rv), flags=pg.FULLSCREEN)

	#rect da imagem de morte (you are dead) / coordenadas
	rect = im3.get_rect()
	rect.bottomleft = (screen.get_rect().bottomleft)

	#efeitos sonoros
	volume = 0.3
	som_morte = pg.mixer.Sound("sound/jeff_aud.mp3")
	som_morte.set_volume(0.1)
	#som_alim = pg.mixer.Sound("mario_coin.mp3")
	#som_alim.set_volume(0.2)
	pg.mixer.music.load("sound/ambuplay.mp3")
	pg.mixer.music.set_volume(volume)
	pg.mixer.music.play(loops=-1)

	sx, sy = 0, 0  # sentido horizontal e vertical
	snake = [[rh / 2, rv / 2]]  # corpo da snake
	tam = 1  # tamanho da snake
	aum = 0  # aumento de partes da snake    
	ali = (0, randint(32, rh - 32), randint(32, rv - 32)) # 0 = maça, 1 = pera, 2 = veneno
	ali2 = (1, randint(32, rh - 32), randint(32, rv - 32))	
	ali3 = (2, randint(32, rh - 32), randint(32, rv - 32)) #alimento posição
	nova_tecla = pg.key.get_pressed()
	loop = True #loop do principal
	rst = 0

	while loop:
		screen.fill(PRETO)
		for ev in pg.event.get():
			if ev.type == pg.QUIT:
				loop = False
				
		# captura das teclas
		tecla = pg.key.get_pressed()
		if tecla[pg.K_ESCAPE]:  # sair do jogo
			loop = False
		
		if tecla[pg.K_m] and not nova_tecla[pg.K_m]:
			if volume > 0:
				volume = 0
			else:
				volume = 0.1
			
			pg.mixer.music.set_volume(volume)

		# controle da direção da snake
		if tecla[pg.K_LEFT]:
			sx, sy = -1, 0
		if tecla[pg.K_RIGHT]:
			sx, sy = 1, 0
		if tecla[pg.K_UP]:
			sx, sy = 0, -1
		if tecla[pg.K_DOWN]:
			sx, sy = 0, 1
		

		if aum > 0:
			aum -= 1
			tam += 1
			snake.append(0)
			
		# movimentar snake
		for i in range(tam - 1, 0, -1):
			snake[i] = snake[i - 1].copy()
		snake[0][0] += sx * 4  # movimento horizontal (x)
		snake[0][1] += sy * 4  # movimento vertical (y)


		# desenhar bordas
		pg.draw.rect(screen, PRETO, (20, 20, rh - 20, 5))
		pg.draw.rect(screen, PRETO, (rh - 16, rv / 2 - 24, 20, 5))
		pg.draw.rect(screen, AZUL, (0, 0, rh, 20))
		pg.draw.rect(screen, AZUL, (0, rv - 20, rh, 20))
		pg.draw.rect(screen, PRETO, (3, 20, 23, rv / 2 - 38))
		pg.draw.rect(screen, PRETO, (3, rv / 2 + 31, 23, rv / 2 - 50))
		pg.draw.rect(screen, AZUL, (0, 0, 20, rv / 2 - 24))
		pg.draw.rect(screen, AZUL, (0, rv / 2 + 24, 20, rv))
		pg.draw.rect(screen, AZUL, (rh - 20, 0, 20, rv / 2 - 24))
		pg.draw.rect(screen, AZUL, (rh - 20, rv / 2 + 24, 20, rv))

		# desenhar alimento

		# desenhar snake
		for i in range(tam):
			sombra = (snake[i][0] + 3, snake[i][1] + 4)
			pg.draw.circle(screen, PRETO, sombra, 12)
		for i in range(tam):
			pg.draw.circle(screen, AMARELO, snake[i], 12)
		if sx == 0 and sy == 0:  # parado
			pg.draw.circle(screen, PRETO, (snake[0][0] - 5, snake[0][1] - 3), 5)
			pg.draw.circle(screen, PRETO, (snake[0][0] + 5, snake[0][1] - 3), 5)
		elif sy == 0:  # movimento horizontal
			pg.draw.circle(screen, PRETO, (snake[0][0] + sx * 3, snake[0][1] - 2), 5)
		else:  # movimento vertical
			pg.draw.circle(screen, PRETO, (snake[0][0] - 5, snake[0][1] + sy * 3), 5)
			pg.draw.circle(screen, PRETO, (snake[0][0] + 5, snake[0][1] + sy * 3), 5)

		# passagens laterais
		if snake[0][1] > rv / 2 - 18 and snake[0][1] < rv / 2 + 18:
			if snake[0][0] > rh + 22:
				snake[0][0] = -22
			elif snake[0][0] < -22:
				snake[0][0] = rh + 22
		else:
			if snake[0][0] < 32 or snake[0][0] > rh - 32 or \
				snake[0][1] < 32 or snake[0][1] > rv -32: #Colisao com a borda esquerda
				c = morte()
				if c == 1:
					rst = 1
				else:
					loop = False
		
		nova_tecla = pg.key.get_pressed()

		#chamando funçoes

		des_alim(ali)
		des_alim(ali2)
		des_alim(ali3)
    

		c1 = colisao(snake, ali, aum)
		c2 = colisao(snake, ali2, aum)
		c3 = colisao(snake, ali3, aum)


		#1
		if c1 != False and c1 != -1:
			ali, aum = c1

		if c1 == -1 and len(snake) > 1:
			snake.pop()

		#2
		if c2 != False and c2 != -1:
			ali2, aum = c2

		if c2 == -1 and len(snake) > 1:
			snake.pop()
			
		#3
		if c3 != False and c3 != -1:
			ali3, aum = c3

		if c3 == -1 and len(snake) > 1:
			snake.pop()

		if rst == 1:
			sx, sy = 0, 0  # sentido horizontal e vertical
			snake = [[rh / 2, rv / 2]]  # corpo da snake
			tam = 1  # tamanho da snake
			aum = 0  # aumento de partes da snake    
			ali = (0, randint(32, rh - 32), randint(32, rv - 32)) # 0 = maça, 1 = pera, 2 = veneno
			ali2 = (1, randint(32, rh - 32), randint(32, rv - 32))	
			ali3 = (2, randint(32, rh - 32), randint(32, rv - 32)) #alimento posição
			nova_tecla = pg.key.get_pressed()
			rst = 0
			
		pg.display.flip()
		clock.tick(60)
	

	pg.quit()

main()
