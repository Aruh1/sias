# DFD Level 0 - Sistem Informasi Akademik Sekolah (SIAS)

```mermaid
flowchart LR
    %% Entitas Eksternal
    Siswa["Siswa"]
    Guru["Guru"]
    Admin["Admin / Tata Usaha"]

    %% Proses Utama
    SIAS(("0.0\nSistem Informasi\nAkademik Sekolah\n(SIAS)"))

    %% Aliran Data
    Siswa -- "Data Pendaftaran" --> SIAS
    SIAS -- "Info Login, Jadwal, Rapor" --> Siswa

    Guru -- "Input Nilai" --> SIAS
    SIAS -- "Info Jadwal" --> Guru

    Admin -- "Data Siswa, Guru,\nMapel, Jadwal" --> SIAS
    SIAS -- "Laporan Akademik" --> Admin

    %% Styling
    style Siswa fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#000
    style Guru fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#000
    style Admin fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#000
    style SIAS fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#000
```
