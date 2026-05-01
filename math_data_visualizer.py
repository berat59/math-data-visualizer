import matplotlib.pyplot as plt 

def grafik_ciz(veriler):
    plt.plot(veriler, marker='o', linestyle='-', color='b')

    plt.title("Veri Analiz Grafiği") # Grafiğin en üstüne başlık yazar.
    plt.xlabel("Veri Sırası")       # Yatay eksenin (x) adını koyar.
    plt.ylabel("Değerler")          # Dikey eksenin (y) adını koyar.
    plt.grid(True)                 # Arka plana kareli defter gibi ızgara çizgileri ekler.

    print("Grafik oluşturuluyor...")
    plt.show()

input_verisi = input("Grafik için sayıları aralarında boşluk olarak girin: ")
sayilar = [float(x) for x in input_verisi.split()]

if len(sayilar) > 0:
    grafik_ciz(sayilar)
else:
    print("Hiç bir veri girmediniz.")