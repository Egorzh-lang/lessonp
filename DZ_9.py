from re import X
import numpy as np
import matplotlib.pyplot as plt

a=1
b=1

x = np.linspace(-2, 0, 2000)



plt.figure(figsize=(8, 6))




def f(x):
    return ((x**b)-(a**b))/x**b

plt.plot(x, f(x), color="black")

#plt.scatter(x, f(np.abs(x)), color="darkmagenta", s=1)

plt.xlabel("Frequency (cm$^{-1}$)")
plt.ylabel("f(x)")
plt.title("График функции с точкой разрыва второго рода")
plt.legend()
plt.grid(True)
plt.ylim(-10, 10)  

left, bottom, width, height = [0.55, 0.55, 0.35, 0.35]
ax2 = plt.gca().add_axes([left, bottom, width, height])
x_inset = np.linspace(-10, 0, 500)
ax2.plot(x_inset, f(x_inset, a, b), color='blue')
ax2.plot(x_inset, g(x_inset, a, b), color='red')
ax2.axhline(y=0, color='black', linestyle='--', linewidth=0.8)
ax2.set_xlim(-10,0)



plt.show()

##############################################################################

import numpy as np
import matplotlib.pyplot as plt

a=1
b=-1

x=np.linspace(-10, 0, 3500)

def f(x):
    return  ((x**b)-(a**b))/x**b

plt.figure(figsize=(5, 6))

plt.subplot(211)
plt.plot(x, f(x), color="red")
plt.grid(True)
plt.ylim(-10, 10) 

a=0.7
b=-0.8

plt.figure(figsize=(5, 6))
plt.subplot(212)
plt.plot(x, f(x), color="blue")



plt.legend()
plt.grid(True)
plt.ylim(-10, 10) 
plt.show()
