# 调试记录
机器学习相关工程调试记录

## tfocr 调试记录

1. tf train 所使用数据一定要和tfrecord数据矩阵格式对齐：

![](tfocr.png)
tf.reshape(...)中[-1, label_num, label_idx], 其中 -1 指训练样本个数不确定,
label_num为要识别字符的个数， 比如识别6个字符， 是矩阵的行,
label_idx 训练字符的种类，是矩阵的列，弄反排序和tfrecord 对不齐就会得到错误的结果。

tfrecord源数据为1,5,8,2:

    [  0 1 0 0 0 0 0 0 0 0  
       0 0 0 0 0 1 0 0 0 0  
       0 0 0 0 0 0 0 0 1 0
       0 0 1 0 0 0 0 0 0 0 ]
以4个数字0-9排序为例:  使用[-1, label_num, label_idx] 排序为：

    1 [  0 1 0 0 0 0 0 0 0 0 ]
    5 [  0 0 0 0 0 1 0 0 0 0 ]
    8 [  0 0 0 0 0 0 0 0 1 0 ]
    2 [  0 0 1 0 0 0 0 0 0 0 ]
使用[-1, label_idx, label_num] 排序为：

    [0 1 0 0]
    [0 0 0 0]
    [0 0 0 0]
    [0 0 0 1]
    [0 0 0 0]
    [0 0 0 0]
    [0 0 0 0]
    [1 0 0 0]
    [1 0 0 0]
    [0 0 0 0]
从而得到不正确的结果.
2. tf end to end 使用原始数据和添加合成的新数据训练对比:

原数据:   train : 538      test: 280    
合成数据:  train: 10000     test: 1000    
* 只使用原数据

    result:   train accuracy: 100%,   test accuracy: 18%    overfitting    
* 原数据：合成数据 ： 100:100   

    result:  train accuracy: 91%,   test accuracy: 60%      
* 原数据：合成数据 ： 64:32

    result:  train accuracy: 80%,   test accuracy: 80%    
从结果可看出添加少量合成数据 对原数据test accuracy 有比较大的提升
***
