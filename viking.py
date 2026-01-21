import time

envanter = []

print("⚔️ VIKING ENVANTER SISTEMINE HOS GELDIN! ⚔️")

while True:

    print("\n-------------------")
    print(f"Çantandakiler: {envanter}")
    print("-----------------")

    print("1. Eşya Ekle (Loot)")
    print("2. Eşya Sil (Sat/At)")
    print("3. Çıkış (Oyuna Dön)")

    seçim = input("Ne yapmak istersin? (1-2-3): ")

    if seçim == "1":
        yeni_esya = input("Çantaya ne ekliyorsun?: ")
        # .append() -> Listeye EKLEME komutu 
        envanter.append(yeni_esya)
        print(f"✅ {yeni_esya} çantaya atıldı!")
    
    elif seçim == "2":
        silinecek = input("Neyi silmek istiyorsun?: ")

        # Listede var mı kontrolü 
        if silinecek in envanter:
            # .remove() -> Listeden SİLME komutu 
            envanter.remove(silinecek)
            print(f"🗑️  {silinecek} çantadan atıldı.") 
        else:
            print("❌ Hata: Böyle bir eşya çantanda yok!")
    elif seçim == "3":
        print("Valhalla'ya dönülüyor... İyi oyunlar!")
        break
    else:
        print("Yanlış tuşa bastın.")
