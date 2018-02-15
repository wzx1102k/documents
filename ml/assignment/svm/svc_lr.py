'''
class sklearn.svm.SVC(  
    C=1.0,    larger values of C, smaller-margin hyperplane, less misclassifying
    kernel=’rbf’, 
    degree=3,  Degree of the polynomial kernel function (‘poly’). Ignored by all other kernels.
    gamma=’auto’, 
    coef0=0.0, 
    shrinking=True, 
    probability=False, 
    tol=0.001,  Tolerance for stopping criterion.
    cache_size=200, 
    class_weight=None, 
    verbose=False, 
    max_iter=-1, 
    decision_function_shape=’ovr’, 
    random_state=None
    )
（1）C: 目标函数的惩罚系数C，用来平衡分类间隔margin和错分样本的，default C = 1.0； 
（2）kernel：参数选择有RBF, Linear, Poly, Sigmoid, 默认的是"RBF"; 
（3）degree：if you choose 'Poly' in param 2, this is effective, degree决定了多项式的最高次幂； 
（4）gamma：核函数的系数('Poly', 'RBF' and 'Sigmoid'), 默认是gamma = 1 / n_features; 
（5）coef0：核函数中的独立项，'RBF' and 'Poly'有效； 
（6）probablity: 可能性估计是否使用(true or false)； 
（7）shrinking：是否进行启发式； 
（8）tol（default = 1e - 3）: svm结束标准的精度; 
（9）cache_size: 制定训练所需要的内存（以MB为单位）； 
（10）class_weight: 每个类所占据的权重，不同的类设置不同的惩罚参数C, 缺省的话自适应； 
（11）verbose: 跟多线程有关，不大明白啥意思具体； 
（12）max_iter: 最大迭代次数，default = 1， if max_iter = -1, no limited; 
（13）decision_function_shape ： ‘ovo’ 一对一, ‘ovr’ 多对多  or None 无, default=None 
（14）random_state ：用于概率估计的数据重排时的伪随机数生成器的种子。
'''

'''
kernel 
linear:  u'*v
poly(polynomial): (gamma*u'*v + coef0)^degree
rbf(radial basis):  exp(-gamma*|u-v|^2)
sigmoid: tanh(gamma*u'*v + coef0)
'''


import numpy as np
import matplotlib.pyplot as plt
import seaborn
from sklearn.linear_model import LinearRegression
from scipy import stats
import pylab as pl
from sklearn.datasets.samples_generator import make_blobs
from sklearn.svm import SVC

## matplotlib 更高级封装，生成画图的grid
seaborn.set()

## 生成聚类测试数据
x, y = make_blobs(n_samples=50, centers=2,
                  random_state=0, cluster_std=0.60)

## 画点
plt.scatter(x[:, 0], x[:, 1], c=y, s=50, cmap='spring')
plt.title('SVM Classifier Linear')
plt.ion()
plt.show()

## 运行 linear svm
clf = SVC(kernel='linear')
clf.fit(x, y)

## 画SVM区域间隔线
def plot_svc_decision_function(clf, ax=None):
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
            print(P[i,j])
    ax.contour(X, Y, P, colors='k',
               levels=[-1, 0, 1], alpha=0.5,
               linestyles=['--', '-', '--'])

plot_svc_decision_function(clf)
plt.ioff()
plt.show()