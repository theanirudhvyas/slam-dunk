#!/usr/bin/env python3
import cv2
import pygame

W = 1920//2
H = 1080//2

pygame.init()
screen = pygame.display.set_mode((W, H))

def display_image(image):
  surface = pygame.surfarray.make_surface(image.swapaxes(0, 1))
  surface = pygame.transform.scale(surface, (W, H))
  screen.blit(surface, (0, 0))
  pygame.display.flip()

def process_frame(img):
  img = cv2.resize(img, (W,H))
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  display_image(img)
  print(img.shape)

if __name__ == "__main__":
  capture = cv2.VideoCapture("travel.mp4")

  while capture.isOpened():
    ret, frame = capture.read()
    if ret:
      process_frame(frame)
      if cv2.waitKey(20) == ord("q"):
        break
    else:
      break

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        break
  pygame.quit()
  cv2.destroyAllWindows()
