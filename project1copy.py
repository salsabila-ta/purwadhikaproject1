listKontak= [
    {
        'idSiswa': 1101,
        'nama': 'timothee',
        'noHp': '087885280995',
        'email': 'timothee@purwadhika.com',
        'alamat': 'brooklyn' 
    },
    {
        'idSiswa': 1102,
        'nama': 'chalamet',
        'noHp': '087885280998',
        'email': 'chalamet@purwadhika.com',
        'alamat': 'west side' 
    }
]

def readKontak():
    read = True
    while read != '3':
        print('''
        =================
        Data Kontak Siswa
        =================

        1. Kontak Seluruh Siswa
        2. Kontak Siswa Tertentu
        3. Kembali Ke Menu Utama''')
        read = input('Silahkan masukan pilihan anda [1-3]: ')
        if read == '1':
            if len(listKontak) != 0:
                print('Kontak Siswa Purwadhika\n')
                print('idSiswa\t| nama  \t| noHp\t\t| email\t\t\t\t| alamat')
                for i in range(len(listKontak)) :
                    print('{}\t| {}  \t| {}\t| {}\t| {}'.format(listKontak[i]['idSiswa'],listKontak[i]['nama'],listKontak[i]['noHp'],listKontak[i]['email'],listKontak[i]['alamat']))
            else:
                print('Tidak ada data siswa')
        elif read == '2':
            if len(listKontak) != 0:
                inputId = int(input('Masukan ID Siswa: '))
                print('Kontak Siswa dengan ID {}'.format(inputId))
                for i in range(len(listKontak)):
                    if inputId == listKontak[i]["idSiswa"]:
                        print('idSiswa\t| nama  \t| noHp\t\t| email\t\t\t\t| alamat')
                        print('{}\t| {}  \t| {}\t| {}\t| {}'.format(listKontak[i]['idSiswa'],listKontak[i]['nama'],listKontak[i]['noHp'],listKontak[i]['email'],listKontak[i]['alamat']))
                        break
                else:
                    print('Tidak ada kontak siswa')
def tambahKontak():
    tambah = True
    while tambah != '2':
        print('''
        ========================
        Menambahkan Kontak Siswa
        ========================
        
        1. Tambah Kontak Siswa
        2. Kembali Ke Menu Utama''')
        tambah = input('Silahkan masukan pilihan anda [1-2]: ')
        if tambah == '1':
            inputId3 = int(input('Masukan ID siswa: '))
            allPrimeKey = [listKontak[i]["idSiswa"] for i in range(len(listKontak))]
            if inputId3 in allPrimeKey:
                print('Kontak sudah ada')
            else:
                newNama = input('Masukan Nama Siswa: ')
                while (True):
                    newNoHp = input('Masukan No Handphone Siswa: ')
                    if newNoHp.isnumeric():
                        break
                newEmail = input('Masukan Email Siswa: ')
                newAlamat = input('Masukan Alamat Siswa: ')
                
                while True: 
                    konfirmTambah = input('Apakah data akan disimpan? (Y/N) ')
                    if konfirmTambah == 'Y' or konfirmTambah == 'N':
                        break 
                if konfirmTambah == 'Y':
                    listKontak.append({
                    'idSiswa': inputId3,
                    'nama': newNama,
                    'noHp': newNoHp,
                    'email': newEmail,
                    'alamat': newAlamat
                })
                    print('Kontak Tersimpan')
                elif konfirmTambah == 'N':
                    print('Kontak Tidak Terupdate')

def ubahKontak():
    ubah = True
    while ubah != '2':
        print('''
        =====================
        Mengubah Kontak Siswa
        =====================
        
        1. Ubah Kontak Siswa
        2. Kembali Ke Menu Utama''')
        ubah = input('Silahkan masukan pilihan anda [1-2]: ')
        if ubah == '1':
            inputId4 = int(input('Masukan ID siswa: '))
            allPrimeKey = [listKontak[i]["idSiswa"] for i in range(len(listKontak))]
            if inputId4 in allPrimeKey:
                i = allPrimeKey.index(inputId4)
                print('idSiswa\t| nama  \t| noHp\t\t| email\t\t\t\t| alamat')
                print('{}\t| {}  \t| {}\t| {}\t| {}'.format(listKontak[i]['idSiswa'],listKontak[i]['nama'],listKontak[i]['noHp'],listKontak[i]['email'],listKontak[i]['alamat']))
                
                while (True):
                    konfirmUbah = input('Tekan Y jika ingin mengubah data, Tekan N jika ingin membatalkan: ')
                    if konfirmUbah == 'Y' or konfirmUbah == 'N':
                        break
                if konfirmUbah == 'Y':
                    while True : 
                        kolomUbah = input('Masukan kolom keterangan yang ingin diubah: ')
                        if kolomUbah == 'nama' or kolomUbah == 'noHp' or kolomUbah == 'email' or kolomUbah == 'alamat':
                            hasilUbah = input('Masukan {} baru: '. format(kolomUbah))
                            while(True):
                                konfirmUbah2 = input('Apakah data akan diubah? (Y/N): ')
                                if konfirmUbah2 == 'Y' or konfirmUbah2 == 'N':
                                    break
                            if konfirmUbah2 == 'Y':
                                listKontak[i][kolomUbah] = hasilUbah
                                print('Data berhasil diubah')
                                break
                            elif konfirmUbah2 == 'N':
                                print('Data tidak diubah')
                                break
                elif konfirmUbah == 'N':
                    print('Data tidak diubah')
            else:
                print('Kontak tidak ada')


def hapusKontak():
    hapus = True
    while hapus != '2':
        print('''
        ======================
        Menghapus Kontak Siswa
        ======================
        
        1. Hapus Kontak Siswa
        2. Kembali Ke Menu Utama''')
        hapus = input('Silahkan masukan pilihan anda [1-2]: ')
        if hapus == '1':
            print('Data Kontak Siswa Purwadhika\n')
            print('idSiswa\t| nama  \t| noHp\t\t| email\t\t\t\t| alamat')
            for i in range(len(listKontak)) :
                print('{}\t| {}  \t| {}\t| {}\t| {}'.format(listKontak[i]['idSiswa'],listKontak[i]['nama'],listKontak[i]['noHp'],listKontak[i]['email'],listKontak[i]['alamat']))
            inputId2 = int(input('Masukan ID siswa: '))
            
            primarykey = [listKontak[i]['idSiswa'] for i in range(len(listKontak))]
            if inputId2 in primarykey:
                while(True):
                    konfirmDel = input('Apakah kontak siswa akan dihapus? (Y/N): ')
                    if konfirmDel == 'Y' or konfirmDel == 'N':
                        break

                if konfirmDel == 'Y':
                    for i in range(len(listKontak)):
                        if listKontak[i]['idSiswa'] == inputId2:
                            del listKontak[i]
                            print('Kontak telah terhapus')
                            break
                    else:
                        print('Kontak tidak tersedia')
                elif konfirmDel == 'N':
                    print('Kontak tidak terhapus')
            else:
                print('ID Siswa Tidak Tersedia')
while True: 
    pilihanMenu = input('''
    =====================================
    Data Kumpulan Kontak Siswa Purwadhika

    List Menu
    1. Data Kontak Siswa
    2. Menambahkan Kontak Siswa
    3. Mengubah Data Siswa
    4. Menghapus Kontak Siswa
    5. Exit

    Silahkan Pilih Main Menu [1-5]: ''')
    
    if(pilihanMenu == '1') :
        readKontak()
    elif(pilihanMenu == '2') :
        tambahKontak()
    elif(pilihanMenu == '3') :
        ubahKontak()
    elif(pilihanMenu == '4') :
        hapusKontak()
    elif(pilihanMenu == '5') :
        print('Thank you and see you!')
        break
    else:
        print('Opsi tidak tersedia')