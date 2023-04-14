# -*- coding: utf-8 -*-
################################################
# Virtual Proxy
# ----------------------------------------------
# By virtual, what we mean is that for all intents and purposess,
# it appears like the object that's supposed to represent, but
# behind the scenes it can offer additional functionality and behave
# differently.
################################################


class Bitmap:
  def __init__(self, filename: str) -> None:
    self.filename = filename
    print(f'Loading image from {self.filename}...')

  def draw(self):
    print(f'Drawing image {self.filename}')
    
    
def draw_image(image: Bitmap):
  print('About to draw image...')
  image.draw()
  print('Done drawing image!')
  

# We do not want to Loading image if not drawing
# Adding a proxy
class LazyBitmap:
  def __init__(self, filename: str) -> None:
    self.filename = filename
    self._bitmap = None
  
  def draw(self):
    if not self._bitmap:
      self._bitmap = Bitmap(self.filename)
    self._bitmap.draw()
  
  
if __name__ == '__main__':
  print('................................................')
  print('The objects:')
  
  bmp = Bitmap('facepalm.jpg')
  draw_image(bmp)
  draw_image(bmp)
  
  bmp = Bitmap('elsalvadormap.jpg')
  #draw_image(bmp)
  
  print('................................................')
  print('Applying the Proxy pattern:')
  
  bmp = LazyBitmap('facepalm.jpg')
  draw_image(bmp)
  draw_image(bmp)
  
  bmp = LazyBitmap('elsalvadormap.jpg')
  #draw_image(bmp)
  
  print('................................................')
  