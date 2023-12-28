from django.shortcuts import render
from django.contrib.auth import authenticate,logout#,login
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import GOAL22,CPA22,RHDT,Foo
from .forms import GOAL22Q1Form,GOAL22Q2Form,GOAL22Q3Form,GOAL22Q3AForm,CPA22CForm,CPA22AForm,TIMEForm,UserForm,FooForm
import os
from datetime import datetime
from django.utils import timezone
#import xlwt
#import xlrd
#from xlutils.copy import copy
import xlsxwriter
import io
import openpyxl as op
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

User = get_user_model()

#def home(request):
#    form = 'hello'
#    return render(request, 'gbd/home.html', {'form': form})

def home(request):
    if request.method == 'POST':
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')
        user = authenticate(username=ID, password=Pass)
        if user:
            if user.is_active:
                auth_login(request,user)
                return HttpResponseRedirect(reverse('sample'))
            else:
                return HttpResponse("your account is not active")
        else:
            return HttpResponse("ID or password is wrong")
    else:
        return render(request, 'gbd/home.html')


def sample(request):
    #obj = RHDT.objects.get(id=1)
    case=0
    if (request.method == 'POST'):
        friend = TIMEForm(request.POST, instance=obj)
        friend.save()
        case=1
    params = {
    #    "FN" : request.user.first_name,
    #    "LN" : request.user.last_name,
    #    "data1":TIMEForm(instance=obj),
        "case":case
    }
    return render(request, 'gbd/sample.html', params)

def GOAL(request):
    response='initial'
    object_list = User.objects.all()
    j=''
    for i in object_list:
        if i.username.startswith("contract"):
            j += i.first_name
            j += "##"
    j=j.split("##")
    del j[-1]      

    data = Foo.objects.all()

#    AA=GOAL22.objects.values_list('GOAL22A1').get(user=i.id)
#    foo_instance = Foo.objects.create(name='test')
    #task = get_object_or_404(GOAL22, user=i.id)

    if (request.method == 'POST'):
        if "DL" in request.POST:
            output = io.BytesIO()
            book = op.Workbook(output)
            book = xlsxwriter.Workbook(output)
            ws = book.add_worksheet('goalsetting')
            format = book.add_format({'border':1})
            format.set_text_wrap()         
            ws.write(1,1,'期初目標設定', format)
            book.close()
            output.seek(0)
            filename = 'goalsetting.xlsx'
            response = HttpResponse(output, content_type='aplication/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=%s' %filename
            return response
        elif "send" in request.POST:
            class SignUpForm(CreateView):
                form_class = SignUpForm
                success_url = reverse_lazy()
        elif "register" in request.POST:
            reg = FooForm(request.POST, request.FILES)

#            name = 'name' in request.POST
#            ctype = 'ctype' in request.POST
#            date1 = 'date1' in request.POST
#            date2 = 'date2' in request.POST
#            upload = 'upload' in request.POST

            #ctype = request.POST['ctype']
            #name = request.POST['name']
            #date1 = request.POST['date1']
            #date2 = request.POST['date2']
            #upload = request.POST['upload']
            #reg = Foo(name=name, ctype=ctype, date1=date1, date2=date2, upload=upload)

            #reg = FooForm(request.POST)
#            reg.save()
            if reg.is_valid():
                reg.save()
                response = "successfully uploaded"
                return redirect(to='/GOAL')
            else :
                response = "failed"

    params = {
        "UserID":request.user,
        "j":j,
        "data":data,
        'form':FooForm,
        'response':response,
        #"data1":GOAL22.objects.values_list('GOAL22A1','GOAL22B1','GOAL22C1','GOAL22D1','GOAL22E1','GOAL22F1','GOAL22G1').get(user=request.user),
        #"data2":GOAL22.objects.values_list('GOAL22AP','GOAL22BP','GOAL22CP','GOAL22DP','GOAL22EP','GOAL22FP','GOAL22GP').get(user=request.user),
        #"data3":GOAL22.objects.values_list('GOAL22A2','GOAL22B2','GOAL22C2','GOAL22D2','GOAL22E2','GOAL22F2','GOAL22G2').get(user=request.user),
        #"data4":GOAL22.objects.values_list('GOAL22A3','GOAL22B3','GOAL22C3','GOAL22D3','GOAL22E3','GOAL22F3','GOAL22G3').get(user=request.user),
        #"data5":GOAL22.objects.values_list('GOAL22AR','GOAL22BR','GOAL22CR','GOAL22DR','GOAL22ER','GOAL22FR','GOAL22GR').get(user=request.user),
        #"data6":GOAL22.objects.values_list('GOAL22AJ','GOAL22BJ','GOAL22CJ','GOAL22DJ','GOAL22EJ','GOAL22FJ','GOAL22GJ').get(user=request.user),
        #"FN":request.user.first_name,
        #"LN":request.user.last_name,
        #"AA":AA,
        }
    return render(request, 'gbd/GOAL.html', params)

def register(request):

    object_list = User.objects.all()
    j=int(0)
    k=request.user.password
    for i in object_list:
        j = j + 1
    m="contract"
    m+=str(j)
    if request.method == "POST":
        form = UserForm(request.POST or None)
#        form.password = str(k)
        if form.is_valid():
            form.save(pword=str(k))
            sample = GOAL22.objects.create(GOAL22A2 = "test")
            sample.save()
            return redirect('GOAL')
        else: 
            return HttpResponse('Invalid')
    else:
        defaultdata = {'username':m}#,'password1':str(k),'passoword2':str(k)}
        form = UserForm(defaultdata)
#        form.password = str(k)
        return render(request, "gbd/register.html",{'form':form,'j':j,'k':k})
    
#    return render(request, 'gbd/register.html',{'form':form,'j':j,'k':k})

def GOAL2(request, name):

    object_list = User.objects.all()
    for i in object_list:
        if i.username == name:
            ID = i.id
            FN = i.first_name
            LN = i.last_name
    
    AA1=GOAL22.objects.values_list('GOAL22Q1').get(user=ID)
    AA2=GOAL22.objects.values_list('GOAL22Q2').get(user=ID)
    AA3=GOAL22.objects.values_list('GOAL22Q3').get(user=ID)
    AA4=GOAL22.objects.values_list('GOAL22Q1A').get(user=ID)
    AA5=GOAL22.objects.values_list('GOAL22Q2A').get(user=ID)
    AA6=GOAL22.objects.values_list('GOAL22Q3A').get(user=ID)

    time=RHDT.objects.values_list('TIME').get(id=1)

    if time[0] == '期初目標設定':
        if int(AA1[0]) == 0:
            sbmt=0
        else:
            if int(AA4[0]) == 0:
                sbmt=1
            else:
                sbmt=2
    elif time[0] == '期中レビュー':
        if int(AA2[0]) == 0:
            sbmt=3
        else:
            if int(AA5[0]) == 0:
                sbmt=4 
            else:
                sbmt=5
    elif time[0] == '期末レビュー':
        if int(AA3[0]) == 0:
            sbmt=6
        else:
            if int(AA6[0]) == 0:
                sbmt=7
            else:
                sbmt=8

    task = get_object_or_404(GOAL22, user=ID)
    if (request.method == 'POST'):
        if "DL" in request.POST:
            output = io.BytesIO()
            book = op.Workbook(output)
            book = xlsxwriter.Workbook(output)
            ws = book.add_worksheet('goalsetting')
            format = book.add_format({'border':1})
            format.set_text_wrap()               
            ws.write(1,1,'期初目標設定', format)
            ws.write(1,2,'ウェイト%', format)
            ws.write(1,3,'期中レビュー', format)
            ws.write(1,4,'期末レビュー', format)
            ws.write(1,5,'評価点数', format)
            ws.write(1,6,'評定者コメント', format)
            ws.write(2,1,task.GOAL22A1, format)
            ws.write(2,2,task.GOAL22AP, format)
            ws.write(3,1,task.GOAL22B1, format)
            ws.write(3,2,task.GOAL22BP, format)
            ws.write(4,1,task.GOAL22C1, format)
            ws.write(4,2,task.GOAL22CP, format)
            ws.write(5,1,task.GOAL22D1, format)
            ws.write(5,2,task.GOAL22DP, format)
            ws.write(6,1,task.GOAL22E1, format)
            ws.write(6,2,task.GOAL22EP, format)
            ws.write(7,1,task.GOAL22F1, format)
            ws.write(7,2,task.GOAL22FP, format)
            ws.write(8,1,task.GOAL22G1, format)
            ws.write(8,2,task.GOAL22GP, format)
            ws.write(2,3,'', format)
            ws.write(2,4,'', format)
            ws.write(2,5,'', format)
            ws.write(2,6,'', format)
            ws.write(3,3,'', format)
            ws.write(3,4,'', format)
            ws.write(3,5,'', format)
            ws.write(3,6,'', format)
            ws.write(4,3,'', format)
            ws.write(4,4,'', format)
            ws.write(4,5,'', format)
            ws.write(4,6,'', format)
            ws.write(5,3,'', format)
            ws.write(5,4,'', format)
            ws.write(5,5,'', format)
            ws.write(5,6,'', format)
            ws.write(6,3,'', format)
            ws.write(6,4,'', format)
            ws.write(6,5,'', format)
            ws.write(6,6,'', format)
            ws.write(7,3,'', format)
            ws.write(7,4,'', format)
            ws.write(7,5,'', format)
            ws.write(7,6,'', format)
            ws.write(8,3,'', format)
            ws.write(8,4,'', format)
            ws.write(8,5,'', format)
            ws.write(8,6,'', format)
            if sbmt >= 3:
                ws.write(2,3,task.GOAL22A2, format)
                ws.write(3,3,task.GOAL22B2, format)
                ws.write(4,3,task.GOAL22C2, format)
                ws.write(5,3,task.GOAL22D2, format)
                ws.write(6,3,task.GOAL22E2, format)
                ws.write(7,3,task.GOAL22F2, format)
                ws.write(8,3,task.GOAL22G2, format)
            if sbmt >= 6:
                ws.write(2,4,task.GOAL22A3, format)
                ws.write(2,5,task.GOAL22AR, format)
                ws.write(2,6,task.GOAL22AJ, format)
                ws.write(3,4,task.GOAL22A3, format)
                ws.write(3,5,task.GOAL22AR, format)
                ws.write(3,6,task.GOAL22AJ, format)
                ws.write(4,4,task.GOAL22A3, format)
                ws.write(4,5,task.GOAL22AR, format)
                ws.write(4,6,task.GOAL22AJ, format)
                ws.write(5,4,task.GOAL22A3, format)
                ws.write(5,5,task.GOAL22AR, format)
                ws.write(5,6,task.GOAL22AJ, format)
                ws.write(6,4,task.GOAL22A3, format)
                ws.write(6,5,task.GOAL22AR, format)
                ws.write(6,6,task.GOAL22AJ, format)
                ws.write(7,4,task.GOAL22A3, format)
                ws.write(7,5,task.GOAL22AR, format)
                ws.write(7,6,task.GOAL22AJ, format)
                ws.write(8,4,task.GOAL22A3, format)
                ws.write(8,5,task.GOAL22AR, format)
                ws.write(8,6,task.GOAL22AJ, format)
            ws.set_column('B:B',33)
            ws.set_column('C:C',11)
            ws.set_column('D:E',33)
            ws.set_column('F:F',11)
            ws.set_column('G:G',33)
            ws.set_row(2,50)
            ws.set_row(3,50)
            ws.set_row(4,50)
            ws.set_row(5,50)
            ws.set_row(6,50)
            ws.set_row(7,50)
            ws.set_row(8,50)
            book.close()
            output.seek(0)
            filename = 'goalsetting.xlsx'
            response = HttpResponse(output, content_type='aplication/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=%s' %filename
            return response
        elif "send" in request.POST:
            if sbmt == 1:        
                task.GOAL22Q1A = 1
                sbmt = 2
                today = datetime.now()
                task.GOAL22Q1Y = today.year
                task.GOAL22Q1M = today.month
                task.GOAL22Q1D = today.day
            elif sbmt == 4:
                sbmt = 5
                task.GOAL22Q2A = 1
                today = datetime.now()
                task.GOAL22Q2Y = today.year
                task.GOAL22Q2M = today.month
                task.GOAL22Q2D = today.day
            elif sbmt == 7:        
                sbmt = 8
                task.GOAL22Q3A = 1
                today = datetime.now()
                task.GOAL22Q3Y = today.year
                task.GOAL22Q3M = today.month
                task.GOAL22Q3D = today.day
            task.save()
        elif "back" in request.POST:
            if sbmt == 1:
                sbmt = 0
                task.GOAL22Q1 = 0
            elif sbmt == 4:
                sbmt = 3
                task.GOAL22Q2 = 0
            elif sbmt == 7:
                sbmt = 6
                task.GOAL22Q3 = 0
            task.save()        

    params = {
        "data1":GOAL22.objects.values_list('GOAL22A1','GOAL22B1','GOAL22C1','GOAL22D1','GOAL22E1','GOAL22F1','GOAL22G1').get(user=ID),
        "data2":GOAL22.objects.values_list('GOAL22AP','GOAL22BP','GOAL22CP','GOAL22DP','GOAL22EP','GOAL22FP','GOAL22GP').get(user=ID),
        "data3":GOAL22.objects.values_list('GOAL22A2','GOAL22B2','GOAL22C2','GOAL22D2','GOAL22E2','GOAL22F2','GOAL22G2').get(user=ID),
        "data4":GOAL22.objects.values_list('GOAL22A3','GOAL22B3','GOAL22C3','GOAL22D3','GOAL22E3','GOAL22F3','GOAL22G3').get(user=ID),
        "data5":GOAL22.objects.values_list('GOAL22AR','GOAL22BR','GOAL22CR','GOAL22DR','GOAL22ER','GOAL22FR','GOAL22GR').get(user=ID),
        "data6":GOAL22.objects.values_list('GOAL22AJ','GOAL22BJ','GOAL22CJ','GOAL22DJ','GOAL22EJ','GOAL22FJ','GOAL22GJ').get(user=ID),
        "sbmt":sbmt,"EMP" : name,"FN" : FN,"LN" : LN,"FN2" : request.user.first_name,"LN2" : request.user.last_name,
        }
    return render(request, 'gbd/GOAL2.html', params)



def GOAL3(request):

    NM=''
    LL=''
    object_list = User.objects.all()
    for i in object_list:
        NM += i.first_name
        NM += i.last_name
        NM += '^'
        LL += i.username
        LL += '^'
    NM=NM.split('^')
    LL=LL.split('^')

    CA1=0
    CA2=0
    CA3=0
    CB1=0
    CB2=0
    CB3=0
    CC1=0
    CC2=0
    CC3=0
    CD1=0
    CD2=0
    CD3=0
    CE1=0
    CE2=0
    CE3=0

    AA1=0
    AA2=0
    AA3=0
    AB1=0
    AB2=0
    AB3=0
    AC1=0
    AC2=0
    AC3=0
    AD1=0
    AD2=0
    AD3=0
    AE1=0
    AE2=0
    AE3=0

    for i in range(5):
        AA=CPA22.objects.values_list('CPA22A1C').get(user=i+2)
        CA1+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22A2C').get(user=i+2)
        CA2+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22A3C').get(user=i+2)
        CA3+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22B1C').get(user=i+2)
        CB1+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22B2C').get(user=i+2)
        CB2+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22B3C').get(user=i+2)
        CB3+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22C1C').get(user=i+2)
        CC1+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22C2C').get(user=i+2)
        CC2+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22C3C').get(user=i+2)
        CC3+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22D1C').get(user=i+2)
        CD1+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22D2C').get(user=i+2)
        CD2+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22D3C').get(user=i+2)
        CD3+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22E1C').get(user=i+2)
        CE1+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22E2C').get(user=i+2)
        CE2+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22E3C').get(user=i+2)
        CE3+=int(AA[0])

        AA=CPA22.objects.values_list('CPA22A1A').get(user=i+2)
        AA1+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22A2A').get(user=i+2)
        AA2+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22A3A').get(user=i+2)
        AA3+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22B1A').get(user=i+2)
        AB1+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22B2A').get(user=i+2)
        AB2+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22B3A').get(user=i+2)
        AB3+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22C1A').get(user=i+2)
        AC1+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22C2A').get(user=i+2)
        AC2+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22C3A').get(user=i+2)
        AC3+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22D1A').get(user=i+2)
        AD1+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22D2A').get(user=i+2)
        AD2+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22D3A').get(user=i+2)
        AD3+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22E1A').get(user=i+2)
        AE1+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22E2A').get(user=i+2)
        AE2+=int(AA[0])
        AA=CPA22.objects.values_list('CPA22E3A').get(user=i+2)
        AE3+=int(AA[0])

    params = {
        "data1":NM,
        "data2":GOAL22.objects.values_list('GOAL22Q1Y','GOAL22Q1M','GOAL22Q1D','GOAL22Q2Y','GOAL22Q2M','GOAL22Q2D','GOAL22Q3Y','GOAL22Q3M','GOAL22Q3D').get(user=2),
        "data3":GOAL22.objects.values_list('GOAL22Q1Y','GOAL22Q1M','GOAL22Q1D','GOAL22Q2Y','GOAL22Q2M','GOAL22Q2D','GOAL22Q3Y','GOAL22Q3M','GOAL22Q3D').get(user=3),
        "data4":GOAL22.objects.values_list('GOAL22Q1Y','GOAL22Q1M','GOAL22Q1D','GOAL22Q2Y','GOAL22Q2M','GOAL22Q2D','GOAL22Q3Y','GOAL22Q3M','GOAL22Q3D').get(user=4),
        "data5":GOAL22.objects.values_list('GOAL22Q1Y','GOAL22Q1M','GOAL22Q1D','GOAL22Q2Y','GOAL22Q2M','GOAL22Q2D','GOAL22Q3Y','GOAL22Q3M','GOAL22Q3D').get(user=5),
        "data6":GOAL22.objects.values_list('GOAL22Q1Y','GOAL22Q1M','GOAL22Q1D','GOAL22Q2Y','GOAL22Q2M','GOAL22Q2D','GOAL22Q3Y','GOAL22Q3M','GOAL22Q3D').get(user=6),
        "data12":CPA22.objects.values_list('CPA22Y','CPA22M','CPA22D').get(user=2),
        "data13":CPA22.objects.values_list('CPA22Y','CPA22M','CPA22D').get(user=3),
        "data14":CPA22.objects.values_list('CPA22Y','CPA22M','CPA22D').get(user=4),
        "data15":CPA22.objects.values_list('CPA22Y','CPA22M','CPA22D').get(user=5),
        "data16":CPA22.objects.values_list('CPA22Y','CPA22M','CPA22D').get(user=6),
        "LL":LL,
        "B1":BB1,"B2":BB2,"B3":BB3,"B4":BB4,"B5":BB5,"B6":BB6,"B7":BB7,"B8":BB8,"B9":BB9,"B10":BB10,"B11":BB11,"B12":BB12,"B13":BB13,"B14":BB14,"B15":BB15,"B16":BB16,"B17":BB17,"B18":BB18,"B19":BB19,"B20":BB20,
        "CA1":CA1/5,"CA2":CA2/5,"CA3":CA3/5,"CB1":CB1/5,"CB2":CB2/5,"CB3":CB3/5,"CC1":CC1/5,"CC2":CC2/5,"CC3":CC3/5,"CD1":CD1/5,"CD2":CD2/5,"CD3":CD3/5,"CE1":CE1/5,"CE2":CE2/5,"CE3":CE3/5,
        "AA1":AA1/5,"AA2":AA2/5,"AA3":AA3/5,"AB1":AB1/5,"AB2":AB2/5,"AB3":AB3/5,"AC1":AC1/5,"AC2":AC2/5,"AC3":AC3/5,"AD1":AD1/5,"AD2":AD2/5,"AD3":AD3/5,"AE1":AE1/5,"AE2":AE2/5,"AE3":AE3/5,
        }
    return render(request, 'gbd/GOAL3.html', params)


def GOAL4(request, name):

    time=RHDT.objects.values_list('TIME').get(id=1)

    if time[0] == '期初目標設定':
        sbmt=0
    elif time[0] == '期中レビュー':
        sbmt=1
    elif time[0] == '期末レビュー':
        sbmt=2

    object_list = User.objects.all()
    for i in object_list:
        if i.username == name:
            ID = i.id
            FN = i.first_name
            LN = i.last_name    

    task = get_object_or_404(GOAL22, user=ID)
    if (request.method == 'POST'):
        if "DL" in request.POST:
            output = io.BytesIO()
            book = op.Workbook(output)
            book = xlsxwriter.Workbook(output)
            ws = book.add_worksheet('goalsetting')
            format = book.add_format({'border':1})
            format.set_text_wrap()               
            ws.write(1,1,'期初目標設定', format)
            ws.write(1,2,'ウェイト%', format)
            ws.write(1,3,'期中レビュー', format)
            ws.write(1,4,'期末レビュー', format)
            ws.write(1,5,'評価点数', format)
            ws.write(1,6,'評定者コメント', format)
            ws.write(2,1,task.GOAL22A1, format)
            ws.write(2,2,task.GOAL22AP, format)
            ws.write(3,1,task.GOAL22B1, format)
            ws.write(3,2,task.GOAL22BP, format)
            ws.write(4,1,task.GOAL22C1, format)
            ws.write(4,2,task.GOAL22CP, format)
            ws.write(5,1,task.GOAL22D1, format)
            ws.write(5,2,task.GOAL22DP, format)
            ws.write(6,1,task.GOAL22E1, format)
            ws.write(6,2,task.GOAL22EP, format)
            ws.write(7,1,task.GOAL22F1, format)
            ws.write(7,2,task.GOAL22FP, format)
            ws.write(8,1,task.GOAL22G1, format)
            ws.write(8,2,task.GOAL22GP, format)
            ws.write(2,3,'', format)
            ws.write(2,4,'', format)
            ws.write(2,5,'', format)
            ws.write(2,6,'', format)
            ws.write(3,3,'', format)
            ws.write(3,4,'', format)
            ws.write(3,5,'', format)
            ws.write(3,6,'', format)
            ws.write(4,3,'', format)
            ws.write(4,4,'', format)
            ws.write(4,5,'', format)
            ws.write(4,6,'', format)
            ws.write(5,3,'', format)
            ws.write(5,4,'', format)
            ws.write(5,5,'', format)
            ws.write(5,6,'', format)
            ws.write(6,3,'', format)
            ws.write(6,4,'', format)
            ws.write(6,5,'', format)
            ws.write(6,6,'', format)
            ws.write(7,3,'', format)
            ws.write(7,4,'', format)
            ws.write(7,5,'', format)
            ws.write(7,6,'', format)
            ws.write(8,3,'', format)
            ws.write(8,4,'', format)
            ws.write(8,5,'', format)
            ws.write(8,6,'', format)
            if sbmt >= 1:
                ws.write(2,3,task.GOAL22A2, format)
                ws.write(3,3,task.GOAL22B2, format)
                ws.write(4,3,task.GOAL22C2, format)
                ws.write(5,3,task.GOAL22D2, format)
                ws.write(6,3,task.GOAL22E2, format)
                ws.write(7,3,task.GOAL22F2, format)
                ws.write(8,3,task.GOAL22G2, format)
            if sbmt == 2:
                ws.write(2,4,task.GOAL22A3, format)
                ws.write(2,5,task.GOAL22AR, format)
                ws.write(2,6,task.GOAL22AJ, format)
                ws.write(3,4,task.GOAL22B3, format)
                ws.write(3,5,task.GOAL22BR, format)
                ws.write(3,6,task.GOAL22BJ, format)
                ws.write(4,4,task.GOAL22C3, format)
                ws.write(4,5,task.GOAL22CR, format)
                ws.write(4,6,task.GOAL22CJ, format)
                ws.write(5,4,task.GOAL22D3, format)
                ws.write(5,5,task.GOAL22DR, format)
                ws.write(5,6,task.GOAL22DJ, format)
                ws.write(6,4,task.GOAL22E3, format)
                ws.write(6,5,task.GOAL22ER, format)
                ws.write(6,6,task.GOAL22EJ, format)
                ws.write(7,4,task.GOAL22F3, format)
                ws.write(7,5,task.GOAL22FR, format)
                ws.write(7,6,task.GOAL22FJ, format)
                ws.write(8,4,task.GOAL22G3, format)
                ws.write(8,5,task.GOAL22GR, format)
                ws.write(8,6,task.GOAL22GJ, format)
            ws.set_column('B:B',33)
            ws.set_column('C:C',11)
            ws.set_column('D:E',33)
            ws.set_column('F:F',11)
            ws.set_column('G:G',33)
            ws.set_row(2,50)
            ws.set_row(3,50)
            ws.set_row(4,50)
            ws.set_row(5,50)
            ws.set_row(6,50)
            ws.set_row(7,50)
            ws.set_row(8,50)
            book.close()
            output.seek(0)
            filename = 'goalsetting.xlsx'
            response = HttpResponse(output, content_type='aplication/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=%s' %filename
            return response

    params = {
        "data1":GOAL22.objects.values_list('GOAL22A1','GOAL22B1','GOAL22C1','GOAL22D1','GOAL22E1','GOAL22F1','GOAL22G1').get(user=ID),
        "data2":GOAL22.objects.values_list('GOAL22AP','GOAL22BP','GOAL22CP','GOAL22DP','GOAL22EP','GOAL22FP','GOAL22GP').get(user=ID),
        "data3":GOAL22.objects.values_list('GOAL22A2','GOAL22B2','GOAL22C2','GOAL22D2','GOAL22E2','GOAL22F2','GOAL22G2').get(user=ID),
        "data4":GOAL22.objects.values_list('GOAL22A3','GOAL22B3','GOAL22C3','GOAL22D3','GOAL22E3','GOAL22F3','GOAL22G3').get(user=ID),
        "data5":GOAL22.objects.values_list('GOAL22AR','GOAL22BR','GOAL22CR','GOAL22DR','GOAL22ER','GOAL22FR','GOAL22GR').get(user=ID),
        "data6":GOAL22.objects.values_list('GOAL22AJ','GOAL22BJ','GOAL22CJ','GOAL22DJ','GOAL22EJ','GOAL22FJ','GOAL22GJ').get(user=ID),
        "EMP" : name,
        "FN" : FN,
        "LN" : LN,
        "FN2" : request.user.first_name,
        "LN2" : request.user.last_name,
        "sbmt":sbmt,
        }
    return render(request, 'gbd/GOAL4.html', params)



def CPA(request):

    AA=CPA22.objects.values_list('CPA22C').get(user=request.user)
    if int(AA[0]) == 0:
        sbmt=0
    else:
        sbmt=1
          
    task = get_object_or_404(CPA22, user=request.user)
    if (request.method == 'POST'):
        if "DL" in request.POST:
            output = io.BytesIO()
            book = op.Workbook(output)
            book = xlsxwriter.Workbook(output)
            ws = book.add_worksheet('competency')
            format = book.add_format({'border':1})
            format.set_text_wrap()          
            ws.merge_range('B3:B5',BB1, format)
            ws.write(2,2,BB2, format)
            ws.write(3,2,BB3, format)
            ws.write(4,2,BB4, format)
            ws.write(2,3,task.CPA22A1C, format)
            ws.write(3,3,task.CPA22A2C, format)
            ws.write(4,3,task.CPA22A3C, format)
            ws.write(2,4,task.CPA22A1A, format)
            ws.write(3,4,task.CPA22A2A, format)
            ws.write(4,4,task.CPA22A3A, format)
            ws.write(2,5,task.CPA22A1K, format)
            ws.write(3,5,task.CPA22A2K, format)
            ws.write(4,5,task.CPA22A3K, format)
            ws.write(2,6,task.CPA22A1P, format)
            ws.write(3,6,task.CPA22A2P, format)
            ws.write(4,6,task.CPA22A3P, format)
            ws.merge_range('B6:B8',BB5, format)
            ws.write(5,2,BB6, format)
            ws.write(6,2,BB7, format)
            ws.write(7,2,BB8, format)
            ws.write(5,3,task.CPA22B1C, format)
            ws.write(6,3,task.CPA22B2C, format)
            ws.write(7,3,task.CPA22B3C, format)
            ws.write(5,4,task.CPA22B1A, format)
            ws.write(6,4,task.CPA22B2A, format)
            ws.write(7,4,task.CPA22B3A, format)
            ws.write(5,5,task.CPA22B1K, format)
            ws.write(6,5,task.CPA22B2K, format)
            ws.write(7,5,task.CPA22B3K, format)
            ws.write(5,6,task.CPA22B1P, format)
            ws.write(6,6,task.CPA22B2P, format)
            ws.write(7,6,task.CPA22B3P, format)
            ws.merge_range('B9:B11',BB9, format)
            ws.write(8,2,BB10, format)
            ws.write(9,2,BB11, format)
            ws.write(10,2,BB12, format)
            ws.write(8,3,task.CPA22C1C, format)
            ws.write(9,3,task.CPA22C2C, format)
            ws.write(10,3,task.CPA22C3C, format)
            ws.write(8,4,task.CPA22C1A, format)
            ws.write(9,4,task.CPA22C2A, format)
            ws.write(10,4,task.CPA22C3A, format)
            ws.write(8,5,task.CPA22C1K, format)
            ws.write(9,5,task.CPA22C2K, format)
            ws.write(10,5,task.CPA22C3K, format)
            ws.write(8,6,task.CPA22C1P, format)
            ws.write(9,6,task.CPA22C2P, format)
            ws.write(10,6,task.CPA22C3P, format)
            ws.merge_range('B12:B14',BB13, format)
            ws.write(11,2,BB14, format)
            ws.write(12,2,BB15, format)
            ws.write(13,2,BB16, format)
            ws.write(11,3,task.CPA22D1C, format)
            ws.write(12,3,task.CPA22D2C, format)
            ws.write(13,3,task.CPA22D3C, format)
            ws.write(11,4,task.CPA22D1A, format)
            ws.write(12,4,task.CPA22D2A, format)
            ws.write(13,4,task.CPA22D3A, format)
            ws.write(11,5,task.CPA22D1K, format)
            ws.write(12,5,task.CPA22D2K, format)
            ws.write(13,5,task.CPA22D3K, format)
            ws.write(11,6,task.CPA22D1P, format)
            ws.write(12,6,task.CPA22D2P, format)
            ws.write(13,6,task.CPA22D3P, format)
            ws.merge_range('B15:B17',BB17, format)
            ws.write(14,2,BB18, format)
            ws.write(15,2,BB19, format)
            ws.write(16,2,BB20, format)
            ws.write(14,3,task.CPA22E1C, format)
            ws.write(15,3,task.CPA22E2C, format)
            ws.write(16,3,task.CPA22E3C, format)
            ws.write(14,4,task.CPA22E1A, format)
            ws.write(15,4,task.CPA22E2A, format)
            ws.write(16,4,task.CPA22E3A, format)
            ws.write(14,5,task.CPA22E1K, format)
            ws.write(15,5,task.CPA22E2K, format)
            ws.write(16,5,task.CPA22E3K, format)
            ws.write(14,6,task.CPA22E1P, format)
            ws.write(15,6,task.CPA22E2P, format)
            ws.write(16,6,task.CPA22E3P, format)
            ws.write(1,1,'コンピテンシー', format)
            ws.write(1,2,'コンピテンシー詳細', format)
            ws.write(1,3,'本人評価', format)
            ws.write(1,4,'評定者評価', format)
            ws.write(1,5,'考察', format)
            ws.write(1,6,'向上プラン', format)
            ws.set_column('B:B',17)
            ws.set_column('C:C',50)
            ws.set_column('D:E',14)
            ws.set_column('F:G',50)
            book.close()
            output.seek(0)
            filename = 'competence.xlsx'
            response = HttpResponse(output, content_type='aplication/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=%s' %filename
            return response
        elif "send" in request.POST:        
            sbmt = 1
            task.CPA22C = sbmt
            task.save()


    params = {
        "FN":request.user.first_name,
        "LN":request.user.last_name,
        "data1":CPA22.objects.values_list('CPA22A1C','CPA22A2C','CPA22A3C','CPA22B1C','CPA22B2C','CPA22B3C','CPA22C1C','CPA22C2C','CPA22C3C','CPA22D1C','CPA22D2C','CPA22D3C','CPA22E1C','CPA22E2C','CPA22E3C').get(user=request.user),
        "data2":CPA22.objects.values_list('CPA22A1A','CPA22A2A','CPA22A3A','CPA22B1A','CPA22B2A','CPA22B3A','CPA22C1A','CPA22C2A','CPA22C3A','CPA22D1A','CPA22D2A','CPA22D3A','CPA22E1A','CPA22E2A','CPA22E3A').get(user=request.user),
        "data3":CPA22.objects.values_list('CPA22A1K','CPA22A2K','CPA22A3K','CPA22B1K','CPA22B2K','CPA22B3K','CPA22C1K','CPA22C2K','CPA22C3K','CPA22D1K','CPA22D2K','CPA22D3K','CPA22E1K','CPA22E2K','CPA22E3K').get(user=request.user),
        "data4":CPA22.objects.values_list('CPA22A1P','CPA22A2P','CPA22A3P','CPA22B1P','CPA22B2P','CPA22B3P','CPA22C1P','CPA22C2P','CPA22C3P','CPA22D1P','CPA22D2P','CPA22D3P','CPA22E1P','CPA22E2P','CPA22E3P').get(user=request.user),
        "B1":BB1,"B2":BB2,"B3":BB3,"B4":BB4,"B5":BB5,"B6":BB6,"B7":BB7,"B8":BB8,"B9":BB9,"B10":BB10,"B11":BB11,"B12":BB12,"B13":BB13,"B14":BB14,"B15":BB15,"B16":BB16,"B17":BB17,"B18":BB18,"B19":BB19,"B20":BB20,
        "sbmt":sbmt,
    }
    return render(request, 'gbd/CPA.html', params)


def CPA2(request,name):

    object_list = User.objects.all()
    for i in object_list:
        if i.username == name:
            ID = i.id
            FN = i.first_name
            LN = i.last_name
    
    AA=CPA22.objects.values_list('CPA22C').get(user=ID)
    CC=CPA22.objects.values_list('CPA22A').get(user=ID)
    if int(AA[0]) == 0:
        sbmt=0
    else:
        if int(CC[0]) == 0:
            sbmt = 1
        else:
            sbmt = 2
          
    task = get_object_or_404(CPA22, user=ID)
    if (request.method == 'POST'):
        if "DL" in request.POST:
            output = io.BytesIO()
            book = op.Workbook(output)
            book = xlsxwriter.Workbook(output)
            ws = book.add_worksheet('competency')
            format = book.add_format({'border':1})
            format.set_text_wrap()          
            ws.merge_range('B3:B5',BB1, format)
            ws.write(2,2,BB2, format)
            ws.write(3,2,BB3, format)
            ws.write(4,2,BB4, format)
            ws.write(2,3,task.CPA22A1C, format)
            ws.write(3,3,task.CPA22A2C, format)
            ws.write(4,3,task.CPA22A3C, format)
            ws.write(2,4,task.CPA22A1A, format)
            ws.write(3,4,task.CPA22A2A, format)
            ws.write(4,4,task.CPA22A3A, format)
            ws.write(2,5,task.CPA22A1K, format)
            ws.write(3,5,task.CPA22A2K, format)
            ws.write(4,5,task.CPA22A3K, format)
            ws.write(2,6,task.CPA22A1P, format)
            ws.write(3,6,task.CPA22A2P, format)
            ws.write(4,6,task.CPA22A3P, format)
            ws.merge_range('B6:B8',BB5, format)
            ws.write(5,2,BB6, format)
            ws.write(6,2,BB7, format)
            ws.write(7,2,BB8, format)
            ws.write(5,3,task.CPA22B1C, format)
            ws.write(6,3,task.CPA22B2C, format)
            ws.write(7,3,task.CPA22B3C, format)
            ws.write(5,4,task.CPA22B1A, format)
            ws.write(6,4,task.CPA22B2A, format)
            ws.write(7,4,task.CPA22B3A, format)
            ws.write(5,5,task.CPA22B1K, format)
            ws.write(6,5,task.CPA22B2K, format)
            ws.write(7,5,task.CPA22B3K, format)
            ws.write(5,6,task.CPA22B1P, format)
            ws.write(6,6,task.CPA22B2P, format)
            ws.write(7,6,task.CPA22B3P, format)
            ws.merge_range('B9:B11',BB9, format)
            ws.write(8,2,BB10, format)
            ws.write(9,2,BB11, format)
            ws.write(10,2,BB12, format)
            ws.write(8,3,task.CPA22C1C, format)
            ws.write(9,3,task.CPA22C2C, format)
            ws.write(10,3,task.CPA22C3C, format)
            ws.write(8,4,task.CPA22C1A, format)
            ws.write(9,4,task.CPA22C2A, format)
            ws.write(10,4,task.CPA22C3A, format)
            ws.write(8,5,task.CPA22C1K, format)
            ws.write(9,5,task.CPA22C2K, format)
            ws.write(10,5,task.CPA22C3K, format)
            ws.write(8,6,task.CPA22C1P, format)
            ws.write(9,6,task.CPA22C2P, format)
            ws.write(10,6,task.CPA22C3P, format)
            ws.merge_range('B12:B14',BB13, format)
            ws.write(11,2,BB14, format)
            ws.write(12,2,BB15, format)
            ws.write(13,2,BB16, format)
            ws.write(11,3,task.CPA22D1C, format)
            ws.write(12,3,task.CPA22D2C, format)
            ws.write(13,3,task.CPA22D3C, format)
            ws.write(11,4,task.CPA22D1A, format)
            ws.write(12,4,task.CPA22D2A, format)
            ws.write(13,4,task.CPA22D3A, format)
            ws.write(11,5,task.CPA22D1K, format)
            ws.write(12,5,task.CPA22D2K, format)
            ws.write(13,5,task.CPA22D3K, format)
            ws.write(11,6,task.CPA22D1P, format)
            ws.write(12,6,task.CPA22D2P, format)
            ws.write(13,6,task.CPA22D3P, format)
            ws.merge_range('B15:B17',BB17, format)
            ws.write(14,2,BB18, format)
            ws.write(15,2,BB19, format)
            ws.write(16,2,BB20, format)
            ws.write(14,3,task.CPA22E1C, format)
            ws.write(15,3,task.CPA22E2C, format)
            ws.write(16,3,task.CPA22E3C, format)
            ws.write(14,4,task.CPA22E1A, format)
            ws.write(15,4,task.CPA22E2A, format)
            ws.write(16,4,task.CPA22E3A, format)
            ws.write(14,5,task.CPA22E1K, format)
            ws.write(15,5,task.CPA22E2K, format)
            ws.write(16,5,task.CPA22E3K, format)
            ws.write(14,6,task.CPA22E1P, format)
            ws.write(15,6,task.CPA22E2P, format)
            ws.write(16,6,task.CPA22E3P, format)
            ws.write(1,1,'コンピテンシー', format)
            ws.write(1,2,'コンピテンシー詳細', format)
            ws.write(1,3,'本人評価', format)
            ws.write(1,4,'評定者評価', format)
            ws.write(1,5,'考察', format)
            ws.write(1,6,'向上プラン', format)
            ws.set_column('B:B',17)
            ws.set_column('C:C',50)
            ws.set_column('D:E',14)
            ws.set_column('F:G',50)
            book.close()
            output.seek(0)
            filename = 'competence.xlsx'
            response = HttpResponse(output, content_type='aplication/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=%s' %filename
            return response
        elif "back" in request.POST:        
            sbmt = 0
            task.CPA22C = sbmt
            task.save()
        elif "send" in request.POST:        
            sbmt = 2
            task.CPA22A = 1
            today = datetime.now()
            task.CPA22Y = today.year
            task.CPA22M = today.month
            task.CPA22D = today.day
            task.save()

    params = {
        "data1":CPA22.objects.values_list('CPA22A1C','CPA22A2C','CPA22A3C','CPA22B1C','CPA22B2C','CPA22B3C','CPA22C1C','CPA22C2C','CPA22C3C','CPA22D1C','CPA22D2C','CPA22D3C','CPA22E1C','CPA22E2C','CPA22E3C').get(user=ID),
        "data2":CPA22.objects.values_list('CPA22A1A','CPA22A2A','CPA22A3A','CPA22B1A','CPA22B2A','CPA22B3A','CPA22C1A','CPA22C2A','CPA22C3A','CPA22D1A','CPA22D2A','CPA22D3A','CPA22E1A','CPA22E2A','CPA22E3A').get(user=ID),
        "data3":CPA22.objects.values_list('CPA22A1K','CPA22A2K','CPA22A3K','CPA22B1K','CPA22B2K','CPA22B3K','CPA22C1K','CPA22C2K','CPA22C3K','CPA22D1K','CPA22D2K','CPA22D3K','CPA22E1K','CPA22E2K','CPA22E3K').get(user=ID),
        "data4":CPA22.objects.values_list('CPA22A1P','CPA22A2P','CPA22A3P','CPA22B1P','CPA22B2P','CPA22B3P','CPA22C1P','CPA22C2P','CPA22C3P','CPA22D1P','CPA22D2P','CPA22D3P','CPA22E1P','CPA22E2P','CPA22E3P').get(user=ID),
        "B1":BB1,"B2":BB2,"B3":BB3,"B4":BB4,"B5":BB5,"B6":BB6,"B7":BB7,"B8":BB8,"B9":BB9,"B10":BB10,"B11":BB11,"B12":BB12,"B13":BB13,"B14":BB14,"B15":BB15,"B16":BB16,"B17":BB17,"B18":BB18,"B19":BB19,"B20":BB20,
        "sbmt":sbmt,
        "EMP" : name,
        "FN" : FN,
        "LN" : LN,
        "FN2" : request.user.first_name,
        "LN2" : request.user.last_name,
    }
    return render(request, 'gbd/CPA2.html', params)




def CPA3(request,name):

    object_list = User.objects.all()
    for i in object_list:
        if i.username == name:
            ID = i.id
            FN = i.first_name
            LN = i.last_name   
         
    task = get_object_or_404(CPA22, user=ID)
    if (request.method == 'POST'):
        if "DL" in request.POST:
            output = io.BytesIO()
            book = op.Workbook(output)
            book = xlsxwriter.Workbook(output)
            ws = book.add_worksheet('competency')
            format = book.add_format({'border':1})
            format.set_text_wrap()          
            ws.merge_range('B3:B5',BB1, format)
            ws.write(2,2,BB2, format)
            ws.write(3,2,BB3, format)
            ws.write(4,2,BB4, format)
            ws.write(2,3,task.CPA22A1C, format)
            ws.write(3,3,task.CPA22A2C, format)
            ws.write(4,3,task.CPA22A3C, format)
            ws.write(2,4,task.CPA22A1A, format)
            ws.write(3,4,task.CPA22A2A, format)
            ws.write(4,4,task.CPA22A3A, format)
            ws.write(2,5,task.CPA22A1K, format)
            ws.write(3,5,task.CPA22A2K, format)
            ws.write(4,5,task.CPA22A3K, format)
            ws.write(2,6,task.CPA22A1P, format)
            ws.write(3,6,task.CPA22A2P, format)
            ws.write(4,6,task.CPA22A3P, format)
            ws.merge_range('B6:B8',BB5, format)
            ws.write(5,2,BB6, format)
            ws.write(6,2,BB7, format)
            ws.write(7,2,BB8, format)
            ws.write(5,3,task.CPA22B1C, format)
            ws.write(6,3,task.CPA22B2C, format)
            ws.write(7,3,task.CPA22B3C, format)
            ws.write(5,4,task.CPA22B1A, format)
            ws.write(6,4,task.CPA22B2A, format)
            ws.write(7,4,task.CPA22B3A, format)
            ws.write(5,5,task.CPA22B1K, format)
            ws.write(6,5,task.CPA22B2K, format)
            ws.write(7,5,task.CPA22B3K, format)
            ws.write(5,6,task.CPA22B1P, format)
            ws.write(6,6,task.CPA22B2P, format)
            ws.write(7,6,task.CPA22B3P, format)
            ws.merge_range('B9:B11',BB9, format)
            ws.write(8,2,BB10, format)
            ws.write(9,2,BB11, format)
            ws.write(10,2,BB12, format)
            ws.write(8,3,task.CPA22C1C, format)
            ws.write(9,3,task.CPA22C2C, format)
            ws.write(10,3,task.CPA22C3C, format)
            ws.write(8,4,task.CPA22C1A, format)
            ws.write(9,4,task.CPA22C2A, format)
            ws.write(10,4,task.CPA22C3A, format)
            ws.write(8,5,task.CPA22C1K, format)
            ws.write(9,5,task.CPA22C2K, format)
            ws.write(10,5,task.CPA22C3K, format)
            ws.write(8,6,task.CPA22C1P, format)
            ws.write(9,6,task.CPA22C2P, format)
            ws.write(10,6,task.CPA22C3P, format)
            ws.merge_range('B12:B14',BB13, format)
            ws.write(11,2,BB14, format)
            ws.write(12,2,BB15, format)
            ws.write(13,2,BB16, format)
            ws.write(11,3,task.CPA22D1C, format)
            ws.write(12,3,task.CPA22D2C, format)
            ws.write(13,3,task.CPA22D3C, format)
            ws.write(11,4,task.CPA22D1A, format)
            ws.write(12,4,task.CPA22D2A, format)
            ws.write(13,4,task.CPA22D3A, format)
            ws.write(11,5,task.CPA22D1K, format)
            ws.write(12,5,task.CPA22D2K, format)
            ws.write(13,5,task.CPA22D3K, format)
            ws.write(11,6,task.CPA22D1P, format)
            ws.write(12,6,task.CPA22D2P, format)
            ws.write(13,6,task.CPA22D3P, format)
            ws.merge_range('B15:B17',BB17, format)
            ws.write(14,2,BB18, format)
            ws.write(15,2,BB19, format)
            ws.write(16,2,BB20, format)
            ws.write(14,3,task.CPA22E1C, format)
            ws.write(15,3,task.CPA22E2C, format)
            ws.write(16,3,task.CPA22E3C, format)
            ws.write(14,4,task.CPA22E1A, format)
            ws.write(15,4,task.CPA22E2A, format)
            ws.write(16,4,task.CPA22E3A, format)
            ws.write(14,5,task.CPA22E1K, format)
            ws.write(15,5,task.CPA22E2K, format)
            ws.write(16,5,task.CPA22E3K, format)
            ws.write(14,6,task.CPA22E1P, format)
            ws.write(15,6,task.CPA22E2P, format)
            ws.write(16,6,task.CPA22E3P, format)
            ws.write(1,1,'コンピテンシー', format)
            ws.write(1,2,'コンピテンシー詳細', format)
            ws.write(1,3,'本人評価', format)
            ws.write(1,4,'評定者評価', format)
            ws.write(1,5,'考察', format)
            ws.write(1,6,'向上プラン', format)
            ws.set_column('B:B',17)
            ws.set_column('C:C',50)
            ws.set_column('D:E',14)
            ws.set_column('F:G',50)
            book.close()
            output.seek(0)
            filename = 'competence.xlsx'
            response = HttpResponse(output, content_type='aplication/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=%s' %filename
            return response

    params = {
        "data1":CPA22.objects.values_list('CPA22A1C','CPA22A2C','CPA22A3C','CPA22B1C','CPA22B2C','CPA22B3C','CPA22C1C','CPA22C2C','CPA22C3C','CPA22D1C','CPA22D2C','CPA22D3C','CPA22E1C','CPA22E2C','CPA22E3C').get(user=ID),
        "data2":CPA22.objects.values_list('CPA22A1A','CPA22A2A','CPA22A3A','CPA22B1A','CPA22B2A','CPA22B3A','CPA22C1A','CPA22C2A','CPA22C3A','CPA22D1A','CPA22D2A','CPA22D3A','CPA22E1A','CPA22E2A','CPA22E3A').get(user=ID),
        "data3":CPA22.objects.values_list('CPA22A1K','CPA22A2K','CPA22A3K','CPA22B1K','CPA22B2K','CPA22B3K','CPA22C1K','CPA22C2K','CPA22C3K','CPA22D1K','CPA22D2K','CPA22D3K','CPA22E1K','CPA22E2K','CPA22E3K').get(user=ID),
        "data4":CPA22.objects.values_list('CPA22A1P','CPA22A2P','CPA22A3P','CPA22B1P','CPA22B2P','CPA22B3P','CPA22C1P','CPA22C2P','CPA22C3P','CPA22D1P','CPA22D2P','CPA22D3P','CPA22E1P','CPA22E2P','CPA22E3P').get(user=ID),
        "B1":BB1,"B2":BB2,"B3":BB3,"B4":BB4,"B5":BB5,"B6":BB6,"B7":BB7,"B8":BB8,"B9":BB9,"B10":BB10,"B11":BB11,"B12":BB12,"B13":BB13,"B14":BB14,"B15":BB15,"B16":BB16,"B17":BB17,"B18":BB18,"B19":BB19,"B20":BB20,
        "EMP" : name,
        "FN" : FN,
        "LN" : LN,
        "FN2" : request.user.first_name,
        "LN2" : request.user.last_name,
    }
    return render(request, 'gbd/CPA3.html', params)


def edit(request, num):
    
    time=RHDT.objects.values_list('TIME').get(id=1)

    if time[0] == '期初目標設定':
        obj = GOAL22.objects.get(user=request.user)
        sbmt=0
        params = {
            "UserID":request.user,
            "data1":GOAL22Q1Form(instance=obj),
            "data2":GOAL22.objects.values_list('GOAL22A1','GOAL22B1','GOAL22C1','GOAL22D1','GOAL22E1','GOAL22F1','GOAL22G1').get(user=request.user),
            "data3":GOAL22.objects.values_list('GOAL22AP','GOAL22BP','GOAL22CP','GOAL22DP','GOAL22EP','GOAL22FP','GOAL22GP').get(user=request.user),
            "data4":GOAL22.objects.values_list('GOAL22A2','GOAL22B2','GOAL22C2','GOAL22D2','GOAL22E2','GOAL22F2','GOAL22G2').get(user=request.user),
            "FN":request.user.first_name,"LN":request.user.last_name,"sbmt":sbmt,
            }

        if (request.method == 'POST'):
            friend = GOAL22Q1Form(request.POST, instance=obj)
            friend.save()
            return redirect(to='/GOAL')

    elif time[0] == '期中レビュー':
        obj = GOAL22.objects.get(user=request.user)
        sbmt=1
        params = {
            "UserID":request.user,
            "data1":GOAL22Q2Form(instance=obj),
            "data2":GOAL22.objects.values_list('GOAL22A1','GOAL22B1','GOAL22C1','GOAL22D1','GOAL22E1','GOAL22F1','GOAL22G1').get(user=request.user),
            "data3":GOAL22.objects.values_list('GOAL22AP','GOAL22BP','GOAL22CP','GOAL22DP','GOAL22EP','GOAL22FP','GOAL22GP').get(user=request.user),
            "data4":GOAL22.objects.values_list('GOAL22A2','GOAL22B2','GOAL22C2','GOAL22D2','GOAL22E2','GOAL22F2','GOAL22G2').get(user=request.user),
            "FN":request.user.first_name,"LN":request.user.last_name,"sbmt":sbmt,
            }

        if (request.method == 'POST'):
            friend = GOAL22Q2Form(request.POST, instance=obj)
            friend.save()
            return redirect(to='/GOAL')

    elif time[0] == '期末レビュー':
        obj = GOAL22.objects.get(user=request.user)
        sbmt=2

        params = {
            "UserID":request.user,
            "data1":GOAL22Q3Form(instance=obj),
            "data2":GOAL22.objects.values_list('GOAL22A1','GOAL22B1','GOAL22C1','GOAL22D1','GOAL22E1','GOAL22F1','GOAL22G1').get(user=request.user),
            "data3":GOAL22.objects.values_list('GOAL22AP','GOAL22BP','GOAL22CP','GOAL22DP','GOAL22EP','GOAL22FP','GOAL22GP').get(user=request.user),
            "data4":GOAL22.objects.values_list('GOAL22A2','GOAL22B2','GOAL22C2','GOAL22D2','GOAL22E2','GOAL22F2','GOAL22G2').get(user=request.user),
            "FN":request.user.first_name,"LN":request.user.last_name,"sbmt":sbmt,
            }

        if (request.method == 'POST'):
            friend = GOAL22Q3Form(request.POST, instance=obj)
            friend.save()
            return redirect(to='/GOAL')

    return render(request, 'gbd/edit.html', params)



def edit2(request, name):

    object_list = User.objects.all()
    for i in object_list:
        if i.username == name:
            ID = i.id
            FN = i.first_name
            LN = i.last_name
    
    obj = GOAL22.objects.get(user=ID)

    params = {
        "data1":GOAL22Q3AForm(instance=obj),
        "data2":GOAL22.objects.values_list('GOAL22A1','GOAL22B1','GOAL22C1','GOAL22D1','GOAL22E1','GOAL22F1','GOAL22G1').get(user=ID),
        "data3":GOAL22.objects.values_list('GOAL22AP','GOAL22BP','GOAL22CP','GOAL22DP','GOAL22EP','GOAL22FP','GOAL22GP').get(user=ID),
        "data4":GOAL22.objects.values_list('GOAL22A2','GOAL22B2','GOAL22C2','GOAL22D2','GOAL22E2','GOAL22F2','GOAL22G2').get(user=ID),
        "data5":GOAL22.objects.values_list('GOAL22A3','GOAL22B3','GOAL22C3','GOAL22D3','GOAL22E3','GOAL22F3','GOAL22G3').get(user=ID),
        "FN":FN,"LN":LN,"EMP":name,
        }

    if (request.method == 'POST'):
        friend = GOAL22Q3AForm(request.POST, instance=obj)
        friend.save()
        return redirect('GOAL2', name=name)

    return render(request, 'gbd/edit2.html', params)


def editCPA(request, num):
    obj = CPA22.objects.get(user=request.user)
    if (request.method == 'POST'):
        friend = CPA22CForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/CPA')

    params = {
        "FN":request.user.first_name,"LN":request.user.last_name,
        "data1":CPA22CForm(instance=obj),
        "data2":CPA22.objects.values_list('CPA22A1A','CPA22A2A','CPA22A3A','CPA22B1A','CPA22B2A','CPA22B3A','CPA22C1A','CPA22C2A','CPA22C3A','CPA22D1A','CPA22D2A','CPA22D3A','CPA22E1A','CPA22E2A','CPA22E3A').get(user=request.user),
        "B1":BB1,"B2":BB2,"B3":BB3,"B4":BB4,"B5":BB5,"B6":BB6,"B7":BB7,"B8":BB8,"B9":BB9,"B10":BB10,"B11":BB11,"B12":BB12,"B13":BB13,"B14":BB14,"B15":BB15,"B16":BB16,"B17":BB17,"B18":BB18,"B19":BB19,"B20":BB20,
        }
    return render(request, 'gbd/editCPA.html', params)

def editCPA2(request,name):

    object_list = User.objects.all()
    for i in object_list:
        if i.username == name:
            ID = i.id
            FN = i.first_name
            LN = i.last_name

    obj = CPA22.objects.get(user=ID)    
    if (request.method == 'POST'):
        friend = CPA22AForm(request.POST, instance=obj)
        friend.save()
        return redirect('CPA2', name=name)

    params = {
        "data1":CPA22.objects.values_list('CPA22A1C','CPA22A2C','CPA22A3C','CPA22B1C','CPA22B2C','CPA22B3C','CPA22C1C','CPA22C2C','CPA22C3C','CPA22D1C','CPA22D2C','CPA22D3C','CPA22E1C','CPA22E2C','CPA22E3C').get(user=ID),
        "data2":CPA22AForm(instance=obj),
        "data3":CPA22.objects.values_list('CPA22A1K','CPA22A2K','CPA22A3K','CPA22B1K','CPA22B2K','CPA22B3K','CPA22C1K','CPA22C2K','CPA22C3K','CPA22D1K','CPA22D2K','CPA22D3K','CPA22E1K','CPA22E2K','CPA22E3K').get(user=ID),
        "data4":CPA22.objects.values_list('CPA22A1P','CPA22A2P','CPA22A3P','CPA22B1P','CPA22B2P','CPA22B3P','CPA22C1P','CPA22C2P','CPA22C3P','CPA22D1P','CPA22D2P','CPA22D3P','CPA22E1P','CPA22E2P','CPA22E3P').get(user=ID),
        "B1":BB1,"B2":BB2,"B3":BB3,"B4":BB4,"B5":BB5,"B6":BB6,"B7":BB7,"B8":BB8,"B9":BB9,"B10":BB10,"B11":BB11,"B12":BB12,"B13":BB13,"B14":BB14,"B15":BB15,"B16":BB16,"B17":BB17,"B18":BB18,"B19":BB19,"B20":BB20,
        "EMP" : name,"FN" : FN,"LN" : LN,"FN2" : request.user.first_name,"LN2" : request.user.last_name,
    }
    return render(request, 'gbd/editCPA2.html', params)


def homeA(request):
    object_list = User.objects.all()
    params = {
        "data" : object_list,
        "ID" : request.user.id
        }
    return render(request, 'gbd/homeA.html', params)

def homeB(request):
    object_list = User.objects.all()
    params = {
        "data" : object_list,
        "ID" : request.user.id
        }
    return render(request, 'gbd/homeB.html', params)

def test(request):
    if (request.method == "POST"):
        subject = "test"
        message = "test mail"
        from_email = "sistema.rh@cosmotec.com.br"
        recipient_list = ["hyuma17@yahoo.co.jp"]
        send_mail(subject, message, from_email, recipient_list)
    params = {
        "ID" : request.user.id
    }
    return render(request, 'gbd/test.html', params)

