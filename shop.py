import menu
import os

snack = [["Popcorn S",15000],["Popcorn M",45000],["Popcorn L",7000],["Lemon Tea ",30000],["Air Mineral",15000],["Soft Drink", 50000]]

snack1 = [["popcorn s", "popcorn m","popcorn l"], [9000,8000,7000]]

cart = []

def printmenu():
  os.system("clear")
  print("     Menu Makanan\n")
  print("No. Item                Harga ")
  for a in range (len(snack)):
    print("%2d. %-15s Rp. %5d" %(a+1,snack[a][0],snack[a][1]))
  order = int(input("\nPilihan Order: "))
  jumlah = int(input("Jumlah: "))
  yn = input("Kamu ingin memesan %s sebanyak %d? (y/n)" %(snack[order-1][0],jumlah))
  if yn == "y":
    #Masukin pesanan ke dalam Array Cart/Orderan/Pesanan
    totalharga = jumlah * snack[order-1][1]
    cart.append([snack[order-1][0],jumlah,snack[order-1][1],totalharga])
    # NamaMakanan, JumlahPesanan, HargaSatuan, TotalHarga (Jumlah x Harga Satuan)
    orderlagi = input("Order lagi? (y/n)")
    if orderlagi == "y":
      printmenu()
    elif orderlagi == "n":
      menu.pesanansnack = cart
      menu.printmenu()
  elif yn == "n":
    printmenu()
