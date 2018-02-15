import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import time
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# 测试数据生成
_x = np.random.randint(-10, 10, (400, 2))
_ = np.linalg.norm(_x, axis=1)
circle_in = _x[_<5]
circle_out = _x[_>8]
x_data = np.vstack((circle_in, circle_out))
x = x_data.tolist()
y_data = np.zeros((x_data.shape[0], 1))
y_data[0:circle_in.shape[0]] = 1
y = y_data.tolist()
keep_prob = tf.placeholder(tf.float32)
prediction_value = y.copy()

# 显示测试数据
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.xlabel('x')
plt.ylabel('y')
plt.xlim((-15, 15))
plt.ylim((-15, 15))
p0 = ax.scatter(x_data[:,1], x_data[:,0], marker = 'o', color = 'k', label='1', s = 50)
plt.title('Tensorflow Logistic Classification')
plt.ion()
plt.show()

# 生成学习网络
# layer0: input
xs = tf.placeholder("float", [None, 2])
ys = tf.placeholder("float", [None, 1])

# layer1:
W1 = tf.Variable(tf.random_normal([2,10]))
bias1 = tf.Variable(tf.zeros([1, 10]) + 0.1)
o1 = tf.nn.relu(tf.matmul(xs, W1) + bias1)

# layer2: output
W2 = tf.Variable(tf.random_normal([10,1]))
bias2 = tf.Variable(0.1)
predict = tf.nn.sigmoid(tf.matmul(o1, W2) + bias2)

# loss  sum( y*log(predict) + (1-y)*log(1-predict) )
loss = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(tf.clip_by_value(predict, 1e-10,1.0)) \
    + (1-ys)*tf.log(tf.clip_by_value(1-predict, 1e-10,1.0)),
                reduction_indices=[1]))

# train method
train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

#init all variables, it will be activated by use sess.run(init)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(200):
        sess.run(train, feed_dict={xs:x, ys:y, keep_prob: 1})
        if i % 1 == 0:
            prediction_value = sess.run(predict, feed_dict={xs:x})
            print(prediction_value)
            try:
                p0.remove()
                p1.remove()
            except Exception:
                pass
            idx_0 = np.where(prediction_value[:, 0] > 0.5)
            p0 = ax.scatter(x_data[idx_0,1], x_data[idx_0,0], marker = '+', color = 'c', label='1', s = 50)
            idx_1 = np.where(prediction_value[:, 0] <= 0.5)
            p1 = ax.scatter(x_data[idx_1,1], x_data[idx_1,0], marker = 'x', color = 'm', label='2', s = 50)
            print(sess.run(loss, feed_dict={xs:x, ys:y}))
            plt.pause(0.1)
            #break

plt.ioff()
plt.show()

print(y)
print(prediction_value)