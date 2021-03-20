import matplotlib.pyplot as plt 
import numpy as np 
def porabola_plotter(a=1,b=1,c=0,title="porabola plotter"):
  x= np.arange(-10,10,0.01)
  y= a*x**2 + b*x +c
  plt.plot(x,y,label="my")
  plt.xlabel("coord: x")
  plt.ylabel("coord: y")
  plt.legend()
  plt.title("base")
  plt.grid()
  plt.show()

porabola_plotter()