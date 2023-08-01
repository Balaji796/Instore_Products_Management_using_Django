from django.shortcuts import render
from Myapp.models import stud,bill,customer
from django.http import HttpResponse
from django.views.generic import View
from .process import html_to_pdf
from django.template.loader import render_to_string
from datetime import date,datetime

# Create your views here.
def view(request):
    return render(request,'start.html')

def register(request):
    return render(request,'register.html')
def add(request):
    ack="REGISTERED SUCCESSFULLY"
    name=request.POST['name']
    clas=request.POST['kg']
    adr=request.POST['type']
    sc=request.POST['quan']
    mail=request.POST['price']
    name=name.upper()
    p=stud(Name=name,Piece_Kg=clas,Type=adr,Quantity=sc,Price=mail)
    p.save()
    return render(request,'ack.html',{'ack':ack})
def registred(request):
    queryset=stud.objects.all().order_by('Name').values()
    return render(request,'existing.html',{'queryset':queryset})
def ad(request):
    if 'employee' in request.POST:
        return render(request,'elog.html')
    if 'manager' in request.POST:
        return render(request,'login.html')
def welcome(request):
    return render(request,'wel.html')
def log(request):
    m=request.POST['pas']
    ack="INCORRECT PASSWORD!!!"
    ak="Try Again!"
    if (m=="abcd"):
        return render(request,'wel.html')
    else:
        return render(request,'login.html',{'ack':ack , 'ak':ak})
def logs(request):
    m=request.POST['pas']
    ack="INCORRECT PASSWORD!!!"
    ak="Try Again!"
    if (m=="emp123"):
        query=bill.objects.all()
        total=0
        for k in query:
            total=total+float(k.cash)
        return render(request,'bill.html',{'queryset':query,'Total':total})
    else:
        return render(request,'elog.html',{'ack':ack , 'ak':ak})

def search(request):
    return render(request,'search.html')

def perform(request):
    gn_name=request.POST['name']
    gn_name=gn_name.upper()
    queryset=stud.objects.filter(Name=gn_name)
    if(len(queryset)==0):
        return render(request,'ack.html',{'ack':"Product not found"}) 
    return render(request,'existing.html',{'queryset':queryset})
def delete(request):
     return render(request,'delete.html')
def perfom(request):
    ack="Product Removed"
    gn_name=request.POST['name']
    gn_name=gn_name.upper()
    queryset=stud.objects.filter(Name=gn_name)
    if len(queryset)==0:
        return render(request,'ack.html',{"ack":"Product not found"})
    else:
        queryset=stud.objects.filter(Name=gn_name).delete()
        return render(request,'ack.html',{"ack":ack})
def show(request):
     if 'steel' in request.POST:
        queryset=stud.objects.filter(Type='Steel')
        if(len(queryset)==0):
            return render(request,'ack.html',{'ack':"Product not found"}) 
        return render(request,'existing.html',{'queryset':queryset})
     if 'alum' in request.POST:
        queryset=stud.objects.filter(Type='Aluminium')
        if(len(queryset)==0):
            return render(request,'ack.html',{'ack':"Product not found"}) 
        return render(request,'existing.html',{'queryset':queryset})
     if 'iron' in request.POST:
        queryset=stud.objects.filter(Type='Iron') | stud.objects.filter(Type='Wood') 
        if(len(queryset)==0):
            return render(request,'ack.html',{'ack':"Product not found"}) 
        return render(request,'existing.html',{'queryset':queryset})
     if 'brass' in request.POST:
        queryset=stud.objects.filter(Type='Brass') | stud.objects.filter(Type='Copper') 
        if(len(queryset)==0):
            return render(request,'ack.html',{'ack':"Product not found"}) 
        return render(request,'existing.html',{'queryset':queryset})
     if 'non' in request.POST:
        queryset=stud.objects.filter(Type='Nonstick') 
        if(len(queryset)==0):
            return render(request,'ack.html',{'ack':"Product not found"}) 
        return render(request,'existing.html',{'queryset':queryset})
     if 'plastic' in request.POST:
        queryset=stud.objects.filter(Type='Plastic')
        if(len(queryset)==0):
            return render(request,'ack.html',{'ack':"Product not found"}) 
        return render(request,'existing.html',{'queryset':queryset})
def vi(request):
     if 'steel' in request.POST:
        queryset=stud.objects.filter(Type='Steel')
        if(len(queryset)==0):
            return render(request,'ack.html',{'ak':"Product not found"}) 
        return render(request,'reg.html',{'queryset':queryset})
     if 'alum' in request.POST:
        queryset=stud.objects.filter(Type='Aluminium')
        if(len(queryset)==0):
            return render(request,'ak.html',{'ack':"Product not found"}) 
        return render(request,'reg.html',{'queryset':queryset})
     if 'iron' in request.POST:
        queryset=stud.objects.filter(Type='Iron') | stud.objects.filter(Type='Wood') 
        if(len(queryset)==0):
            return render(request,'ak.html',{'ack':"Product not found"}) 
        return render(request,'reg.html',{'queryset':queryset})
     if 'brass' in request.POST:
        queryset=stud.objects.filter(Type='Brass') | stud.objects.filter(Type='Copper') 
        if(len(queryset)==0):
            return render(request,'ak.html',{'ack':"Product not found"}) 
        return render(request,'reg.html',{'queryset':queryset})
     if 'non' in request.POST:
        queryset=stud.objects.filter(Type='Nonstick') 
        if(len(queryset)==0):
            return render(request,'ak.html',{'ack':"Product not found"}) 
        return render(request,'reg.html',{'queryset':queryset})
     if 'plastic' in request.POST:
        queryset=stud.objects.filter(Type='Plastic')
        if(len(queryset)==0):
            return render(request,'ak.html',{'ack':"Product not found"}) 
        return render(request,'reg.html',{'queryset':queryset})
def get(request):
    if 'add' in request.POST:
        name=request.POST['name']
        quan=request.POST['quan']
        name=name.upper()
        queryset=stud.objects.filter(Name=name)
        if(len(queryset)==0):
            return render(request,'ak.html',{'ack':"Product not found"}) 
        for i in queryset:
            pri=float(i.Price)
            i.Quantity=i.Quantity-float(quan) 
            i.save()
        tot=pri*float(quan)
        queue=bill.objects.filter(Name=name)
        if(len(queue)==0):
            p=bill(Name=name,quan=float(quan),price=pri,cash=tot)
            p.save()
        else:
            for i in queue:
                i.quan=float(i.quan)+float(quan)
                i.cash=float(i.price)*float(i.quan)
                i.save()
        query=bill.objects.all()
        total=0
        today = date.today()
        # dd/mm/YY
        d1 = today.strftime("%d-%m-%Y")
        for k in query:
            total=total+float(k.cash)
        return render(request,'bill.html',{'queryset':query,'Total':total,'price':tot})
    if 'bill' in request.POST:
        query=bill.objects.all()
        total=0
        today = date.today()
        # dd/mm/YY
        d1 = today.strftime("%d-%m-%Y")
        for k in query:
            total=total+float(k.cash)
        return render(request,'exist.html',{'queryset':query,'Total':total,'price':total,'date':d1})
    if 'remove' in request.POST:
        query=bill.objects.all()
        for k in query:
            p=stud.objects.filter(Name=k.Name)
            l=k.quan
            for i in p:
                i.Quantity=float(i.Quantity)+float(l)
                i.save()
        bill.objects.all().delete()
        query=bill.objects.all()
        total=0
        for k in query:
            total=total+float(k.cash)
        return render(request,'bill.html',{'queryset':query,'Total':total})


def store(request):
    if 'remove' in request.POST:
        name=request.POST['pro']
        name=name.upper()
        queryset=bill.objects.filter(Name=name)
        for k in queryset:
            p=stud.objects.filter(Name=k.Name)
            l=k.quan
            for i in p:
                i.Quantity=float(i.Quantity)+float(l)
                i.save()
        bill.objects.filter(Name=name).delete()
        query=bill.objects.all()
        total=0
        today = date.today()
        # dd/mm/YY
        d1 = today.strftime("%d-%m-%Y")
        for k in query:
            total=total+float(k.cash)
        return render(request,'exist.html',{'queryset':query,'Total':total,'price':total,'date':d1})
    if 'new' in request.POST:
        da=request.POST['dat']
        phone=request.POST['phone']
        addr=request.POST['addr']
        amount=request.POST['total']
        p=customer(date=da,phone=phone,addr=addr,amount=amount)
        p.save()
        bill.objects.all().delete()
        return render(request,'bill.html')
    if 'download' in request.POST:
            query=bill.objects.all()
            total=0
            today = date.today()
            # dd/mm/YY
            d1 = today.strftime("%d-%m-%Y")
            for k in query:
                    total=total+float(k.cash)

            open('templates/temp.html', "w").write(render_to_string('download.html', {'queryset': query,'Total':total,'date':d1}))

            # Converting the HTML template into a PDF file
            pdf = html_to_pdf('temp.html')
            
            # rendering the template
            return HttpResponse(pdf, content_type='application/pdf')
    if 'cancle' in request.POST:
        query=bill.objects.all()
        for k in query:
            p=stud.objects.filter(Name=k.Name)
            l=k.quan
            for i in p:
                i.Quantity=float(i.Quantity)+float(l)
                i.save()
        bill.objects.all().delete()
        query=bill.objects.all()
        total=0
        today = date.today()
        # dd/mm/YY
        d1 = today.strftime("%d-%m-%Y")
        for k in query:
            total=total+float(k.cash)
        return render(request,'exist.html',{'queryset':query,'Total':total,'price':total,'date':d1})
def customers(request):
    '''queryset=customer.objects.all().exclude(date="").exclude(date=None)'''
    return render(request,'custom.html')
def do(request):
    dat=request.POST['dat']
    queryset=customer.objects.filter(date=dat).exclude(amount="0").exclude(amount=None)
    total=0  
    for k in queryset:
        total=total+float(k.amount)

    return render(request,'customer.html',{'queryset':queryset,'sales':total})

def wel(request):
     return render(request,'welcom.html')

def reg(request):
    queryset=stud.objects.all().order_by('Name').values()
    return render(request,'reg.html',{'queryset':queryset})
def bills(request):
        query=bill.objects.all()
        total=0
        for k in query:
            total=total+float(k.cash)
        return render(request,'bill.html',{'queryset':query,'Total':total})

def update(request):
    return render(request,'update.html')
def new(request):
    ack="UPDATED SUCCESSFULLY"
    name=request.POST['name']
    name=name.upper()
    queryset=stud.objects.filter(Name=name)
    if(len(queryset)==0):
            return render(request,'ack.html',{'ack':"Product not found"}) 
    if 'ad' in request.POST:
         quan=request.POST['quan']
         for i in queryset:
            pri=i.Quantity+float(quan) 
            i.Quantity=pri
            i.save()
         return render(request,'ack.html',{'ack':ack})
    if 'qua' in request.POST:
        quan=request.POST['quan']
        for i in queryset:
            i.Quantity=quan 
            i.save()
        return render(request,'ack.html',{'ack':ack})
    if 'pri' in request.POST:
        price=request.POST['price']
        for i in queryset:
            i.Price=price
            i.save()
        return render(request,'ack.html',{'ack':ack})
def see(request):
    return render(request,'esearch.html')
def es(request):
    gn_name=request.POST['name']
    gn_name=gn_name.upper()
    queryset=stud.objects.filter(Name=gn_name)
    if(len(queryset)==0):
        return render(request,'ak.html',{'ack':"Product not found"}) 
    return render(request,'reg.html',{'queryset':queryset})





















