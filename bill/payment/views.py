from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
import re
from datetime import date
# from easy_pdf.views import PDFTemplateView
import smtplib
from email.mime.text import MIMEText
# from easy_pdf.rendering import *
# from django.template import Context, Template


# Create your views here.


def index(request):
    return render(request, 'payment/index.html')


comp = {
    "Bsnl": Bsnl,
    "Electricity": Electricity,
    "Water": Water,
    "Gas": Gas,
    "Cable": Cable,
    "Paper": Paper,
    "Telecom1": Telecom1,
    "Telecom2": Telecom2
}


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def detail(request, aadhar_id):
    print('*' * 100)
    print(get_ip(request))
    print('*' * 100)
    user = get_object_or_404(User, id=aadhar_id)
    return render(request, 'payment/detail.html', {'user': user})


def user_login(request):
    if request.method == 'POST':
        x = dict(request.POST)
        print(x)
        user = authenticate(request, username=x['email'][0], password=x['password'][0])
        if user is not None:
            print("Present")
            login(request, user)
            return redirect('payment:detail1')
        else:
            return render(request, 'payment/user_login.html', {'error': True})
    else:
        if request.user.is_authenticated:
            return redirect('payment:detail1')
        return render(request, 'payment/user_login.html', {'error': False})


def detail1(request):
    if request.user.is_authenticated:
        try:
            user = UserList.objects.get(email=request.user.username)
        except UserList.DoesNotExist:
            logout(request)
            return redirect('payment:user_login')
        return render(request, 'payment/detail.html', {'user': user})
    else:
        raise Http404("Login ya dingdong")


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('payment:index')
    else:
        return redirect('payment:index')


def company_detail(request):
    if request.user.is_authenticated:
        usern = request.user.username
        global comp
        if usern not in comp:
            logout(request)
            return redirect('payment:company_login')
        all_bills = comp[usern].objects.all()
        if request.method == 'POST':
            reqlen = len(request.POST)
            if reqlen == 2:
                ul = ''
                you = []
                for i in all_bills:
                    ul += str(i.aadhar) + '\n\t'
                    you .append(i.aadhar.email)
                body = '''This message is a reminder to make sure you pay the following bills\n''' + usern + '''
                        ''' + ul + '''

                        Please pay the above bill as soon as possible.

                        Email from online bill payment portal
                                   http://127.0.0.1:8000/payment/ for more information'''
                msg = MIMEText(body)
                me = ''
                msg['Subject'] = 'Bill payment reminder'
                msg['From'] = me
                msg['To'] = str(you)
                print('*' * 100)
                print(msg)
                print('*' * 100)
                if me == '':
                    print("Not sent")
                else:
                    s = smtplib.SMTP('localhost')
                    s.sendmail(me, you, msg.as_string())
                    s.quit()
                    print("Sent")
                return render(request, 'payment/company.html', {'all_bills': all_bills,
                                                                'name': usern.upper(),
                                                                'toast': True
                                                                })
            else:
                val = dict(request.POST)

                try:
                    name = val['name'][0].split()
                    firstn = name[0]
                    lastn = name[1]
                    print(firstn)
                    print(lastn)
                    i = comp[usern].objects.get(aadhar=UserList.objects.get(first=firstn, last=lastn))
                except:
                    return render(request, 'payment/company.html', {'all_bills': all_bills,
                                                                    'name': usern.upper(),
                                                                    'toast': False
                                                                    })
                print(i.pk)
                return redirect('payment:due_bill', i.pk)

        else:
            return render(request, 'payment/company.html', {'all_bills': all_bills,
                                                            'name': usern.upper(),
                                                            'toast': False
                                                            })
    else:
        raise Http404("Login ya dingdong")


def company_login(request):
    if request.method == 'POST':
        x = dict(request.POST)
        user = authenticate(request, username=x['name'][0], password=x['password'][0])
        if user is not None:
            login(request, user)
            return redirect('payment:company_detail')
        else:
            return render(request, 'payment/company_login.html', {'error': True})
    else:
        if request.user.is_authenticated:
            return redirect('payment:company_detail')
        return render(request, 'payment/company_login.html', {'error': False})


def due_bill(request, bill_id):

    global comp
    if request.user.is_authenticated and request.user.username in comp:
        usern = request.user.username
        try:
            i = comp[usern].objects.get(pk=bill_id)
        except comp[usern].DoesNotExist:
            raise Http404("Invalid user id")
        if request.method == 'POST':
            body = '''This message is a reminder to make sure you pay the following bills
                    ''' + usern + '''
                    username - ''' + str(i.aadhar) + '''
                    Bill date           ''' + str(i.bill_date) + '''
                    Bill due date       ''' + str(i.due_date) + '''
                    Bill amount         ''' + str(i.bill) + '''
                    Consumption units   ''' + str(i.consumption) + '''

                    Please pay the above bill as soon as possible.

                    Email from online bill payment portal
                               http://127.0.0.1:8000/payment/ for more information'''
            msg = MIMEText(body)
            me = ''
            you = i.aadhar.email
            msg['Subject'] = 'Bill payment reminder'
            msg['From'] = me
            msg['To'] = you
            print('*'*100)
            print(msg)
            print('*'*100)
            if me == '':
                print("Not sent")
            else:
                s = smtplib.SMTP('localhost')
                s.sendmail(me, [you], msg.as_string())
                s.quit()
                print("Sent")
            return render(request, 'payment/due_bill.html', {'bills': i, 'name': usern.upper(), 'toast': True})
        else:
            return render(request, 'payment/due_bill.html', {'bills': i, 'name': usern.upper(), 'toast': False})
    else:
        raise Http404("Login ya dingdong")


def register(request):
    error_msg = [False, False, False, False, False, False, False, False]
    pre_fill = ['', '', '', '', '', '', '', '']
    if request.method == 'POST':
        x = dict(request.POST)
        print("*"*125)
        for k in x:
            print(k, "----", x[k][0])
        print("*" * 125)
        error = 0
        if not x['phone'][0].isdigit():
            error = 1
            error_msg[4] = 'Invalid Phone Number'
        if not x['zip'][0].isdigit():
            error = 1
            error_msg[7] = 'Invalid Zipcode'
        try:
            temp = User.objects.get(username=x['email'][0])
            error = 1
            error_msg[0] = 'Email already exists'
        except User.DoesNotExist:
            pass
        if (not bool(re.match(".*[0-9].*", x['password1'][0]))) or\
                (not bool(re.match('.*[a-zA-Z].*', x['password1'][0]))) or (len(x['password1'][0]) < 8):
            error = 1
            error_msg[1] = 'Password must contain at least one letter at least one number ' \
                           'and should be a minimum of 8 characters long'
        if not x['first'][0].isalpha():
            error = 1
            error_msg[2] = 'First name must only contain letters'
        if not x['last'][0].isalpha():
            error = 1
            error_msg[3] = 'Last name must only contain letters'
        if not x['city'][0].isalpha():
            error = 1
            error_msg[5] = 'City name must only contain letters'
        if len(x['area'][0]) == 0:
            error = 1
            error_msg[6] = 'Invalid area'
        if x['password2'][0] != x['password1'][0]:
            error = 1
            error_msg[2] = "Mismatch password"
        if not error:
            ul = UserList()
            ul.first = x['first'][0]
            ul.last = x['last'][0]
            ul.phone = int(x['phone'][0])
            ul.city = x['city'][0]
            ul.area = x['area'][0]
            ul.zip = int(x['zip'][0])
            ul.email = x['email'][0]
            ul.password = x['password1'][0]
            ul.bal = 0
            ul.save()
            user = User.objects.create_user(x['email'][0], x['email'][0], x['password1'][0])
            user.last_name = x['last'][0]
            user.first_name = x['first'][0]
            user.save()
            return redirect('payment:user_login')
        pre_fill[4] = x['phone'][0]
        pre_fill[7] = x['zip'][0]
        pre_fill[0] = x['email'][0]
        pre_fill[1] = x['password1'][0]
        pre_fill[2] = x['first'][0]
        pre_fill[3] = x['last'][0]
        pre_fill[5] = x['city'][0]
        pre_fill[6] = x['area'][0]
        return render(request, 'payment/register.html', {'error': error_msg, 'pre_fill': pre_fill})
    else:
        return render(request, 'payment/register.html', {'error': error_msg, 'pre_fill': pre_fill})


def upload(request):
    global comp
    if request.user.is_authenticated and request.user.username in comp:
        usern = request.user.username
        if request.method == 'POST':
            entries = []
            file = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            uploaded_file_url = fs.url(filename)
            # print(uploaded_file_url)
            f = open("C:\\Projects\\Django\\bill\\" + uploaded_file_url, 'r')
            contents = f.read()
            error = 0
            # print(contents.split('\n'))
            for i in contents.split('\n'):
                # print(i)
                if len(i.split()) != 6 and len(i.split()) != 0:
                    # print("unsuccessful at line", i)
                    raise Http404('upload failed at line' + str(i))
                if len(i.split()) == 0:
                    # print("Successful")
                    return render(request, 'payment/upload.html')
                sub = i.split()
                # print(sub)
                if not sub[0].isdigit() or not sub[3].isdigit() or not sub[4].isdigit():
                    print("format in 0 3 4")
                    error = 1
                if not bool(re.match("[10]", sub[5])):
                    print("status error")
                    error = 1
                if not bool(re.match("[0-9]{4}[-/][0-9]{2}[-/][0-9]{2}", sub[1])):
                    print("bill date error")
                    error = 1
                if not bool(re.match("[0-9]{4}[-/][0-9]{2}[-/][0-9]{2}", sub[2])):
                    print("bill due date error")
                    error = 1
                if error == 0:
                    try:
                        aadhar = UserList.objects.get(id=int(sub[0]))
                    except UserList.DoesNotExist:
                        print("Unnable to get user")
                        error = 1
                if error == 1:
                    # print("Error in line", i)
                    raise Http404('upload failed at line' + str(i))
                else:
                    sub[0] = UserList.objects.get(id=int(sub[0]))
                    sub[1] = date(int(sub[1][:4]), int(sub[1][5:7]), int(sub[1][8:]))
                    sub[2] = date(int(sub[2][:4]), int(sub[2][5:7]), int(sub[2][8:]))
                    sub[3] = int(sub[3])
                    sub[4] = int(sub[4])
                    sub[5] = int(sub[5])
                    # print(sub)
                    entries.append(tuple(sub))

            for i in entries:
                # print("adding entry", i)
                x = comp[usern]()
                x.aadhar, x.bill_date, x.due_date = i[0], i[1], i[2]
                x.bill, x.consumption, x.status = i[3], i[4], i[5]
                x.save()
            print("Successful")
            return redirect('payment:company_detail')
        return render(request, 'payment/upload.html', {'name': usern.upper()})
    else:
        return redirect('payment/company/login')


# class HelloPDFView(PDFTemplateView):
#     template_name = 'hello123.html'


def gen(request):
    if request.method == 'POST':
        x = dict(request.POST)
        print(x)
        y = x['action'][0].split()
        company = y[0]
        num = int(y[1])
        global comp
        bill = comp[company].objects.get(pk=num)
        if request.user.is_authenticated:
            try:
                user = UserList.objects.get(email=request.user.username)
            except UserList.DoesNotExist:
                logout(request)
                return redirect('payment:user_login')
            return render(request, 'payment/gen.html', {'bill': bill, 'name': company})
        else:
            raise Http404("Login ya dingdong")
    else:
        raise Http404("wtf")


def user_change_password(request):
    if request.user.is_authenticated:
        global comp
        name = request.user.username
        if request.method == "POST":
            x = dict(request.POST)
            user = authenticate(request, username=name, password=x['old'][0])
            if user is not None:
                if (not bool(re.match(".*[0-9].*", x['new1'][0]))) or \
                        (not bool(re.match('.*[a-zA-Z].*', x['new1'][0]))) or (len(x['new1'][0]) < 8):
                    msg = 'The password must contain at least one number and one character.' \
                        ' The password must also be more than 8 characters long'
                    return render(request, 'payment/user_change_password.html', {'error': True, 'msg': msg})
                if x['new2'][0] != x['new1'][0]:
                    msg = 'Password mismatch'
                    return render(request, 'payment/user_change_password.html', {'error': True, 'msg': msg})
                u = User.objects.get(username=name)
                u.set_password(x['new1'][0])
                u.save()
                user = authenticate(request, username=name, password=x['new1'][0])
                login(request, user)
                return redirect('payment:detail1')
            else:
                return render(request, 'payment/user_change_password.html', {'error': True,
                                                                                 'msg': 'Wrong old password'})
        else:
            if name in comp:
                return redirect('payment:company_change_password')
            return render(request, 'payment/user_change_password.html', {'error': False, 'msg': ''})
    else:
        raise Http404("Login ya dingdong")


def company_change_password(request):
    if request.user.is_authenticated:
        global comp
        name = request.user.username
        if request.method == "POST":
            x = dict(request.POST)
            user = authenticate(request, username=name, password=x['old'][0])
            if user is not None:
                if (not bool(re.match(".*[0-9].*", x['new1'][0]))) or \
                        (not bool(re.match('.*[a-zA-Z].*', x['new1'][0]))) or (len(x['new1'][0]) < 8):
                    msg = 'The password must contain at least one number and one character.' \
                          ' The password must also be more than 8 characters long'
                    return render(request, 'payment/company_change_password.html', {'error': True, 'msg': msg})
                if x['new2'][0] != x['new1'][0]:
                    msg = 'Password mismatch'
                    return render(request, 'payment/user_change_password.html', {'error': True, 'msg': msg})
                u = User.objects.get(username=name)
                u.set_password(x['new1'][0])
                u.save()
                user = authenticate(request, username=name, password=x['new1'][0])
                login(request, user)
                return redirect('payment:company_detail')
            else:
                return render(request, 'payment/company_change_password.html', {'error': True,
                                                                                'msg': 'Wrong old password'})
        else:
            if name not in comp:
                return redirect('payment:user_change_password')
            return render(request, 'payment/company_change_password.html', {'error': False, 'msg': ''})
    else:
        raise Http404("Login ya dingdong")


def burner(request):
    if request.method == 'POST':
        x = dict(request.POST)
        print(x)
        user = authenticate(request, username=x['email'][0], password=x['password'][0])
        if user is not None:
            print("Present")
            login(request, user)
            return redirect('payment:detail1')
        else:
            return redirect('payment:user_login')
    else:
        if request.user.is_authenticated:
            return redirect('payment:detail1')
        return render(request, 'payment/burner.html', {})
