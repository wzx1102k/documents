# 软件安装
记录常用软件的安装信息

## 中文输入法安装

####  步骤1. 下载必要库
```
    sudo apt install libopencc1 fcitx-libs fcitx-libs-qt
    sudo dpkg –i sogoupinyin_2.0.0.0078_amd64.deb
```
#### 步骤2. fcitx 环境变量配置

参考[fcitx输入法打死切换不出来](https://bbs.archlinuxcn.org/viewtopic.php?id=1862),
在 ~/.xprofile 中写  
```
    export GTK_IM_MODULE=fcitx
    export QT_IM_MODULE=fcitx
    export XMODIFIERS=@im=fcitx
```
#### 步骤3. 中文输入法配置

>1. 在Language Support中增加汉语，然后选择输入法系统为fcitx
2. 重启系统
3. 在Text Entry中增加Sogou Pinyin
4. 使用Ctrl+space即可开启搜狗输入法

#### 步骤4. 特殊字符修复

参考 [ubuntu中shift键打不出特殊符号](http://blog.csdn.net/linxingqianglai/article/details/51813548),
将输入源英语（英国）改成英语（美国）, 则 # @ 显示正常
****
## markdown 常用使用快捷键

参考[markdown语法大全](https://www.jianshu.com/p/c4e93e97143c) 和
[段落与换行](http://xianbai.me/learn-md/article/syntax/paragraphs-and-line-breaks.html)

>1. 段落的前后必须是空行
2. 段内每行换行，可以行尾+2空格
3. 插入代码前需要换行， 四个空格表示代码段
4. 使用 \*，\+，\- 表示无序列表, 特殊字符前加\\
5. 使用 \!\[描述\]\(图片链接地址\) 插入图像
6. 使用 \[描述\]\(链接地址\) 为文字增加外链接。
7. 使用 \`代码\` 表示行内代码块。
8. 使用 一对\`\`\`区隔代码段
9. 使用 \> \>> \>>>等段落缩进

*****
## atom

#### atom install jupyter notebook package
> - install node.js  npm  node-gyp

    - fix bug at line 34 In main.js at /home/$USER/.atom/packages/jupyter-notebook/lib

    参考[fix notebook bug](https://github.com/cloutiertyler/atom-notebook/commit/cf2ab0e66a8e7b470b7d88a03191bcaed477bf2a)

    - install jupyter notebook package

####  [conda使用不同版本python](https://conda.io/docs/user-guide/tasks/manage-python.html)
```       
        #step 1. create python env
        #py27 for python2.7
        conda create -n py27 python=2.7 anaconda
        #py36 for python3.6
        conda create -n python36 python=3.6 anaconda

        #change default to python2.7   - activate py27
        activate py27

        #verify new env
        conda info --envs
        python --version
```
#### [node.js 是用来做什么的? ](https://www.zhihu.com/question/33578075)

      一种javascript的运行环境， 能够使javascript 脱离浏览器运行

####  [npm模块安装机制简介](http://www.ruanyifeng.com/blog/2016/01/npm-install.html)

     npm 是node的模块管理器，通过npm install相关命令 就能安装别人写好的模块。

#### [windows下安装node-gyp](https://www.jianshu.com/p/2b831714bbff)

    gyp是一种根据c++源代码编译的工具， node-gyp是为node编译c++扩展时候使用的编译工具。

    `npm install --global --production windows-build-tools`  (use python2.7 env)
*****
