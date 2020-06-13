from django.shortcuts import render
import random
import requests

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

#1. 사용자가 url경로에 이름을 입력하면
#2. 그 이름과 무작위 음식 하나 보여주는 페이지 작성
#2-1. random.choice(menu)
#3. urls -> views -> template

def namefood(request,name):
    foods = ['삼겹살', '짜장면', '닭꼬치']
    food = random.choice(foods)
    context = {
        'name': name,
        'food': food
    }
    return render(request, 'pages/namefood.html', context)

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    context = {
        'name': name,
        'age': age
    }
    return render(request, 'pages/catch.html', context)

#1. 사용자가 숫자 입력
#2. 입력 받은 숫자 만큼 반복해서
#3. 리스트에 로또 번호 담는다
#3-1. random.sample(range(1,46),6)
#4. 입력한 숫자와 로또번호 리스트를 출력
#5. ul태그를 사용 한줄 씩 출력

def lotto_throw(request):
    return render(request, 'pages/lotto_throw.html')

def lotto_catch(request):
    num = int(request.GET.get('num'))
    lottos = []
    for data in range(num):
        lottos.append(random.sample(range(1,46),6))

    #sort로 리스트 안의 숫자들을 정렬해줬다
    for lotto in lottos:
        print(sorted(lotto))
        
    for lotto in lottos:
        print(lottos.sort())
    context = {
        'num': num,
        'lottos': lottos,
    }
    return render(request, 'pages/lotto_catch.html', context)

def artii(request):
    return render(request, 'pages/artii.html')

def result(request):
    message = request.GET.get('message')
    result = requests.get(f'http://artii.herokuapp.com/make?text={message}').text
    context = {
        'result': result
    }
    return render(request, 'pages/result.html', context)