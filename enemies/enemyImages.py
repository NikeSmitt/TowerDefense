import os
import pygame


class EnemiesImages:

    def __init__(self):
        self._scorpion_images = None
        self._wizard_images = None
        self._club_images = None

    def get_scorpion_images(self, width=64, height=64):
        if self._scorpion_images is None:
            original = [pygame.image.load(os.path.join(
                "game_assets/enemies/1", f"1_enemies_1_run_0{x:02d}.png"
            )) for x
                   in range(20)]
            self._scorpion_images = [pygame.transform.scale(img, (height, width)) for img in original]
        return self._scorpion_images[:]

    def get_wizard_images(self, width=64, height=64):
        if self._wizard_images is None:
            original = [pygame.image.load(os.path.join(
                "game_assets/enemies/2", f"2_enemies_1_run_0{x:02d}.png"
            )) for x in range(20)]
            self._wizard_images = [pygame.transform.scale(img, (height, width)) for img in original]
        return self._wizard_images[:]

    def get_club_images(self, width=64, height=64):
        if self._club_images is None:
            original = [pygame.image.load(os.path.join(
                "game_assets/enemies/5", f"5_enemies_1_run_0{x:02d}.png"
            )) for x in range(20)]
            self._club_images = [pygame.transform.scale(img, (height, width)) for img in original]
        return self._club_images[:]


enemies_image = EnemiesImages()
