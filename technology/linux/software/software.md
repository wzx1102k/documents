# 软件安装
记录常用软件的安装信息

## 中文输入法安装

###  步骤1. 下载必要库

  sudo apt install libopencc1 fcitx-libs fcitx-libs-qt

  sudo dpkg –i sogoupinyin_2.0.0.0078_amd64.deb

### 步骤2. fcitx 环境变量配置

参考 https://bbs.archlinuxcn.org/viewtopic.php?id=1862
在 ~/.xprofile 中写
  export GTK_IM_MODULE=fcitx
  export QT_IM_MODULE=fcitx
  export XMODIFIERS=@im=fcitx

### 步骤3. 中文输入法配置

1.在Language Support中增加汉语，然后选择输入法系统为fcitx
2.重启系统
3.在Text Entry中增加Sogou Pinyin
4.使用Ctrl+space即可开启搜狗输入法

### 步骤4. 特殊字符修复

参考 http://blog.csdn.net/linxingqianglai/article/details/51813548
将输入源英语（英国）改成英语（美国）, 则 # @ 显示正常
