"""
Tabel Relasi - Sistem Informasi Akademik Sekolah (SIAS)
Skema Tabel Relasi dengan garis FK — background putih, teks hitam.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def draw_tabel_relasi():
    fig, ax = plt.subplots(1, 1, figsize=(18, 12))
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 12)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor("white")

    # ── Judul ──
    ax.text(
        9,
        11.5,
        "Tabel Relasi - Sistem Informasi Akademik Sekolah (SIAS)",
        ha="center",
        va="center",
        fontsize=16,
        fontweight="bold",
        color="black",
    )

    # ── Palet ──
    HEADER_FILL = "#2563eb"
    HEADER_TXT = "white"
    ROW_FILL = "#f8fafc"
    ROW_EDGE = "#d1d5db"
    PK_COLOR = "#dc2626"
    FK_COLOR = "#ea580c"
    TXT = "black"
    TXT_DIM = "#374151"

    # ── Helper: Tabel ──
    def draw_table(x, y, title, columns, width=3.8):
        row_h = 0.38
        header_h = 0.5
        positions = {}

        # Header
        header = mpatches.FancyBboxPatch(
            (x, y - header_h),
            width,
            header_h,
            boxstyle="round,pad=0.05",
            fc=HEADER_FILL,
            ec=HEADER_FILL,
            lw=1.5,
        )
        ax.add_patch(header)
        ax.text(
            x + width / 2,
            y - header_h / 2,
            title,
            ha="center",
            va="center",
            fontsize=11,
            fontweight="bold",
            color=HEADER_TXT,
        )

        # Baris kolom
        for i, (col_name, col_type) in enumerate(columns):
            ry = y - header_h - (i + 1) * row_h
            row = mpatches.Rectangle(
                (x, ry), width, row_h, fc=ROW_FILL, ec=ROW_EDGE, lw=1
            )
            ax.add_patch(row)

            prefix = ""
            color = TXT_DIM
            if col_type == "PK":
                prefix = "[PK] "
                color = PK_COLOR
            elif col_type == "FK":
                prefix = "[FK] "
                color = FK_COLOR

            ax.text(
                x + 0.15,
                ry + row_h / 2,
                f"{prefix}{col_name}",
                ha="left",
                va="center",
                fontsize=9,
                color=color,
                fontfamily="monospace",
            )

            positions[col_name] = {
                "left": (x, ry + row_h / 2),
                "right": (x + width, ry + row_h / 2),
                "center": (x + width / 2, ry + row_h / 2),
            }

        return positions

    # ── Helper: Garis FK ──
    def fk_line(start, end, label="", rad=0.3, color=FK_COLOR):
        ax.annotate(
            "",
            xy=end,
            xytext=start,
            arrowprops=dict(
                arrowstyle="-|>",
                color=color,
                lw=1.5,
                connectionstyle=f"arc3,rad={rad}",
            ),
        )
        if label:
            mx = (start[0] + end[0]) / 2
            my = (start[1] + end[1]) / 2
            ax.text(
                mx,
                my,
                label,
                ha="center",
                va="center",
                fontsize=7,
                color=color,
                fontstyle="italic",
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.9),
            )

    # ══════════ TABEL ══════════
    pos_siswa = draw_table(
        1.0,
        10.0,
        "tb_siswa",
        [
            ("NIS", "PK"),
            ("Nama_Siswa", ""),
            ("Tanggal_Lahir", ""),
            ("Jenis_Kelamin", ""),
            ("Alamat", ""),
            ("No_Telepon", ""),
            ("Agama", ""),
        ],
        width=3.8,
    )

    pos_guru = draw_table(
        13.2,
        10.0,
        "tb_guru",
        [
            ("NIP", "PK"),
            ("Nama_Guru", ""),
            ("Spesialisasi", ""),
            ("No_Telepon", ""),
            ("Alamat", ""),
            ("Email", ""),
            ("Pendidikan_Terakhir", ""),
        ],
        width=3.8,
    )

    pos_mapel = draw_table(
        7.5,
        10.0,
        "tb_mapel",
        [
            ("Kode_Mapel", "PK"),
            ("Nama_Mapel", ""),
            ("Tingkat_Kelas", ""),
            ("KKM", ""),
            ("Semester", ""),
            ("Kurikulum", ""),
            ("NIP", "FK"),
        ],
        width=3.8,
    )

    pos_nilai = draw_table(
        4.0,
        4.5,
        "tb_nilai",
        [
            ("ID_Nilai", "PK"),
            ("NIS", "FK"),
            ("Kode_Mapel", "FK"),
            ("Nilai_Tugas", ""),
            ("Nilai_UTS", ""),
            ("Nilai_UAS", ""),
        ],
        width=3.8,
    )

    # ══════════ GARIS FK ══════════
    # tb_mapel.NIP -> tb_guru.NIP
    fk_line(
        pos_mapel["NIP"]["right"],
        pos_guru["NIP"]["left"],
        label="1 : N",
        rad=-0.15,
    )

    # tb_nilai.NIS -> tb_siswa.NIS
    fk_line(
        pos_nilai["NIS"]["left"],
        pos_siswa["NIS"]["left"],
        label="1 : N",
        rad=0.25,
    )

    # tb_nilai.Kode_Mapel -> tb_mapel.Kode_Mapel
    fk_line(
        pos_nilai["Kode_Mapel"]["right"],
        pos_mapel["Kode_Mapel"]["left"],
        label="1 : N",
        rad=0.25,
    )

    # ── Keterangan Kardinalitas ──
    box_props = dict(boxstyle="round,pad=0.4", fc="#f1f5f9", ec="#94a3b8", lw=1.5)
    ax.text(
        9.0,
        1.3,
        (
            "Kardinalitas:\n"
            "  GURU (1) --- (N) MATA_PELAJARAN  ->  1 Guru mengajar banyak Mapel\n"
            "  SISWA (M) --- (N) MATA_PELAJARAN  ->  dipecah menjadi tabel NILAI\n"
            "  SISWA (1) --- (N) NILAI  ->  1 Siswa punya banyak Nilai"
        ),
        ha="center",
        va="center",
        fontsize=9,
        color=TXT,
        bbox=box_props,
        linespacing=1.8,
        fontfamily="monospace",
    )

    plt.tight_layout()
    plt.savefig(
        "output/tabel_relasi.png",
        dpi=200,
        bbox_inches="tight",
        facecolor=fig.get_facecolor(),
    )
    plt.show()
    print("[OK] Tabel Relasi berhasil disimpan ke output/tabel_relasi.png")


if __name__ == "__main__":
    import os

    os.makedirs("output", exist_ok=True)
    draw_tabel_relasi()
