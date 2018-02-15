import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import time
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# 测试数据生成
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

# 显示测试数据
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, y_data)
plt.title('Tensorflow Logistic  Regression')
plt.ion()
plt.show()

# 生成学习网络
# layer0: input
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

# layer1:
W1 = tf.Variable(tf.random_normal([1,10]))
bias1 = tf.Variable(tf.zeros([1, 10]) + 0.1)
o1 = tf.nn.relu(tf.matmul(xs, W1) + bias1)

# layer2: output
W2 = tf.Variable(tf.random_normal([10,1]))
bias2 = tf.Variable(0.1)
predict = tf.matmul(o1, W2) + bias2

# loss
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - predict),
                     reduction_indices=[1]))

# train method
train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

#init all variables, it will be activated by use sess.run(init)
init = tf.global_variables_initializer()


with tf.Session() as sess:
    sess.run(init)
    for i in range(1000):
        sess.run(train, feed_dict={xs:x_data, ys:y_data})
        if i % 50 == 0:
            prediction_value = sess.run(predict, feed_dict={xs:x_data})
            try:
                ax.lines.remove(lines[0])
            except Exception:
                pass
            lines = ax.plot(x_data, prediction_value, 'r-', lw=2)
            print(sess.run(loss, feed_dict={xs:x_data, ys:y_data}))
            plt.pause(0.1)

plt.ioff()
plt.show()
