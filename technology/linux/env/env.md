# 新linux环境启动配置脚本

## auto_setup.sh

    apt-get update
    apt install vim
    apt install python3-pip
    pip3 install tensorflow

    #gitbook
    apt install npm
    npm install gitbook-cli -g
    cp /usr/bin/nodejs /usr/bin/node  # fix node cann't find because name is nodejs
***
## .bashrc

    alias python='/usr/bin/python3.5'
***
## git 配置

#### git ssh-key 配置

    git config --global user.name "wzx1102k"
    git config --global user.email "409747794@qq.com"
    git config --global core.editor vim
    git config --global push.default simple
    ssh-keygen -t rsa -C "409747794@qq.com"
将生成的密钥内容添加到github key配置项中， 然后使用ssh测试是否OK。

    ssh -T git@github.com

#### gitbook 配置
* 登录到Github，创建一个新的仓库，名称我们就命令为book，这样我就就得到了一个book的空仓库。
* 克隆仓库到本地：`git clone git@github.com:USER_NAME/book.git`。
* 创建一个新分支：`git checkout -b gh-pages`，注意，分支名必须为gh-pages。
* gitbook build 完成后拷贝静态网站到book仓库中 `gitbook build src des`
* 将分支push到仓库：`git push -u origin gh-pages`。
