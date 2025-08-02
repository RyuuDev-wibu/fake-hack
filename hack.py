import os
os.system("color 0A")  # <- ini butuh os di-import dulu

import time, sys, random
from tkinter import messagebox, Tk
import webbrowser


def ketik(teks, jeda=0.03):
    for char in teks:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(jeda)
    print()

def loading(bar="▒█", total=20, delay=0.1):
    for i in range(total):
        sys.stdout.write(bar)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Buat folder loot (kalau belum ada)
if not os.path.exists("loot"):
    os.makedirs("loot")
    open("loot/chat.db", "w").write("Chat backup...")
    open("loot/lokasi.json", "w").write('{"lokasi": "Jakarta"}')
    open("loot/foto.jpg", "w").write("fake_image_data")

# GUI Warning Popup
root = Tk()
root.withdraw()
messagebox.showerror("SYSTEM BREACH", "Sistemmu telah dibobol!")

# Simulasi Hack
ketik("[TARGET FOUND] HP: Android | IP: 192.168.1.5")
ketik("[LINKED] Menyusup ke jaringan target...")
loading()

ketik("[ACCESS GRANTED] Port 8080 terbuka.")
ketik("Mengambil informasi perangkat...")
loading()
ketik("> Nomor: +6281252456382")
ketik("> Lokasi: Malang")
ketik("> Baterai: 50%")

time.sleep(1)
ketik("\n[INJECTING PAYLOAD] --> payload_remote.apk")
loading("█", 30, 0.01)

ketik("[INSTALLED] Menyalakan kamera, mic, dan GPS...")
ketik("[LIVE FEED] 👁️ Mereka tidak sadar...")
ketik("[SENDING MESSAGE] 'Kamu sedang diawasi 😈'")

time.sleep(1)
ketik("\n[DOWNLOADING FILES] 📁 chat.db, foto.jpg, lokasi.json...")
loading("▌", 25, 0.05)

ketik("\n📦 File yang diambil:")
for f in os.listdir("loot"):
    ketik(f" - {f}", 0.02)

ketik("\n[DISCONNECTING] Menghapus jejak digital...")
time.sleep(1)
ketik("✔ Misi selesai. Sistem kembali aman.")

import webbrowser
webbrowser.open("https://web.whatsapp.com/send?text=Kamu%20sedang%20diawasi.%20Saya%20tahu%20segala%20gerak-gerikmu.")

