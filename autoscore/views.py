import time
import pandas as pd
from django.shortcuts import render,HttpResponse
from django.http import FileResponse

# Create your views here.

EXCLE_FILE = r'F:\Django_projects\Auto_score_wjw\autoscore\score.xlsx'
SAVE_FILE = r'F:\Django_projects\Auto_score_wjw\autoscore\savescore.xlsx'
SUBJECT_LIST = ['chinese','math','english','wuli','huaxue','shengwu']
ERROR_FILE = r'F:\Django_projects\Auto_score_wjw\autoscore\error.txt'
NAME_LIST = ['金筱易', '徐嘉孺', '冯国申', '杨书勤', '王建为', '宋祎垌', '王天骏', '曹佳硕', '王希蒙', '穆玥彤', '栾博业', '王禹璇', '金云鹏', '张靖悦', '赵益铭', '解丰硕', '滕金楠', '赵一博', '尧洁', '董钰鑫', '张馨童', '李思佳', '许新敏', '刘佳欣', '陈冬妮', '英瑞桐', '康汝佳怡', '张田佳含', '郑荟竹', '王奥涵', '石成功', '于世畔', '刘一田', '赵津磊', '白长健', '高艺鸣', '付晓玮', '李宇梁', '沈春潇', '李昶杰', '程铄茜', '沈凯文', '杨箫宁', '杨思齐', '刘宇凡', '薛宇轩', '周艺卓',]
NAME_DICT = dict.fromkeys(NAME_LIST,False)
data = pd.DataFrame(pd.read_excel(EXCLE_FILE))

def setdeafult(request):
    global NAME_DICT
    global data
    if request.method == 'GET':
        return render(request,'set_default.html')
    password = request.POST.get('password')
    if password == '0319':
        NAME_DICT = dict.fromkeys(NAME_LIST, False)
        data = pd.DataFrame(pd.read_excel(EXCLE_FILE))
        try:
            data.to_excel(SAVE_FILE)
        except Exception as e:
            with open(ERROR_FILE,'wt') as f:
                info = str(time.asctime()) + str(e) + '\n'
                f.write(info)
            return render(request,'contact_admin.html')
        return render(request,'setdefault_sucess.html')
    else:
        return render(request,'setdefault_false.html')

def index(request):
    if request.method == 'GET':
        return render(request,'auto_score.html')
    else:
        print(request.POST)
        username = request.POST.get('username')
        if username not in NAME_LIST:
            return render(request,'namenotexist.html')
        NAME_DICT[username] = True
        chinese = request.POST.get('chinese')
        math = request.POST.get('math')
        english = request.POST.get('english')
        wuli = request.POST.get('wuli')
        huaxue = request.POST.get('huaxue')
        shengwu = request.POST.get('shengwu')
        try:
            data['chinese'][data['Name'] == username] = float(chinese)
            data['math'][data['Name'] == username] = float(math)
            data['english'][data['Name'] == username] = float(english)
            data['wuli'][data['Name'] == username] = float(wuli)
            data['huaxue'][data['Name'] == username] = float(huaxue)
            data['shengwu'][data['Name'] == username] = float(shengwu)
        except ValueError as e:
            pass
        try:
            data.to_excel(SAVE_FILE)
        except Exception as e:
            with open(ERROR_FILE,'wt') as f:
                info = str(time.asctime()) + str(e) + '\n'
                f.write(info)
            return render(request,'contact_admin.html')
        return render(request,'sucess.html')


def check(request):
    if request.method == 'GET':
        return render(request,'check.html')

def ajax_namelist(request):
    return HttpResponse(str({k for k,v in NAME_DICT.items() if v == False}))

def file_down(request):
    file=open(SAVE_FILE,'rb')
    response = FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="savescore.xlsx"'
    return response
