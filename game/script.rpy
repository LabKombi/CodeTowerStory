# script.rpy

# Definisikan gambar dan karakter
image bg start = "images/tower_start.png"
image bg level1_1 = "images/tower_part_1.png"
image bg level1_2 = "images/tower_part_2.png"
image bg level1_3 = "images/tower_part_3.png"
image bg level1_4 = "images/tower_part_4.png"
image bg level1_5 = "images/tower_part_5.png"
image bg completed = "images/tower_completed.png"
image bg main_menu = "images/main_menu.png"

define e = Character('Ari', color="#32CD32")

# Menu Utama
label main_menu:
    scene bg main_menu
    e "Selamat datang di petualangan membangun Tower!"
    e "Pilih level yang ingin kamu mainkan."

    menu:
        "Mulai Petualangan":
            jump level_1
        "Keluar":
            return

# Level 1 Pembukaan
label level_1:
    scene bg start
    e "Aku mulai perjalanan ini untuk membangun Tower yang hebat. Ini adalah awal dari segalanya."

    menu:
        "Lanjutkan":
            jump quiz_1

# Kuis Level 1 - Membangun Bagian 1
label quiz_1:
    scene bg level1_1
    e "Aku mulai membangun bagian pertama tower dengan hati-hati. Sebelum melanjutkan, jawab pertanyaannya!"
    
    menu:
        "Bahasa Pemrograman":
            $ correct_answer = False
            jump try_again
        "Markup Language":
            $ correct_answer = True
            jump build_part_2

# Jika jawaban salah
label try_again:
    e "Jawaban salah, coba lagi!"
    jump quiz_1

# Bagian 2 - Membangun Tower
label build_part_2:
    scene bg level1_2
    e "Bagian pertama selesai! Sekarang aku melanjutkan ke bagian kedua tower."
    jump quiz_2

# Kuis Level 1 - Membangun Bagian 2
label quiz_2:
    scene bg level1_2
    e "Aku harus memastikan bagian kedua terbangun dengan benar. Waktunya untuk kuis!"
    
    menu:
        "Cascading Style Sheets":
            $ correct_answer = True
            jump build_part_3
        "Control Style Sheets":
            $ correct_answer = False
            jump try_again

# Bagian 3 - Membangun Tower
label build_part_3:
    scene bg level1_3
    e "Sekarang tower sudah lebih tinggi! Aku harus hati-hati membangun bagian ketiga."
    jump quiz_3

# Kuis Level 1 - Membangun Bagian 3
label quiz_3:
    scene bg level1_3
    e "Bagian ketiga akan menjadi yang paling penting. Apa yang harus aku lakukan?"
    
    menu:
        "Bahasa Pemrograman":
            $ correct_answer = True
            jump build_part_4
        "Markup Language":
            $ correct_answer = False
            jump try_again

# Bagian 4 - Membangun Tower
label build_part_4:
    scene bg level1_4
    e "Bagian keempat hampir selesai. Aku perlu memastikan semuanya sempurna."
    jump quiz_4

# Kuis Level 1 - Membangun Bagian 4
label quiz_4:
    scene bg level1_4
    e "Satu lagi pertanyaan penting. Apa itu Python?"
    
    menu:
        "Bahasa Pemrograman":
            $ correct_answer = True
            jump build_part_5
        "Sistem Operasi":
            $ correct_answer = False
            jump try_again

# Bagian 5 - Membangun Tower
label build_part_5:
    scene bg level1_5
    e "Ini bagian terakhir dari tower! Aku hanya perlu menyelesaikan ini."
    jump quiz_5

# Kuis Level 1 - Membangun Bagian 5
label quiz_5:
    scene bg level1_5
    e "Terakhir, pertanyaan terakhir!"
    
    menu:
        "Version Control":
            $ correct_answer = True
            jump level_completed
        "Sistem Operasi":
            $ correct_answer = False
            jump try_again

# Level Selesai
label level_completed:
    scene bg completed
    e "Tower telah selesai dibangun! Kamu berhasil menyelesaikan level ini."
    menu:
        "Kembali ke Menu Utama":
            jump main_menu
        "Keluar":
            return
