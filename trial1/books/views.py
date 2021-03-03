import json

import psycopg2
from django.shortcuts import render
from django.http import HttpResponse;
from django.views import View;
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core import serializers
# Create your views here.
# from trial1.books.models import Books
# from trial1.books.models import Books
from .models import Books
from .forms import BookForm, Login
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# @csrf_exempt

# @login_required(login_url='books/list.html')

def index(request):
    # if request.user.is_authenticated == True:
    #     print(request.user)
        if request.method == 'GET':
            return HttpResponse("hello world")
        else:
            return HttpResponse("post triggered")
    # else:
    #     return HttpResponse("npt authenticated")


# class SayNamaste(View):
#     def get(self, request):
#         return HttpResponse("namaste")
#
#     def post(self, request):
#         print("inside Post")
#         return HttpResponse("namaste from post")
def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)# it returns user model so we can call save method
        if form.is_valid():
            form.save()
            return  redirect('login')

        else:
            return render(request, 'books/register.html', context={'tmp': form})

    form = UserCreationForm()
    return render(request, 'books/register.html', context={'tmp': form})


def loginform(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('tweetie',)
        else:
            input_content = {'login_form': Login(request.POST)}
            return render(request, 'books/login.html', input_content)


    input_content = {'login_form': Login}
    return render(request, 'books/login.html', input_content)

# class loginform(View):
#     def get(self, request):
#         input_content = {'login_form': Login}
#         return render(request, template_name='books/login.html', context=input_content)

@ login_required(login_url='/books/login/',)
def Tweete(request):
    headerstemp = {
        'Authorization': "Bearer AAAAAAAAAAAAAAAAAAAAAF%2BmMQEAAAAAIEU33Kt766x2cesS4R4rZ6JHGkQ%3DFqkGjUlNKU7x7PJDM2qKE3WQzhwIY4PBhWcaiSyF2CtejlUAsI"
    }
    r = requests.get('https://api.twitter.com/1.1/trends/place.json?id=1', headers=headerstemp)
    tmp = r.json()
    # return HttpResponse(out)
    # input_content = {'trendingtweets': out}
    input_content = {'trendingtweets': tmp[0]['trends']}

    return render(request, template_name='books/twitter.html', context=input_content)

def logoutfunc(request):
    logout(request)
    return redirect('login')

# class Tweete(View):
#     def get(self, request):
#         headerstemp = {
#             'Authorization': "Bearer AAAAAAAAAAAAAAAAAAAAAF%2BmMQEAAAAAIEU33Kt766x2cesS4R4rZ6JHGkQ%3DFqkGjUlNKU7x7PJDM2qKE3WQzhwIY4PBhWcaiSyF2CtejlUAsI"
#         }
#         r = requests.get('https://api.twitter.com/1.1/trends/place.json?id=1', headers=headerstemp)
#         tmp = r.json()
#         print(tmp)
#         out = ''
#         for i in tmp[0]['trends']:
#             print(i['name'])
#             print('\n')
#             out = out + i['name'] + '\n'
#         # return HttpResponse(out)
#         # input_content = {'trendingtweets': out}
#         input_content = {'trendingtweets': tmp[0]['trends']}
#
#         return render(request, template_name='books/twitter.html', context=input_content)
#         # try :
#         #     User.objects.get(username='asd')
#         # except Exception:
#         #     User.objects.create_user(username='', password='das')
#         #     authenticate(request,username,password)
#         #
#         # try:
#         #     authenticate(request, username, password)
#         #     login(username, password)
#         #     redirect('books\tweetie')
#         # except Exception:
#         #     return HttpResponse("error in creds")
#         #
#         # try:
#         #     logout(username, password)
#         # except Exception:
#         #     return HttpResponse("error in creds")
#
#         # request.user will have user objects instance if user is logged in else  it will be anonymous
#


@method_decorator(csrf_exempt, name='dispatch')
class BookView(View):
    def get(self, request):
        try:
            all_books_obj = Books.objects.all()
            # all_books_obj = persons.objects.all()
            harsh_books = all_books_obj.filter(name="harsh")
            print(harsh_books)
            print(type(all_books_obj))
            output = serializers.serialize("json", all_books_obj)
            print(type(output))
            input_content = {'books': all_books_obj, 'book_form': BookForm}
            return render(request, template_name='books/list.html', context=input_content)
            # return HttpResponse(output, content_type='application/json')
        except User.DoesNotExist:
            return HttpResponse("user doesnt exist")
        except Exception:
            return HttpResponse("some error occured", status=400)

    def post(self, request):
        print(request.POST)
        inp_form = BookForm(request.POST)
        print(inp_form)
        if inp_form.is_valid():
            name = inp_form.cleaned_data['name']
            description = inp_form.cleaned_data['description']
            book_obj = Books.objects.create(name=name, description=description)
            op = {}
            op['name'] = book_obj.name
            op['description'] = book_obj.description
            print("before json dumping {}".format(op))
            obj_string = json.dumps(op)
            print("After dumping {}".format(obj_string))
            op = "successfully created book record with "+obj_string
            return HttpResponse(op)
        else :
            return render(request, template_name='books/list.html',context={'book_form': inp_form})





        #previoud data
        # print(request.body)
        # inp = json.loads(request.body)
        # print(inp)
        # # from trial1.books.models import Books
        # book_obj = Books.objects.create(name=inp['name'], description=inp["description"])
        # op = {}
        # op['name'] = book_obj.name
        # op['description'] = book_obj.description
        # print("before json dumping {}".format(op))
        # obj_string = json.dumps(op)
        # print("After dumping {}".format(obj_string))
        # op = "successfully created book record with "+obj_string
        # # book_obj.save()
        # return HttpResponse(op)

    def delete(self, request):
        input = json.loads(request.body)
        inp_name = input['name']
        print(inp_name)
        filtered_books = Books.objects.filter(name=inp_name)
        print(filtered_books)
        for tmp in filtered_books:
            tmp.delete()
        return HttpResponse("deleted books")

    def put(self, request):
        input = json.loads(request.body)
        inp_name = input['name']
        filter_books = Books.objects.filter(name=inp_name)#this will return a list so cannot see directly
        print(filter_books)
        for bookt in filter_books:

            print(bookt.description)
            bookt.description = "new update"
            bookt.save()
        return HttpResponse("books updated")
