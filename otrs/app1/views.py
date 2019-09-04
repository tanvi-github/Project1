from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from .form import DocumentForm,RegistrationForm,TrainerLogin,TrainerRegForm
from .models import tb_Registration,tb_TrainerRegistration


# Create your views here.
def hello(request):
    return HttpResponse("<h1>hello</h1>")

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index.html')
    else:
        form = DocumentForm()
    return render(request, 'app1/upload.html', { 'form': form })

def index1(request):
    return render(request, 'app1/index.html')

from.models import Document1
#x1 = None
def Display_Image(request):
    p = Document1.objects.filter(description='resume').values('document')
    for x in p:
        print(x['document'])
        x1 = x['document']
    return render(request, 'app1/display.html', {"image": x1})

def Register(request):
    if request.method=='POST':
       # form = UserCreationForm(request.POST)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            technology = form.cleaned_data['technology']
            trainer_name = form.cleaned_data['trainer_name']
            lab_assign = form.cleaned_data['lab_assign']
            batch_type = form.cleaned_data['batch_type']
            batch_status = form.cleaned_data['batch_status']
            batch_code = form.cleaned_data['batch_code']

            p = tb_Registration(technology=technology, trainer_name=trainer_name, lab_assign=lab_assign,
                                batch_type=batch_type, batch_status=batch_status, batch_code=batch_code)
            p.save()
            #form.save()
            print("1111111111")
            #return HttpResponseRedirect('app1/thanks.html')
            return render(request,"app1/thanks.html",{'technology':technology,'trainer_name':trainer_name,'lab_assign':lab_assign,
                                                      'batch_type':batch_type,'batch_status':batch_status,'batch_code':batch_code})
        else:
            #form = UserCreationForm()
            #args = {'form':form}
            print("2222222222")
            return render(request,"app1/reg_batch.html" ,{'form':form})
    else:
        form = RegistrationForm()
        #args = form
        print("2333333333")
        return render(request,"app1/reg_batch.html" ,{'form':form})

def trainerRegistration(request):
    if request.method == 'POST':
        form = TrainerRegForm(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['Name']
            Emp_ID = form.cleaned_data['Employee_ID']
            Gender = form.cleaned_data['Gender']
            Email_ID = form.cleaned_data['Email_ID']
            Contact = form.cleaned_data['Contact']
            Password = form.cleaned_data['Password']
            Password1 = form.cleaned_data['Password1']
            if Password == Password1:
                tr = tb_TrainerRegistration(Name=Name, Gender=Gender, Employee_ID=Emp_ID, Email_ID=Email_ID, Contact=Contact, Password=Password)
                tr.save()
                return HttpResponse("Registration Successful")
                #return render(request, "OTRS/Display.html", {'Name': Name, 'Email_ID': Email_ID, 'Employee_ID': Emp_ID, 'Contact': Contact})
            else:
                return HttpResponse("Password didn't match")
        else:
            return render(request, "app1/TrainerReg.html", {'form': form})
    else:
        form = TrainerRegForm()
        return render(request, "app1/TrainerReg.html", {'form': form})

#VIEWS FOR TRAINER LOGIN
def trainerLogin(request):
    if request.method == 'POST':
        form = TrainerLogin(request.POST)
        if form.is_valid():
            Emp_ID = form.cleaned_data['Employee_ID']
            Password = form.cleaned_data['Password']
            tl = tb_TrainerRegistration.objects.filter(Employee_ID=Emp_ID, Password=Password)
            if (tl.count() > 0):
                return HttpResponse("LOGIN SUCCESSFUL")
            else:
                return HttpResponseNotFound('<h1>No Page here<h1>')
        else:
            return render(request, "app1/TrainerLogin.html", {'form': form})
    else:
        form = TrainerLogin()
        return render(request, "app1/TrainerLogin.html", {'form': form})