import random
import statistics


kitaplar = [
 {"isim": "Veri Bilimi 101", "yazar": "Ali", "tur": "Bilim", "satis": 1200, "yil": 2021},
 {"isim": "Python ile Yapay Zeka", "yazar": "Ayşe", "tur": "Bilim", "satis": 950, "yil":2020},
 {"isim": "İstatistik Temelleri", "yazar": "Ali", "tur": "Akademik", "satis": 700, "yil": 2019},
 {"isim": "Makine Öğrenmesi", "yazar": "Can", "tur": "Bilim", "satis": 1800, "yil": 2022},
 {"isim": "Veri Görselleştirme", "yazar": "Deniz", "tur": "Sanat", "satis": 400, "yil": 2018},
 {"isim": "Matematiksel Modelleme", "yazar": "Ali", "tur": "Akademik", "satis": 1500,"yil": 2021},
 {"isim": "Bilgi Toplumu", "yazar": "Ayşe", "tur": "Sosyal", "satis": 600, "yil": 2022}]

def en_cok_satan(kitaplar):
  en_cok_satan_kitap = max(kitaplar, key=lambda x: x["satis"])
  return en_cok_satan_kitap


def yazar_satislari(kitaplar):
  yazar_satislari_dict = {}
  for kitap in kitaplar:
    yazar = kitap["yazar"]
    satis = kitap["satis"]
    if yazar in yazar_satislari_dict:
      yazar_satislari_dict[yazar] += satis
    else:
      yazar_satislari_dict[yazar] = satis
  return yazar_satislari_dict

print("En çok satan kitap:", en_cok_satan(kitaplar))
print("Yazar satışları:", yazar_satislari(kitaplar))


def kitap_tur(kitaplar):
  turler=set()
  for kitap in kitaplar:
    turler.add(kitap["tur"])
  print("Tüm kitap türleri:", turler)

  kitap_isimleri_bin_ustu = []
  for kitap in kitaplar:
    if kitap["satis"] > 1000:
      kitap_isimleri_bin_ustu.append(kitap["isim"])
      print(f"Kitap Adı: {kitap['isim']}, Satış Adedi: {kitap['satis']}") # Corrected print statement

  print("Satış adedi 1000'den fazla olan kitap isimleri:", kitap_isimleri_bin_ustu)


kitap_tur(kitaplar)


kitaplar_2020_sonrası = list(filter(lambda x: x["yil"] >= 2020, kitaplar))
artirilmis_satislar = list(map(lambda x: x["satis"] * 1.1, kitaplar))
kitaplar_satista_sirali = sorted(kitaplar, key=lambda x: x["satis"], reverse=True)
print("2020'den Sonra Çıkan Kitaplar:", kitaplar_2020_sonrası)
print("Artırılmış Satışlar:", artirilmis_satislar)
print("Sıralanmış Kitaplar (Satista Sirali):", kitaplar_satista_sirali)


ortalama_satis = statistics.mean([kitap["satis"] for kitap in kitaplar])
en_cok_satan_tur= max(set([kitap["tur"] for kitap in kitaplar]), key=lambda tur: sum([kitap["satis"] for kitap in kitaplar if kitap["tur"] == tur]))
satis_sapmasi=statistics.stdev([kitap["satis"] for kitap in kitaplar])
print("Ortalama Satış Adedi:", ortalama_satis)
print("En Çok Satan Tür:", en_cok_satan_tur)
print("Satışların Standart Sapması:", satis_sapmasi)



# Kitap listesini rastgele %70 eğitim (train), %30 test verisine ayırın
train_size = int(len(kitaplar) * 0.7)
train_data = random.sample(kitaplar, train_size)
test_data = [kitap for kitap in kitaplar if kitap not in train_data]

print("Eğitim Verisi:")
print(train_data)
print("\nTest Verisi:")
print(test_data)

# Eğitim verisinden yazarların ortalama satışını hesaplayın.
yazar_satis_toplam = {}
yazar_kitap_sayisi = {}

for kitap in train_data:
    yazar = kitap["yazar"]
    satis = kitap["satis"]
    if yazar in yazar_satis_toplam:
        yazar_satis_toplam[yazar] += satis
        yazar_kitap_sayisi[yazar] += 1
    else:
        yazar_satis_toplam[yazar] = satis
        yazar_kitap_sayisi[yazar] = 1

yazar_ortalama_satis = {yazar: yazar_satis_toplam[yazar] / yazar_kitap_sayisi[yazar] for yazar in yazar_satis_toplam}

print("\nEğitim Verisinden Yazar Ortalama Satışları:")
print(yazar_ortalama_satis)

# Test verisinde, hangi kitapların satışlarının bu ortalamanın üzerinde olduğunu kontrol edin.
print("\nTest Verisindeki Kitapların Ortalama Üzerinde Satışları:")
for kitap in test_data:
    yazar = kitap["yazar"]
    satis = kitap["satis"]
    if yazar in yazar_ortalama_satis and satis > yazar_ortalama_satis[yazar]:
        print(f"{kitap['isim']} (Yazar: {yazar}): Satış ({satis}) ortalama ({yazar_ortalama_satis[yazar]:.2f}) üzerinde.")
    elif yazar in yazar_ortalama_satis:
         print(f"{kitap['isim']} (Yazar: {yazar}): Satış ({satis}) ortalama ({yazar_ortalama_satis[yazar]:.2f}) altında veya eşit.")
    else:
        print(f"{kitap['isim']} (Yazar: {yazar}): Eğitim verisinde yazar bilgisi bulunamadı.")