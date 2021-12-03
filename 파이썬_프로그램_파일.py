allclear=0
clearnumber=0
a=0
c=0
s=0
while allclear!=1:
    if clearnumber==3:
        print('모든 엔딩을 클리어하셨습니다. 축하합니다!당신은 소개팅의 달인이 되셨습니다.')
        break
    elif clearnumber==0:
        print( ' <시작> 하시려면 Enter를 눌러주세요')
    b=str(input(''))
    print('-----------------------------------------------------')
    print('클리어된 엔딩의 수:', clearnumber)
    print('정해진 엔딩의 수:3')
    print('-----------------------------------------------------')
    #게임시작-이름입력
    print('안녕하세요! 반갑습니다.')
    Myname=''
    while Myname=='':
        Myname = input('이름을 입력하세요:')
        if Myname!='':
            break

    #이상형 키 고르기
    number = 170
    print('안녕하세요 ' + Myname + '님')
    print()
    tall = input('당신이 원하는 이상형의 키를 적어주세요. :')
    tall = int(tall)

    if tall > number :
        print('170cm보다 큰 사람을 원하시는 군요!')
    if tall < number :
        print('170cm보다 작은사람을 원하시는 군요!')
    if tall == number :
        print('170cm 원하시는 군요!')

    #이상형 직업 고르기
    print( )
    print ('보기 중 당신이 원하는 이상형의 직업은 무엇인가요?')
    print ('|     |보기|   [사업가,사무직,예술가,무직]     |')
    work = input("입력 : ")
    print('당신이 원하는 직업은 ' + work + ' (이)군요!')

    print( )
    print('당신은 어떤 동물을 좋아하나요?')
    face = input("입력 : ")
    print('당신은 ' + face + '을(를) 좋아하시군요!')
    print( )
    print('당신에게 적합한 이상형을 찾아보겠습니다')

    #이상형 클래스 만들기
    class Contact:
        def __init__(self, name, tall, work,face):
            self.name = name
            self.tall = tall
            self.work = work
            self.face = face
     
        def print_info(self):
            print(f"이름 : {self.name}, 키 : {self.tall}, 직업 : {self.work},얼굴 : {self.face}")
     
     
    # 딕셔너리 생성과 동시에 키,값 하나 세팅
    d = {'A씨': Contact('A씨', tall ,work,face+'상')}
     
    # 딕셔너리에 클래스 객체를 값으로 추가1
    p1 = Contact('B씨', 160, '마법사', '악어상')
    d[p1.name] = p1

    # 출력2 : 딕셔너리 값 출력
    print()
    print('당신의 이상형')
    for k in d.keys():
        d[k].print_info()

    print('당신에게 적합한 이상형은 A씨 입니다')

    #호감도
    Employee = 0
    AFeeling = 0

    #튜토리얼
    print('(*따르릉)')
    print('당신의 이상형과 적합한 사람을 찾았습니다. 그 사람과 데이트할 장소는 카페입니다.')
    print()
    print()
    print('종업원: 어서오세요.')
    print()
    print('이제 게임의 연습을 해봅시다.')
    print('당신의 눈 앞에는 카페 종업원이 있고 여러 메뉴가 있습니다.')
    print('종업원의 호감도는 ','0' ,'이고,')
    print('호감도는 당신이 어떤 행동을 하느냐에 따라 달라질 수 있습니다.')
    print()
    print('종업원: ')

    #튜_선택지
    while 1:
        drink=str(input("< ①아메리카노/ ②카페라떼/ ③바닐라라떼/ ④오렌지쥬스 (1~4)> 중 주문해주세요.\n"))
        if drink == '1':
            print("종업원: 아메리카노 주문받았습니다.")
            print()
            print("종업원의 총 호감도는",Employee,"입니다.")
            break
            
        elif drink == '2':
            print("종업원: 카페라떼 주문받았습니다.")
            print()
            print("종업원의 총 호감도는",Employee,"입니다.")
            break
            
        elif drink == '3':
            print("종업원: 바닐라라떼 주문받았습니다.")
            print()
            print("종업원의 총 호감도는",Employee,"입니다.")
            break
            
        elif drink == '4':
            print("종업원: ...오렌지쥬스 주문받았습니다. (이런거 마실거면 왜 카페까지 오는거야)")
            print()
            print('종업원의 호감도 하락 : -10')
            Employee += -10
            print("종업원의 총 호감도는",Employee,"입니다.")
            break
            
        else:
            print ("없는 메뉴입니다. 다시 골라주세요.")

    #튜_호감도에 따른 결과
            
    if Employee==0 :
        print("당신을 향한 종업원의 호감도는...")
        for i in range(10,0,-1):
            for j in range (1,i+1,1):
                print('두구',end=' ')
            print()
        print("< A >")
        print("종업원의 한마디 : 집에나 가고싶다.")
        
    elif Employee<=0 :
        print("당신을 향한 종업원의 호감도는...")
        for i in range(10,0,-1):
            for j in range (1,i+1,1):
                print('두구',end=' ')
            print()
        print("< F >")
        print("종업원의 한마디 : 오렌지쥬스는 마트에도 팝니다.")
        

    #본게임            
    print()
    print()
    print('---------------------------------------------------')
    print()
    print('어떻게 하는지 이해가 되셨나요? ')
    print('때마침 저 멀리 당신의 소개팅 상대가 걸어옵니다.')
    print('상대방이 원하는게 뭔지 곰곰히 생각한 후 선택지를 골라보세요!')
    print()
    print('------------')
    print('<카페>')
    print()
    print('저 멀리 소개받기로한 A씨가 보인다.')
    print()
    print('A: 안녕하세요')

    #본_선택지
    while 2:
        answer = str(input('<You: ①안녕하세요, 00이한테 말씀 많이 들었어요./ ② 엥... 사진이 훨 나으세요!>\n'))
        if answer == '1':
            print()
            print('You: 안녕하세요, 00이한테 말씀 많이 들었어요.')
            print("A : 아 정말요? 00가 뭐라고 말했어요?ㅎㅎ")
            print()
            AFeeling += 30
            print('A의 호감도 상승 : ', AFeeling, '.')
            print('A의 호감도: ',AFeeling, '.')
            break
        
        elif answer == '2':
            print()
            print("A : 아 네...",Myname,"씨도 사진이 더 나으세용ㅎ")
            AFeeling += -10
            print('A의 호감도 하락 : -10 ')
            print('A의 호감도: ', AFeeling , '.')
            print()
            break
        else:
            print ("A: 네? 뭐라고 하셨어요? 다시 말씀해주세요")
    print ()
    print ("A : 여기 커피 냄새 되게 좋네요... 어, 혹시 어디서 타는 냄새 안나요?\n ")
    while 3 :
        answer2 = str(input('<You: ①그러게요 원두 볶는 냄새인가? ②어, 맡으셨구나... 타는 제 마음, 알아주셨네요.>\n'))
        if answer2 == '1':
            print()
            print("A : 아 정말 그러네요.", Myname,"씨는 커피 좋아하세요?")
            print('당신은 A와 커피에 대해 얘기하다 서로의 커피 취향이 같다는 사실을 알았습니다.')
            print()
            AFeeling += 30
            print('A의 호감도 상승: +30')
            print('A의 호감도: ',AFeeling, '.')
            break
        elif answer2 == '2':
            print()
            print("A: 아...네... 고약하네요.")
            print('A의 표정이 미묘해집니다.')
            print()
            AFeeling += -30
            print('A의 호감도 대폭 하락: -30')
            print('A의 호감도: ',AFeeling, '.')
            break
        else:
            print ("A: 네? 뭐라고 하셨어요? 다시 말씀해주세요")

    # 집가는길
    print('와 집을 가는 도중 멀리서 큰 트럭이 다가옵니다. A는 다가오는 트럭을 보지못한 채 ',Myname,'님과 대화하고 있습니다. 이때 당신의 선택은?')
    # 선택지
    track=[1,2]
    #선택
    answer=0
    while answer != 1 or 2:
        answer=str(input('1번 : A를 잡아당겨 보호한다/ 2번: 그냥 무시한다 : '))
        if answer=='1':
            print()
            print(' You :  괜찮아요? 많이 놀랐죠?')
            print('A : 괘.. 괜찮아요 (두근)')
            print('A의 호감도 상승: +20')
            AFeeling += AFeeling+20
            print('A의 호감도:',AFeeling,'.')
            break
        elif answer == '2' :
            print()
            print('You:.........')
            print('A는 자신에게 신경을 쓰지 않는 당신한테 조금 실망한다')
            print(' A의 호감도 감소: -20')
            AFeeling += AFeeling-20
            print('A의 호감도:',AFeeling,'.')
            break
        elif answer != 1 or 2:
            print('선택지가 아닙니다 다시 선택해주세요')

    #집앞
    print('A씨의 집앞까지 온 당신! A가 말을 걸어옵니다')
    print('당신을 향한 A의  호감도는...')
    print('Enter를 눌러 진행 해주세요')

    b=str(input(''))

    if AFeeling>= 70:
        for i in range(10,0,-1):
            for j in range(1,i+1,1):
                print('두구',end=' ')
            print()
        b=str(input(''))
        print('< A >')
        b=str(input(''))
        print('다음에 또 만나요! 연락 기다릴게요!')
        print('엔딩을 달성했습니다')
        if a==1:
            print('이미 달성된 엔딩입니다')
            continue
        a=a+1
        clearnumber= clearnumber+1        
        print('클리어된 엔딩의 수:',clearnumber)
        b=str(input('다시 이어하시겠습니까?(다시 시작하려면Enter)'))
    elif AFeeling>=0:
        for i in range(10,0,-1):
            for j in range(1,i+1,1):
                print('두구',end=' ')
            print()
        b=str(input(''))
        print('< F >')
        b=str(input(''))
        print('조심히가세요!(다음에 그는 연락이 없었다)')
        print('엔딩을 달성했습니다')
        if c==1:
            print('이미 달성된 엔딩입니다')
            continue

        clearnumber= clearnumber+1
        c=c+1
        print('클리어된 엔딩의 수:',clearnumber)
        b=str(input('다시 이어하시겠습니까?(다시 시작하려면Enter)'))
    elif AFeeling<=0:
        for i in range(10,0,-1):
            for j in range(1,i+1,1):
                print('두구',end=' ')
            print()
        b=str(input(''))
        print('< S >')
        b=str(input(''))
        print('날 이렇게 대한 사람은 당신이 처음이야')
        print('엔딩을 달성했습니다')
        if s==1:
            print('이미 달성된 엔딩입니다')
            continue
            
        s=s+1
        clearnumber= clearnumber+1        
        print('클리어된 엔딩의 수:',clearnumber)
        b=str(input('다시 이어하시겠습니까?(다시 시작하려면Enter)'))        



