"""
Main Runner - Sistem Informasi Akademik Sekolah (SIAS)
Menjalankan semua script untuk menghasilkan diagram ke folder output/.
"""

import os


# Pastikan folder output ada
os.makedirs("output", exist_ok=True)

# Nonaktifkan plt.show() agar bisa jalan tanpa GUI (optional)
import matplotlib

matplotlib.use("Agg")  # Backend non-interaktif

print("=" * 60)
print("  Generating SIAS Diagrams")
print("=" * 60)

# 1. DFD Level 0
print("\n[1/5] DFD Level 0 ...")
from dfd_level_0 import draw_dfd_level_0

draw_dfd_level_0()

# 2. DFD Level 1
print("\n[2/5] DFD Level 1 ...")
from dfd_level_1 import draw_dfd_level_1

draw_dfd_level_1()

# 3. ERD 1 Relasi
print("\n[3/5] ERD 1 Relasi ...")
from erd_1_relasi import draw_erd_1_relasi

draw_erd_1_relasi()

# 4. ERD Banyak Relasi
print("\n[4/5] ERD Banyak Relasi ...")
from erd_banyak_relasi import draw_erd_banyak_relasi

draw_erd_banyak_relasi()

# 5. Tabel Relasi
print("\n[5/5] Tabel Relasi ...")
from tabel_relasi import draw_tabel_relasi

draw_tabel_relasi()

print("\n" + "=" * 60)
print("  [OK] Semua diagram berhasil dibuat di folder output/")
print("=" * 60)
print("\nFile yang dihasilkan:")
for f in sorted(os.listdir("output")):
    fpath = os.path.join("output", f)
    size_kb = os.path.getsize(fpath) / 1024
    print(f"  - output/{f}  ({size_kb:.1f} KB)")
