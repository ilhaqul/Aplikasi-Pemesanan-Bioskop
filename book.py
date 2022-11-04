import menu
import os
os.system("clear")

seat = [['_'for a in range(10)]for a in range(10)]
baris = ["A","B","C","D","E","F","G","H","I","J"]

def printkursi():
  os.system("clear")
  print("   "+"_"*46)
  print("   "+"|"+"_"*19+"Screen"+"_"*19+"|")
  print("\n")
  for i in range(len(seat)//2):
    print("{:2}. |{:1}| |{:1}| |{:1}| |{:1}| |{:1}|      |{:1}| |{:1}| |{:1}| |{:1}| |{:1}|".format(baris[i] , seat[i][0],seat[i][1],seat[i][2],seat[i][3],seat[i][4],seat[i][5],seat[i][6],seat[i][7],seat[i][8],seat[i][9]))
  print("")
  for i in range((len(seat)//2),(len(seat))):
    print("{:2}. |{:1}| |{:1}| |{:1}| |{:1}| |{:1}|      |{:1}| |{:1}| |{:1}| |{:1}| |{:1}|".format(baris[i] , seat[i][0],seat[i][1],seat[i][2],seat[i][3],seat[i][4],seat[i][5],seat[i][6],seat[i][7],seat[i][8],seat[i][9]))
  print("{:2}.  {:1}   {:1}   {:1}   {:1}   {:1}        {:1}   {:1}   {:1}   {:1}".format(" ","1","2","3","4","5","6","7","8","9","10"))

def bookingseat():
  coma = [-1]
  book = []
  y_book = []
  x_book = []
  count_book = 0

  print("           Pesan Kursi\n")
  printkursi()
  
  book = input("Booking: ")
  
  for a in range (len(book)):
    if book[a] == ",":
      coma.append(a)
      count_book +=1

  for a in range (0,count_book+1):
    y_book.append(baris.index(book[coma[a]+1]))
    x_book.append(int(book[coma[a]+2])-1)
    seat[y_book[a]][x_book[a]]="X"

  printkursi()

  yesno = input("Kamu yakin? [y/n]")

  if yesno == "y":
    menu.jumlahkursi += count_book + 1
    menu.pesanankursi += ","+book
    menu.printmenu()
  elif yesno =="n":
    for a in range (0,count_book+1):
      y_book.append(baris.index(book[coma[a]+1]))
      x_book.append(int(book[coma[a]+2])-1)
      seat[y_book[a]][x_book[a]]=" "


