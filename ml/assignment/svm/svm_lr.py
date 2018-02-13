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
from matplotlib import style
style.use("ggplot")
from sklearn import svm

'''x = np.array([[1,2],
             [5,8],
             [1.5,1.8],
             [8,8],
             [1,0.6],
             [9,11],
             [6,4],
             [5,4]])

y = [0,1,0,1,0,1,1,0]'''

x = np.array([[1,2],
             [2,2],
             [3,2],
             [4,2],
             [1,4],
             [2,4],
             [3,4],
             [4,4]])

y = [0,0,0,0,1,1,1,1]
plt.scatter(x[:, 0], x[:, 1])
plt.title('SVM Linear')
plt.xlim((0, 10))
plt.ylim((0, 10))
plt.ion()
plt.show()
plt.pause(1)

clf = svm.SVC(kernel='linear', C = 10)
clf.fit(x,y)

w = clf.coef_[0]
print(w)
print('SVM Predict %d' %clf.predict([[-0.8, -1]]))
print('Point (5,5) to svm line direction: %d' %clf.decision_function([[5, 5]]))
a = -w[0] / w[1]

xx = np.linspace(0,12)
yy = a * xx - clf.intercept_[0] / w[1]

h0 = plt.plot(xx, yy, 'k-', label="non weighted div")

plt.scatter(x[:, 0], x[:, 1], c = y)
plt.legend()

plt.ioff()
plt.show()