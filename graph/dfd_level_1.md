# DFD Level 1 - Sistem Informasi Akademik Sekolah (SIAS)
> **Notasi: Yourdon & DeMarco**

```mermaid
---
title: DFD Level 1 - Sistem Informasi Akademik Sekolah (SIAS)
config:
    layout: elk
---

flowchart TD
    %% ── Entitas Eksternal (kotak persegi) ──
    TU["Admin / Tata Usaha"]
    Siswa["Siswa"]
    Guru["Guru"]

    %% ── Proses (lingkaran / bubble) ── 7 Proses
    P1(("1.0 Pendaftaran Siswa"))
    P2(("2.0 Pendataan Guru"))
    P3(("3.0 Penginputan Mapel"))
    P4(("4.0 Pengaturan Jadwal"))
    P5(("5.0 Pengelolaan Nilai"))
    P6(("6.0 Pengelolaan Tata Usaha"))
    P7(("7.0 Cetak Laporan Akademik"))

    %% ── Data Store (6 tabel) ──
    D1[("D1 | tb_siswa")]
    D2[("D2 | tb_guru")]
    D3[("D3 | tb_mapel")]
    D4[("D4 | tb_jadwal")]
    D5[("D5 | tb_nilai")]
    D6[("D6 | tb_tata_usaha")]

    %% ── P1: Pendaftaran Siswa ──
    TU -- "Form Data Siswa Baru" --> P1
    P1 -- "Simpan Data Siswa" --> D1
    P1 -- "Info Login" --> Siswa

    %% ── P2: Pendataan Guru (DIPISAH dari Mapel) ──
    TU -- "Data Guru" --> P2
    P2 -- "Simpan Data Guru" --> D2

    %% ── P3: Penginputan Mapel (DIPISAH dari Guru) ──
    TU -- "Data Mapel" --> P3
    P3 -- "Simpan Data Mapel" --> D3

    %% ── P4: Pengaturan Jadwal ──
    TU -- "Susun Jadwal" --> P4
    D2 -- "Data Guru" --> P4
    D3 -- "Data Mapel" --> P4
    D1 -- "Data Siswa" --> P4
    P4 -- "Simpan Jadwal" --> D4
    P4 -- "Info Jadwal" --> Siswa
    P4 -- "Info Jadwal" --> Guru

    %% ── P5: Pengelolaan Nilai ──
    Guru -- "Input Nilai" --> P5
    TU -- "Input Nilai" --> P5
    D1 -- "Validasi Siswa" --> P5
    D3 -- "Validasi Mapel" --> P5
    P5 -- "Simpan Nilai" --> D5

    %% ── P6: Pengelolaan Tata Usaha ──
    TU -- "Data Administrasi" --> P6
    D1 -- "Data Siswa" --> P6
    D2 -- "Data Guru" --> P6
    D3 -- "Data Mapel" --> P6
    P6 -- "Simpan Data TU" --> D6

    %% ── P7: Cetak Laporan Akademik ──
    D1 -- "Data Siswa" --> P7
    D4 -- "Data Jadwal" --> P7
    D5 -- "Data Nilai" --> P7
    D6 -- "Data TU" --> P7
    P7 -- "Laporan Rapor" --> Siswa
    P7 -- "Arsip Laporan" --> TU

    %% ── Styling (hitam-putih Yourdon/DeMarco) ──
    style TU fill:#fff,stroke:#000,stroke-width:2px,color:#000
    style Siswa fill:#fff,stroke:#000,stroke-width:2px,color:#000
    style Guru fill:#fff,stroke:#000,stroke-width:2px,color:#000

    style P1 fill:#fff,stroke:#000,stroke-width:2px,color:#000
    style P2 fill:#fff,stroke:#000,stroke-width:2px,color:#000
    style P3 fill:#fff,stroke:#000,stroke-width:2px,color:#000
    style P4 fill:#fff,stroke:#000,stroke-width:2px,color:#000
    style P5 fill:#fff,stroke:#000,stroke-width:2px,color:#000
    style P6 fill:#fff,stroke:#000,stroke-width:2px,color:#000
    style P7 fill:#fff,stroke:#000,stroke-width:2px,color:#000

    style D1 fill:#fff,stroke:#000,stroke-width:2px,color:#000
    style D2 fill:#fff,stroke:#000,stroke-width:2px,color:#000
    style D3 fill:#fff,stroke:#000,stroke-width:2px,color:#000
    style D4 fill:#fff,stroke:#000,stroke-width:2px,color:#000
    style D5 fill:#fff,stroke:#000,stroke-width:2px,color:#000
    style D6 fill:#fff,stroke:#000,stroke-width:2px,color:#000
```
