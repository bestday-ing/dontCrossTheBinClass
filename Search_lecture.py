count = 0
table_x = []
table_y = []

search_table_x = []
search_table_y = []
#좌표의 cell위치를 저장할 변수
#따로 return을 받지 않고 이 변수를 GUI_main에서 바로 사용

def get_clicked_pos(row, column):
    print("Pos :  %d , %d" % (row, column))  # 선택된 영역 row,col 받아오기

def get_dragged_pos(row,col):     #drag시 선택된 영역 row, col 받아오기
    table_x.append(row)
    table_y.append(col)
    print('\nStart pos : ' + str(table_x[0])+' , '+str(table_y[0]))                          #시작 지점
    print('End pos : ' + str(table_x[len(table_x)-1])+
          ' , '+str(table_y[len(table_y)-1]))  #끝   지점

def reset_table():
    del table_x[:]
    del table_y[:]

