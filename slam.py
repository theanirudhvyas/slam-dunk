#!/usr/bin/env python3
import cv2
from display import Display

W = 1920//2
H = 1080//2

display = Display(W, H)


def process_frame(img):
  img = cv2.resize(img, (W,H))
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  display.paint(img)
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

    display.done()
  display.close()
  cv2.destroyAllWindows()
