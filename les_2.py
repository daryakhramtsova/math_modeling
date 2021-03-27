import matplotlib.pyplot as plt 
import numpy as np
plt.plot([1,1,5,5,1],[1,5,5,1,1],marker="o")

plt.xlabel("coord: x")
plt.ylabel("coord: y")  
plt.legend()
plt.title("base")
plt.grid()
plt.axis('equal')  
plt.show()
porabola_plotter()