#implementation of two player ticktac toe game in python
the_board= {
    '7':'', 
    '8':'',
    '9':'',
    '4':'',
    '5':'',
    '6':'',
    '1':'',
    '2':'',
    '3':''
        }
board_keys=[]
for key in the_board:
    board_keys.append(key)
def print_board(board):
    print(board['7']+board['8']+ board['9'])
    print('************')
    print(board['4']+board['5']+ board['6'])
    print('************')   
    print(board['1']+board['2']+ board['3'])
    print('************')
def game():
    count=0
    turn='x'
    for i in range(10):
        print_board(the_board)
        print('it is your turn'+ turn + 'move to which place')
        move = input()
        if the_board [move]== ' ':
            the_board [move] = turn
            count += 1
        else:
            print('That place is already filled. \n which place should we go')
            continue
        if count >=5 :
            if the_board ['7'] == the_board['8'] == the_board['9'] != ' ':
                print_board(the_board) 
                print('\n game over \n')
                print('**************'  + turn + 'won.*********') 
                break
game()            
             
        
    