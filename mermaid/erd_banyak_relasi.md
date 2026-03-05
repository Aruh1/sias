# ERD Banyak Relasi - Sistem Informasi Akademik Sekolah (SIAS)

```mermaid
erDiagram
    SISWA {
        string NIS PK
        string Nama_Siswa
        date Tanggal_Lahir
        string Jenis_Kelamin
        string Alamat
        string No_Telepon
        string Agama
    }

    GURU {
        string NIP PK
        string Nama_Guru
        string Spesialisasi
        string No_Telepon
        string Alamat
        string Email
        string Pendidikan_Terakhir
    }

    MATA_PELAJARAN {
        string Kode_Mapel PK
        string Nama_Mapel
        string Tingkat_Kelas
        int KKM
        string Semester
        string Kurikulum
    }

    NILAI {
        int ID_Nilai PK
        string NIS FK
        string Kode_Mapel FK
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
> - SISWA (M) --- (N) MATA_PELAJARAN → dipecah menjadi tabel NILAI
> - SISWA (1) --- (N) NILAI → 1 Siswa punya banyak Nilai
