# Judul Sistem: Sistem Informasi Akademik Sekolah (SIAS)

---

## 1. DFD Level 1 (Data Flow Diagram)

**A. Entitas Eksternal (3 Entitas):**

1. Siswa
2. Guru
3. Admin / Tata Usaha

**B. Data Store (5 Data Store):**

* **D1:** Data Siswa
* **D2:** Data Guru
* **D3:** Data Mata Pelajaran (Mapel)
* **D4:** Data Jadwal
* **D5:** Data Nilai

**C. Proses Utama (5 Proses):**

1. **1.0 Registrasi & Pendataan Siswa**
* *Aliran:* Admin memasukkan form data siswa baru $\rightarrow$ Proses 1.0 menyimpan data ke **D1 (Data Siswa)**. Admin memberikan info login ke Siswa.


2. **2.0 Pendataan Guru & Mapel**
* *Aliran:* Admin menginput profil guru dan daftar mata pelajaran $\rightarrow$ Proses 2.0 menyimpan data ke **D2 (Data Guru)** dan **D3 (Data Mapel)**.


3. **3.0 Pengaturan Jadwal Pelajaran**
* *Aliran:* Admin mengambil data dari D2 dan D3 untuk menyusun jadwal $\rightarrow$ Proses 3.0 menyimpan jadwal ke **D4 (Data Jadwal)**. Guru dan Siswa menerima informasi jadwal dari proses ini.


4. **4.0 Pengelolaan Nilai Akademik**
* *Aliran:* Guru memasukkan nilai ujian siswa $\rightarrow$ Proses 4.0 memvalidasi berdasarkan D1 dan D3, lalu menyimpannya ke **D5 (Data Nilai)**.


5. **5.0 Cetak Laporan Akademik (Rapor)**
* *Aliran:* Proses 5.0 mengambil data dari D1, D4, dan D5 $\rightarrow$ menghasilkan Laporan Hasil Belajar (Rapor) yang diberikan kepada Siswa dan diarsipkan oleh Admin.



---

## 2. ERD Full Relasi (Entity Relationship Diagram)

**A. Entitas dan Atribut (3 Entitas, Masing-masing > 5 Atribut):**

1. **Entitas: SISWA**
* *Atribut:* **NIS (Primary Key)**, Nama_Siswa, Tanggal_Lahir, Jenis_Kelamin, Alamat, No_Telepon, Agama.


2. **Entitas: GURU**
* *Atribut:* **NIP (Primary Key)**, Nama_Guru, Spesialisasi, No_Telepon, Alamat, Email, Pendidikan_Terakhir.


3. **Entitas: MATA_PELAJARAN**
* *Atribut:* **Kode_Mapel (Primary Key)**, Nama_Mapel, Tingkat_Kelas, KKM (Kriteria Ketuntasan Minimal), Semester, Kurikulum.



**B. Relasi Tambahan (Junction Table):**

* **Relasi NILAI** (Menghubungkan Siswa dan Mata Pelajaran)
* *Atribut:* **ID_Nilai (Primary Key)**, NIS (Foreign Key), Kode_Mapel (Foreign Key), Nilai_Tugas, Nilai_UTS, Nilai_UAS.



---

## 3. Tabel Relasi & Kardinalitas

Berdasarkan ERD di atas, berikut adalah skema tabel database relasionalnya:

* **tb_siswa** (`NIS` [PK], `Nama_Siswa`, `Tanggal_Lahir`, `Jenis_Kelamin`, `Alamat`, `No_Telepon`, `Agama`)
* **tb_guru** (`NIP` [PK], `Nama_Guru`, `Spesialisasi`, `No_Telepon`, `Alamat`, `Email`, `Pendidikan_Terakhir`)
* **tb_mapel** (`Kode_Mapel` [PK], `Nama_Mapel`, `Tingkat_Kelas`, `KKM`, `Semester`, `Kurikulum`, `NIP` [FK])
* **tb_nilai** (`ID_Nilai` [PK], `NIS` [FK], `Kode_Mapel` [FK], `Nilai_Tugas`, `Nilai_UTS`, `Nilai_UAS`)

**Kardinalitas (3 Jenis Relasi Utama):**

1. **One-to-Many (1:N) - Antara `GURU` dan `MATA_PELAJARAN**`
* *Penjelasan:* 1 (Satu) orang Guru dapat mengajar N (Banyak) Mata Pelajaran, tetapi 1 (Satu) Mata Pelajaran dalam sistem ini ditetapkan hanya diajar oleh 1 Guru (sebagai penanggung jawab). Oleh karena itu, *Primary Key* `NIP` dari tabel Guru masuk sebagai *Foreign Key* ke tabel Mapel.


2. **Many-to-Many (M:N) - Antara `SISWA` dan `MATA_PELAJARAN**`
* *Penjelasan:* M (Banyak) Siswa dapat mengambil N (Banyak) Mata Pelajaran, dan sebaliknya. Karena database relasional tidak bisa menangani M:N secara langsung, relasi ini dipecah menjadi tabel baru (tabel *junction/intersection*), yaitu tabel **`tb_nilai`**.


3. **One-to-Many (1:N) - Antara `SISWA` dan `NILAI**`
* *Penjelasan:* Sebagai hasil pemecahan M:N di atas, 1 (Satu) Siswa dapat memiliki N (Banyak) rekaman Nilai (untuk berbagai mata pelajaran), namun 1 (Satu) rekaman nilai tersebut hanya dimiliki secara spesifik oleh 1 (Satu) Siswa.



---