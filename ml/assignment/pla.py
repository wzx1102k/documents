import numpy as np
import matplotlib
import matplotlib.pyplot as plt 

LEN = 40
x = (np.random.rand(LEN,2) - 0.5) * 10
line = np.random.rand(2,1)
label = np.sign(np.dot(x, line))
label[label == 0] = 1


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
idx_0 = np.where(label[:, 0] == -1)

# error label point
#label[list(idx_0[0])[0], 0] = 1
#idx_0 = np.where(label[:, 0] == -1)

p0 = ax.scatter(x[idx_0,1], x[idx_0,0], marker = '+', color = 'c', label='-1', s = 50)
idx_1 = np.where(label[:, 0] == 1)
p1 = ax.scatter(x[idx_1,1], x[idx_1,0], marker = 'x', color = 'm', label='1', s = 50)
plt.title('PLA')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim((-6,6))
plt.ylim((-6,6))
plt.legend()
plt.grid(True)
#use ion to show onetime and disapear
plt.ion()
plt.show()


cnt = 0
pla = np.zeros((2,1))
_update = 0

while cnt<LEN:
    _update = np.sign(np.dot(x[cnt,:], pla)) * label[cnt, 0]
    if _update <= 0:
        _x = x[cnt, :]
        _x.shape = (1,2)
        _x = np.transpose(_x)
        pla = pla + _x*label[cnt, 0]
        cnt = 0
    else:
        cnt = cnt+1
        continue
    try:
        ax.lines.remove(lines[0])
    except Exception:
        pass
    if pla[0, :] == 0:
        line_x = 0
        line_y = np.linspace(-5,5,50)
        lines = ax.plot(line_x, line_y, 'r-', lw=2)
    else:
        k = -pla[1,:]/pla[0,:]
        line_x = np.linspace(-5,5,50) 
        line_y = k*line_x
        lines = ax.plot(line_x, line_y, 'r-', lw=2)
    plt.pause(0.5)
plt.ioff()
plt.show()
print(pla)