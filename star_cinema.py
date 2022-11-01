class Star_Cinema:
  __hall_list = []
  def entry_hall(self, hall_name):
    self.__hall_list.append(hall_name)
 
class Hall(Star_Cinema):
  def __init__(self, rows, cols, hall_no):
    self.rows = rows
    self.cols = cols
    self.hall_no = hall_no
    self.seats = {}
    self.show_list = []
    self.entry_hall(self)
    
  def entry_show(self, id, movie_name, time):
    self.tp = (id, movie_name, time)
    self.show_list.append(self.tp)
    arr = []
    for i in range(self.rows):
      col = []
      c = chr(65+i)
      for j in range(self.cols):
        col.append(c+str(j))
      arr.append(col)
    self.seats[id] = arr
  
  def book_seats(self, cust_name, cust_phone, id, seats_dimention):
    self.cust_name = cust_name
    self.cust_phone = cust_phone
    self.seats_dimention = seats_dimention[0]+seats_dimention[1]
    self.is_booked = False
    if id in self.seats.keys():
      i = ord(seats_dimention[0])-65
      j = int(seats_dimention[1])
      if(self.seats[id][i][j] != 'X'):
        self.seats[id][i][j] = 'X'
        self.is_booked = False
      elif self.seats[id][i][j] == 'X':
        print(f'THIS SEATS WERE BOOKED - {self.seats_dimention}')
        self.is_booked = True
    else:
      print("show id not found")

  def view_show_list(self):
    print('AVAILABLE SHOWS FOR TONIGHT' )
    x = '-'
    # print('\n')
    print(x.ljust(90, x))
    for lst in self.show_list:
      print(f'MOVIE NAME: {lst[1].ljust(25," ")} SHOW ID: {lst[0].ljust(15," ")} TIME: {lst[2]}')
    print(x.ljust(90, x))
    print('\n')

  def view_available_seats(self, id):
    if id in self.seats.keys():
      for i in self.show_list:
        if i[0] == id:
          print(f'MOVIE NAME: {i[1].ljust(25, " ")} TIME: {i[2].ljust(15, " ")}')
          break
      print('X for already booked seats')
      x = '-'
      l = (self.cols -1) * 7 +2
      print(x.ljust(l, x))
      for st in self.seats[id]:
        for i in range(0, self.cols):
          print(f'{st[i].ljust(7, " ")}' , end ="")
        print('\n')
      print(x.ljust(l, x))
    else:
      print('SHOW IS NOT AVAILABLE')

cine_plex = Hall(4, 5, 'SC100')

cine_plex.entry_show('cp123', 'Black Adam', 'Oct 31 2022 8:30PM')
cine_plex.entry_show('cp125', 'Black Panther', 'Oct 31 2022 9:30PM')

while(True):
  print('\n1. VIEW ALL SHOWS FOR TODAY')
  print('2. VIEW AVAILABLE SEATS')
  print('3. BOOK TICKETS')
  print('4. ENTER ZERO TO CLOSE THE TICKET COUNTER')
  try:
    a = int(input('ENTER OPTION: '))
    print('\n')
    if a == 1:
      cine_plex.view_show_list()
    elif a == 2:
      show_id = input('ENTER SHOW ID: ')
      print('\n')
      cine_plex.view_available_seats(show_id)
    elif a == 3:
      cust_name = input('ENTER CUSTOMER NAME:')
      cust_phone = input('ENTER CUSTOMER PHONE NUMBER:')
      show_id = input('ENTER SHOW ID:')
      n = int(input('ENTER NUMBER OF TICKETS: '))
      st = []
      for i in range(0, n):
        seat_no = input('ENTER SEAT NO:')
        cine_plex.book_seats(cust_name, cust_phone, show_id, (seat_no[0],seat_no[1]))
        if cine_plex.is_booked is False:
          st.append(seat_no)
      if cine_plex.is_booked is False:
        print('\n##### TICKET BOOKED SUCCESSFULLY!! #####')
        x = '-'
        print(x.ljust(70, x))
        print(f'NAME : {cust_name} \nPHONE NUMBER: {cust_phone} \n')
        for i in cine_plex.show_list:
          if i[0] == show_id:
            print(f'MOVIE NAME: {i[1].ljust(25, " ")} MOVIE TIME: {i[2].ljust(15, " ")}')
            break
        print('TICKETS: ', end = '')
        for i in range(0, len(st)):
          print(st[i], end = ' ')
        print(f'\nHALL: {cine_plex.hall_no}\n')
        print(x.ljust(70, x))
    elif a == 0:
      print('GOOD NIGHT!\n')
      break
    else:
      print('Invalid option, please pick a correct option.')
  except:
    print("Please enter a numeric value")

