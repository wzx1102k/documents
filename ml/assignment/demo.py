import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs

# 测试数据生成
x_data = np.linspace(-20, 20, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)

y_1 = np.square(x_data)
y_2 = 10 * x_data + 3
y_3 = 20 * np.sin(x_data)
y_4 = y_1 + y_2 + y_3
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.xlabel('x')
plt.ylabel('y')
plt.xlim((-25, 25))
plt.ylim((-200, 200))
lines = ax.plot(x_data, y_1, 'r-', lw=2)
lines = ax.plot(x_data, y_2, 'b-', lw=2)
lines = ax.plot(x_data, y_3, 'g-', lw=2)
lines = ax.plot(x_data, y_4, 'y-', lw=2)
plt.show()
