import requests
import re
from os import system
from time import sleep
from ast import literal_eval

def getLineDir(url,s):
    r = s.get(url,verify=False)
    r.encoding = r.apparent_encoding
    rt = r.text
    LineDir_info = dict()
    uuid_list = re.findall('(?<=data-uuid=")\d+',rt)
    busdir_list = re.findall('\((.*?)\)',rt)
    for i in [1,2]:
        flist = []
        flist.append(uuid_list[i-1])
        flist.append(busdir_list[i-1])
        LineDir_info["{}".format(i)]=flist
    return LineDir_info

def getbus(busid,s):
    url = 'http://www.bjbus.com/home/ajax_rtbus_data.php?act=busTime&selBLine=1&selBDir={}&selBStop=1'.format(busid)
    r = s.get(url,verify=False)
    html = literal_eval(r.text)['html']
    busc = re.findall('(?<=id=")\d+(?=m"><i  class="busc")',html)
    busc = [int(i)-1 for i in busc]
    buss = re.findall('(?<=id=")\d+(?="><i class="buss")',html)
    buss = [int(i)-1 for i in buss]
    bus_list = re.findall('(?<=title=").+?(?=")',html)
    return busc,buss,bus_list

def print_res(busc,buss,bus_list):
    for i in range(0,len(bus_list)):
        if i in busc:
            print("====================\t<======途中车辆")
        elif i in buss:
            print("{0:{1}<10}\t<------到站".format(bus_list[i],chr(12288)))
            continue
        print("{0:{1}<10}".format(bus_list[i],chr(12288)))

def rec_str(mystr):
    # 输入't19'或者'T19'都能自动转换为'特19'
    return re.sub('t','特',mystr,flags=re.I)

def main():
    s = requests.Session()
    UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    header = {'User-Agent':UA}
    s.headers.update(header)

    bus = rec_str(input("输入查询车次："))
    selbline = requests.utils.quote(bus)
    url_getLineDir = 'http://www.bjbus.com/home/ajax_rtbus_data.php?act=getLineDir&selBLine={}'.format(selbline)
    line_info = getLineDir(url_getLineDir,s) #获取班车的特征码以及始末站

    fint = input("选择方向：\n[1]{}\n[2]{}\n选择(Enter确认):".format(line_info["1"][1],line_info["2"][1]))
    res = system('cls')
    uuid = line_info[fint][0]

    # 循环查询,间隔10s
    while 1:
        busc,buss,bus_list = getbus(uuid,s)
        print_res(busc,buss,bus_list)
        sleep(10)
        res = system("cls")

main()
