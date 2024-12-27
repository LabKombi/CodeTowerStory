# script.rpy

# Definisikan gambar main menu
image bg main_menu = "images/main_menu.png"

# Level 1
image bg level1_start = "images/tower_start_1.png"
image bg level1_1 = "images/tower_part_1_1.png"
image bg level1_2 = "images/tower_part_2_1.png"
image bg level1_3 = "images/tower_part_3_1.png"
image bg level1_4 = "images/tower_part_4_1.png"
image bg level1_5 = "images/tower_part_5_1.png"
image bg level1_completed = "images/tower_completed_1.png"

# Level 2
image bg level2_start = "images/tower_start_2.png"
image bg level2_1 = "images/tower_part_1_2.png"
image bg level2_2 = "images/tower_part_2_2.png"
image bg level2_3 = "images/tower_part_3_2.png"
image bg level2_4 = "images/tower_part_4_2.png"
image bg level2_5 = "images/tower_part_5_2.png"
image bg level2_completed = "images/tower_completed_2.png"

# Level 3
image bg level3_start = "images/tower_start_3.png"
image bg level3_1 = "images/tower_part_1_3.png"
image bg level3_2 = "images/tower_part_2_3.png"
image bg level3_3 = "images/tower_part_3_3.png"
image bg level3_4 = "images/tower_part_4_3.png"
image bg level3_5 = "images/tower_part_5_3.png"
image bg level3_completed = "images/tower_completed_3.png"

define e = Character('Ari', color="#32CD32")

# Menu Utama
label main_menu:
    scene bg main_menu
    e "Selamat datang di petualangan membangun Tower!"
    e "Pilih level yang ingin kamu mainkan."

    menu:
        "Level Pemula":
            jump level_1
        "Level Menengah":
            jump level_2
        "Level Mahir":
            jump level_3
        "Keluar":
            return

# Implementasi Level 1
label level_1:
    scene bg level1_start
    e "Pada suatu hari, Ari, seorang pemuda penuh semangat yang gemar belajar hal baru, menemukan sebuah peta tua di perpustakaan desa."
    e "Peta itu memperlihatkan lokasi sebuah menara legendaris yang disebut Menara Teknologi, konon mampu menghubungkan dunia."
    e "Namun, menara itu sudah lama runtuh, dan hanya pecahan-pecahan utamanya yang tersebar di lima tempat berbeda."
    e "Untuk membangun kembali menara tersebut, Ari harus mengumpulkan kelima bagian dan menjawab pertanyaan yang akan menguji pengetahuannya tentang dunia teknologi."
    jump level_1_part_1

label level_1_part_1:
    scene bg level1_1
    e "Dengan tekad yang membara, Ari memulai perjalanan. Tidak jauh dari desanya, ia menemukan bagian pertama: sebuah fondasi kokoh namun sederhana yang ditandai dengan simbol aneh berupa huruf '< >'"
    e "Di sampingnya terdapat sebuah batu berukir yang menyala saat Ari mendekat. Ukiran itu bertuliskan,"
    e "Ini adalah dasar dari semua. Jawablah pertanyaanku:"
    e "Apa itu HTML?"
    menu:
        "Markup Language":
            e "Ari berpikir sejenak, lalu menjawab dengan yakin, 'Markup Language!' Seketika itu, fondasi bersinar dan terangkat ke udara, membentuk dasar dari menara yang megah."
            e '"Hebat, kamu berhasil menemukan fondasi," terdengar suara misterius dari udara. "Tapi ini baru permulaan. Bagian kedua menunggu di lembah URL, di mana jalur-jalur tersembunyi yang menghubungkan dunia harus kau temukan."'
            e 'Dengan penuh rasa ingin tahu, Ari melanjutkan perjalanannya menuju lembah itu, siap untuk menjawab tantangan berikutnya.'
            jump level_1_part_2
        "Machine Language":
            jump try_again_level_1
        "Markup Syntax":
            jump try_again_level_1
        "Modular Programming":
            jump try_again_level_1

label level_1_part_2:
    scene bg level1_2
    e "Setelah perjalanan yang panjang, Ari tiba di lembah URL. Di sana, ia menemukan bagian kedua dari menara, yang berbentuk seperti sebuah peta bercabang. Sebuah batu lainnya bersinar, dengan pertanyaan yang tertulis di atasnya:"
    e "Apa itu CSS?"
    menu:
        "Cascading Style Sheets":
            e 'Tanpa ragu, Ari menjawab, "Cascading Style Sheets!" Batu itu memancarkan cahaya terang, dan bagian kedua menara terbang ke tempatnya di atas fondasi.'
            e '"Luar biasa," kata suara itu lagi. "Selanjutnya, kau harus menuju bangunan Python, tempat kau akan menemukan kekuatan yang mendasari logika modern."'
            jump level_1_part_3
        "Control Style Sheets":
            jump try_again_level_1_2
        "Custom Script Source":
            jump try_again_level_1_2
        "Code Styling System":
            jump try_again_level_1_2

label level_1_part_3:
    scene bg level1_3
    e "Ari melanjutkan perjalanan ke bangunan Python. Di sana, ia melihat sebuah struktur unik berbentuk seperti ular melingkar. Sebuah batu bercahaya menantinya dengan pertanyaan baru:"
    e "Apa itu Python?"
    menu:
        "Python adalah bahasa pemrograman.":
            e '"Python adalah bahasa pemrograman!" jawab Ari. Bagian ketiga menara mulai bersinar dan terbang ke tempatnya, menambah keindahan pada menara yang sedang dibangun.'
            e '"Kamu sudah semakin dekat," ujar suara itu. "Sekarang, pergilah ke bagian Versi. Di sana, kamu akan belajar tentang pentingnya pengelolaan perubahan."'
            jump level_1_part_4
        "Python adalah sistem operasi.":
            jump try_again_level_1_3
        "Python adalah framework.":
            jump try_again_level_1_3
        "Python adalah database.":
            jump try_again_level_1_3

label level_1_part_4:
    scene bg level1_4
    e "Ari mendaki Bukit Versi, di mana ia menemukan bagian keempat: sebuah mekanisme dengan simbol cabang pohon. Batu di dekatnya menanyakan:"
    e "Apa kegunaan Git?"
    menu:
        "Git digunakan untuk version control.":
            e '"Git digunakan untuk version control!" jawab Ari tanpa ragu. Mesin itu mulai bergerak, dan bagian keempat menara melesat ke atas, menambahkan lapisan dinamis yang membawa kehidupan pada menara.'
            e '"Luar biasa, Ari," kata suara itu lagi, terdengar lebih dekat sekarang. "Tinggal satu bagian terakhir. Pergilah ke Puncak API. Di sana, kau akan menghubungkan semuanya."'
            jump level_1_part_5
        "Git digunakan untuk debugging.":
            jump try_again_level_1_4
        "Git digunakan untuk styling halaman.":
            jump try_again_level_1_4
        "Git digunakan untuk menjalankan aplikasi.":
            jump try_again_level_1_4

label level_1_part_5:
    scene bg level1_5
    e "Dengan semangat, Ari mendaki ke Puncak API. Di puncak itu, ia menemukan bagian terakhir, berbentuk seperti jaringan bercahaya yang melingkupi semua bagian menara. Batu terakhir bersinar dengan pertanyaan:"
    e 'Apa itu API?'
    menu:
        "API adalah Application Programming Interface.":
            e 'Ari mengambil napas dalam-dalam dan menjawab, "Application Programming Interface!" Cahaya terang melesat ke langit, dan bagian terakhir menyatu dengan menara, menyelesaikan struktur megah tersebut.'
            e 'Menara Teknologi kini berdiri tegak, bersinar dengan kemegahan dan kekuatan. Ari merasa bangga dan bahagia, karena ia telah berhasil menjawab semua tantangan dan membangun kembali simbol pengetahuan teknologi.'
            jump level_1_completed
        "API adalah Advanced Protocol Integration.":
            jump try_again_level_1_5
        "API adalah Automated Process Information.":
            jump try_again_level_1_5
        "API adalah Adaptive Programming Interface.":
            jump try_again_level_1_5

label level_1_completed:
    scene bg level1_completed
    e "Selamat! Tower level ini selesai dibangun!"
    jump main_menu

label try_again_level_1:
    e "Jawaban salah! Coba lagi."
    jump level_1_part_1

label try_again_level_1_2:
    e "Jawaban salah! Coba lagi."
    jump level_1_part_2

label try_again_level_1_3:
    e "Jawaban salah! Coba lagi."
    jump level_1_part_3

label try_again_level_1_4:
    e "Jawaban salah! Coba lagi."
    jump level_1_part_4

label try_again_level_1_5:
    e "Jawaban salah! Coba lagi."
    jump level_1_part_5

# Implementasi Level 2
label level_2:
    scene bg level2_start
    e "Aku akan menghadapi tantangan yang lebih sulit. Ini level kedua!"
    jump level_2_part_1

label level_2_part_1:
    scene bg level2_1
    e "Bagian pertama dimulai. Jawab pertanyaan ini!"
    menu:
        "HTML adalah HyperText Markup Language.":
            jump level_2_part_2
        "HTML adalah HighText Machine Language.":
            jump try_again_level_2
        "HTML adalah Hierarchical Text Language.":
            jump try_again_level_2
        "HTML adalah Hosting Template Language.":
            jump try_again_level_2

label level_2_part_2:
    scene bg level2_2
    e "Bagian kedua selesai. Jawab pertanyaan berikutnya!"
    menu:
        "URL adalah Uniform Resource Locator.":
            jump level_2_part_3
        "URL adalah Universal Resource Locator.":
            jump try_again_level_2_1
        "URL adalah Unified Resource Locator.":
            jump try_again_level_2_1
        "URL adalah Unitary Resource Locator.":
            jump try_again_level_2_1

label level_2_part_3:
    scene bg level2_3
    e "Bagian ketiga sangat penting! Jawab pertanyaan ini!"
    menu:
        "CSS digunakan untuk mengatur gaya halaman web.":
            jump level_2_part_4
        "CSS digunakan untuk membuat struktur halaman web.":
            jump try_again_level_2_3
        "CSS digunakan untuk memprogram logika aplikasi.":
            jump try_again_level_2_3
        "CSS digunakan untuk menyimpan data.":
            jump try_again_level_2_3

label level_2_part_4:
    scene bg level2_4
    e "Bagian keempat hampir selesai. Pertanyaan ini kunci!"
    menu:
        "JavaScript adalah bahasa pemrograman untuk web.":
            jump level_2_part_5
        "JavaScript adalah framework untuk backend.":
            jump try_again_level_2_4
        "JavaScript adalah database untuk aplikasi.":
            jump try_again_level_2_4
        "JavaScript adalah software design pattern.":
            jump try_again_level_2_4

label level_2_part_5:
    scene bg level2_5
    e "Ini adalah bagian terakhir! Jawab pertanyaan terakhir!"
    menu:
        "HTTP adalah HyperText Transfer Protocol.":
            jump level_2_completed
        "HTTP adalah Hosting Transfer Protocol.":
            jump try_again_level_2_5
        "HTTP adalah Hyper Transfer Text Protocol.":
            jump try_again_level_2_5
        "HTTP adalah Host Text Transfer Protocol.":
            jump try_again_level_2_5

label level_2_completed:
    scene bg level2_completed
    e "Selamat! Tower level ini selesai dibangun!"
    jump main_menu

label try_again_level_2:
    e "Jawaban salah! Coba lagi."
    jump level_2_part_1

label try_again_level_2_2:
    e "Jawaban salah! Coba lagi."
    jump level_2_part_2

label try_again_level_2_3:
    e "Jawaban salah! Coba lagi."
    jump level_2_part_3

label try_again_level_2_4:
    e "Jawaban salah! Coba lagi."
    jump level_2_part_4

label try_again_level_2_5:
    e "Jawaban salah! Coba lagi."
    jump level_2_part_5

# Implementasi Level 3
label level_3:
    scene bg level3_start
    e "Sekarang saatnya menghadapi tantangan terberat. Ini adalah level terakhir!"
    jump level_3_part_1

label level_3_part_1:
    scene bg level3_1
    e "Bagian pertama dimulai. Jawab pertanyaan ini!"
    menu:
        "SQL digunakan untuk mengelola database.":
            jump level_3_part_2
        "SQL adalah framework frontend.":
            jump try_again_level_3
        "SQL adalah library Python.":
            jump try_again_level_3
        "SQL adalah bahasa untuk debugging.":
            jump try_again_level_3

label level_3_part_2:
    scene bg level3_2
    e "Bagian kedua selesai. Jawab pertanyaan berikutnya!"
    menu:
        "Docker digunakan untuk containerization.":
            jump level_3_part_3
        "Docker digunakan untuk debugging.":
            jump try_again_level_3
        "Docker digunakan untuk frontend styling.":
            jump try_again_level_3
        "Docker digunakan untuk hosting file.":
            jump try_again_level_3

label level_3_part_3:
    scene bg level3_3
    e "Bagian ketiga sangat penting! Jawab pertanyaan ini!"
    menu:
        "API memungkinkan komunikasi antara sistem.":
            jump level_3_part_4
        "API digunakan untuk menyimpan data lokal.":
            jump try_again_level_3
        "API adalah library untuk framework tertentu.":
            jump try_again_level_3
        "API adalah protokol untuk enkripsi data.":
            jump try_again_level_3

label level_3_part_4:
    scene bg level3_4
    e "Bagian keempat hampir selesai. Pertanyaan ini kunci!"
    menu:
        "React adalah library untuk membuat UI.":
            jump level_3_part_5
        "React adalah database untuk aplikasi.":
            jump try_again_level_3
        "React adalah bahasa pemrograman baru.":
            jump try_again_level_3
        "React adalah web server framework.":
            jump try_again_level_3

label level_3_part_5:
    scene bg level3_5
    e "Ini adalah bagian terakhir! Jawab pertanyaan terakhir!"
    menu:
        "RESTful API adalah pendekatan arsitektur API.":
            jump level_3_completed
        "RESTful API adalah framework backend.":
            jump try_again_level_3
        "RESTful API adalah library frontend.":
            jump try_again_level_3
        "RESTful API adalah database.":
            jump try_again_level_3

label level_3_completed:
    scene bg level3_completed
    e "Selamat! Tower terakhir selesai dibangun! Petualanganmu berhasil!"
    return

label try_again_level_3:
    e "Jawaban salah! Coba lagi."
    jump level_3_part_1
