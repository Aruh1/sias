# ERD Banyak Relasi - Sistem Informasi Akademik Sekolah (SIAS)
> **Notasi: Yourdon & DeMarco (Chen-style ERD)**

```mermaid
erDiagram
    SISWA {
        string NIS PK "Primary Key"
        string Nama_Siswa
        date Tanggal_Lahir
        string Jenis_Kelamin
        string Alamat
        string No_Telepon
        string Agama
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
        string NIS FK "Foreign Key -> SISWA"
        string Kode_Mapel FK "Foreign Key -> MAPEL"
        float Nilai_Tugas
        float Nilai_UTS
        float Nilai_UAS
    }

    GURU ||--o{ MATA_PELAJARAN : "Mengajar"
    SISWA ||--o{ NILAI : "Memiliki"
    MATA_PELAJARAN ||--o{ NILAI : "Untuk"
```

> **Kardinalitas:**
> - GURU (1) --- (N) MATA_PELAJARAN → 1 Guru mengajar banyak Mapel
> - SISWA (M) --- (N) MATA_PELAJARAN → dipecah via tabel NILAI (Junction)
> - SISWA (1) --- (N) NILAI → 1 Siswa punya banyak Nilai
