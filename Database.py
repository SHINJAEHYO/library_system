with open('c:/input.txt', "r") as f :
    books = f.read().splitlines() #txt파일 내용을 리스트로 받아와
for n in range(len(books)) :      #이중 리스트로 만들기
    i = books[n].split()    
    books[n] = i
