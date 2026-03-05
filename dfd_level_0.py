"""
DFD Level 0 - Sistem Informasi Akademik Sekolah (SIAS)
Diagram Konteks — Notasi Yourdon & DeMarco.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def draw_dfd_level_0():
    fig, ax = plt.subplots(1, 1, figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor("white")

    # ── Judul ──
    ax.text(
        7,
        8.5,
        "DFD Level 0 - Sistem Informasi Akademik Sekolah",
        ha="center",
        va="center",
        fontsize=16,
        fontweight="bold",
        color="black",
    )
    ax.text(
        7,
        8.0,
        "Notasi: Yourdon & DeMarco",
        ha="center",
        va="center",
        fontsize=10,
        fontstyle="italic",
        color="gray",
    )

    # ── Warna & Style ──
    ENTITY_EDGE = "black"
    PROC_EDGE = "black"
    ARROW_C = "black"
    TXT = "black"

    # ── Helper: Entitas Eksternal (kotak) ──
    def draw_entity(cx, cy, label):
        w, h = 2.6, 1.2
        rect = mpatches.FancyBboxPatch(
            (cx - w / 2, cy - h / 2),
            w,
            h,
            boxstyle="square,pad=0",
            facecolor="white",
            edgecolor=ENTITY_EDGE,
            linewidth=2,
        )
        ax.add_patch(rect)
        ax.text(
            cx,
            cy,
            label,
            ha="center",
            va="center",
            fontsize=12,
            fontweight="bold",
            color=TXT,
        )

    # ── Helper: Proses (lingkaran / bubble) ──
    def draw_process(cx, cy, label, radius=1.5):
        circle = plt.Circle(
            (cx, cy),
            radius,
            facecolor="white",
            edgecolor=PROC_EDGE,
            linewidth=2,
        )
        ax.add_patch(circle)
        ax.text(
            cx,
            cy,
            label,
            ha="center",
            va="center",
            fontsize=10,
            fontweight="bold",
            color=TXT,
            linespacing=1.5,
        )

    # ── Helper: Panah lurus ──
    def draw_arrow(x1, y1, x2, y2, label, label_side="above"):
        ax.annotate(
            "",
            xy=(x2, y2),
            xytext=(x1, y1),
            arrowprops=dict(arrowstyle="-|>", color=ARROW_C, lw=1.5),
        )
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        offset = 0.25 if label_side == "above" else -0.25
        if abs(y2 - y1) < 0.5:
            ax.text(
                mx,
                my + offset,
                label,
                ha="center",
                va="center",
                fontsize=8,
                color="black",
                fontstyle="italic",
            )
        else:
            ax.text(
                mx + offset * 2,
                my,
                label,
                ha="center",
                va="center",
                fontsize=8,
                color="black",
                fontstyle="italic",
            )

    # ── Posisi ──
    siswa_pos = (2.0, 4.5)
    guru_pos = (12.0, 4.5)
    admin_pos = (7.0, 1.2)
    proc_pos = (7.0, 4.5)

    # ── Gambar ──
    draw_entity(*siswa_pos, "Siswa")
    draw_entity(*guru_pos, "Guru")
    draw_entity(*admin_pos, "Admin /\nTata Usaha")
    draw_process(*proc_pos, "0.0\nSistem Informasi\nAkademik Sekolah\n(SIAS)")

    # ── Panah Siswa <-> Proses ──
    draw_arrow(3.4, 4.8, 5.5, 4.8, "Info Login, Jadwal, Rapor", "above")
    draw_arrow(5.5, 4.2, 3.4, 4.2, "Data Pendaftaran", "below")

    # ── Panah Guru <-> Proses ──
    draw_arrow(10.6, 4.8, 8.5, 4.8, "Info Jadwal", "above")
    draw_arrow(8.5, 4.2, 10.6, 4.2, "Input Nilai", "below")

    # ── Panah Admin <-> Proses ──
    draw_arrow(7.5, 1.8, 7.8, 3.0, "Laporan Akademik", "above")
    draw_arrow(6.2, 3.0, 6.5, 1.8, "Data Siswa, Guru,\nMapel, Jadwal", "above")

    plt.tight_layout()
    plt.savefig(
        "output/dfd_level_0.png",
        dpi=200,
        bbox_inches="tight",
        facecolor=fig.get_facecolor(),
    )
    plt.show()
    print("[OK] DFD Level 0 berhasil disimpan ke output/dfd_level_0.png")


if __name__ == "__main__":
    import os

    os.makedirs("output", exist_ok=True)
    draw_dfd_level_0()
