import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs

DIMENSION = 2
KNUM = 4
SAMPLE_CNT = 240
SAMPLE_CNT_2 = SAMPLE_CNT//2
SAMPLE_CNT_4 = SAMPLE_CNT//4
SAMPLE_CNT_4_3 = SAMPLE_CNT_2 + SAMPLE_CNT_4
train_step = 100


def label_reset(x, kpoint):
    _label = np.zeros((x.shape[0], 1))
    for i in range(0, x.shape[0]):
        _ = np.linalg.norm(x[i,:] - kpoint, axis=1)
        _label[i] = np.argmin(_, 0)
 
    return _label
    

def kpoint_reset(x, label):
    _kpoint = np.zeros((KNUM, DIMENSION))
    idx = 0
    for i in range(0, KNUM):
        idx = np.where(label[:, 0] == i)
        _kpoint[i] = np.mean(x[idx], axis=0)
    return _kpoint

def cal_total(x, kpoint, label):
    _sum = 0
    for i in range(0, KNUM):
        idx = np.where(label[:, 0] == i)
        _linalg = np.linalg.norm(x[idx] - kpoint[i], axis=1)
        _sum += np.sum(_linalg)
    _sum /= SAMPLE_CNT
    return _sum

'''
# x, y, label
x = np.zeros((SAMPLE_CNT, DIMENSION))
x = np.random.randint(-20, 20, (SAMPLE_CNT, DIMENSION))
'''
x, _ = make_blobs(n_samples=SAMPLE_CNT, n_features=DIMENSION, centers=KNUM, center_box=(-20, 20), cluster_std=1.5)

label = np.zeros((SAMPLE_CNT, 1))

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
p0 = ax.scatter(x[:,1], x[:,0], marker = 'o', color = 'k', label='1', s = 50)
plt.title('KMEANS')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim((-25, 25))
plt.ylim((-25, 25))
plt.grid(True)
#use ion to show onetime and disapear
plt.ion()
plt.show()


#kmeans init
kpoint = np.random.randint(-20, 20, (KNUM, DIMENSION))
kpoint_min = kpoint.copy()

label = label_reset(x, kpoint)
label_min = label.copy()

sum = cal_total(x, kpoint, label)
sum_min = sum
delta = sum

for i in range(train_step):
    kpoint = np.random.randint(-20, 20, (KNUM, DIMENSION))
    label = label_reset(x, kpoint)
    sum = cal_total(x, kpoint, label)
    delta = sum
    while delta > 0.001:
        kpoint = kpoint_reset(x, label)
        label = label_reset(x, kpoint)
        _sum = cal_total(x, kpoint, label)
        delta = sum - _sum
        sum = _sum
        print("sum: %f" %sum)
        try:
            p0.remove()
            p1.remove()
            p2.remove()
            p3.remove()
        except Exception:
            pass
        idx_0 = np.where(label[:, 0] == 0)
        p0 = ax.scatter(x[idx_0,1], x[idx_0,0], marker = '+', color = 'c', label='1', s = 50)
        idx_1 = np.where(label[:, 0] == 1)
        p1 = ax.scatter(x[idx_1,1], x[idx_1,0], marker = 'x', color = 'm', label='2', s = 50)
        idx_2 = np.where(label[:, 0] == 2)
        p2 = ax.scatter(x[idx_2,1], x[idx_2,0], marker = '*', color = 'b', label='3', s = 50)
        idx_3 = np.where(label[:, 0] == 3)
        p3 = ax.scatter(x[idx_3,1], x[idx_3,0], marker = 'o', color = 'g', label='4', s = 50)
        plt.pause(0.1)
    if sum < sum_min:
        print("Update sum_min: %f" %sum)
        sum_min = sum
        kpoint_min = kpoint.copy()
        label_min = label.copy()
try:
    p0.remove()
    p1.remove()
    p2.remove()
    p3.remove()
except Exception:
    pass
idx_0 = np.where(label_min[:, 0] == 0)
p0 = ax.scatter(x[idx_0,1], x[idx_0,0], marker = '+', color = 'c', label='1', s = 50)
idx_1 = np.where(label_min[:, 0] == 1)
p1 = ax.scatter(x[idx_1,1], x[idx_1,0], marker = 'x', color = 'm', label='2', s = 50)
idx_2 = np.where(label_min[:, 0] == 2)
p2 = ax.scatter(x[idx_2,1], x[idx_2,0], marker = '*', color = 'b', label='3', s = 50)
idx_3 = np.where(label_min[:, 0] == 3)
p3 = ax.scatter(x[idx_3,1], x[idx_3,0], marker = 'o', color = 'g', label='4', s = 50)
plt.ioff()
plt.show()
print(sum)
