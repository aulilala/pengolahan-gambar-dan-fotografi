import numpy as np
from matplotlib import pyplot as plt

# membuat grafik batang vertikal menggunakan python
# Data for plotting
penjualan = (40, 82, 13, 17, 28, 25, 27)
tahun = (2000, 2001, 2002, 2003, 2004, 2005, 2006)
# untuk menampilkan gambar grafik ke layar.
# memberikan ukuran pada output dengan urutan panjang x lebar
plt.figure(figsize= (10,5)) # untuk ukuran dari luaran
plt.bar(tahun, penjualan)
plt.title("Laporan Penjualan Getah Karet") # untuk memberikan judul
plt.xlabel("Tahun")
plt.ylabel("Penjualan (dalam kg)")
plt.grid()
plt.show()


# membuat grafik batang horizontal menggunakan python
# Data for plotting
penjualan = (40, 82, 13, 17, 28, 25, 27)
tahun = (2000, 2001, 2002, 2003, 2004, 2005, 2006)
# untuk menampilkan gambar grafik ke layar.
# memberikan ukuran pada output dengan urutan panjang x lebar
plt.figure(figsize= (10,5)) # untuk ukuran dari luaran
plt.barh(tahun, penjualan)
plt.title("Laporan Penjualan Getah Karet") # untuk memberikan judul
plt.xlabel("Tahun")
plt.ylabel("Penjualan (dalam kg)")
plt.grid()
plt.show()


# membuat grafik garis menggunakan python
# Data for plotting
penjualan = (40, 82, 13, 17, 28, 25, 27)
tahun = (2000, 2001, 2002, 2003, 2004, 2005, 2006)
# untuk menampilkan gambar grafik ke layar.
# memberikan ukuran pada output dengan urutan panjang x lebar
plt.figure(figsize= (10,5)) # untuk ukuran dari luaran
plt.plot(tahun, penjualan)
plt.title("Laporan Penjualan Getah Karet") # untuk memberikan judul
plt.xlabel("Tahun")
plt.ylabel("Penjualan (dalam kg)")
plt.grid()
plt.show()


# membuat grafik lingkaran menggunakan python
# Data for plotting
penjualan = (40, 82, 13, 17, 28, 25, 27)
tahun = (2000, 2001, 2002, 2003, 2004, 2005, 2006)
# untuk menampilkan gambar grafik ke layar.
# memberikan ukuran pada output dengan urutan panjang x lebar
plt.figure(figsize= (10,5)) # untuk ukuran dari luaran
plt.pie(penjualan, labels=tahun)
plt.title("Laporan Penjualan Getah Karet") # untuk memberikan judul
plt.xlabel("Tahun")
plt.ylabel("Penjualan (dalam kg)")
plt.grid()
plt.show()


# membuat  grafik lingkaran terpisah menggunakan python
# Data for plotting
penjualan = (40, 82, 13, 17, 28, 25, 27)
tahun = (2000, 2001, 2002, 2003, 2004, 2005, 2006)
# untuk menampilkan gambar grafik ke layar.
# memberikan ukuran pada output dengan urutan panjang x lebar
explode = (0, 0.1, 0, 0, 0, 0, 0)

plt.figure(figsize= (10,5)) # untuk ukuran dari luaran
plt.pie(penjualan, explode=explode, labels=tahun)
plt.title("Laporan Penjualan Getah Karet") # untuk memberikan judul
plt.xlabel("Tahun")
plt.ylabel("Penjualan (dalam kg)")
plt.grid()
plt.show()


# membuat  grafik garis 2 menggunakan python
# Data for plotting
penjualan1 = (40, 82, 13, 17, 28 )
tahun1 = (2000, 2001, 2002, 2003, 2004 )
penjualan2 = (50, 66, 25, 45, 31)
tahun2 = (2010, 2011, 2012, 2013, 2014)
#grafik 1
plt.figure(figsize= (7, 5)) # untuk ukuran dari luaran
plt.subplot(2, 1, 1)
plt. plot (tahun1, penjualan1)
plt.title("Laporan Penjualan Getah Karet Semester 1") # untuk memberikan judul
plt.xlabel("Tahun")
plt.ylabel("Penjualan (dalam kg)")
plt.grid()
plt.show()
#grafik 2
plt.subplot(2, 1, 1)
plt.plot(tahun2, penjualan2)
plt.title("Laporan Penjualan Getah Karet Semester 2") # untuk memberikan judul
plt.xlabel("Tahun")
plt.ylabel("Penjualan (dalam kg)")
plt.grid ()
plt.tight_layout()
plt.show()
