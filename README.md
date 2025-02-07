# 🏦 Basit Banka Hesap Yönetim Sistemi

Bu proje, Python ile yazılmış bir **banka hesap yönetim sistemidir**. Kullanıcılar hesap oluşturabilir, giriş yapabilir, para yatırabilir, para çekebilir ve işlem geçmişlerini görüntüleyebilir.

## 📌 Özellikler

✅ Hesap oluşturma  
✅ Hesaba giriş yapma  
✅ Para yatırma ve çekme  
✅ Bakiye sorgulama  
✅ İşlem geçmişini görüntüleme  
✅ Kullanıcı verilerini **CSV dosyasında** saklama

## 🚀 Kurulum ve Çalıştırma

### 1️⃣ Depoyu Klonla

```sh
git clone https://github.com/kullaniciadi/repo-adi.git
cd repo-adi
```

### 2️⃣ Gerekli Bağımlılıkları Yükle

Bu proje, standart Python kütüphanelerini kullanmaktadır. Harici bir bağımlılık gerekmemektedir. Ancak, bağımsız bir ortam oluşturmak için **virtual environment** kullanabilirsiniz:

```sh
python -m venv venv
source venv/bin/activate  # (Windows için: venv\Scripts\activate)
```

### 3️⃣ Uygulamayı Başlat

```sh
python main.py
```

## 📂 Dosya Yapısı

```
📂 repo-adi/
 ├── main.py            # Ana Python dosyası
 ├── accounts.csv       # Kullanıcı verilerinin saklandığı dosya
 ├── README.md          # Proje açıklamaları
```

## 📖 Kullanım

Uygulama çalıştırıldığında şu menü görüntülenir:

```
Yapmak istediğiniz işlemi seçiniz:
1 - Yeni Hesap Aç
2 - Hesaba Giriş Yap
3 - Çıkış
```

Kullanıcı yeni bir hesap açabilir veya mevcut hesabına giriş yaparak işlemlerini gerçekleştirebilir.

## 🛠 Teknolojiler

Bu proje aşağıdaki Python kütüphanelerini kullanmaktadır:

- `os` → Dosya işlemleri için
- `datetime` → Zaman damgası oluşturmak için

## 📌 Katkıda Bulunma

Eğer projeye katkı sağlamak istiyorsanız:

1. Depoyu forklayın
2. Yeni bir branch oluşturun (`git checkout -b yeni-ozellik`)
3. Değişikliklerinizi yapın ve commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. `git push` ile değişikliklerinizi gönderin
5. Bir **pull request** oluşturun

## 📜 Lisans

Bu proje **MIT Lisansı** altında dağıtılmaktadır. Daha fazla bilgi için `LICENSE` dosyasına göz atabilirsiniz.
