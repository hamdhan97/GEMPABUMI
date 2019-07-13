#!/usr/bin/python
# Data Gempa Terkini
# Coded by Muhamad Hamdan Sobirin
# www.hamdhan.blognive.com
import requests
import xml.dom.minidom as xmlget
import os
class bcolors:
    MERAH='\033[0;32m'
    KUNING='\033[01;31m'
    NORMAL='\033[0m'
    CYAN='\033[0;36m'
    BIRU='\033[0;34m'
    HIJAU='\033[1;37m'

def main():
    response = requests.get('http://data.bmkg.go.id/autogempa.xml')
    result = (response.text)
    save = open('result.xml','w')
    save.write('%s' %result,)
    save.close()
    rxml = xmlget.parse("result.xml")

    Tanggal = rxml.getElementsByTagName("Tanggal")[0].firstChild.data
    Jam = rxml.getElementsByTagName("Jam")[0].firstChild.data
    Lintang = rxml.getElementsByTagName("Lintang")[0].firstChild.data
    Bujur = rxml.getElementsByTagName("Bujur")[0].firstChild.data
    Magnitude = rxml.getElementsByTagName("Magnitude")[0].firstChild.data
    Kedalaman = rxml.getElementsByTagName("Kedalaman")[0].firstChild.data
    Wilayah = rxml.getElementsByTagName("Wilayah1")[0].firstChild.data
    Potensi = rxml.getElementsByTagName("Potensi")[0].firstChild.data

    print " Tanggal     : {}".format(Tanggal)
    print " Jam         : {}".format(Jam)
    print bcolors.CYAN
    print " Lintang     : {}".format(Lintang)
    print " Bujur       : {}".format(Bujur)
    print " Magnitude   : {}".format(Magnitude)
    print " Kedalaman   : {}".format(Kedalaman)
    print bcolors.HIJAU
    print " Wilayah     : {}".format(Wilayah)
    print " Potensi     : {}".format(Potensi)


# Clear layar
os.system('cls' if os.name == 'nt' else 'clear')

print bcolors.KUNING
print "============================================="
print "        INFO GEMPA DAN TSUNAMI TERINI        "
print "  Gampa Terkini yang diambil dari data BMKG  "
print "     Mod By     : Hacker Cyber Team Tegal              "
print "     Contact Me : mochamadhamdhan@gmail.com     "
print "     Blog       : www.hamdhan.blognive.com       "
print "     Instagram  : @muhamadhamdansobirin               "
print "     Thanks to  : Muhamad Hamdan Sobirin                  "
print " Semoga kita dalam lindungan ALLAH S.W.T     "
print "============================================="
print bcolors.NORMAL
print 
if __name__ == "__main__":
    main()
    # Remove file result.xml
    if os.path.exists("result.xml"):
        os.remove("result.xml")
    else:
        print("The file does not exists")
    print bcolors.NORMAL
