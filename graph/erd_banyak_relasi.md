# ERD Banyak Relasi - Sistem Informasi Akademik Sekolah (SIAS)

```mermaid
---
title: ERD Banyak Relasi - Sistem Informasi Akademik Sekolah (SIAS)
config:
    layout: elk
---

erDiagram
    SISWA {
        string NIS PK "Primary Key"
        string Nama_Siswa
        date Tanggal_Lahir
        string Jenis_Kelamin
        string Alamat
        string No_Telepon
        string Agama
        string Kelas
    }

    GURU {
        string NIP PK "Primary Key"
        string Nama_Guru
        string Spesialisasi
        string No_Telepon
        string Alamat
        string Email
        string Pendidikan_Terakhir
    }

    MATA_PELAJARAN {
        string Kode_Mapel PK "Primary Key"
        string Nama_Mapel
        string Tingkat_Kelas
        int KKM
        string Semester
        string Kurikulum
    }

    NILAI {
        int ID_Nilai PK "Primary Key"
        string NIS FK "FK -> SISWA"
        string Kode_Mapel FK "FK -> MATA_PELAJARAN"
        float Nilai_Tugas
        float Nilai_UTS
        float Nilai_UAS
    }

    JADWAL {
        int ID_Jadwal PK "Primary Key"
        string Hari
        string Jam
        string NIP FK "FK -> GURU"
        string Kelas
        string Kode_Mapel FK "FK -> MATA_PELAJARAN"
    }

    TATA_USAHA {
        int ID_TU PK "Primary Key"
        string NIS FK "FK -> SISWA"
        string NIP FK "FK -> GURU"
        string Kode_Mapel FK "FK -> MATA_PELAJARAN"
        string Nama
        string Penjaga_TU
    }

    %% Relasi GURU - MAPEL (1:N)
    GURU ||--o{ MATA_PELAJARAN : "Mengajar"

    %% Relasi SISWA - NILAI (1:N) — junction M:N Siswa-Mapel
    SISWA ||--o{ NILAI : "Memiliki"
    MATA_PELAJARAN ||--o{ NILAI : "Untuk"

    %% Relasi JADWAL
    GURU ||--o{ JADWAL : "Mengajar di"
    MATA_PELAJARAN ||--o{ JADWAL : "Dijadwalkan"

    %% Relasi TATA_USAHA (menghubungkan Siswa, Guru, Mapel)
    SISWA ||--o{ TATA_USAHA : "Diadministrasikan"
    GURU ||--o{ TATA_USAHA : "Dicatat"
    MATA_PELAJARAN ||--o{ TATA_USAHA : "Dikelola"
```

> **Kardinalitas:**
> - GURU (1) --- (N) MATA_PELAJARAN → 1 Guru mengajar banyak Mapel
> - SISWA (M) --- (N) MATA_PELAJARAN → dipecah via tabel NILAI
> - GURU (1) --- (N) JADWAL → 1 Guru punya banyak Jadwal
> - MATA_PELAJARAN (1) --- (N) JADWAL → 1 Mapel dijadwalkan banyak kali
> - TATA_USAHA menghubungkan SISWA, GURU, MATA_PELAJARAN untuk administrasi
