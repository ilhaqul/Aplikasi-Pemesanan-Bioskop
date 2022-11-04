import book
import shop
import os

jumlahkursi = 0
pesanankursi = ""
pesanansnack = []

def printcart():
  global jumlahkursi
  global pesanankursi
  global pesanansnack

  total = 0
  print("          Pesanan Kamu\n")
  print("No. Item         Jumlah  Total Harga")
  for a in range (len(pesanansnack)+1):
    if(a == len(pesanansnack)): 
      hargatiket = 40000
      totaltiket = hargatiket * jumlahkursi

      if jumlahkursi > 0:
        print("%d %-15s %2d %12d" %(a+1,pesanankursi[1:len(pesanankursi)],jumlahkursi,totaltiket))
    else:
      print("%d %-15s %2d %12d" %(a+1, pesanansnack[a][0], pesanansnack[a][1],pesanansnack[a][3]))
      total = total + pesanansnack[a][3]
  print("Total Harga %21d" %(total+totaltiket))
  print("\n1. Bayar")
  print("2. Pesan lagi?")
  print("3. Batalkan pesanan, kembali ke menu.")
  pilih = int(input("Input: "))
  if pilih == 1:
    print("Kamu telah membayar pesanan kamu, terimakasih")
  elif pilih == 2:
    printmenu()
  elif pilih == 3:
    pesanansnack = []
    pesanankursi = ""
    jumlahkursi = 0
    print("Pesanan kamu telah dibatalkan.")
    input("Tekan enter untuk kembali ke menu")
    printmenu()
  else:
    printcart()


def printmenu():
  os.system("clear")
  pilih=0
  print("Cinema XXL\n")
  print("1. Pesan Kursi")
  print("2. Beli Snack")
  print("3. Pembayaran")
  print("4. Batalkan Pesanan dan keluar")
  pilih = int(input("Pilih: "))
  if pilih == 1:
    book.bookingseat()
  elif pilih == 2:
    shop.printmenu()
  elif pilih == 3:
    if pesanansnack == [] and jumlahkursi == 0:
      input("Kamu belum memesan sama sekali.\nTekan enter untuk kembali")
      printmenu()
    else:
      printcart()
  elif pilih == 4:
    print('Kamu telah membatalkan semua pesanan')
    exit
    