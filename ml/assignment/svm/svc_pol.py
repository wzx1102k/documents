import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import style
style.use("ggplot")
from sklearn import svm
from sklearn.datasets.samples_generator import make_blobs

## 测试数据生成
_x = np.random.randint(-10, 10, (400, 2))
_ = np.linalg.norm(_x, axis=1)
circle_in = _x[_<5]
circle_out = _x[_>8]
x = np.vstack((circle_in, circle_out))
y = np.zeros(x.shape[0])
y[0:circle_in.shape[0]] = 1

## 初始化plot
plt.xlabel('x')
plt.ylabel('y')
plt.xlim((-15, 15))
plt.ylim((-15, 15))
plt.scatter(x[:, 0], x[:, 1])
plt.title('SVM Classifier Pol-RBF')
plt.ion()
plt.show()
plt.pause(1)

## 运行SVC核
svc_rbf = svm.SVC(kernel='rbf', C=1e3, gamma=0.1)
svc_poly = svm.SVC(kernel='poly', C=1e3, degree=2)
#svc_sig = svm.SVC(kernel='sigmoid', C=1e3, gamma=0.1)
svc_rbf.fit(x, y)
#svc_sig.fit(x, y)
svc_poly.fit(x, y)

## 画SVM区域等高线
def plot_svc_decision_function(clf, ax=None, color='k'):
    """Plot the decision function for a 2D SVC"""
    if ax is None:
        ax = plt.gca()
    x = np.linspace(plt.xlim()[0], plt.xlim()[1], 30)
    y = np.linspace(plt.ylim()[0], plt.ylim()[1], 30)
    Y, X = np.meshgrid(y, x)
    P = np.zeros_like(X)
    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            #获取点到SVM中间线的距离
            P[i, j] = clf.decision_function([[xi, yj]])
            #print(P[i,j])
    C = ax.contour(X, Y, P, colors=color,
        levels=[0], alpha=0.5,
        linestyles=['-'])

plot_svc_decision_function(svc_rbf, color='b')
#plot_svc_decision_function(svc_sig, color='g')
plot_svc_decision_function(svc_poly, color='r')

## 添加标注
rbf_label = mpatches.Patch(color='b', label='rbf')
poly_label = mpatches.Patch(color='r', label='poly')

## 显示数据
plt.scatter(x[:, 0], x[:, 1], c = y)
plt.legend(handles=[rbf_label, poly_label])
plt.ioff()
plt.show()