import pygame
import os

class SoundHandler():
	# Location of this py file
	loc = os.path.dirname(os.path.abspath(__file__))
	effects = dict()

	@classmethod
	def initialize_effects(self):
		self.effects['fire'] = pygame.mixer.Sound(os.path.join(self.loc, 'sound', 'ak47sound_mixdown_1.wav'))
		self.effects['explosion1'] = pygame.mixer.Sound(os.path.join(self.loc, 'sound', 'explosionsound_mixdown_1.wav'))
	
	@classmethod
	def playBGM(self):
		pygame.mixer.music.load('sound/bgm.mp3')
		pygame.mixer.music.play(-1)
