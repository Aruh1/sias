"""
DFD Level 1 - Sistem Informasi Akademik Sekolah (SIAS)
3 Entitas, 5 Data Store, 5 Proses — Notasi Yourdon & DeMarco.
Data Store = dua garis paralel horizontal terbuka (open-ended).
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def draw_dfd_level_1():
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
        "DFD Level 1 - Sistem Informasi Akademik Sekolah (SIAS)",
        ha="center",
        va="center",
        fontsize=18,
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

    # ── Palet (hitam-putih Yourdon/DeMarco) ──
    EDGE = "black"
    TXT = "black"
    ARROW_C = "black"

    # ── Helper: Entitas Eksternal (kotak persegi) ──
    def entity(cx, cy, text):
        w, h = 2.4, 1.0
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
            text,
            ha="center",
            va="center",
            fontsize=11,
            fontweight="bold",
            color=TXT,
        )

    # ── Helper: Proses (lingkaran / bubble) ──
    def process(cx, cy, pid, text, r=0.85):
        c = plt.Circle((cx, cy), r, fc="white", ec=EDGE, lw=2)
        ax.add_patch(c)
        ax.text(
            cx,
            cy + 0.2,
            pid,
            ha="center",
            va="center",
            fontsize=9,
            fontweight="bold",
            color=TXT,
        )
        ax.text(
            cx,
            cy - 0.2,
            text,
            ha="center",
            va="center",
            fontsize=7.5,
            color=TXT,
            linespacing=1.3,
        )

    # ── Helper: Data Store (dua garis paralel terbuka — Yourdon/DeMarco) ──
    def datastore(cx, cy, did, text):
        w = 3.0
        h = 0.35
        # Dua garis horizontal paralel
        ax.plot(
            [cx - w / 2, cx + w / 2],
            [cy + h, cy + h],
            color=EDGE,
            lw=1.5,
            solid_capstyle="butt",
        )
        ax.plot(
            [cx - w / 2, cx + w / 2],
            [cy - h, cy - h],
            color=EDGE,
            lw=1.5,
            solid_capstyle="butt",
        )
        # Garis vertikal kiri (pemisah ID)
        ax.plot(
            [cx - w / 2 + 0.55, cx - w / 2 + 0.55], [cy - h, cy + h], color=EDGE, lw=1.0
        )
        # Teks ID
        ax.text(
            cx - w / 2 + 0.275,
            cy,
            did,
            ha="center",
            va="center",
            fontsize=9,
            fontweight="bold",
            color=TXT,
        )
        # Teks nama
        ax.text(cx + 0.15, cy, text, ha="center", va="center", fontsize=9, color=TXT)

    # ── Helper: Panah ──
    def arrow(x1, y1, x2, y2, label="", off=(0, 0.2), fs=7):
        ax.annotate(
            "",
            xy=(x2, y2),
            xytext=(x1, y1),
            arrowprops=dict(arrowstyle="-|>", color=ARROW_C, lw=1.2),
        )
        if label:
            mx = (x1 + x2) / 2 + off[0]
            my = (y1 + y2) / 2 + off[1]
            ax.text(
                mx,
                my,
                label,
                ha="center",
                va="center",
                fontsize=fs,
                color="black",
                fontstyle="italic",
            )

    # ══════════ POSISI ══════════
    E_ADMIN = (1.5, 7.0)
    E_SISWA = (18.5, 11.0)
    E_GURU = (18.5, 3.0)

    P1 = (5.0, 11.0)
    P2 = (5.0, 7.0)
    P3 = (10.0, 7.0)
    P4 = (10.0, 3.0)
    P5 = (15.0, 7.0)

    D1 = (10.0, 12.5)
    D2 = (5.0, 4.0)
    D3 = (10.0, 4.8)
    D4 = (15.0, 10.5)
    D5 = (15.0, 4.0)

    # ══════════ GAMBAR ══════════
    entity(*E_ADMIN, "Admin /\nTata Usaha")
    entity(*E_SISWA, "Siswa")
    entity(*E_GURU, "Guru")

    process(*P1, "1.0", "Registrasi &\nPendataan Siswa")
    process(*P2, "2.0", "Pendataan\nGuru & Mapel")
    process(*P3, "3.0", "Pengaturan\nJadwal")
    process(*P4, "4.0", "Pengelolaan\nNilai")
    process(*P5, "5.0", "Cetak Laporan\nAkademik")

    datastore(*D1, "D1", "Data Siswa")
    datastore(*D2, "D2", "Data Guru")
    datastore(*D3, "D3", "Data Mapel")
    datastore(*D4, "D4", "Data Jadwal")
    datastore(*D5, "D5", "Data Nilai")

    # ══════════ ALIRAN (PANAH) ══════════
    # P1: Registrasi
    arrow(2.7, 7.5, 4.2, 10.5, "Form Data\nSiswa Baru", off=(-1.0, 0))
    arrow(5.85, 11.3, 8.5, 12.5, "Simpan Data", off=(0, 0.2))
    arrow(5.85, 11.0, 17.3, 11.0, "Info Login", off=(0, 0.25))

    # P2: Pendataan Guru & Mapel
    arrow(2.7, 7.0, 4.15, 7.0, "Data Guru\n& Mapel", off=(0, 0.3))
    arrow(5.0, 6.15, 5.0, 4.35, "Simpan", off=(-0.5, 0))
    arrow(5.85, 6.5, 8.5, 5.15, "Simpan", off=(0, 0.25))

    # P3: Pengaturan Jadwal
    arrow(6.5, 4.2, 9.15, 6.5, "Data Guru", off=(-0.7, 0.15))
    arrow(10.0, 5.15, 10.0, 6.15, "Data Mapel", off=(0.7, 0))
    arrow(2.7, 6.7, 9.15, 6.8, "Susun Jadwal", off=(0, -0.35))
    arrow(10.85, 7.5, 13.5, 10.3, "Simpan", off=(0.4, 0))
    arrow(10.85, 6.5, 17.3, 3.3, "Info\nJadwal", off=(0.7, 0.3))
    arrow(10.85, 7.5, 17.3, 10.7, "Info\nJadwal", off=(0.5, 0.2))

    # P4: Pengelolaan Nilai
    arrow(17.3, 3.0, 10.85, 3.0, "Input Nilai\nUjian", off=(0, 0.35))
    arrow(10.2, 12.15, 10.3, 3.85, "Validasi\nSiswa", off=(0.7, 0))
    arrow(10.0, 4.45, 10.0, 3.85, "Validasi\nMapel", off=(0.7, 0))
    arrow(10.85, 3.0, 13.5, 3.8, "Simpan Nilai", off=(0, -0.3))

    # P5: Cetak Laporan
    arrow(11.5, 12.3, 14.5, 7.85, "Data\nSiswa", off=(-0.6, 0))
    arrow(15.0, 10.15, 15.0, 7.85, "Data\nJadwal", off=(0.6, 0))
    arrow(15.0, 4.35, 15.0, 6.15, "Data\nNilai", off=(0.6, 0))
    arrow(15.85, 7.5, 17.3, 10.6, "Laporan\nRapor", off=(0.6, 0))
    arrow(14.15, 7.0, 2.7, 6.7, "Arsip\nLaporan", off=(0, -0.35))

    plt.tight_layout()
    plt.savefig(
        "output/dfd_level_1.png",
        dpi=200,
        bbox_inches="tight",
        facecolor=fig.get_facecolor(),
    )
    plt.show()
    print("[OK] DFD Level 1 berhasil disimpan ke output/dfd_level_1.png")


if __name__ == "__main__":
    import os

    os.makedirs("output", exist_ok=True)
    draw_dfd_level_1()
