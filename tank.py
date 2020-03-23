import os
import cfg
import pygame
from modules import *


def main(cfg):

	pygame.init()
	pygame.mixer.init()
	screen = pygame.display.set_mode((cfg.WIDTH, cfg.HEIGHT))
	pygame.display.set_caption(cfg.TITLE)

	sounds = {}
	for key, value in cfg.AUDIO_PATHS.items():
		sounds[key] = pygame.mixer.Sound(value)
		sounds[key].set_volume(1)

	is_dual_mode = gameStartInterface(screen, cfg)

	levelfilepaths = [os.path.join(cfg.LEVELFILEDIR, filename) for filename in sorted(os.listdir(cfg.LEVELFILEDIR))]

	for idx, levelfilepath in enumerate(levelfilepaths):
		switchLevelIterface(screen, cfg, idx+1)
		game_level = GameLevel(idx+1, levelfilepath, sounds, is_dual_mode, cfg)
		is_win = game_level.start(screen)
		if not is_win: break
	is_quit_game = gameEndIterface(screen, cfg, is_win)
	return is_quit_game


if __name__ == '__main__':
	while True:
		is_quit_game = main(cfg)
		if is_quit_game:
			break