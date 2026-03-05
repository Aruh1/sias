"""
ERD Banyak Relasi - Sistem Informasi Akademik Sekolah (SIAS)
ERD lengkap: 3 Entitas + Junction NILAI, relasi 1:N dan M:N
Notasi: Yourdon & DeMarco (Chen-style ERD).
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def draw_erd_banyak_relasi():
    fig, ax = plt.subplots(1, 1, figsize=(20, 14))
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 14)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor("white")

    # ── Judul ──
    ax.text(
        10,
        13.5,
        "ERD Banyak Relasi - Sistem Informasi Akademik Sekolah (SIAS)",
        ha="center",
        va="center",
        fontsize=16,
        fontweight="bold",
        color="black",
    )
    ax.text(
        10,
        13.0,
        "Notasi: Yourdon & DeMarco",
        ha="center",
        va="center",
        fontsize=10,
        fontstyle="italic",
        color="gray",
    )

    # ── Palet (hitam-putih) ──
    EDGE = "black"
    TXT = "black"
    LINE_C = "black"

    # ── Helper: Entitas (kotak) ──
    def entity(cx, cy, label):
        w, h = 3.2, 1.3
        r = mpatches.FancyBboxPatch(
            (cx - w / 2, cy - h / 2),
            w,
            h,
            boxstyle="square,pad=0",
            fc="white",
            ec=EDGE,
            lw=2,
        )
        ax.add_patch(r)
        ax.text(
            cx,
            cy,
            label,
            ha="center",
            va="center",
            fontsize=13,
            fontweight="bold",
            color=TXT,
        )

    # ── Helper: Relasi (diamond) ──
    def relation(cx, cy, label, size=1.0):
        diamond = mpatches.RegularPolygon(
            (cx, cy),
            numVertices=4,
            radius=size,
            orientation=0,
            fc="white",
            ec=EDGE,
            lw=2,
        )
        ax.add_patch(diamond)
        ax.text(
            cx,
            cy,
            label,
            ha="center",
            va="center",
            fontsize=10,
            fontweight="bold",
            color=TXT,
        )

    # ── Helper: Atribut (elips) ──
    def attribute(cx, cy, label, is_pk=False, is_fk=False):
        lw = 2.0 if (is_pk or is_fk) else 1.2
        ls = "--" if is_fk else "-"
        e = mpatches.Ellipse(
            (cx, cy), 1.9, 0.65, fc="white", ec=EDGE, lw=lw, linestyle=ls
        )
        ax.add_patch(e)
        # PK underlined
        if is_pk:
            ax.text(
                cx,
                cy,
                label,
                ha="center",
                va="center",
                fontsize=8,
                color=TXT,
                fontweight="bold",
            )
            tw = len(label) * 0.07
            ax.plot([cx - tw, cx + tw], [cy - 0.13, cy - 0.13], color=TXT, lw=1.5)
        elif is_fk:
            ax.text(
                cx,
                cy,
                label,
                ha="center",
                va="center",
                fontsize=8,
                color=TXT,
                fontstyle="italic",
            )
        else:
            ax.text(cx, cy, label, ha="center", va="center", fontsize=8, color=TXT)

    # ── Helper: Garis ──
    def line(x1, y1, x2, y2):
        ax.plot([x1, x2], [y1, y2], color=LINE_C, lw=1.0, zorder=0)

    # ══════════ POSISI ══════════
    SISWA = (4.0, 10.0)
    GURU = (16.0, 10.0)
    MAPEL = (10.0, 5.0)
    NILAI_ENT = (4.0, 5.0)

    R_MENGAJAR = (13.0, 7.5)
    R_MEMILIKI = (4.0, 7.5)
    R_UNTUK = (7.0, 5.0)

    # ══════════ GAMBAR ══════════
    entity(*SISWA, "SISWA")
    entity(*GURU, "GURU")
    entity(*MAPEL, "MATA_PELAJARAN")
    entity(*NILAI_ENT, "NILAI\n(Junction)")

    relation(*R_MENGAJAR, "Mengajar", size=0.9)
    relation(*R_MEMILIKI, "Memiliki", size=0.9)
    relation(*R_UNTUK, "Untuk", size=0.9)

    # ── Garis + Kardinalitas ──
    line(GURU[0], GURU[1] - 0.65, R_MENGAJAR[0], R_MENGAJAR[1] + 0.9)
    line(R_MENGAJAR[0], R_MENGAJAR[1] - 0.9, MAPEL[0] + 1.6, MAPEL[1] + 0.65)
    ax.text(14.2, 9.0, "1", fontsize=13, fontweight="bold", color=TXT)
    ax.text(11.5, 6.3, "N", fontsize=13, fontweight="bold", color=TXT)

    line(SISWA[0], SISWA[1] - 0.65, R_MEMILIKI[0], R_MEMILIKI[1] + 0.9)
    line(R_MEMILIKI[0], R_MEMILIKI[1] - 0.9, NILAI_ENT[0], NILAI_ENT[1] + 0.65)
    ax.text(3.5, 9.0, "1", fontsize=13, fontweight="bold", color=TXT)
    ax.text(3.5, 6.3, "N", fontsize=13, fontweight="bold", color=TXT)

    line(NILAI_ENT[0] + 1.6, NILAI_ENT[1], R_UNTUK[0] - 0.9, R_UNTUK[1])
    line(R_UNTUK[0] + 0.9, R_UNTUK[1], MAPEL[0] - 1.6, MAPEL[1])
    ax.text(5.8, 5.25, "N", fontsize=13, fontweight="bold", color=TXT)
    ax.text(8.3, 5.25, "1", fontsize=13, fontweight="bold", color=TXT)

    # ══════════ ATRIBUT SISWA ══════════
    siswa_attrs = [
        ("NIS", True, False),
        ("Nama_Siswa", False, False),
        ("Tanggal_Lahir", False, False),
        ("Jenis_Kelamin", False, False),
        ("Alamat", False, False),
        ("No_Telepon", False, False),
        ("Agama", False, False),
    ]
    siswa_pos = [
        (1.2, 12.5),
        (3.0, 12.8),
        (5.0, 12.8),
        (6.8, 12.5),
        (1.5, 11.5),
        (3.5, 11.8),
        (5.5, 11.5),
    ]
    for (lab, pk, fk), (ax_, ay) in zip(siswa_attrs, siswa_pos):
        attribute(ax_, ay, lab, is_pk=pk, is_fk=fk)
        line(ax_, ay - 0.32, SISWA[0], SISWA[1] + 0.65)

    # ══════════ ATRIBUT GURU ══════════
    guru_attrs = [
        ("NIP", True, False),
        ("Nama_Guru", False, False),
        ("Spesialisasi", False, False),
        ("No_Telepon", False, False),
        ("Alamat", False, False),
        ("Email", False, False),
        ("Pendidikan_Terakhir", False, False),
    ]
    guru_pos = [
        (13.2, 12.5),
        (15.0, 12.8),
        (17.0, 12.8),
        (18.8, 12.5),
        (13.5, 11.5),
        (15.5, 11.8),
        (17.5, 11.5),
    ]
    for (lab, pk, fk), (ax_, ay) in zip(guru_attrs, guru_pos):
        attribute(ax_, ay, lab, is_pk=pk, is_fk=fk)
        line(ax_, ay - 0.32, GURU[0], GURU[1] + 0.65)

    # ══════════ ATRIBUT MAPEL ══════════
    mapel_attrs = [
        ("Kode_Mapel", True, False),
        ("Nama_Mapel", False, False),
        ("Tingkat_Kelas", False, False),
        ("KKM", False, False),
        ("Semester", False, False),
        ("Kurikulum", False, False),
    ]
    mapel_pos = [
        (10.0, 3.2),
        (12.0, 3.0),
        (14.0, 3.3),
        (10.0, 2.2),
        (12.0, 2.0),
        (14.0, 2.3),
    ]
    for (lab, pk, fk), (ax_, ay) in zip(mapel_attrs, mapel_pos):
        attribute(ax_, ay, lab, is_pk=pk, is_fk=fk)
        line(ax_, ay + 0.32, MAPEL[0], MAPEL[1] - 0.65)

    # ══════════ ATRIBUT NILAI ══════════
    nilai_attrs = [
        ("ID_Nilai", True, False),
        ("NIS", False, True),
        ("Kode_Mapel", False, True),
        ("Nilai_Tugas", False, False),
        ("Nilai_UTS", False, False),
        ("Nilai_UAS", False, False),
    ]
    nilai_pos = [
        (1.0, 3.2),
        (2.8, 3.0),
        (1.0, 2.2),
        (2.8, 2.0),
        (1.0, 1.2),
        (2.8, 1.0),
    ]
    for (lab, pk, fk), (ax_, ay) in zip(nilai_attrs, nilai_pos):
        attribute(ax_, ay, lab, is_pk=pk, is_fk=fk)
        line(ax_, ay + 0.32, NILAI_ENT[0], NILAI_ENT[1] - 0.65)

    # ── Legenda ──
    ax.text(15.5, 0.8, "Legenda:", fontsize=9, fontweight="bold", color=TXT)
    # PK
    ax.text(15.5, 0.35, "___  = Primary Key (underlined)", fontsize=8, color=TXT)
    # FK
    ax.text(15.5, -0.05, "- - -  = Foreign Key (dashed)", fontsize=8, color=TXT)

    plt.tight_layout()
    plt.savefig(
        "output/erd_banyak_relasi.png",
        dpi=200,
        bbox_inches="tight",
        facecolor=fig.get_facecolor(),
    )
    plt.show()
    print("[OK] ERD Banyak Relasi berhasil disimpan ke output/erd_banyak_relasi.png")


if __name__ == "__main__":
    import os

    os.makedirs("output", exist_ok=True)
    draw_erd_banyak_relasi()
