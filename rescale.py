import cv2 as cv

def rescaleFrame(frame, scale=0.75):
  # Resizeing the video, image, live cam
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)
  dimensions = (width,height)

  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
cv.waitKey(0)


def changeRes(width,height):
  # Live video
  capture.set(3,width)
  capture.set(4,height)


# Image Show
img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat', img)
resized_image = rescaleFrame(img)
cv.imshow('Image Resized', resized_image)

# Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4')
while True:
  isTrue, frame = capture.read()
  frame_resized = rescaleFrame(frame)
  cv.imshow('Video', frame)
  cv.imshow('Video Resized',frame_resized)
  if cv.waitKey(20) & 0xFF == ord('d'):
    break
capture.release()
cv.destroyAllWindows()
