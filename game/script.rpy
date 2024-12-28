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

define e = Character('Althar', color="#32CD32")
define a = Character('Ari', color="#32CD32")

# Menu Utama
label main_menu:
    play music "audio/main_menu.mp3" loop
    scene bg main_menu
    e "Dalam semesta yang dipenuhi teknologi dan misteri, berdiri tiga menara megah yang dulunya melambangkan kejeniusan umat manusia."
    e "Namun, waktu telah meruntuhkan menara-menara itu menjadi puing-puing."
    e "Hari ini, seorang pemuda pemberani bernama Ari berdiri di persimpangan takdir."
    e "Apakah kamu siap membantu Ari membangun kembali Menara Teknologi yang legendaris?"
    e "Pilih tingkat tantangan yang sesuai dengan keberanianmu, dan mari kita mulai petualangan ini."

    menu:
        "Level Pemula":
            stop music
            jump level_1
        "Level Menengah":
            stop music
            jump level_2
        "Level Mahir":
            stop music
            jump level_3
        "Keluar":
            return

# Implementasi Level 1
label level_1:
    play music "audio/level_1.mp3" loop
    scene bg level1_start
    e "Hari itu, Ari menemukan peta tua di sebuah perpustakaan yang nyaris terlupakan. Peta itu mengungkapkan lokasi sebuah menara kuno, Menara Teknologi."
    e "Dikatakan bahwa menara itu memiliki kekuatan untuk menghubungkan dunia, namun kini hancur menjadi puing-puing yang tersebar."
    e "Dengan keberanian dan tekad, Ari memutuskan untuk memulai perjalanan, mengumpulkan pecahan-pecahan menara tersebut."
    e "Setiap pecahan menyimpan pertanyaan yang menguji pengetahuan dan kemampuannya."
    a '"Jika aku bisa menyelesaikan ini," pikir Ari, "Aku dapat membangun kembali sesuatu yang luar biasa untuk dunia."'
    e "Dan dengan langkah pertama yang penuh semangat, perjalanan ini pun dimulai..."
    jump level_1_part_1

label level_1_part_1:
    scene bg level1_1
    e "Dengan tekad yang membara, Ari memulai perjalanan. Tidak jauh dari desanya, ia menemukan bagian pertama: sebuah fondasi kokoh namun sederhana yang ditandai dengan simbol aneh berupa huruf '< >'"
    e "Di sampingnya terdapat sebuah batu berukir yang menyala saat Ari mendekat. Ukiran itu bertuliskan,"
    e "Ini adalah dasar dari semua. Jawablah pertanyaanku:"
    e "Apa itu HTML?"
    menu:

        "Machine Language":
            jump try_again_level_1
        "Markup Syntax":
            jump try_again_level_1
        "Markup Language":
            a "Ari berpikir sejenak, lalu menjawab dengan yakin, 'Markup Language!' Seketika itu, fondasi bersinar dan terangkat ke udara, membentuk dasar dari menara yang megah."
            e '"Hebat, kamu berhasil menemukan fondasi," terdengar suara misterius dari udara. "Tapi ini baru permulaan. Bagian kedua menunggu di lembah URL, di mana jalur-jalur tersembunyi yang menghubungkan dunia harus kau temukan."'
            e 'Dengan penuh rasa ingin tahu, Ari melanjutkan perjalanannya menuju lembah itu, siap untuk menjawab tantangan berikutnya.'
            jump level_1_part_2
        "Modular Programming":
            jump try_again_level_1

label level_1_part_2:
    scene bg level1_2
    e "Setelah perjalanan yang panjang, Ari tiba di lembah URL. Di sana, ia menemukan bagian kedua dari menara, yang berbentuk seperti sebuah peta bercabang. Sebuah batu lainnya bersinar, dengan pertanyaan yang tertulis di atasnya:"
    e "Apa itu CSS?"
    menu:
        "Cascading Style Sheets":
            a 'Tanpa ragu, Ari menjawab, "Cascading Style Sheets!" Batu itu memancarkan cahaya terang, dan bagian kedua menara terbang ke tempatnya di atas fondasi.'
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
        "Python adalah sistem operasi.":
            jump try_again_level_1_3
        "Python adalah bahasa pemrograman.":
            a '"Python adalah bahasa pemrograman!" jawab Ari. Bagian ketiga menara mulai bersinar dan terbang ke tempatnya, menambah keindahan pada menara yang sedang dibangun.'
            e '"Kamu sudah semakin dekat," ujar suara itu. "Sekarang, pergilah ke bagian Versi. Di sana, kamu akan belajar tentang pentingnya pengelolaan perubahan."'
            jump level_1_part_4
        "Python adalah framework.":
            jump try_again_level_1_3
        "Python adalah database.":
            jump try_again_level_1_3

label level_1_part_4:
    scene bg level1_4
    e "Ari mendaki Bukit Versi, di mana ia menemukan bagian keempat: sebuah mekanisme dengan simbol cabang pohon. Batu di dekatnya menanyakan:"
    e "Apa kegunaan Git?"
    menu:
        "Git digunakan untuk debugging.":
            jump try_again_level_1_4
        "Git digunakan untuk styling halaman.":
            jump try_again_level_1_4
        "Git digunakan untuk menjalankan aplikasi.":
            jump try_again_level_1_4
        "Git digunakan untuk version control.":
            a '"Git digunakan untuk version control!" jawab Ari tanpa ragu. Mesin itu mulai bergerak, dan bagian keempat menara melesat ke atas, menambahkan lapisan dinamis yang membawa kehidupan pada menara.'
            e '"Luar biasa, Ari," kata suara itu lagi, terdengar lebih dekat sekarang. "Tinggal satu bagian terakhir. Pergilah ke Puncak API. Di sana, kau akan menghubungkan semuanya."'
            jump level_1_part_5

label level_1_part_5:
    scene bg level1_5
    e "Dengan semangat, Ari mendaki ke Puncak API. Di puncak itu, ia menemukan bagian terakhir, berbentuk seperti jaringan bercahaya yang melingkupi semua bagian menara. Batu terakhir bersinar dengan pertanyaan:"
    e 'Apa itu API?'
    menu:
        "API adalah Advanced Protocol Integration.":
            jump try_again_level_1_5
        "API adalah Automated Process Information.":
            jump try_again_level_1_5
        "API adalah Application Programming Interface.":
            jump level_1_completed
        "API adalah Adaptive Programming Interface.":
            jump try_again_level_1_5

label level_1_completed:
    scene bg level1_completed
    e "Cahaya terang memenuhi langit saat Menara Pemula selesai dibangun. Ari berdiri di bawahnya, merasa bangga atas usahanya."
    a '"Aku tahu ini baru awal," pikirnya. "Namun menara ini adalah simbol dari semangat dan tekad."'
    e 'Dengan pemandangan menara yang megah, Ari melanjutkan langkahnya, bersiap menuju tantangan berikutnya.'
    stop music
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
    play music "audio/level_2.mp3" loop
    scene bg level2_start
    e 'Dengan semangat baru, Ari menatap menara kedua, Menara Pengetahuan Menengah.'
    a '"Ini lebih sulit," pikirnya. "Namun aku telah belajar dari tantangan pertama."'
    e 'Suara misterius bergema kembali, "Kau telah membuktikan dirimu, Ari. Namun, pengetahuan dasar saja tidak cukup. Tantangan di menara ini akan menguji pemahaman yang lebih dalam."'
    e "Dengan keberanian, Ari melangkah maju, menghadapi pertanyaan-pertanyaan yang lebih rumit."
    jump level_2_part_1

label level_2_part_1:
    scene bg level2_1
    e 'Ari tiba di lokasi Menara Pengetahuan Menengah. Menara ini sudah berdiri sebagian, namun terlihat belum sempurna. "Bagian pertama adalah fondasi kuat yang baru," kata suara itu. "Jawab pertanyaan ini:"'
    e 'Apa kepanjangan dari HTML?'
    menu:
        "HTML adalah HyperText Markup Language.":
            a 'Ari menjawab, "HTML adalah HyperText Markup Language!" Fondasi menara bersinar lebih terang, memberikan stabilitas pada strukturnya.'
            jump level_2_part_2
        "HTML adalah HighText Machine Language.":
            jump try_again_level_2
        "HTML adalah Hierarchical Text Language.":
            jump try_again_level_2
        "HTML adalah Hosting Template Language.":
            jump try_again_level_2

label level_2_part_2:
    scene bg level2_2
    e 'Bagian berikutnya muncul. "Kita butuh jalur penghubung di sini. Jawablah:"'
    e 'Apa itu URL?'
    menu:
        "URL adalah Universal Resource Locator.":
            jump try_again_level_2_2
        "URL adalah Unified Resource Locator.":
            jump try_again_level_2_2
        "URL adalah Uniform Resource Locator.":
            a '"URL adalah Uniform Resource Locator!" jawab Ari dengan percaya diri. Bagian kedua menara terangkat, memperkuat koneksi antarbagian.'
            jump level_2_part_3
        "URL adalah Unitary Resource Locator.":
            jump try_again_level_2_2

label level_2_part_3:
    scene bg level2_3
    e '"Keindahan menara ini membutuhkan gaya," kata suara itu.'
    e '"Apa kegunaan CSS?"'
    menu:
        "CSS digunakan untuk membuat struktur halaman web.":
            jump try_again_level_2_3
        "CSS digunakan untuk memprogram logika aplikasi.":
            jump try_again_level_2_3
        "CSS digunakan untuk menyimpan data.":
            jump try_again_level_2_3
        "CSS digunakan untuk mengatur gaya halaman web.":
            a '"CSS digunakan untuk mengatur gaya halaman web!" Bagian ketiga menara bersinar cerah, melengkapi estetika menara.'
            jump level_2_part_4

label level_2_part_4:
    scene bg level2_4
    e '"Selanjutnya, kita butuh kekuatan logika. Apa itu JavaScript?"'
    menu:
        "JavaScript adalah framework untuk backend.":
            jump try_again_level_2_4
        "JavaScript adalah database untuk aplikasi.":
            jump try_again_level_2_4
        "JavaScript adalah bahasa pemrograman untuk web.":
            a '"JavaScript adalah bahasa pemrograman untuk web!" Bagian keempat menara mulai berdenyut dengan energi dinamis.'
            jump level_2_part_5
        "JavaScript adalah software design pattern.":
            jump try_again_level_2_4

label level_2_part_5:
    scene bg level2_5
    e '"Dan terakhir, jawab pertanyaan ini: Apa itu HTTP?"'
    menu:
        "HTTP adalah HyperText Transfer Protocol.":
            a '"HTTP adalah HyperText Transfer Protocol!" Bagian terakhir menyatu dengan menara, menyelesaikan struktur megah Menara Pengetahuan Menengah.'
            jump level_2_completed
        "HTTP adalah Hosting Transfer Protocol.":
            jump try_again_level_2_5
        "HTTP adalah Hyper Transfer Text Protocol.":
            jump try_again_level_2_5
        "HTTP adalah Host Text Transfer Protocol.":
            jump try_again_level_2_5

label level_2_completed:
    scene bg level2_completed
    e 'Saat bagian terakhir menara kedua menyatu, cahaya emas menyelimuti struktur itu, menandakan penyelesaiannya.'
    e '"Luar biasa, Ari," suara itu bergema. "Kau telah menunjukkan bahwa dirimu layak. Tapi perjalanan ini belum selesai."'
    a '"Aku siap," jawab Ari dengan mantap, menatap menara terakhir di kejauhan.'
    e "Dengan tekad yang semakin kuat, ia bersiap menghadapi tantangan terakhir."
    stop music
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
    play music "audio/level_3.mp3" loop
    scene bg level3_start
    e '"Kau telah sampai di tahap terakhir," suara misterius berbicara dengan nada penuh hormat.'
    e '"Menara Pengetahuan Mahir adalah puncak dari perjalananmu. Tantangan ini akan menentukan apakah kau benar-benar memahami inti dari teknologi."'
    e 'Ari menatap menara itu, struktur setengah jadi yang menjulang tinggi di depannya. Ia tahu bahwa tantangan ini akan menjadi ujian terbesar.'
    a '"Aku tidak akan menyerah," gumamnya, melangkah maju dengan keyakinan penuh.'
    jump level_3_part_1

label level_3_part_1:
    scene bg level3_1
    e 'Di depan Ari, menara terakhir menjulang, namun sebagian besar masih berupa kerangka. Ia harus menjawab lima pertanyaan terakhir untuk menyempurnakannya.'
    e '"Pertama, kita butuh fondasi data."'
    e 'Apa kegunaan SQL?'
    menu:
        "SQL adalah framework frontend.":
            jump try_again_level_3
        "SQL adalah library Python.":
            jump try_again_level_3
        "SQL adalah bahasa untuk debugging.":
            jump try_again_level_3
        "SQL digunakan untuk mengelola database.":
            a '"SQL digunakan untuk mengelola database!" jawab Ari dengan mantap. Fondasi menara langsung menyala, memancarkan cahaya yang kokoh.'
            jump level_3_part_2

label level_3_part_2:
    scene bg level3_2
    e '"Selanjutnya, kita butuh wadah yang kuat untuk sistem ini," kata suara itu. "Apa kegunaan Docker?"'
    menu:
        "Docker digunakan untuk containerization.":
            a '"Docker digunakan untuk containerization!" jawab Ari. Bagian kedua dari menara mulai menyatu, menambah struktur yang stabil.'
            jump level_3_part_3
        "Docker digunakan untuk debugging.":
            jump try_again_level_3_2
        "Docker digunakan untuk frontend styling.":
            jump try_again_level_3_2
        "Docker digunakan untuk hosting file.":
            jump try_again_level_3_2

label level_3_part_3:
    scene bg level3_3
    e '"Kita memerlukan penghubung antar sistem. Jawablah pertanyaan ini: Apa kegunaan API?"'
    menu:
        "API digunakan untuk menyimpan data lokal.":
            jump try_again_level_3_3
        "API memungkinkan komunikasi antara sistem.":
            a '"API memungkinkan komunikasi antara sistem!" Ari menjawab dengan penuh keyakinan. Bagian ketiga menara menyala, menyempurnakan koneksi antarbagian.'
            jump level_3_part_4
        "API adalah library untuk framework tertentu.":
            jump try_again_level_3_3
        "API adalah protokol untuk enkripsi data.":
            jump try_again_level_3_3

label level_3_part_4:
    scene bg level3_4
    e '"Selanjutnya, kita butuh teknologi untuk menyusun tampilan interaktif. Apa itu React?"'
    menu:
        "React adalah database untuk aplikasi.":
            jump try_again_level_3_4
        "React adalah library untuk membuat UI.":
            a '"React adalah library untuk membuat UI!" seru Ari. Bagian keempat menara menyatu, menambah dimensi visual yang memukau.'
            jump level_3_part_5
        "React adalah bahasa pemrograman baru.":
            jump try_again_level_3_4
        "React adalah web server framework.":
            jump try_again_level_3_4

label level_3_part_5:
    scene bg level3_5
    e '"Terakhir, kau harus memahami arsitektur modern. Apa itu RESTful API?"'
    menu:
        "RESTful API adalah framework backend.":
            jump try_again_level_3_5
        "RESTful API adalah library frontend.":
            jump try_again_level_3_5
        "RESTful API adalah pendekatan arsitektur API.":
            a '"RESTful API adalah pendekatan arsitektur API!" jawab Ari dengan penuh semangat. Bagian terakhir menara melesat ke tempatnya, melengkapi struktur megah Menara Pengetahuan Mahir.'
            jump level_3_completed
        "RESTful API adalah database.":
            jump try_again_level_3_5

label level_3_completed:
    scene bg level3_completed
    e 'Menara Pengetahuan Mahir kini berdiri kokoh, menyatu dengan dua menara lainnya, menciptakan pemandangan yang megah.'
    e 'Jaringan cahaya yang menghubungkan ketiga menara memancar ke langit, membentuk simbol keabadian pengetahuan dan inovasi.'
    e '"Ari," suara itu terdengar lembut. "Apa yang telah kau lakukan adalah lebih dari sekadar membangun menara. Kau telah membangkitkan semangat pengetahuan yang akan menginspirasi dunia."'
    a 'Ari tersenyum, merasakan kepuasan yang mendalam. Ia tahu bahwa perjalanan ini telah mengubahnya, menjadikannya lebih kuat dan bijaksana.'
    e '"Tamat."'
    stop music
    jump main_menu

label try_again_level_3:
    e "Jawaban salah! Coba lagi."
    jump level_3_part_1

label try_again_level_3_2:
    e "Jawaban salah! Coba lagi."
    jump level_3_part_2

label try_again_level_3_3:
    e "Jawaban salah! Coba lagi."
    jump level_3_part_3

label try_again_level_3_4:
    e "Jawaban salah! Coba lagi."
    jump level_3_part_4

label try_again_level_3_5:
    e "Jawaban salah! Coba lagi."
    jump level_3_part_5
