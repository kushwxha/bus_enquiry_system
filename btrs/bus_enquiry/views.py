from decimal import Decimal
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from .models import Bus, User, Book
# bus_enquiry/views.py

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', context = {'page' : 'Home'})
    else:
        return render(request, 'register.html', context = {'page' : 'Register'})


def user_login(request):
    context = {}
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, 'success.html', {'form': form})
        else:
            context["error"] = "Provide Valid Credentials"
            return render(request, 'login.html', {'form':form})
    else:
        initial_data = {'username':'','password':'' }
        form = AuthenticationForm(initial=initial_data)
        return render(request, 'login.html',{'form':form})


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'thank.html')
        else:
            return render(request, 'register.html', {'form':form})
    else:
        initial_data = {'username':'','password1':'','password2':'' }
        form = UserCreationForm(initial=initial_data)
        return render(request, 'register.html',{'form':form})
    
def user_logout(request):
        context = {}
        logout(request)
        context['error'] = "You have been logged out"
        return redirect('login')


@login_required(login_url='login')
def findbus(request):
    context = {}
    if request.method == 'POST':
        source = request.POST.get('source')
        dest = request.POST.get('dest')
        date = request.POST.get('date')
        bus_list = Bus.objects.all().filter(source=source, dest=dest,date=date)
        if bus_list:
            return render(request, 'bus_list.html', locals())
        else:
            context['error'] = "No buses available"
            return render(request, 'findbus.html', context)
    else:
        return render(request, 'findbus.html', context)
    

@login_required(login_url='login')
def bookings(request):
    context = {}
    if request.method == 'POST':
        id = request.POST.get('bus_id')
        seats = int(request.POST.get('no_seats'))
        bus = Bus.objects.get(id = id)
        if bus:
            if bus.rem > int(seats):
                name = bus.bus_name
                source = bus.source
                dest = bus.dest
                nos = Decimal(bus.nos)
                price = bus.price
                cost = bus.price * int(seats)
                date = bus.date
                time = bus.time
                username = request.user.username
                email = request.user.email
                userid = request.user.id
                rem = bus.rem - seats
                Bus.objects.filter(id = id).update(rem = rem)
                book = Book.objects.create(name= username, email= email,cost = cost, userid = userid , bus_name = name, source = source, busid =id, dest = dest, price = price, nos = seats, date = date, time = time, status = 'Booked') 
                print('------------book id-----------', book.id)
                return render(request, 'booking.html', {'book': book})
            else:
                context['error'] = "Sorry select fewer number of seats"
                return render(request, 'findbus.html', context)
    else:
        return render(request, 'findbus.html')
    
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'success.html', context)


@login_required(login_url='signin')
def cancellings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('bus_id')
        #seats_r = int(request.POST.get('no_seats'))

        try:
            book = Book.objects.get(id=id_r)
            bus = Bus.objects.get(id=book.busid)
            rem_r = bus.rem + book.nos
            Bus.objects.filter(id=book.busid).update(rem=rem_r)
            #nos_r = book.nos - seats_r
            Book.objects.filter(id=id_r).update(status='CANCELLED')
            Book.objects.filter(id=id_r).update(nos=0)
            return redirect(seebookings)
        except Book.DoesNotExist:
            context["error"] = "Sorry You have not booked that bus"
            return render(request, 'error.html', context)
    else:
        return render(request, 'findbus.html')


@login_required(login_url='signin')
def seebookings(request,new={}):
    context = {}
    id_r = request.user.id
    book_list = Book.objects.filter(userid=id_r)
    if book_list:
        return render(request, 'booklist.html', locals())
    else:
        context["error"] = "Sorry no buses booked"
        return render(request, 'findbus.html', context)

def buslist(request):
    context = {}
    bus_list = Bus.objects.all()
    if bus_list:
        return render(request, 'bus_list.html', locals())
    else:
        context["error"] = "Sorry no buses available"
        return render(request, 'findbus.html', context)