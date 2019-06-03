import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

fig,ax = plt.subplots()

x = np.arange(0,2*np.pi,0.01)
line, = ax.plot(x,np.sin(x))

# animation function传入的值是当前frame的number
def animate(i):
    # 更新ydata的值
    line.set_ydata(np.sin(x+i/100))
    return line,

def init_animate():
    line.set_ydata(np.sin(x))
    return line,



# func:每一帧更新的函数
# frames:100个update
# init_func：最开始的一帧
# interval:多少毫秒更新一次
# blit：是否局部更新（局部更高效，但mac只能选false）
ani = animation.FuncAnimation(fig=fig,func=animate,frames=100,init_func=init_animate,interval=20,blit=False)

# plt.plot()
plt.show()