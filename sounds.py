import pygame
import os

class SoundHandler():

	effects = dict()

	@classmethod
	def initialize_effects(self):
		self.effects['fire'] = pygame.mixer.Sound('sound' + os.sep + 'ak47sound_mixdown_1.wav')
		self.effects['explosion1'] = pygame.mixer.Sound('sound' + os.sep + 'explosionsound_mixdown_1.wav')
	
	@classmethod
	def playBGM(self):
		pygame.mixer.music.load('sound/bgm.mp3')
		pygame.mixer.music.play(-1)
