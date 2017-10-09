import sys
import os
from PIL import Image

def main():
  if len(sys.argv) != 3:
    print('usage: ./blending.py sourceImage targetImage')
    sys.exit(1)
  else:
    if not os.path.exists(sys.argv[1]):
      print("The sourceImage file doesn't exist")
      sys.exit(1)

    source = Image.open(sys.argv[1])
    sourceWidth, sourceHeight = source.size


    if not os.path.exists(sys.argv[2]):
      print("The targetImage file doesn't exist")
      sys.exit(1)

    target = Image.open(sys.argv[2])
    targetWidth, targetHeight = target.size


  isTargetLargest = (targetWidth > sourceWidth) and (targetHeight > sourceHeight)

  if not isTargetLargest:
    print("The target image must be longer than the source")

  #source.show()
  #target.show()

  pasting = paste(source, target)
  pasting.show()

  blend33 = blend_33(source, target)
  blend33.show()

  gradientBlend = gradient_blend(source, target, 0.33)
  gradientBlend.show()

# Image Paste Function
def paste(source, target):
  pixSource = source.load()
  targetDup = target.copy()
  pixTarget = targetDup.load()
  sourceWidth, sourceHeight = source.size
  for x in range(0,sourceWidth):
    for y in range(0, sourceHeight):
      pixTarget[x,y] = pixSource[x,y]
  return targetDup

# Image Blending 33% Source Image, 67% TargetImage
def blend_33(source, target):
  pixSource = source.load()
  targetDup = target.copy()
  pixTarget = targetDup.load()
  sourceWidth, sourceHeight = source.size
  for x in range(0,sourceWidth):
    for y in range(0, sourceHeight):
      R = int(pixSource[x,y][0] * 0.33 + pixTarget[x,y][0] * 0.67)
      G = int(pixSource[x,y][1] * 0.33 + pixTarget[x,y][1] * 0.67)
      B = int(pixSource[x,y][2] * 0.33 + pixTarget[x,y][2] * 0.67)
      pixTarget[x,y] = (R,G,B)
  return targetDup

# Image Gradient Blending from blend percentage to 0
def gradient_blend(source, target, blend):
  pixSource = source.load()
  targetDup = target.copy()
  pixTarget = targetDup.load()
  sourceWidth, sourceHeight = source.size
  for x in range(0,sourceWidth):
    gradientXdecrease = blend * (float(x) / sourceWidth)
    for y in range(0, sourceHeight):
      gradientYdecrease = blend * (float(y) / sourceHeight)
      gradientDecrease = max(gradientXdecrease, gradientYdecrease)
      srcBlend = blend - gradientDecrease
      targetBlend = 1 - srcBlend
      R = int(pixSource[x,y][0] * srcBlend + pixTarget[x,y][0] * targetBlend)
      G = int(pixSource[x,y][1] * srcBlend + pixTarget[x,y][1] * targetBlend)
      B = int(pixSource[x,y][2] * srcBlend + pixTarget[x,y][2] * targetBlend)
      pixTarget[x,y] = (R,G,B)
  return targetDup

if __name__ == '__main__':
  main()
