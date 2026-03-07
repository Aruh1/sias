# Tabel Relasi - Sistem Informasi Akademik Sekolah (SIAS)

```mermaid
---
title: Tabel Relasi - Sistem Informasi Akademik Sekolah (SIAS)
config:
    layout: elk
--- 
erDiagram
    tb_siswa {
        string NIS PK
        string Nama_Siswa
        date Tanggal_Lahir
        string Jenis_Kelamin
        string Alamat
        string No_Telepon
        string Agama
        string Kelas
    }

    tb_guru {
        string NIP PK
        string Nama_Guru
        string Spesialisasi
        string No_Telepon
        string Alamat
        string Email
        string Pendidikan_Terakhir
    }

    tb_mapel {
        string Kode_Mapel PK
        string Nama_Mapel
        string Tingkat_Kelas
        int KKM
        string Semester
        string Kurikulum
        string NIP FK "FK -> tb_guru"
    }

    tb_nilai {
        int ID_Nilai PK
        string NIS FK "FK -> tb_siswa"
        string Kode_Mapel FK "FK -> tb_mapel"
        float Nilai_Tugas
        float Nilai_UTS
        float Nilai_UAS
    }

    tb_jadwal {
        int ID_Jadwal PK
        string Hari
        string Jam
        string NIP FK "FK -> tb_guru"
        string Kelas
        string Kode_Mapel FK "FK -> tb_mapel"
    }

    tb_tata_usaha {
        int ID_TU PK
        string NIS FK "FK -> tb_siswa"
        string NIP FK "FK -> tb_guru"
        string Kode_Mapel FK "FK -> tb_mapel"
        string Nama
        string Penjaga_TU
    }

    %% Foreign Key Relationships
    tb_guru ||--o{ tb_mapel : "NIP (1:N)"
    tb_siswa ||--o{ tb_nilai : "NIS (1:N)"
    tb_mapel ||--o{ tb_nilai : "Kode_Mapel (1:N)"
    tb_guru ||--o{ tb_jadwal : "NIP (1:N)"
    tb_mapel ||--o{ tb_jadwal : "Kode_Mapel (1:N)"
    tb_siswa ||--o{ tb_tata_usaha : "NIS (1:N)"
    tb_guru ||--o{ tb_tata_usaha : "NIP (1:N)"
    tb_mapel ||--o{ tb_tata_usaha : "Kode_Mapel (1:N)"
```

> **Kardinalitas:**
> - GURU (1) --- (N) MAPEL → 1 Guru mengajar banyak Mapel
> - SISWA (1) --- (N) NILAI → 1 Siswa punya banyak Nilai
> - MAPEL (1) --- (N) NILAI → 1 Mapel punya banyak Nilai
> - GURU (1) --- (N) JADWAL → 1 Guru punya banyak Jadwal
> - MAPEL (1) --- (N) JADWAL → 1 Mapel dijadwalkan banyak kali
> - TATA_USAHA → Junction/admin yang menghubungkan Siswa, Guru, Mapel
