import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import svm

x = np.array([[1,2],
             [5,8],
             [1.5,1.8],
             [8,8],
             [1,0.6],
             [9,11],
             [6,4],
             [5,4]])

y = [0,1,0,1,0,1,1,0]

plt.scatter(x[:, 0], x[:, 1])
plt.title('SVM Linear')
plt.ion()
plt.show()
plt.pause(1)

clf = svm.SVC(kernel='linear', C = 0.01)
clf.fit(x,y)

w = clf.coef_[0]
print(w)

a = -w[0] / w[1]

xx = np.linspace(0,12)
yy = a * xx - clf.intercept_[0] / w[1]

h0 = plt.plot(xx, yy, 'k-', label="non weighted div")

plt.scatter(x[:, 0], x[:, 1], c = y)
plt.legend()

plt.ioff()
plt.show()