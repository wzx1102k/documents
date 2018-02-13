import numpy as np
import matplotlib
import matplotlib.pyplot as plt 

def cal_loss(_pocket, _x, _label):
    _cal = np.sign(np.dot(_x, _pocket))
    _cal.shape = (40,1)
    idx = np.where(_cal[:, 0] != _label[:, 0])
    loss = np.sum(_cal[:, 0] != _label[:, 0])
    return list(idx[0]), loss

LEN = 40
x = (np.random.rand(LEN,2) - 0.5) * 10
line = np.random.rand(2,1)
label = np.sign(np.dot(x, line))
label[label == 0] = 1


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
idx_0 = np.where(label[:, 0] == -1)

# error label point
label[list(idx_0[0])[0], 0] = 1
idx_0 = np.where(label[:, 0] == -1)

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



# random init best pocket and min loss value
pocket_best = np.random.randint(-5,5, (2,1))
_, min_loss = cal_loss(pocket_best, x, label)
cnt = 0

for i in range(15):
    # random pocket and cur loss for each period
    pocket = np.random.randint(-5,5, (2,1))
    _pocket = pocket
    idx, cur_loss = cal_loss(pocket, x, label)
    while cnt < len(idx):
        _x = x[idx[cnt], :]
        _x.shape = (2,1)
        _pocket = pocket + _x * label[idx[cnt], 0]
        _, cur_loss = cal_loss(_pocket, x, label)
        # compare cur loss with min loss
        if cur_loss < min_loss:
            break
        else:
            cnt = cnt + 1
    if cnt != len(idx):
        pocket_best = _pocket
        _, min_loss = cal_loss(pocket_best, x, label)
    try:
        ax.lines.remove(lines[0])
    except Exception:
        pass

    if pocket_best[0,:] == 0:
        line_x = 0
        line_y = np.linspace(-5,5,50)
        lines = ax.plot(line_x, line_y, 'r-', lw=2)
    else:
        k = -pocket_best[1,:]/pocket_best[0,:]
        line_x = np.linspace(-5,5,50) 
        line_y = k*line_x
        lines = ax.plot(line_x, line_y, 'r-', lw=2)
    plt.pause(0.5)
    cnt = 0

plt.ioff()
plt.show()
print(pocket_best)