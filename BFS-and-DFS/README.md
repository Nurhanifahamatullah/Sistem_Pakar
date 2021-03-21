# Sistem Pakar " Breadth first search (BFS) dan Depth First Search (DFS)

  Breadth first search (BFS) adalah algoritma yang melakukan pencarian secara melebar yang mengunjungi node secara preorder yaitu mengunjungi suatu node kemudian mengunjungi semua node yang bertetangga dengan node tersebut terlebih dahulu. Selanjutnya, node yang belum dikunjungi dan bertetangga dengan node-node yang tadi dikunjungi , demikian seterusnya. Jika graf berbentuk pohon berakar, maka semua node pada aras d dikunjungi lebih dahulu sebelum node-node pada aras d+1. 
  Algoritma ini memerlukan sebuah antrian q untuk menyimpan node yang telah dikunjungi. Node-node ini diperlukan sebagai acuan untuk mengunjungi node-node yang bertetanggaan dengannya. Tiap node yang telah dikunjungi masuk ke dalam antrian hanya satu kali. 
  Cara Kerja Algoritma BFS :
  1. Masukkan simpul ujung (akar) ke dalam antrian.
  2. Ambil simpul dari awal antrian, lalu cek apakah simpul merupakan solusi.
  3. Jika simpul merupakan solusi, pencarian selesai dan hasil dikembalikan.
  4. Jika simpul bukan solusi, masukkan seluruh simpul yang bertetangga dengan simpul tersebut (simpul anak) ke dalam antrian.
  5. Jika antrian kosong dan setiap simpul sudah dicek, pencarian selesai dan mengembalikan hasil solusi tidak ditemukan.
  6. Ulangi pencarian dari langkah kedua.
  Contohnya, 
  peta = {'A':set(['B']),
        'B':set(['C','A']),
        'C':set(['H','B','I','D']),
        'D':set(['C','E','H','F']),
        'E':set(['D']),
        'F':set(['D','G']),
        'G':set(['F','H']),
        'H':set(['L','C','G','D']),
        'I':set(['C','J','K']),
        'J':set(['I']),
        'K':set(['L','I']),
        'L':set(['K','H'])}
  saat kita menjalankan program Akan tampil kotak dialog kosongan untuk menuliskan program yang akan kita jalankan.
  Tulis bfs(graf, ‘A’, ‘L’)
  ‘A’ = awal
  ‘L’ = tujuan
  Setelah itu munculah jalur yang dilewati dari awal ‘A’ sampai tujuan ‘L’, yaitu ['A', 'B', 'C', 'H', 'L'] 

  Sedangkan  Depth First Search (DFS) adalah salah satu algoritma penelusuran struktur graf / pohon berdasarkan kedalaman. Node ditelusuri dari root kemudian ke salah satu node anaknya ( misalnya prioritas penelusuran berdasarkan anak pertama [Node sebelah kiri] ), maka penelusuran dilakukan terus melalui node anak pertama dari node anak pertama level sebelumnya hingga mencapai level terdalam. 
  Setelah sampai di level terdalam, penelusuran akan kembali ke 1 level sebelumnya untuk menelusuri node anak kedua pada pohon biner [node sebelah kanan] lalu kembali ke langkah sebelumnya dengan menelusuri node anak pertama lagi sampai level terdalam dan seterusnya.
  Contohnya,
  peta = {'A':set(['B']),
        'B':set(['C','A']),
        'C':set(['H','B','I','D']),
        'D':set(['C','E','H','F']),
        'E':set(['D']),
        'F':set(['D','G']),
        'G':set(['F','H']),
        'H':set(['L','C','G','D']),
        'I':set(['C','J','K']),
        'J':set(['I']),
        'K':set(['L','I']),
        'L':set(['K','H'])}
  saat kita menjalankan program Akan tampil kotak dialog kosongan untuk menuliskan program yang akan kita jalankan.
  Tulis dfs(graf, ‘A’, ‘L’)
  ‘A’ = awal
  ‘L’ = tujuan
  Setelah itu munculah jalur yang dilewati dari awal ‘A’ sampai tujuan ‘L’, yaitu ['A', 'B', 'C', 'I', 'K', 'L']
  