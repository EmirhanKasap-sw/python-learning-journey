import random 
print('TAŞ-KAĞIT-MAKAS Oyununa Hoş Geldin!')
print('Çıkmak için q tusuna basın')

while True:
    # 1. BİZİM HAMLEMİZ
    benim_secim = input('Seçimin(Taş,Kağıt-Makas):')
    # Çıkış kontrolü
    if benim_secim == 'q':
        print('Oyun bitti, iyi geceler kral!')
        break
    # 2. BİLGİSAYARIN HAMLESİ
    pc_secim = random.choice (['Taş','Kağıt','Makas'])
    print('Bilgisayarın seçimi: '+ pc_secim)
    # 3. KAPIŞMA ZAMANI 
    if benim_secim == pc_secim:
        print('BERABEREEE!!!') 
    elif benim_secim == 'Taş':
        if pc_secim == 'Makas':
            print('KAZANDINNNN') 
        else:
            print('KAYBETTİNNNN')
    elif benim_secim == 'Kağıt':
        if pc_secim == 'Taş':
            print('KAZANDINNN')
        else:
            print('KYBETTİNNN')
    elif benim_secim == 'Makas':
        if pc_secim == 'Kağıt':
            print('KAZANDINNN')
        else:
            print('KAYBETTİNN') 
    else:
            print('Yanlış yazdın KRALL.Lütfen Taş,Kağıt,Makas yaz ve boşluk bırakma .')
            print('(Baş harfleri büyük yazmaya dikkat et)')

