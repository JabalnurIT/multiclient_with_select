# Tugas 01 Pemrograman Jaringan D

## Anggota Kelompok
<table>
 	<tr>
 		<td> Nama </td>
 		<td> NRP</td>
 	</tr>
 	<tr>
 		<td> Sejati Bakti Raga </td>
 		<td> 5025201007 </td>
 	</tr>
  <tr>
 		<td> Zunia Aswaroh </td>
 		<td> 5025201058 </td>
 	</tr>
  <tr>
 		<td> Jabalnur </td>
 		<td> 5025201241 </td>
 	</tr>
 </table>
 
 ## Membuat Program Client-Server 
 Ketentuan:
 Klien:
- Meminta ke server untuk mengunduh salah satu file pada folder files dengan cara mengirim string: "download nama_file". 
- Menerima isi file dari server
- Melakukan parsing message header. Message header tidak ikut ditulis ke dalam file
- Isi file yang telah diterima dari server, disimpan dalam sebuah file sesuai ekstensi filenya.

Server:
- Menerima pesan berupa "download nama_file"
- Membaca file yang diminta oleh klien
- Menambahkan message header yang diletakkan sebelum isi file dengan struktur sebagai berikut (contoh raw message header):
	file-name: contoh.html,\n
	file-size: 2048,\n
	\n\n
- Mengirim isi file yang telah dibaca ke klien
- Server dapat menangani banyak klien (implementasikan modul select DAN serversocket pada Python, tetapi pada file server yang berbeda).
- Buffer socket = 1024 bytes.

Challenge:
- Mengirim/menerima file yang ukurannya lebih besar daripada buffer pada socket.
- Menggunakan virtual box untuk simulasi dua host atau lebih.

 ## Struktur Folder:
 - 5025201007_5025201058_5025201241
	- client
		- client_select.py
		- client_serversocket.py
	- server
		- server_select.py
		- server_serversocket.py
		- files
		
 ## Cara Menjalankan Program
 
 ### Satu Client
 + Membuka terminal baru
 + kemudian ketikan `python3 server/server_serversocket.py` untuk menjalankan dari sisi server
 + selanjutnya buka terminal baru untuk menjalankan dari sisi client
 + ketikan `python3 client/client_serversocket.py` 
 + terakhir inputkan "download nama_file" pada terminal
 
 ### Multi-client
 + Membuka terminal baru
 + kemudian ketikan `python3 server/server_select.py` untuk menjalankan dari sisi server
 + selanjutnya buka terminal baru untuk menjalankan dari sisi client
 + ketikan `python3 client/client_selet.py` 
 + terakhir inputkan "download nama_file" pada terminal
 
 
