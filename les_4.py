import matplotlib.pyplot as plt 
import numpy as np
def circle_plotter(a=1,b=2):
  x = np.arange(0.1,10,0.1)
  
  x, y = np.meshgrid(x, y)
  fxy=((a**2)((x**2)*(b**2)))/(a**2)
  plt.contour(x, y, fxy, levels=[radius**2])
  plt.axis('equal')
  plt.show()

circle_plotter()