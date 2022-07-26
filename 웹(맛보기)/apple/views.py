from django.shortcuts import render



# Create your views here.
# render 시 경로설정을 잘 해주어야 함 

def page1(request):
    return render(request, 'main/page1.html')

#숙소 정보 지도 시각화 
        #알고리즘으로 나온 결과 값 :  first_result = 
        # print(form) #함수 잘 돌아가는지 확인하기 위해 print를 사용합니다
        # print(form['age']) #딕셔너리형태  (key : age / value : 터미널 하단에 뜨는 숫자(실제로 내가 입력창에 쓴 거))          
    #render : HTML 연결해주는 함수  / request : HTML을 담아주는 함수     
    # return render(request, 'main/page2.html', {'dog_age' : my_dog_age})
def page2(request):
    
    if request.method  == 'POST':
        form = request.POST
        
    return render(request, 'main/page2.html', form)


#숙소근처 즐길거리 정보 지도 시각화
def page3(request):
    
    if request.method  == 'POST':
        form = request.POST
        
    return render(request, 'main/page3.html', form)

#마지막 페이지 로드 
def page4(request):
    return render(request, 'main/page4.html')

#배경화면 출력 확인용 page
def background(request):
    return render(request, 'main/background.html')
