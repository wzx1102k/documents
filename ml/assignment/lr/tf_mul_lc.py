import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
import time
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

DIMENSION = 2
KNUM = 4
SAMPLE_CNT = 240

def init_variable(name, shape):
    return(tf.get_variable(name, shape=shape, initializer=tf.contrib.layers.xavier_initializer()))
        
# 测试数据生成
x_data, y_data = make_blobs(n_samples=SAMPLE_CNT, n_features=DIMENSION, centers=KNUM, center_box=(-20, 20), cluster_std=1.5)
x = x_data.tolist()
label=np.zeros((SAMPLE_CNT, KNUM))

label[y_data==0] = [0,0,0,1]
label[y_data==1] = [0,0,1,0]
label[y_data==2] = [0,1,0,0]
label[y_data==3] = [1,0,0,0]

y = label.tolist()
keep_prob = tf.placeholder(tf.float32)
prediction_value = y.copy()

# 显示测试数据
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.xlabel('x')
plt.ylabel('y')
plt.xlim((-30, 30))
plt.ylim((-30, 30))
p0 = ax.scatter(x_data[:,1], x_data[:,0], marker = 'o', color = 'k', label='1', s = 50)
plt.title('Tensorflow Logistic Classification')
plt.ion()
plt.show()

# 生成学习网络
# layer0: input
xs = tf.placeholder("float", [None, 2])
ys = tf.placeholder("float", [None, 4])
keep_prob = tf.placeholder(tf.float32)
 
# layer1:
W1 = init_variable('W1', [2,20])
bias1 = init_variable('b1', [1,20])
o1 = tf.nn.relu(tf.matmul(xs, W1) + bias1)
o1_drop = tf.nn.dropout(o1, keep_prob)

# layer2:
W2 = init_variable('W2', [20,20])
bias2 = init_variable('b2', [1,20])
o2 = tf.nn.relu(tf.matmul(o1_drop, W2) + bias2)
o2_drop = tf.nn.dropout(o2, keep_prob)

# layer2: output
W3 = init_variable('W3', [20,4])
bias3 = init_variable('b3', [1,4])
#predict = tf.nn.softmax(tf.matmul(o2_drop, W3) + bias3)
o3 = tf.matmul(o2_drop, W3) + bias3
predict = tf.nn.softmax(o3)

# loss  sum( y*log(predict) )
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=o3, labels=ys))
#loss = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(predict), reduction_indices=[1]))

# train method
#train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
train = tf.train.AdamOptimizer(1e-3).minimize(loss)

#init all variables, it will be activated by use sess.run(init)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(200):
        sess.run(train, feed_dict={xs:x, ys:y, keep_prob: 0.5})
        if i % 1 == 0:
            prediction_value = sess.run(predict, feed_dict={xs:x, keep_prob: 1})
            try:
                p0.remove()
                p1.remove()
                p2.remove()
                p3.remove()
            except Exception:
                pass
            idx_0 = np.where(np.argmax(prediction_value, axis=1) == 0)
            p0 = ax.scatter(x_data[idx_0,1], x_data[idx_0,0], marker = '+', color = 'c', label='1', s = 50)
            idx_1 = np.where(np.argmax(prediction_value, axis=1) == 1)
            p1 = ax.scatter(x_data[idx_1,1], x_data[idx_1,0], marker = 'x', color = 'm', label='2', s = 50)
            idx_2 = np.where(np.argmax(prediction_value, axis=1) == 2)
            p2 = ax.scatter(x_data[idx_2,1], x_data[idx_2,0], marker = '*', color = 'b', label='3', s = 50)
            idx_3 = np.where(np.argmax(prediction_value, axis=1) == 3)
            p3 = ax.scatter(x_data[idx_3,1], x_data[idx_3,0], marker = 'o', color = 'g', label='4', s = 50)
            print(sess.run(loss, feed_dict={xs:x, ys:y, keep_prob: 1}))
            plt.pause(0.1)
            #break

plt.ioff()
plt.show()
