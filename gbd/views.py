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
from .models import GOAL22,CPA22,RHDT,Foo,MM,senha
from .forms import GOAL22Q1Form,GOAL22Q2Form,GOAL22Q3Form,GOAL22Q3AForm,CPA22CForm,CPA22AForm,TIMEForm,UserForm,UserForm2,FooForm,MMForm,senhaForm
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
#from django.conf import settings


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
    object_list = User.objects.all()
    case=0
    if (request.method == 'POST'):
        friend = TIMEForm(request.POST, instance=obj)
        friend.save()
        case=1
    params = {
    #    "FN" : request.user.first_name,
    #    "LN" : request.user.last_name,
    #    "data1":TIMEForm(instance=obj),
        "case":case,
        "object_list":object_list,
        "UserID":request.user,
        }
    return render(request, 'gbd/sample.html', params)

def GOAL(request):
    response='please input contract information and click upload'
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
                response = "successfully uploaded!!"
#                return redirect(to='/GOAL')

            else :
                response = "failed"

    params = {
        "UserID":request.user,
        "j":j,
        "data":data,
        'form':FooForm,
        'response':response,
        }
    return render(request, 'gbd/GOAL.html', params)


def CPA(request):

    response='please input meeting detail and click upload button'
    data = MM.objects.all()
    AA1=MM.objects.all().values()
    #AA2=MM.objects.values_list('name').get(pk=10)

    if (request.method == 'POST'):
        if "register" in request.POST:
            reg = MMForm(request.POST, request.FILES)
            if reg.is_valid():
                reg.save()
                response = "successfully uploaded!!"
            else :
                response = "failed"
    params = {
        "UserID":request.user,
        "data":data,'form':MMForm,'response':response,'file':"file",
        'AA1':AA1,#'AA2':AA2,'AA3':AA3,'AA4':AA4,'AA5':AA5,'AA6':AA6,
        }
    return render(request, 'gbd/CPA.html', params)

#def register2(CreateView):
#    model = User
#    form_class = UserCreationForm
#    success_url = reverse_lazy('sample')

#    def get_success_url(self):
#        return reverse('sample')

def register(request):

    text = "please input new person's informaion and click register"
    object_list = User.objects.all()
    if request.method == "POST":
        BB = request.POST.get('password2')
#        defaultdata = {'first_name':str(text)}#,'password1':str(k),'passoword2':str(k)}
#        form = UserForm(defaultdata)
        form = UserForm(request.POST or None)
#        form = UserForm(defaultdata, request.POST or None)
#        form.password = str(k)
        if form.is_valid():
#            form.first_name=str(text)
#            form.save(first_name=str(text))
#            form.save(pword=str(k))
#            sample = GOAL22.objects.create(GOAL22A2 = "test")
#            sample.save()
            form.save()
            AA = User.objects.values_list("id", flat=True).order_by("-id")
            AA = AA[0]
            text = int(AA)
            changeFN = User.objects.get(id=text)
            changeFN.first_name=BB
            changeFN.save()
            text = "successfully created the new account !!"
        else: 
            return HttpResponse('Invalid')
    else:
#        defaultdata = {'username':m}#,'password1':str(k),'passoword2':str(k)}
#        form = UserForm(defaultdata)
        form = UserForm()
#        form.password = str(k)
    return render(request, "gbd/register.html",{'form':form,"text":text,"object_list":object_list})#,'j':j,'k':k})
    
#    return render(request, 'gbd/register.html',{'form':form,'j':j,'k':k})

def GOAL2(request):

    text = 'please select the user to be eliminated and click delete'
    if (request.method == 'POST'):
        num = request.POST.dict()
        num = num.popitem()
        num = num[0]
        num = int(num)
        eliminate = User.objects.get(id=num)
        eliminate.delete()
        text = "successfully eliminated the user"
    else:  
        AA=1

    object_list = User.objects.all() 
    params = {"object_list":object_list,"text":text}
    return render(request, 'gbd/GOAL2.html', params)

def GOAL3(request):

    text = 'please select contract to be eliminated and click delete'
    if (request.method == 'POST'):
        num = request.POST.dict()
        num = num.popitem()
        num = num[0]
        num = int(num)
        eliminate = Foo.objects.get(id=num)
        eliminate.delete()
        text = "successfully eliminated the contract"
    else:  
        AA=1

    object_list = Foo.objects.all() 
    params = {"object_list":object_list,"text":text}
    return render(request, 'gbd/GOAL3.html', params)


def CPA2(request):

    text = 'please select meeting minutes to be eliminated and click delete'
    if (request.method == 'POST'):
        num = request.POST.dict()
        num = num.popitem()
        num = num[0]
        num = int(num)
        eliminate = MM.objects.get(id=num)
        eliminate.delete()
        text = "successfully eliminated the meeting minutes"
    else:  
        AA=1

    object_list = MM.objects.all() 
    params = {"object_list":object_list,"text":text}
    return render(request, 'gbd/CPA2.html', params)

def test(request):

    text=''
    object_list = User.objects.all() 
    data='nothing'
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER,'upU.txt')
    f = open(my_file,'r', encoding='UTF-8')
    data = f.read()
    data = data.replace('\n','^')
    data = data.split('^')
    BB = len(data)
    CC = int(BB)/2
    CC = int(CC)
    if request.method == 'POST':
        for i in range(CC) :
            AA = User()
            AA.username = data[2*i]
            AA.password = data[2*i+1]
            AA.first_name = data[2*i+1]
            AA.save()
            AA.set_password(str(data[2*i+1]))
            AA.save()
            text = "successfully recovered the accounts !!"
    else:
        text = 'test'
    return render(request, "gbd/test.html",{"text":data,"object_list":object_list})#,"AA1":AA1,"AA2":AA2,"AA3":AA3,})#,'j':j,'k':k})


def edit2(request, num):

    num=int(num)
    obj = MM.objects.get(id=num)
    params = {"EMP":num,"obj":obj}
    return render(request, 'gbd/edit2.html', params)

def GOAL4(request):

    obj=Foo.objects.all()

    text=''
    data='nothing'
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER,'upC.txt')
    f = open(my_file,'r', encoding='UTF-8')
    data = f.read()
    data = data.replace('\n','^')
    data = data.split('^')
    BB = len(data)
    CC = int(BB)/5
    CC = int(CC)
    if request.method == 'POST':
        for i in range(CC) :
            AA = Foo()
            AA.name = data[5*i]
            AA.ctype = data[5*i+1]
            AA.date1 = data[5*i+2]
            AA.date2 = data[5*i+3]
            j=str(data[5*i+4])
            j=j.replace("_","")
            AA.upload = j
#            AA.upload = data[5*i+4]
#            dscr = str(data[5*i+4])
#            my_file2 = os.path.join(THIS_FOLDER,dscr)
#            AA.upload = my_file2
            AA.save()
            text = "successfully recovered the accounts !!"
    else:
        text = 'test'
    params = {"obj":obj,"data":data,"CC":CC}
    return render(request, 'gbd/GOAL4.html', params)

def CPA3(request):

    obj=MM.objects.all()

    text=''
    data='nothing'
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER,'upM.txt')
    f = open(my_file,'r', encoding='UTF-8')
    data = f.read()
    data = data.replace(' ## ','##')
    data = data.replace(' ##','^')
    data = data.replace('##','^')
    data = data.split('^')
    BB = len(data)
    CC = int(BB)/6
    CC = int(CC)
    if request.method == 'POST':
        for i in range(CC) :
            AA = MM()
            AA.name = data[6*i]
            AA.participant1 = data[6*i+1]
            AA.participant2 = data[6*i+2]
            AA.date = data[6*i+3]
            AA.detail = data[6*i+5]
            if str(data[6*i+4]) == 'none':
                AA.material = ''
            else :
                j=str(data[6*i+4])
                j=j.replace("_","")
                AA.material = j
            AA.save()
            text = "successfully recovered the accounts !!"
    else:
        text = 'test'
    params = {"obj":obj,"data":data,"CC":CC}
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


def editCPA(request):

    obj1=Foo.objects.all()
    obj2=MM.objects.all()
    
    import glob
    AA = glob.glob('./media/contract/*')
    BB = glob.glob('./media/meetingminutes/*')

    if (request.method == 'POST'):
        for i in AA:
            new = i.replace(" ","")
            new = new.replace("　","")
            os.rename(i,new)
        for i in BB:
            new = i.replace(" ","")
            new = new.replace("　","")
            os.rename(i,new)
        return redirect(to='/editCPA')

    params = {"obj1":obj1,"obj2":obj2,"AA":AA,"BB":BB}
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


