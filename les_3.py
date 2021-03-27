import matplotlib.pyplot as plt 
import numpy as np
def porabola_plotter(a=1,title="porabola plotter"):
  x= np.arange(0.1,10,0.01)
  y= a/x
  plt.plot(x,y,label="my")
  plt.xlabel("coord: x")
  plt.ylabel("coord: y")
  plt.show()

porabola_plotter()