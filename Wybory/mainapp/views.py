from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# Create your views here.
from django.http import HttpResponse
from .forms import LoginForm
from .models import osoba_gl
from .models import Lista_K
from .models import Lista
from .models import Kandydat
from .models import Wybory
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.conf import  settings
from django.template.loader import render_to_string
from django.views.generic import View
from mainapp.utils import render_to_pdf #created in step 4
def glos(request, b):
    try:

        list=request.POST.getlist('choice')

        spr=Wybory.objects.get(id=request.session['w'])
        sprl=Lista.objects.get( id_wybory=request.session['w'], id_osoba=request.session['login'] )

    except (KeyError):
        # Redisplay the question voting form.
        return HttpResponse("niedziala  "+str(request.session['w']))
    else:




        if spr.ilosc >= len(list):
            for pom in list:

                selected_choice=Lista_K.objects.get(id_Kandynaci=pom)
                selected_choice.liczba_gl += 1
                selected_choice.save()
        else:
            return HttpResponse('Zbyt duza ilosc glosu')

        sprl.czy_glos=1
        sprl.save()
        return HttpResponse('Udalo sie '+str(spr.ilosc))


def sprawdz(data_do):
    if data_do >timezone.now():
        return 1
    else:
        return 0



def kand(request, id_w):
    w= Wybory.objects.filter(id=id_w)
    t=timezone.now()
    if request.session['login']>0 and w[0].data_koncowa > t :
            idkand=[]

            id_k=Lista_K.objects.filter(id_wybory=id_w)
            if len(id_k)>0:
                for pom2 in id_k:
                    idkand.append((pom2.id_Kandynaci))
            p = idkand

            s=request.session['login']
            context={'p':p,'s':s}
    return render(request, 'mainapp/kandydaci.html', context)


def base2(request):
    if(request.session['login']>0):
        idkand=[]
        kan=[]
        z=Kandydat.objects.all()
        wybor=Lista.objects.filter(id_osoba=request.session['login'])
        return render(request,'mainapp/base2.html',{'wybor':wybor})




def glowna(request):
     if(request.session['login']>0):

        wybor=Lista.objects.filter(id_osoba=request.session['login'])
        t= timezone.now()

        return render(request,'mainapp/glowna.html',{'wybor':wybor,'t':t})


def glowna2(request):
     if(request.session['login']>0):

        z=Kandydat.objects.all()
        wybor=Lista.objects.filter(id_osoba=request.session['login'])
        t= timezone.now()
        return render(request,'mainapp/glowna2.html',{'wybor':wybor,'t':t})



def post_list(request):
    logout(request)
    z=Kandydat.objects.all()
    context= {'z': z}
    return render(request, 'mainapp/post_list.html', context)

def zaloguj(request ,id_w):
    w= Wybory.objects.filter(id=id_w)
    t=timezone.now()
    sprl=Lista.objects.get( id_wybory=id_w, id_osoba=request.session['login'] )
    if request.session['login']>0 and w[0].data_koncowa  and  sprl.czy_glos==0  :
            idkand=[]
            a= request.session['w']=id_w;
            id_k=Lista_K.objects.filter(id_wybory=id_w)
            if len(id_k)>0:
                for pom2 in id_k:
                    idkand.append((pom2.id_Kandynaci))
            p = idkand

            b=1



    sesja=request.session['login']
    context= { 's':sesja,'idk':idkand ,'p':p,}
    return render(request, 'mainapp/zalog.html', context)

def logout(request):
    try:
        del request.session['login']
    except KeyError:
        pass
    return HttpResponse('Jesteś wylogowany')

def menup(request):
    if(request.session['login']>0):

        return render(request,'mainapp/main.html',{})

def login(request):
    logout(request)
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            osoba= osoba_gl.objects.all()
            for gor in osoba:
                pesel=gor.Pesel
                passw=gor.haslo
                if pesel ==cd['pesel']and passw==cd['password']:
                    request.session['login']=gor.id

                    return HttpResponseRedirect('/index')
            #return HttpResponse(str(kandydaci[2].id))

        else:
            return HttpResponse('Złehaslo ')
    else:
        form=LoginForm()
        logout(request)
    return render(request ,'mainapp/login.html',{'form':form})

def zapytanie(request):
    if(request.session['login']>0):
        if request.method == "POST":


            return render(request,'mainapp/Zapytanie.html',{})



def wynik(request):
    wybor=Lista.objects.filter(id_osoba=request.session['login'])
    Wyborki=[]
    klist=[]
    b=Lista_K
    t=timezone.now()
    for  pom in wybor:
        if pom.id_wybory.data_koncowa < t:
            Wyborki.append(pom.id_wybory)
    max=0
    kand=[]
    for pom in Wyborki:
        k=b.objects.filter(id_wybory=pom)
        klist.append(k)


    context={'w':Wyborki,'b': klist}
    # return HttpResponse(str(klist[0][0].id))
    return  render(request,'mainapp/wynik.html' ,context)




def get(request,id_w, *args, **kwargs):
        if(request.session['login']>0):
            w= Wybory.objects.get(id=id_w)
            glosy = w.ilosc
            pom = Lista.objects.filter(id_wybory=id_w)
            ile= len(pom)
            pom2=Lista.objects.filter(id_wybory=id_w).filter(czy_glos=1)
            ile_g=len(pom2)
            wynik=ile_g/glosy*ile *100
            t=timezone.now()
            idkand=[]
            id_k=Lista_K.objects.filter(id_wybory=id_w)

            p = id_k

            s=request.session['login']
            context={'p':p,'s':s ,'w':w,'wynik':wynik}
        pdf = render_to_pdf('mainapp/wynik2.html', context)
        return HttpResponse(pdf, content_type='application/pdf')
