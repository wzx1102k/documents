# 机器学习常用tool总结
*******
## tensorflow

#### tensorflow general

![](tf_high_api.png)
![](tf_compare.png)

- tf xavier init
![](tf_xavier.png)

- 使用tf.concat连接多个神经网络输出    
```
    tf.concat(values, concat_dim, name='concat') # 0 : 行， 1: 列
    # fc2_*  大小: 1*54;    predict 大小：1*324
    predict = tf.concat([fc2_1, fc2_2, fc2_3, fc2_4, fc2_5, fc2_6], 1)
```
- mnist 数据集合 image 是有做过正则化的    
参考[数据预处理](http://ufldl.stanford.edu/wiki/index.php/%E6%95%B0%E6%8D%AE%E9%A2%84%E5%A4%84%E7%90%86)
在处理自然图像时，我们获得的像素值在 [0,255] 区间中，常用的处理是将这些像素值除以 255，使它们缩放到 [0,1] 中.

- tf.clip_by_value(A, min, max)    
输入一个张量A，把A中的每一个元素的值都压缩在min和max之间。小于min的让它等于min，大于max的元素的值等于max。

- [What's the difference between softmax and softmax_cross_entropy_with_logits?](https://stackoverflow.com/questions/34240703/whats-the-difference-between-softmax-and-softmax-cross-entropy-with-logits)

- softmax:  需要额外写loss function
```
predict = tf.nn.softmax(tf.add(tf.matmul(x, W),  b))
loss = tf.reduce_mean(-tf.reduce_sum(y_true * tf.log(predict), [1]))
```
- softmax_cross_entropy_with_logit  计算softmax 以及交叉熵(loss)
```
predict = tf.add(tf.matmul(x, W),  b)
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=predict, labels=y_true))
```

#### tensorflow use gpu

- 查看平台是否支持gpu
```
from tensorflow.python.client import device_lib
device_lib.list_local_devices()

[name: "/device:CPU:0"
 device_type: "CPU"
 memory_limit: 268435456
 locality {
 }
 incarnation: 16925341359735686096, name: "/device:GPU:0"
 device_type: "GPU"
 memory_limit: 292159488
 locality {
   bus_id: 1
 }
 incarnation: 6286052981776494181
 physical_device_desc: "device: 0, name: Tesla K80, pci bus id: 0000:00:04.0, compute capability: 3.7"]
```
- [如何查看tensorflow跑的是gpu版本还是cpu版本？](https://www.zhihu.com/question/263850405)
```
# Creates a graph.
a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
c = tf.matmul(a, b)
# Creates a session with log_device_placement set to True.
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
# Runs the op.
print(sess.run(c))

Device mapping:
/job:localhost/replica:0/task:0/device:GPU:0 -> device: 0, name: Tesla K40c, pci bus
id: 0000:05:00.0
b: /job:localhost/replica:0/task:0/device:GPU:0
a: /job:localhost/replica:0/task:0/device:GPU:0
MatMul: /job:localhost/replica:0/task:0/device:GPU:0
[[ 22.  28.]
 [ 49.  64.]]
```
- [tensorflow use gpu train mnist cnn](https://stackoverflow.com/questions/44868914/using-gpu-vs-cpu-in-tensorflow-deep-mnist-example)
```
with tf.device('/gpu:0'):
    W_conv1 = weight_variable([5, 5, 1, 32])
    b_conv1 = bias_variable([32])
    ...
    with tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)) as sess:
        sess.run(tf.global_variables_initializer())
        ...
        for i in range(20000):
            ...
```
- 新服务器如何配置GPU运行环境？
    + 查看是否支持GPU
        `! lspci -nnk | grep -i nvidia`
    +  安装cuda lib [Adding GPUs to Instances](https://cloud.google.com/compute/docs/gpus/add-gpus#verify-driver-install)
```
#!/bin/bash
echo "Checking for CUDA and installing."
# Check for CUDA and try to install.
if ! dpkg-query -W cuda-8-0; then
    # The 16.04 installer works with 16.10.
    curl -O https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_8.0.61-1_amd64.deb
    dpkg -i ./cuda-repo-ubuntu1604_8.0.61-1_amd64.deb
    sudo apt-get update
    sudo apt-get install cuda-8-0 -y
fi
# Enable persistence mode
sudo nvidia-smi -pm 1

#performance optimizing
#for K80
sudo nvidia-smi -ac 2505,875
sudo nvidia-smi --auto-boost-default=DISABLE

#check cuda version
nvcc -V
```
    +  [NVIDIA官网下载对应cudnn lib](https://developer.nvidia.com/rdp/cudnn-download)
        `dpkg -i ./libcudnn6_6.0.21-1+cuda8.0_amd64.deb`

    + [安装gpu tensorflow](https://github.com/tensorflow/tensorflow/issues/15604)
        如果出现版本不对齐问题，查看tensorflow 依赖cuda version。 `pip3 install --upgrade tensorflow-gpu==1.4`

    + [failed call to cuDevicePrimaryCtxReta in: CUDA_ERROR_ECC_UNCORRECTABLE](https://stackoverflow.com/questions/16238458/cannot-create-context-on-nvidia-device-with-ecc-enabled)
`nvidia-smi --reset-ecc-errors=0 -g 0`


*****
## numpy

- 矩阵操作

> - 全0矩阵 `np.zeros()`
> - 全1矩阵 `np.ones([1, 4])`
> - 填充矩阵 `np.full([2, 3], 1.2)`
> - 随机矩阵 `np.empty([2, 3])`
> - 单位矩阵(对角矩阵) `np.identity(3) / eye()`
> - 对角矩阵(带偏移) `np.diagflat([1, 2, 3], k=1)`
> - 下三角矩阵 `np.tri()`
> - 范德蒙矩阵 `np.vander()`
> - `np.sign(0)` 输出0， `np.sign(>0)`输出1， `np.sign(<0)` 输出-1
> 合并列矩阵  `np.vstack((a,b))` ,合并行矩阵  `np.hstack((a,b))`

- 数值运算 axis = 0 表示列， axis = 1  表示行

> - np.mean(a, axis=0) # axis=0，计算每一列的均值  
> - np.linalg.norm(x, ord=None, axis=None, keepdims=False)   计算范数， 默认二范数 求欧式距离/向量内积
> - `np.shape` 求矩阵大小,  `np.shape[0]` 求行大小, `np.shape[1]` 求列大小

****
## matplotlib
- matplotlib.pyplot.gca
    use `plt.gca()`  to get current polar axes on the current figure.

- 不同颜色线条进行标注

```
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

rbf_label = mpatches.Patch(color='b', label='rbf')
poly_label = mpatches.Patch(color='r', label='poly')
plt.legend(handles=[rbf_label, poly_label])
plt.show()
```

****
## sklearn

- make_blob 生成聚类测试数据

```
from sklearn.datasets.samples_generator import make_blobs

sklearn.datasets.make_blobs(
            n_samples=100,
            n_features=2,
            centers=3,
            cluster_std=1.0,
            center_box=(-10.0, 10.0),
            shuffle=True,
             random_state=None
)

x, label = make_blobs(
    n_samples=SAMPLE_CNT,
    n_features=DIMENSION,
    centers=KNUM,
    center_box=(-10, 10)
)
```

- svc lib

```
class sklearn.svm.SVC(  
    C=1.0,    larger values of C, smaller-margin hyperplane, less misclassifying
    kernel=’rbf’, ‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
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
```
>- C: 目标函数的惩罚系数C，用来平衡分类间隔margin和错分样本的，default C = 1.0；
>- kernel：参数选择有RBF, Linear, Poly, Sigmoid, 默认的是"RBF";
>- degree：if you choose 'Poly' in param 2, this is effective, degree决定了多项式的最高次幂；
>- gamma：核函数的系数('Poly', 'RBF' and 'Sigmoid'), 默认是gamma = 1 / n_features;
>- coef0：核函数中的独立项，'RBF' and 'Poly'有效；
>- probablity: 可能性估计是否使用(true or false)；
>- shrinking：是否进行启发式；
>- tol（default = 1e - 3）: svm结束标准的精度;
>- cache_size: 制定训练所需要的内存（以MB为单位）；
>- class_weight: 每个类所占据的权重，不同的类设置不同的惩罚参数C, 缺省的话自适应；
>- verbose: 跟多线程有关，不大明白啥意思具体；
>- max_iter: 最大迭代次数，default = 1， if max_iter = -1, no limited;
>- decision_function_shape ： ‘ovo’ 一对一, ‘ovr’ 多对多  or None 无, default=None
>- random_state ：用于概率估计的数据重排时的伪随机数生成器的种子。

```
from sklearn.svm import SVC

clf = SVC(decision_function_shape='ovo') #ovo为一对一  
clf.fit(X,Y)  
dec = clf.decision_function([[x, y]])    #返回的是样本距离超平面的距离
```
***
