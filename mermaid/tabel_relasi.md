# Tabel Relasi - Sistem Informasi Akademik Sekolah (SIAS)

```mermaid
erDiagram
    tb_siswa {
        string NIS PK
        string Nama_Siswa
        date Tanggal_Lahir
        string Jenis_Kelamin
        string Alamat
        string No_Telepon
        string Agama
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
        string NIP FK
    }

    tb_nilai {
        int ID_Nilai PK
        string NIS FK
        string Kode_Mapel FK
        float Nilai_Tugas
        float Nilai_UTS
        float Nilai_UAS
    }

    tb_guru ||--o{ tb_mapel : "NIP (1:N)"
    tb_siswa ||--o{ tb_nilai : "NIS (1:N)"
    tb_mapel ||--o{ tb_nilai : "Kode_Mapel (1:N)"
```

> **Kardinalitas:**
> - GURU (1) --- (N) MATA_PELAJARAN → 1 Guru mengajar banyak Mapel
> - SISWA (M) --- (N) MATA_PELAJARAN → dipecah menjadi tabel NILAI
> - SISWA (1) --- (N) NILAI → 1 Siswa punya banyak Nilai
