# linux 常用问题总结

## apt install 取消后 不能继续apt install ?
E: Unable to lock directory /var/cache/apt/archives/

    sudo rm /var/cache/apt/archives/lock
****