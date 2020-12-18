# inputan untuk memasukkan nama pembeli, tentunya nama bertipe data string
inputNama = (str(input("Masukkan nama pembeli: ")))


def namaDanHargaBarang():
    #key-Value
    key = {1: "Barang 1 = Rp.50.000",
           2: "Barang 2 = Rp.60.000",
           3: "Barang 3 = Rp.54.000",
           4: "Barang 4 = Rp.90.000",
           5: "Barang 5 = Rp.100.000",
           6: "Barang 6 = Rp.35.000",
           7: "Barang 7 = Rp.120.000"
           }
    #perintah untuk mencetak key-Value
    print("Menu dan Harga Barang")
    print("1.", key[1])
    print("2.", key[2])
    print("3.", key[3])
    print("4.", key[4])
    print("5.", key[5])
    print("6.", key[6])
    print("7.", key[7])
    

#Mencetak method
namaDanHargaBarang()

#input
pilihBarang = (int(input("\nPilih barang yang di beli: ")))
jumlah = (int(input("Masukkan jumlah pembelian: ")))

#kondisi statemen
if pilihBarang == 1:
    harga = 50000
    totalHarga = jumlah * harga
    print("Total harga barang: {}\n".format(int(totalHarga)))

elif pilihBarang == 2:
    harga = 60000
    totalHarga = jumlah * harga
    print("Total harga barang: {}\n".format(int(totalHarga)))

elif pilihBarang == 3:
    harga = 54000
    totalHarga = jumlah * harga
    print("Total harga barang: {}\n".format(int(totalHarga)))

elif pilihBarang == 4:
    harga = 90000
    totalHarga = jumlah * harga
    print("Total harga barang: {}\n".format(int(totalHarga)))

elif pilihBarang == 5:
    harga = 100000
    totalHarga = jumlah * harga
    print("Total harga barang: {}\n".format(int(totalHarga)))

elif pilihBarang == 6:
    harga = 35000
    totalHarga = jumlah * harga
    print("Total harga barang: {}\n".format(int(totalHarga)))

elif pilihBarang == 7:
    harga = 120000
    totalHarga = jumlah * harga
    print("Total harga barang: {}\n".format(int(totalHarga)))

else:
    print("Masukkan pilihan dengan benar ya")

# kondisi untuk inputPertanyaan antara dengan masukkan inputan harus Kapital "Y"
pilihBool_Y = "Y"
pilihBool_T = "T"

# inputan untuk menanyakan pelanggan mempunyai kartu apa tidak
inputPertanyaan = (str(input("Apakah pembeli memiliki kartu member (Y/T): ")))


# method kartu
def Kartu():
    # key-Value
    key = {1: "Platinum-ABC",
           2: "Gold-ABC",
           3: "Silver-ABC"}
    # perintah untuk mencetak key-Value
    print("Kartu Member Yang dimiliki apa?")
    print("1.", key[1])
    print("2.", key[2])
    print("3.", key[3])

    # inputan untuk memilih kartu
    pilihKartu = (int(input("\nPilih kartu: ")))

    # kondisi dalam pemilihan kartu
    if pilihKartu == 1:
        kartuPlatinum()
    elif pilihKartu == 2:
        kartuGold()
    elif pilihKartu == 3:
        kartuSilver()
    # pengecualian jika tidak ada kartu member
    else:
        return "Masukkan pilihan kartu dengan benar"


# method kartu platinum
def kartuPlatinum():
    print("Anda memiliki kartu member Platinum mendapakan:")
    print("-Merchendise\n-Voucher belanja seilai Rp.100.000\n-Diskon belanja sebesar 10%\n\n")
    #rumus diskon 10%
    diskonPlatinum = (totalHarga * (10 / 100))
    #total harga setelah harga di diskon
    totalSetelahDiskonPlatinum = (totalHarga - diskonPlatinum)
    # perintah untuk mencetak nama, total belanja, dan total belanja setelah diskon
    print("Hai,{}".format(str(inputNama)))
    print("Belanja anda sebesar: Rp.{}".format(int(totalHarga)))
    print("Total belanja anda setelah diskon 10% senilai: Rp.{}\n".format(int(totalSetelahDiskonPlatinum)))
    #input
    pelangganBayar = (int(input("Jumlah uang yang di bayarkan: Rp.")))
    #rumus kembalian uang pelanggan
    kembalian = (pelangganBayar - totalSetelahDiskonPlatinum)

    # kondisi jika uang yang di bayarkan sama dengan total harga setelah diskon
    if pelangganBayar == totalSetelahDiskonPlatinum:
        print("Uang anda pas")

    #perulangan
    while pelangganBayar >= totalSetelahDiskonPlatinum:
        print("Kembalian uang: {}".format(int(kembalian)))
        break
    else:
        print("\nJumlah uang yang di bayarkan harus lebih dari harga yang harus di bayar ya")
        Ulangi = "Y"
        ulangiLagi = (str(input("Ulangi lagi (Y): ")))
        #perulangan
        while ulangiLagi == Ulangi:
            pelangganBayar2 = (int(input("Jumlah uang yang di bayarkan: Rp.")))
            kembalian2 = pelangganBayar2 - totalSetelahDiskonPlatinum
            # kondisi jika uang yang di bayarkan sama dengan total harga setelah diskon
            if pelangganBayar2 == totalSetelahDiskonPlatinum:
                print("Uang anda pas")
            print(("Kembalian uang: {}".format(int(kembalian2))))
            break
        else:
            print("Anda memang keras kepala")
            exit()

    #keluar dari kondisi
    exit()


# method kartu gold
def kartuGold():
    print("Anda memiliki kartu member Gold anda mendapatkan:")
    if totalHarga >= 300000:
        print("-Voucher belanja seilai Rp.100.000\n-Diskon belanja sebesar 10%\n\n")
        #rumus diskon 10%
        diskonGold = (totalHarga * (10 / 100))
        #total harga setelah harga di diskon
        totalSetelahDiskonGold = (totalHarga - diskonGold)
        # perintah untuk mencetak nama, total belanja, dan total belanja setelah diskon
        print("Hai,{}".format(str(inputNama)))
        print("Belanja anda sebesar: Rp.{}".format(int(totalHarga)))
        print("Total belanja anda setelah diskon 10% senilai: Rp.{}\n".format(int(totalSetelahDiskonGold)))
        #input
        pelangganBayar = (int(input("Jumlah uang yang di bayarkan: Rp.")))
        #rumus kembalian uang pelanggan
        kembalian = (pelangganBayar - totalSetelahDiskonGold)

        #kondisi jika uang yang di bayarkan sama dengan total harga setelah diskon
        if pelangganBayar == totalSetelahDiskonGold:
            print("Uang anda pas")

        #perulangan
        while pelangganBayar >= totalSetelahDiskonGold:
            print("Kembalian uang: {}".format(int(kembalian)))
            break
        else:
            print("\nJumlah uang yang di bayarkan harus lebih dari harga yang harus di bayar ya")
            Ulangi = "Y"
            ulangiLagi = (str(input("Ulangi lagi (Y): ")))
            #perulangan
            while ulangiLagi == Ulangi:
                pelangganBayar2 = (int(input("Jumlah uang yang di bayarkan: Rp.")))
                kembalian2 = pelangganBayar2 - totalSetelahDiskonGold
                # kondisi jika uang yang di bayarkan sama dengan total harga setelah diskon
                if pelangganBayar2 == totalSetelahDiskonGold:
                    print("Uang anda pas")
                print(("Kembalian uang: {}".format(int(kembalian2))))
                break
            else:
                print("Anda memang keras kepala")
                exit()

    else:
        print("Hai,{}".format(str(inputNama)))
        print("Belanja anda sebesar: Rp.{}".format(int(totalHarga)))
        print("Jika pembelian anda di atas Rp.300.000 anda akan mendapatkan voucher belanja sebesar Rp.100.000,"
              "\ndan diskon 10%, yuk belanja lagi supaya mendaptkan voucher belanja dan dikson 10%")

        pelangganBayar = (int(input("Jumlah uang yang di bayarkan: Rp.")))
        kembalian = (pelangganBayar - totalHarga)

        # kondisi jika uang yang di bayarkan sama dengan total harga
        if pelangganBayar == totalHarga:
            print("Uang anda pas")

        #perulangan
        while pelangganBayar >= totalHarga:
            print("Kembalian uang: {}".format(int(kembalian)))
            break
        else:
            print("\nJumlah uang yang di bayarkan harus lebih dari harga yang harus di bayar ya")
            Ulangi = "Y"
            ulangiLagi = (str(input("Ulangi lagi (Y): ")))
            #perulangan
            while ulangiLagi == Ulangi:
                pelangganBayar2 = (int(input("Jumlah uang yang di bayarkan: Rp.")))
                kembalian2 = pelangganBayar2 - totalHarga

                # kondisi jika uang yang di bayarkan sama dengan total harga
                if pelangganBayar2 == totalHarga:
                    print("Uang anda pas")
                print(("Kembalian uang: {}".format(int(kembalian2))))
                break
            else:
                print("Anda memang keras kepala")
                exit()
    #keluar dari kondisi
    exit()

# method kartu silver
def kartuSilver():
    if totalHarga >= 200000:
        print("Anda kartu member Silver anda mendapatkan:")
        print("Potongan belanja sebesar Rp.50.000\n\n")
        #deklarasi potongan
        potongan = 50000
        # rumus untuk alur potongan belanja jika total pembelian di atas Rp.200.000
        totalSetelahDiskonSilver = (totalHarga - potongan)
        # perintah untuk mencetak nama, total belanja, dan total belanja setelah diskon
        print("Hai,{}".format(str(inputNama)))
        print("Belanja anda sebesar: Rp.{}".format(int(totalHarga)))
        print("Total belanja anda setelah di potong menjadi: Rp.{}\n".format(int(totalSetelahDiskonSilver)))
        #input
        pelangganBayar = (int(input("Jumlah uang yang di bayarkan: Rp.")))
        #rumus kembalian uang pelanggan
        kembalian = (pelangganBayar - totalSetelahDiskonSilver)

        # kondisi jika uang yang di bayarkan sama dengan total harga setelah diskon
        if pelangganBayar == totalSetelahDiskonSilver:
            print("Uang anda pas")

        #perulangan
        while pelangganBayar >= totalSetelahDiskonSilver:
            print("Kembalian uang: {}".format(int(kembalian)))
            break
        else:
            print("\nJumlah uang yang di bayarkan harus lebih dari harga yang harus di bayar ya")
            Ulangi = "Y"
            ulangiLagi = (str(input("Ulangi lagi (Y): ")))
            #perulangan
            while ulangiLagi == Ulangi:
                pelangganBayar2 = (int(input("Jumlah uang yang di bayarkan: Rp.")))
                kembalian2 = pelangganBayar2 - totalSetelahDiskonSilver

                # kondisi jika uang yang di bayarkan sama dengan total harga setelah diskon
                if pelangganBayar2 == totalSetelahDiskonSilver:
                    print("Uang anda pas")
                print(("Kembalian uang: {}".format(int(kembalian2))))
                break
            else:
                print("Anda memang keras kepala")
                exit()

    else:
        print("Hai,{}".format(str(inputNama)))
        print("Belanja anda sebesar: Rp.{}".format(int(totalHarga)))
        print("Anda tidak mendapatkan promo\n")
        print("Anda akan mendapatkan potongan harga sebesar Rp.50.000 Jika pembelian di atas Rp.200.000")
        print("Belanja lagi yuk sampai pembelian sebesar Rp.200.000 nanti akan mendapatkan potongan sebesar Rp.50.000\n")
        #input
        pelangganBayar = (int(input("Jumlah uang yang di bayarkan: Rp.")))
        #rumus kembalian uang pelanggan
        kembalian = (pelangganBayar - totalHarga)

        # kondisi jika uang yang di bayarkan sama dengan total harga
        if pelangganBayar == totalHarga:
            print("Uang anda pas")

        #perulangan
        while pelangganBayar >= totalHarga:
            print("Kembalian uang: {}".format(int(kembalian)))
            break
        else:
            print("\nJumlah uang yang di bayarkan harus lebih dari harga yang harus di bayar ya")
            Ulangi = "Y"
            ulangiLagi = (str(input("Ulangi lagi (Y): ")))
            #perulangan
            while ulangiLagi == Ulangi:
                pelangganBayar2 = (int(input("Jumlah uang yang di bayarkan: Rp.")))
                kembalian2 = pelangganBayar2 - totalHarga

                # kondisi jika uang yang di bayarkan sama dengan total harga
                if pelangganBayar2 == totalHarga:
                    print("Uang anda pas")
                print(("Kembalian uang: {}".format(int(kembalian2))))
                break
            else:
                print("Anda memang keras kepala")
                exit()

    #keluar dari kondisi
    exit()

# percabangan
if inputPertanyaan == pilihBool_Y:
    #mencetak method kartu
    print(Kartu())
    #proses berhenti/keluar jika selesai
    exit()

while inputPertanyaan == pilihBool_T:
    print("Hai,{}".format(str(inputNama)))
    print("Belanja anda sebesar: Rp.{}".format(int(totalHarga)))
    print("Anda tidak mendapatkan hadiah dari kami Toko ABC karena tidak memiliki kartu member")
    #input
    pelangganBayar = (int(input("Jumlah uang yang di bayarkan: Rp.")))
    #rumus kembalian
    kembalian = (pelangganBayar - totalHarga)

    # kondisi jika uang yang di bayarkan sama dengan total harga
    if pelangganBayar == totalHarga:
        print("Uang anda pas")

    #perulangan
    while pelangganBayar >= totalHarga:
        print("Kembalian uang: {}".format(int(kembalian)))
        break
    else:
        print("\nJumlah uang yang di bayarkan harus lebih dari harga yang harus di bayar ya")
        Ulangi = "Y"
        ulangiLagi = (str(input("Ulangi lagi (Y): ")))
        #perulangan
        while ulangiLagi == Ulangi:
            pelangganBayar2 = (int(input("Jumlah uang yang di bayarkan: Rp.")))
            kembalian2 = pelangganBayar2 - totalHarga

            # kondisi jika uang yang di bayarkan sama dengan total harga
            if pelangganBayar2 == totalHarga:
                print("Uang anda pas")
            print(("Kembalian uang: {}".format(int(kembalian2))))
            break
        else:
            print("Anda memang keras kepala")
            exit()

    break
else:
    print("Hai,{}".format(str(inputNama)))
    print("Tolong inputkan dengan benar ya")
