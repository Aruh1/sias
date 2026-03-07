# ERD 1 Relasi - GURU (1:N) MATA_PELAJARAN

> Notasi Chen: Kotak = Entitas, Diamond = Relasi, Oval = Atribut, **Atribut PK digarisbawahi**

```mermaid
---
title: ERD 1 Relasi - GURU (1:N) MATA_PELAJARAN
---

flowchart LR
    %% ── Entitas ──
    GURU["GURU"]
    MAPEL["MATA_PELAJARAN"]

    %% ── Relasi ──
    R1{"Mengajar"}

    %% ── Koneksi Entitas — Relasi ──
    GURU ---|"1"| R1
    R1 ---|"N"| MAPEL

    %% ── Atribut GURU ──
    G_NIP(["<u>NIP</u>"])
    G_Nama(["Nama_Guru"])
    G_Spesialisasi(["Spesialisasi"])
    G_Telp(["No_Telepon"])
    G_Alamat(["Alamat"])
    G_Email(["Email"])
    G_Pendidikan(["Pendidikan_Terakhir"])

    GURU --- G_NIP
    GURU --- G_Nama
    GURU --- G_Spesialisasi
    GURU --- G_Telp
    GURU --- G_Alamat
    GURU --- G_Email
    GURU --- G_Pendidikan

    %% ── Atribut MATA_PELAJARAN ──
    M_Kode(["<u>Kode_Mapel</u>"])
    M_Nama(["Nama_Mapel"])
    M_Tingkat(["Tingkat_Kelas"])
    M_KKM(["KKM"])
    M_Semester(["Semester"])
    M_Kurikulum(["Kurikulum"])

    MAPEL --- M_Kode
    MAPEL --- M_Nama
    MAPEL --- M_Tingkat
    MAPEL --- M_KKM
    MAPEL --- M_Semester
    MAPEL --- M_Kurikulum

    %% ── Styling ──
    style GURU fill:#fff,stroke:#000,stroke-width:2px,color:#000
    style MAPEL fill:#fff,stroke:#000,stroke-width:2px,color:#000
    style R1 fill:#fff,stroke:#000,stroke-width:2px,color:#000

    style G_NIP fill:#fff,stroke:#000,stroke-width:2px,color:#000
    style G_Nama fill:#fff,stroke:#000,stroke-width:1px,color:#000
    style G_Spesialisasi fill:#fff,stroke:#000,stroke-width:1px,color:#000
    style G_Telp fill:#fff,stroke:#000,stroke-width:1px,color:#000
    style G_Alamat fill:#fff,stroke:#000,stroke-width:1px,color:#000
    style G_Email fill:#fff,stroke:#000,stroke-width:1px,color:#000
    style G_Pendidikan fill:#fff,stroke:#000,stroke-width:1px,color:#000

    style M_Kode fill:#fff,stroke:#000,stroke-width:2px,color:#000
    style M_Nama fill:#fff,stroke:#000,stroke-width:1px,color:#000
    style M_Tingkat fill:#fff,stroke:#000,stroke-width:1px,color:#000
    style M_KKM fill:#fff,stroke:#000,stroke-width:1px,color:#000
    style M_Semester fill:#fff,stroke:#000,stroke-width:1px,color:#000
    style M_Kurikulum fill:#fff,stroke:#000,stroke-width:1px,color:#000
```

> **Kardinalitas:** 1 Guru mengajar banyak Mata Pelajaran (1 : N)
>
> **Legenda:** `[kotak]` = Entitas | `{diamond}` = Relasi | `([oval])` = Atribut | <u>underline</u> = Primary Key
