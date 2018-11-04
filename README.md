# bjbus-query
北京实时公交查询爬虫(spider for Beijing real-time bus infomation)  
官网查询实时公交操作繁琐，在手机上更是不好用，直接写成爬虫脚本，便于桌面使用。结合Android上的Termux，以及简单的sh脚本，就能方便在手机上看公交信息了。一般用的也就固定的几趟车，可以自行修改参数，定制查询。

# 函数说明
> getLineDir(url,s)

**输入**：对应的网址`url`(可以通过抓包得到)；程序起始由requests创建的Session对象`s`  
该函数用于获取指定公交的信息，包括往、返方向的车辆的特征值`uuid`,以及始末站信息。结果返回到LineDir_info字典中。

> getbus(busid,s)

**输入**：特定公交特定方向的特征值`busid`，即`uuid`值；程序起始由requests创建的Session对象`s`  
该函数在选定车次及方向之后，用于获取公交到站的信息，返回的参数`busc`、`buss`、`bus_list`分别表示途中车辆、到站车辆、站点名称。

> print_res(busc,buss,bus_list)

用于格式化输出信息。

> rec_Str(mystr)

用于处理文本，避免繁琐的中文输入，如输入`t19`，程序会自动处理为服务器能识别的`特19`，其他规则可以自行添加。

> main()

主函数，用于创建会话（session），处理用户交互信息，间隔一定时间更新状态等。

注：仅用于学习交流
