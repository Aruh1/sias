# Judul Sistem: Sistem Informasi Akademik Sekolah (SIAS)

---

## Daftar Diagram

Semua diagram menggunakan **Mermaid.js** dan tersedia di folder [`graph/`](graph/):

| No  | Diagram           | File                                                 | Keterangan                |
| --- | ----------------- | ---------------------------------------------------- | ------------------------- |
| 1   | DFD Level 0       | [`dfd_level_0.md`](graph/dfd_level_0.md)             | Diagram Konteks           |
| 2   | DFD Level 1       | [`dfd_level_1.md`](graph/dfd_level_1.md)             | 7 Proses, 6 Data Store    |
| 3   | ERD 1 Relasi      | [`erd_1_relasi.md`](graph/erd_1_relasi.md)           | GURU (1:N) MATA_PELAJARAN |
| 4   | ERD Banyak Relasi | [`erd_banyak_relasi.md`](graph/erd_banyak_relasi.md) | 6 Entitas, semua relasi   |
| 5   | Tabel Relasi      | [`tabel_relasi.md`](graph/tabel_relasi.md)           | 6 Tabel, semua FK         |

---

## 1. DFD Level 0 (Diagram Konteks)

Notasi: **Yourdon & DeMarco**

**Entitas Eksternal (3):** Siswa, Guru, Tata Usaha

| Entitas    | Data Masuk ke Sistem                   | Data Keluar dari Sistem          |
| ---------- | -------------------------------------- | -------------------------------- |
| Siswa      | Data Siswa                             | Info Guru, Jadwal, Mapel, Nilai  |
| Guru       | Data Guru, Nilai, Mapel                | Info Siswa, Jadwal, Mapel, Nilai |
| Tata Usaha | Data Siswa, Guru, Mapel, Jadwal, Nilai | Laporan Akademik                 |

---

## 2. DFD Level 1

Notasi: **Yourdon & DeMarco** — Pendataan Guru & Mapel **DIPISAH**.

**A. Entitas Eksternal (3):** Siswa, Guru, Admin / Tata Usaha

**B. Data Store (6):**

| Data Store | Tabel         |
| ---------- | ------------- |
| D1         | tb_siswa      |
| D2         | tb_guru       |
| D3         | tb_mapel      |
| D4         | tb_jadwal     |
| D5         | tb_nilai      |
| D6         | tb_tata_usaha |

**C. Proses (7):**

1. **1.0 Pendaftaran Siswa**
   - *Aliran:* TU memasukkan form data siswa baru → Proses 1.0 menyimpan ke **D1 (tb_siswa)**. Siswa menerima info login.

2. **2.0 Pendataan Guru**
   - *Aliran:* TU menginput profil guru → Proses 2.0 menyimpan ke **D2 (tb_guru)**.

3. **3.0 Penginputan Mapel**
   - *Aliran:* TU menginput data mata pelajaran → Proses 3.0 menyimpan ke **D3 (tb_mapel)**.

4. **4.0 Pengaturan Jadwal**
   - *Aliran:* TU menyusun jadwal menggunakan data dari D1, D2, D3 → Proses 4.0 menyimpan ke **D4 (tb_jadwal)**. Siswa dan Guru menerima info jadwal.

5. **5.0 Pengelolaan Nilai**
   - *Aliran:* Guru/TU memasukkan nilai ujian → Proses 5.0 memvalidasi dari D1 dan D3, lalu menyimpan ke **D5 (tb_nilai)**.

6. **6.0 Pengelolaan Tata Usaha**
   - *Aliran:* TU mengelola data administrasi dengan data dari D1, D2, D3 → Proses 6.0 menyimpan ke **D6 (tb_tata_usaha)**.

7. **7.0 Cetak Laporan Akademik**
   - *Aliran:* Proses 7.0 mengambil data dari D1, D4, D5, D6 → menghasilkan Laporan Rapor untuk Siswa dan arsip untuk TU.

---

## 3. ERD (Entity Relationship Diagram)

**A. Entitas dan Atribut (6 Entitas):**

1. **SISWA**
   - *Atribut:* **NIS (PK)**, Nama_Siswa, Tanggal_Lahir, Jenis_Kelamin, Alamat, No_Telepon, Agama, Kelas.

2. **GURU**
   - *Atribut:* **NIP (PK)**, Nama_Guru, Spesialisasi, No_Telepon, Alamat, Email, Pendidikan_Terakhir.

3. **MATA_PELAJARAN**
   - *Atribut:* **Kode_Mapel (PK)**, Nama_Mapel, Tingkat_Kelas, KKM, Semester, Kurikulum.

4. **NILAI** *(Junction Table: Siswa ↔ Mapel)*
   - *Atribut:* **ID_Nilai (PK)**, NIS (FK), Kode_Mapel (FK), Nilai_Tugas, Nilai_UTS, Nilai_UAS.

5. **JADWAL**
   - *Atribut:* **ID_Jadwal (PK)**, Hari, Jam, NIP (FK), Kelas, Kode_Mapel (FK).

6. **TATA_USAHA**
   - *Atribut:* **ID_TU (PK)**, NIS (FK), NIP (FK), Kode_Mapel (FK), Nama, Penjaga_TU.

**B. Relasi:**

| Relasi            | Entitas 1      | Entitas 2      | Kardinalitas |
| ----------------- | -------------- | -------------- | ------------ |
| Mengajar          | GURU           | MATA_PELAJARAN | 1 : N        |
| Memiliki          | SISWA          | NILAI          | 1 : N        |
| Untuk             | MATA_PELAJARAN | NILAI          | 1 : N        |
| Mengajar di       | GURU           | JADWAL         | 1 : N        |
| Dijadwalkan       | MATA_PELAJARAN | JADWAL         | 1 : N        |
| Diadministrasikan | SISWA          | TATA_USAHA     | 1 : N        |
| Dicatat           | GURU           | TATA_USAHA     | 1 : N        |
| Dikelola          | MATA_PELAJARAN | TATA_USAHA     | 1 : N        |

---

## 4. Tabel Relasi & Kardinalitas

Skema tabel database relasional (6 tabel):

- **tb_siswa** (`NIS` [PK], `Nama_Siswa`, `Tanggal_Lahir`, `Jenis_Kelamin`, `Alamat`, `No_Telepon`, `Agama`, `Kelas`)
- **tb_guru** (`NIP` [PK], `Nama_Guru`, `Spesialisasi`, `No_Telepon`, `Alamat`, `Email`, `Pendidikan_Terakhir`)
- **tb_mapel** (`Kode_Mapel` [PK], `Nama_Mapel`, `Tingkat_Kelas`, `KKM`, `Semester`, `Kurikulum`, `NIP` [FK])
- **tb_nilai** (`ID_Nilai` [PK], `NIS` [FK], `Kode_Mapel` [FK], `Nilai_Tugas`, `Nilai_UTS`, `Nilai_UAS`)
- **tb_jadwal** (`ID_Jadwal` [PK], `Hari`, `Jam`, `NIP` [FK], `Kelas`, `Kode_Mapel` [FK])
- **tb_tata_usaha** (`ID_TU` [PK], `NIS` [FK], `NIP` [FK], `Kode_Mapel` [FK], `Nama`, `Penjaga_TU`)

**Kardinalitas (Penjelasan):**

1. **1:N — GURU → MATA_PELAJARAN**
   - 1 Guru mengajar N Mata Pelajaran. `NIP` dari tb_guru masuk sebagai FK ke tb_mapel.

2. **M:N — SISWA ↔ MATA_PELAJARAN** *(dipecah via tb_nilai)*
   - M Siswa mengambil N Mata Pelajaran. Dipecah menjadi junction table **tb_nilai**.

3. **1:N — SISWA → NILAI**
   - 1 Siswa memiliki N rekaman Nilai.

4. **1:N — GURU → JADWAL**
   - 1 Guru punya N slot Jadwal mengajar.

5. **1:N — MATA_PELAJARAN → JADWAL**
   - 1 Mata Pelajaran dijadwalkan N kali.

6. **TATA_USAHA** *(Junction/Admin)*
   - Menghubungkan SISWA, GURU, MATA_PELAJARAN untuk administrasi akademik.

---