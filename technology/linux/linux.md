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
- df, du, fdisk
    + 查看文件夹 size
    ```
    [root@localhost webpy]# du -sh
    3.2M	.
    ```
    + 查看分区还剩多少空间
    ```
    [root@localhost /]# df -hl
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/simfs       10G  4.1G  6.0G  41% /
    none            256M  4.0K  256M   1% /dev
    none            256M     0  256M   0% /dev/shm
    ```
    + 查看物理硬盘
    ```
    root@ubuntu:/home/cloud/workspace/project/documents# fdisk -l
    Disk /dev/sda: 60 GiB, 64424509440 bytes, 125829120 sectors
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: dos
    Disk identifier: 0x8971d5ea
    Device     Boot     Start       End   Sectors Size Id Type
    /dev/sda1  *         2048 119539711 119537664  57G 83 Linux
    /dev/sda2       119541758 125827071   6285314   3G  5 Extended
    /dev/sda5       119541760 125827071   6285312   3G 82 Linux swap / Solaris
    ```
