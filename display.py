import pygame

class Display(object):
  def __init__(self, W, H):
    pygame.init()
    self.screen = pygame.display.set_mode((W, H))
    self.W = W
    self.H = H

  def paint(self, image):
    surface = pygame.surfarray.make_surface(image.swapaxes(0, 1))
    surface = pygame.transform.scale(surface, (self.W, self.H))
    self.screen.blit(surface, (0, 0))
    pygame.display.flip()

  def done(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return True
    return False

  def close(self):
    pygame.quit()


