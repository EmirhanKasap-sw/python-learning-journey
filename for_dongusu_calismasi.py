import time
# --- 1. VERİ YAPISI: LİSTE (List/Array) ---
# Köşeli parantez []miçinde birden çok veriyi tutarız.
ganimet_cuvali = ["Altın Kadeh", "Gümüş Kolye","Paslı Kılıç", "Altın Kadeh", "Elmas", "Tahta Kaşık", "Altın Kadeh" ]

print(f"💰 Çuvalda toplam {len(ganimet_cuvali)} parça eşya var.")
print("Sayım başlıyor...\n")

altin_sayisi = 0
degerli_esya_sayisi = 0

# --- 2. FOR DÖNGÜSÜ (Listeyi Dönme) ---
# "ganimet_cuvali"ndaki her bir "esya" için şu kodu çalıştır:
for esya in ganimet_cuvali:

    print(f"Sandıktan çıkan: {esya}")
    time.sleep(1) # Bir saniye bekle(Heyecan olsun)    
    # Kontrol Yapısı
    if esya == "Altın Kadeh":
        print("  ->HOOO! Altın Bulduk!")
        altin_sayisi +=1 # Sayacı 1 arttır (altin_sayisi = altin_sayisi +1)
        degerli_esya_sayisi +=1

    elif esya == "Elmas":
        print("  -> VAY CANINA! Nadir Parça!!")
        degerli_esya_sayisi +=1

    elif esya == "Paslı Kılıç" or esya == "Tahta Kaşık":
        print("  -> Çöp... Bunu at gitsin.")

print("\n" + "-"*30)
print(f"Rapor:")
print(f"Toplam Altın Kadeh: {altin_sayisi}")
print(f"Toplam Değerli Eşya: {degerli_esya_sayisi}")
print("-"*30)
