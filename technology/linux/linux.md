# linux总结
linux相关总结
******
- apt lock

```
E: Could not get lock /var/lib/dpkg/lock - open (11 Resource temporarily unavailable)

E: Unable to lock the administration directory (/var/lib/dpkg/) is another process using it?

sudo rm /var/lib/apt/lists/lock

sudo rm /var/cache/apt/archives/lock

sudo rm /var/lib/dpkg/lock
```
- lsof

```
$ lsof /dev/video0
COMMAND   PID   USER   FD   TYPE DEVICE SIZE/OFF  NODE NAME
cheese  31526 kirill  mem    CHR   81,0          18321 /dev/video0
cheese  31526 kirill   23u   CHR   81,0      0t0 18321 /dev/video0
```

查看端口号占用情况(eg. Port80)

```
[root@localhost www.wzx1102k.com]# lsof -i:80
COMMAND  PID USER   FD   TYPE    DEVICE SIZE/OFF NODE NAME
nginx   1449 root    6u  IPv4 423446322      0t0  TCP *:http (LISTEN)
nginx   2012  www    6u  IPv4 423446322      0t0  TCP *:http (LISTEN)
```
