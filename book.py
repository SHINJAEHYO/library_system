import Database
data = Database.books #간단히 사용하기 위해 전역변수 data 선언

def menu() : #메뉴 출력 함수
    print("1.도서 추가")
    print("2.도서 검색")
    print("3.도서 정보 수정")
    print("4.도서 삭제")
    print("5.현재 총 도서 목록 출력")
    print("6.저장")
    print("7.프로그램 나가기(자동저장)")


def add_book() : #도서 추가 함수
    newbook = input("\n도서명, 저자, 출판연도, 출판사명, 장르를 입력하세요(스페이스바로 구분) : ").split()
    Database.books.append(newbook)
    print("추가되었습니다.")


def find_book() : #도서 찾기 함수
    print("\n도서명(1), 저자(2), 출판일(3), 출판사명(4), 장르(5)")
    fnum = int(input("\n무엇으로 검색하시겠습니까?(숫자) : "))
    if fnum == 1 :
        name = input("\n도서명 : ")
        for i in range(len(data)) :
             if(name == data[i][0]) :
              print(data[i])
    elif fnum == 2 : 
        name = input("\n저자 : ")
        for i in range(len(data)) :
             if(name == data[i][1]) :
              print(data[i])        
    elif fnum == 3 :
        name = input("\n출판일 : ")
        for i in range(len(data)) :
             if(name == data[i][2]) :
              print(data[i])
    elif fnum == 4 :
        name = input("\n출판사명 : ")
        for i in range(len(data)) :
             if(name == data[i][3]) :
              print(data[i])
    elif fnum == 5 :
        name = input("\n장르 : ")
        for i in range(len(data)) :
             if(name == data[i][4]) :
              print(data[i]) 


def modify_book() : #도서 수정 함수
    print_book()
    i = int(input("\n수정할 도서데이터 번호를 입력하세요.(1번부터 시작) : ")) - 1
    print("\n도서명(1), 저자(2), 출판일(3), 출판사명(4), 장르(5)")
    mnum = int(input("\n무엇을 수정하시겠습니까?(숫자) : "))
    if mnum == 1 :
        data[i][0] = input("\n수정내용 : ")
        print("수정되었습니다.")
    elif mnum == 2 :
        data[i][1] = input("\n수정내용 : ")
        print("수정되었습니다.")
    elif mnum == 3 :
        data[i][2] = input("\n수정내용 : ")
        print("수정되었습니다.")
    elif mnum == 4 :
        data[i][3] = input("\n수정내용 : ")
        print("수정되었습니다.")
    elif mnum == 5 :
        data[i][4] = input("\n수정내용 : ")
        print("수정되었습니다.")           


def delete_book() : #도서 삭제 함수
    print_book()
    i = int(input("\n삭제할 도서데이터 번호를 입력하세요.(1번부터 시작) : ")) - 1
    del data[i]
    print("삭제되었습니다.")


def print_book() : #전체 도서 출력 함수
    print("도서명 / 저자 / 출판일 / 출판사명 / 장르 순\n")
    for i in range(len(data)) : #출력 형식
        print(i+1,"(", data[i][0],"/", data[i][1], "/", data[i][2], "/", data[i][3], "/", data[i][4], ")")


def save_book() : #저장 함수
    with open('c:/input.txt', "w") as f : #쓰기 형태로 파일 열기
        for i in range(len(data)) : #이중 배열을 초기 txt파일 형태로 바꾸기
            f.write(data[i][0])
            f.write(" ")
            f.write(data[i][1])
            f.write(" ")
            f.write(data[i][2])
            f.write(" ")
            f.write(data[i][3])
            f.write(" ")
            f.write(data[i][4])
            f.write("\n")
    print("저장되었습니다.")


def close_book() : #프로그램 종료 함수
    exit(save_book())

#메인 함수 부분
while True :
    menu()
    num = int(input("\n수행할 기능의 번호를 입력하세요 : "))
    
    if num == 1 :
        add_book()
    elif num == 2 :
        find_book()
    elif num == 3 :
        modify_book()
    elif num == 4 :
        delete_book()
    elif num == 5 :
        print_book()
    elif num == 6 :
        save_book()    
    elif num == 7 :
        close_book()         


