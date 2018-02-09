# 新linux环境启动配置脚本

## auto_setup.sh
```
    apt-get update
    apt install vim
    apt install terminator
    apt install python3-pip
    apt install python3-tk
    pip3 install tensorflow
    pip3 install scipy
    pip3 install matplotlib


    # 翻墙
    add-apt-repository ppa:hzwhuang/ss-qt5
    apt-get update
    apt-get install shadowsocks-qt5
    apt-get install proxychains

    #gitbook
    apt install npm
    npm install gitbook-cli -g
    cp /usr/bin/nodejs /usr/bin/node  # fix node cann't find because name is nodejs

    #opencv
    # download opencv source code
    git clone https://github.com/opencv/opencv_contrib.git
    git clone https://github.com/opencv/opencv.git

    # download related lib
    apt-get install build-essential
    apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
    apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

    # cmake opencv
    cd ~/opencv
    mkdir release
    cd release
    cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..

    # release opencv libs
    sudo make
    sudo make install

```
****
## conda

参考[windows下安装node-gyp](https://www.jianshu.com/p/2b831714bbff)

```
conda install -c conda-forge nodejs
conda install -c cpcloud npm
npm install -g node-gyp
apm -v
```
****

## .bashrc
```
    alias python='/usr/bin/python3.5'
```
****
## terminator
参考[5分钟入手Terminator](https://www.jianshu.com/p/cee2de32ca28)
****

## vim配置
>* vim 颜色配置
  - 编辑.vimrc， 添加`set t_Co=256`
  - 替换c.vim `cp c.vim /usr/share/vim/vim74/syntax/`
****

## atom 配置
> * [atom配置视频](https://www.youtube.com/watch?v=DjEuROpsvp4)
    - 勾选 Scroll Past End
    -  
* 如何在WIN10环境下ATOM中使用anaconda python lib?
    - atom安装hydrogen package
    - 命令行打开anaconda prompt
    - 在anaconda prompt下执行atom
    - 编写python脚本并执行

****
## git 配置

#### git ssh-key 配置
```
    git config --global user.name "wzx1102k"
    git config --global user.email "409747794@qq.com"
    git config --global core.editor vim
    git config --global push.default simple
    ssh-keygen -t rsa -C "409747794@qq.com"
```
将生成的密钥内容添加到github key配置项中， 然后使用ssh测试是否OK。
```
    ssh -T git@github.com
```
#### gitbook 配置
* 登录到Github，创建一个新的仓库，名称我们就命令为book，这样我就就得到了一个book的空仓库。
* 克隆仓库到本地：`git clone git@github.com:USER_NAME/book.git`。
* 创建一个新分支：`git checkout -b gh-pages`，注意，分支名必须为gh-pages。
* gitbook build 完成后拷贝静态网站到book仓库中 `gitbook build src des`
* 将分支push到仓库：`git push -u origin gh-pages`。
********
## 代理翻墙设置
* 命令行代理设置
```
export ALL_PROXY=socks5://127.0.0.1:1080
# export http_proxy="http://localhost:port"
# export https_proxy="http://localhost:port"
```
* VM虚拟机 ubuntu 网页浏览设置      
 参考[VMWare虚拟机通过主机shadowsocks代理上网](http://blog.csdn.net/u010726042/article/details/53187937)
  - shadowsocks.exe并勾选“允许局域网连接”
  - ubuntu System Settings – Network – Network proxy勾选Manual（手动）,
  地址全部填宿主机IP（局域网网段），设置好代理端口    
* VM虚拟机 ubuntu 命令行代理设置
 参考[Ubuntu 14.04下安装ss及proxychains](https://www.jianshu.com/p/941bf811f9c2)
 - 安装shadowsocks
 - 配置 ss.json

```
    {
        "server":"服务器地址",
        "server_port":服务器端口,
        "local_address":"127.0.0.1",
        "local_port":1080,
        "password":"密钥",
        "timeout":300,
        "method":"aes-256-cfb",
        "fast_open":false
    }
```

  -  启动SS `sslocal -c ss.json &`
  -  修改`/etc/proxychains.conf`， 将socks4改成socks5
  -  proxychains运行想要翻墙的软件， 比如`proxychains git clone git@github.com:wzx1102k/tensorflow.git`
* proxychains wget can't work ?     
  参考[proxychains cannot get wget working](https://stackoverflow.com/questions/4287358/proxychains-cannot-get-wget-working),
  修改`/usr/lib/proxychains3/proxyresolv`， 将dns改成8.8.8.8
