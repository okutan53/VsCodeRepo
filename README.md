BANK: Basit Banka Hesap Yönetim Sistemi
Bu proje, Python ile yazılmış bir banka hesap yönetim sistemidir. Kullanıcılar hesap oluşturabilir, giriş yapabilir, para yatırabilir, para çekebilir ve işlem geçmişlerini görüntüleyebilir.
:pushpin: Özellikler
:white_check_mark: Hesap oluşturma
:white_check_mark: Hesaba giriş yapma
:white_check_mark: Para yatırma ve çekme
:white_check_mark: Bakiye sorgulama
:white_check_mark: İşlem geçmişini görüntüleme
:white_check_mark: Kullanıcı verilerini CSV dosyasında saklama
:rocket: Kurulum ve Çalıştırma
:one: Depoyu Klonla
git clone https://github.com/kullaniciadi/repo-adi.git
cd repo-adi
:two: Gerekli Bağımlılıkları Yükle
Bu proje, standart Python kütüphanelerini kullanmaktadır. Harici bir bağımlılık gerekmemektedir. Ancak, bağımsız bir ortam oluşturmak için virtual environment kullanabilirsiniz:
python -m venv venv
source venv/bin/activate # (Windows için: venv\Scripts\activate)
:three: Uygulamayı Başlat
python main.py
:open_file_folder: Dosya Yapısı
📂 repo-adi/
├── main.py # Ana Python dosyası
├── accounts.csv # Kullanıcı verilerinin saklandığı dosya
├── README.md # Proje açıklamaları
:book: Kullanım
Uygulama çalıştırıldığında şu menü görüntülenir:
Yapmak istediğiniz işlemi seçiniz:
1 - Yeni Hesap Aç
2 - Hesaba Giriş Yap
3 - Çıkış
Kullanıcı yeni bir hesap açabilir veya mevcut hesabına giriş yaparak işlemlerini gerçekleştirebilir.
🛠 Teknolojiler
Bu proje aşağıdaki Python kütüphanelerini kullanmaktadır:
os → Dosya işlemleri için
datetime → Zaman damgası oluşturmak için
:pushpin: Katkıda Bulunma
Eğer projeye katkı sağlamak istiyorsanız:
Depoyu forklayın
Yeni bir branch oluşturun (git checkout -b yeni-ozellik)
Değişikliklerinizi yapın ve commit edin (git commit -m 'Yeni özellik eklendi')
git push ile değişikliklerinizi gönderin
Bir pull request oluşturun
:scroll: Lisans
Bu proje MIT Lisansı altında dağıtılmaktadır. Daha fazla bilgi için LICENSE dosyasına göz atabilirsiniz.
