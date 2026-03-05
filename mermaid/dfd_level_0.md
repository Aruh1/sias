# DFD Level 0 - Sistem Informasi Akademik Sekolah (SIAS)
> **Notasi: Yourdon & DeMarco**

```mermaid
flowchart LR
    %% Entitas Eksternal (kotak persegi)
    Siswa["Siswa"]
    Guru["Guru"]
    Admin["Admin / Tata Usaha"]

    %% Proses Utama (lingkaran / bubble)
    SIAS(("0.0\nSistem Informasi\nAkademik Sekolah\n(SIAS)"))

    %% Aliran Data
    Siswa -- "Data Pendaftaran" --> SIAS
    SIAS -- "Info Login, Jadwal, Rapor" --> Siswa

    Guru -- "Input Nilai" --> SIAS
    SIAS -- "Info Jadwal" --> Guru

    Admin -- "Data Siswa, Guru,\nMapel, Jadwal" --> SIAS
    SIAS -- "Laporan Akademik" --> Admin

    %% Styling (hitam-putih Yourdon/DeMarco)
    style Siswa fill:#fff,stroke:#000,stroke-width:2px,color:#000
    style Guru fill:#fff,stroke:#000,stroke-width:2px,color:#000
    style Admin fill:#fff,stroke:#000,stroke-width:2px,color:#000
    style SIAS fill:#fff,stroke:#000,stroke-width:2px,color:#000
```
