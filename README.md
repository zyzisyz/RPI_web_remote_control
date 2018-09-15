# RPI_web_remote_control

利用树莓派远程控制空调等家电的开关

## 简要介绍

这是一个利用网页远程控制树莓派发出红外信号控制空调等家电的小项目or实验，简单来说，可以在回家的路上用手机通过网页控制，提前将空调打开，设定成需要的温度。同时可以在网页上实时监控室内的温度和湿度。

代码主要使用Python的flask框架编写。为了能在公网下远程访问树莓派，使用[frp内网穿透工具](https://github.com/fatedier/frp.git)。

### 功能概要

1. 远程控制空调
2. 远程监控室内温湿度
3. 远程操控LED灯

## 所用元器件

1. 树莓派3B+ ×1
2. SD卡（8GB） ×1
3. 红外发射和接收模块 ×1
4. 温湿度传感模块 ×1
6. 发光二极管 x1
7. 树莓派拓展板 x2
8. 杜邦线 若干
9. 具有公网IP的VPS x1

## 最终效果图

### 前端网页效果图

因为对前端不是很熟，这个网页写的很简单。但基本实现了我们需要显示的功能和按键。

![image](https://github.com/zyzisyz/RPI_WEB_REMOTE_CONTROL/blob/master/img/1.png)

更多效果图可以查看img文件夹下的图片

### 实物连接图

![image](https://github.com/zyzisyz/RPI_WEB_REMOTE_CONTROL/blob/master/img/4.jpg)

## 文件结构说明

```tree
RPI_web_remote_control/         
|-- img                     //用于存放README.md演示图片
|-- net_setting             //用于存放内网穿透的设置文件
|-- README.md               
`-- web_interface           //用于存放Python写的flask工程
```

## 如何使用

如果你有一定的使用Linux经验和对flask这样的web应用框架有一定的了解，相信你一定能很快的上手，配置好内网穿透和安装好flask后直接运行web_interface下的app.py文件就可以了。