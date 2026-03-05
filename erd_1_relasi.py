"""
ERD 1 Relasi - Sistem Informasi Akademik Sekolah (SIAS)
ERD dengan 1 relasi: GURU (1:N) MATA_PELAJARAN
Notasi: Yourdon & DeMarco (Chen-style ERD).
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def draw_erd_1_relasi():
    fig, ax = plt.subplots(1, 1, figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor("white")

    # ── Judul ──
    ax.text(
        8,
        9.5,
        "ERD 1 Relasi - GURU (1) ---- (N) MATA PELAJARAN",
        ha="center",
        va="center",
        fontsize=15,
        fontweight="bold",
        color="black",
    )
    ax.text(
        8,
        9.0,
        "Notasi: Yourdon & DeMarco",
        ha="center",
        va="center",
        fontsize=10,
        fontstyle="italic",
        color="gray",
    )

    # ── Palet (hitam-putih) ──
    EDGE = "black"
    PK_EDGE = "black"
    TXT = "black"
    LINE_C = "black"

    # ── Helper: Entitas (kotak) ──
    def entity(cx, cy, label):
        w, h = 3.0, 1.2
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
    def relation(cx, cy, label):
        s = 0.9
        diamond = mpatches.RegularPolygon(
            (cx, cy), numVertices=4, radius=s, orientation=0, fc="white", ec=EDGE, lw=2
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
    def attribute(cx, cy, label, is_pk=False):
        lw = 2.2 if is_pk else 1.3
        e = mpatches.Ellipse((cx, cy), 2.0, 0.7, fc="white", ec=EDGE, lw=lw)
        ax.add_patch(e)
        display = label
        if is_pk:
            # Garis bawah untuk PK (underline)
            ax.text(
                cx,
                cy,
                display,
                ha="center",
                va="center",
                fontsize=9,
                color=TXT,
                fontweight="bold",
            )
            # Underline
            tw = len(label) * 0.08
            ax.plot([cx - tw, cx + tw], [cy - 0.15, cy - 0.15], color=TXT, lw=1.5)
        else:
            ax.text(cx, cy, display, ha="center", va="center", fontsize=9, color=TXT)

    # ── Helper: Garis ──
    def line(x1, y1, x2, y2):
        ax.plot([x1, x2], [y1, y2], color=LINE_C, lw=1.0, zorder=0)

    # ══════════ POSISI ══════════
    GURU = (4.5, 5.0)
    MAPEL = (11.5, 5.0)
    REL = (8.0, 5.0)

    # ══════════ GAMBAR ══════════
    entity(*GURU, "GURU")
    entity(*MAPEL, "MATA_PELAJARAN")
    relation(*REL, "Mengajar")

    line(6.0, 5.0, 7.1, 5.0)
    line(8.9, 5.0, 10.0, 5.0)

    ax.text(6.3, 5.3, "1", fontsize=13, fontweight="bold", color=TXT)
    ax.text(9.5, 5.3, "N", fontsize=13, fontweight="bold", color=TXT)

    # ══════════ ATRIBUT GURU ══════════
    guru_attrs = [
        ("NIP", True),
        ("Nama_Guru", False),
        ("Spesialisasi", False),
        ("No_Telepon", False),
        ("Alamat", False),
        ("Email", False),
        ("Pendidikan_Terakhir", False),
    ]
    guru_positions = [
        (1.5, 7.5),
        (3.5, 7.8),
        (5.5, 7.5),
        (1.2, 3.0),
        (3.0, 2.5),
        (5.0, 2.5),
        (6.5, 3.0),
    ]
    for (label, pk), (ax_, ay) in zip(guru_attrs, guru_positions):
        attribute(ax_, ay, label, is_pk=pk)
        line(
            ax_,
            ay + (0.35 if ay > 5 else -0.35),
            GURU[0],
            GURU[1] + (0.6 if ay > 5 else -0.6),
        )

    # ══════════ ATRIBUT MAPEL ══════════
    mapel_attrs = [
        ("Kode_Mapel", True),
        ("Nama_Mapel", False),
        ("Tingkat_Kelas", False),
        ("KKM", False),
        ("Semester", False),
        ("Kurikulum", False),
    ]
    mapel_positions = [
        (9.5, 7.8),
        (11.5, 7.8),
        (13.5, 7.5),
        (9.5, 2.5),
        (11.5, 2.5),
        (13.5, 3.0),
    ]
    for (label, pk), (ax_, ay) in zip(mapel_attrs, mapel_positions):
        attribute(ax_, ay, label, is_pk=pk)
        line(
            ax_,
            ay + (0.35 if ay > 5 else -0.35),
            MAPEL[0],
            MAPEL[1] + (0.6 if ay > 5 else -0.6),
        )

    plt.tight_layout()
    plt.savefig(
        "output/erd_1_relasi.png",
        dpi=200,
        bbox_inches="tight",
        facecolor=fig.get_facecolor(),
    )
    plt.show()
    print("[OK] ERD 1 Relasi berhasil disimpan ke output/erd_1_relasi.png")


if __name__ == "__main__":
    import os

    os.makedirs("output", exist_ok=True)
    draw_erd_1_relasi()
