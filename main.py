import os
from datetime import datetime

adres = "accounts.csv"
#dosya açma
# :pushpin: Dosya açma fonksiyonu (varsa okuma, yoksa oluşturma)
def DosyaAc(adres):
    if not os.path.exists(adres):
        with open(adres, "w", encoding="UTF-8") as dosya:
            pass  # Eğer dosya yoksa oluştur ve kapat
    return open(adres, "r+", encoding="UTF-8")

# :pushpin: Hesapları yükleme fonksiyonu
def HesaplariYukle():
    with DosyaAc(adres) as dosya:
        hesaplar = dosya.readlines()

    hesap_dict = {}
    for satir in hesaplar:
        account_number, holder_name, balance, password, transactions = satir.strip().split(";")
        hesap_dict[account_number] = {
            "holder_name": holder_name,
            "account_number": account_number,
            "balance": float(balance),
            "password": password,
            "transactions": transactions.split("|") if transactions else []
        }
    return hesap_dict

# :pushpin: Hesapları kaydetme fonksiyonu
def HesaplariKaydet(hesaplar):
    with DosyaAc(adres) as dosya:
        dosya.seek(0)
        dosya.truncate()
        for hesap in hesaplar.values():
            transaction_str = "|".join(hesap["transactions"])
            dosya.write(f"{hesap['account_number']};{hesap['holder_name']};{hesap['balance']};{hesap['password']};{transaction_str}\n")

# :pushpin: Yeni hesap oluşturma fonksiyonu
def HesapOlustur(hesaplar):
    holder_name = input("Hesap sahibinin adı: ")

    # 6 haneli hesap numarası oluşturma
    account_number = str(datetime.now().timestamp()).replace('.', '')[-6:]

    # Şifre belirleme
    password = input("Şifre belirleyin (en az 4 karakter): ")
    while len(password) < 4:
        print("Şifre en az 4 karakter olmalıdır!")
        password = input("Şifre belirleyin: ")

    hesaplar[account_number] = {
        "holder_name": holder_name,
        "account_number": account_number,
        "balance": 0.0,
        "password": password,
        "transactions": []
    }
    HesaplariKaydet(hesaplar)
    print(f"Hesap oluşturuldu! Hesap Numaranız: {account_number}")

# :pushpin: Hesaba giriş yapma fonksiyonu
def HesapGiris(hesaplar):
    while True:
        account_number = input("Hesap numaranızı girin (Çıkış için 'q' tuşuna basın): ")
        if account_number == "q":
            return None

        if account_number not in hesaplar:
            print("Hesap bulunamadı!")
            continue

        password = input("Şifrenizi girin: ")
        if hesaplar[account_number]["password"] == password:
            print(f"\nHoşgeldiniz, {hesaplar[account_number]['holder_name']}!\n")
            return account_number
        else:
            print("Hatalı şifre!")

# :pushpin: Kullanıcıya özel menü
def KullaniciMenusu(hesaplar, account_number):
    while True:
        print(f"\nHesap Numaranız: {account_number}")
        print("1 - Para Yatır")
        print("2 - Para Çek")
        print("3 - Bakiye Sorgula")
        print("4 - İşlem Geçmişi")
        print("5 - Çıkış")

        islem = input("Seçiminiz: ")
        if islem == "1":
            ParaYatir(hesaplar, account_number)
        elif islem == "2":
            ParaCek(hesaplar, account_number)
        elif islem == "3":
            BakiyeSorgula(hesaplar, account_number)
        elif islem == "4":
            IslemGecmisi(hesaplar, account_number)
        elif islem == "5":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim!")

# :pushpin: Para yatırma fonksiyonu
def ParaYatir(hesaplar, account_number):
    try:
        amount = float(input("Yatırılacak miktar: "))
        if amount <= 0:
            print("Geçersiz miktar!")
            return
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")
        return

    hesaplar[account_number]["balance"] += amount
    hesaplar[account_number]["transactions"].append(
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Deposit: +{amount}"
    )
    HesaplariKaydet(hesaplar)
    print(f"Yeni bakiye: {hesaplar[account_number]['balance']}")

# :pushpin: Para çekme fonksiyonu
def ParaCek(hesaplar, account_number):
    try:
        amount = float(input("Çekilecek miktar: "))
        if amount <= 0:
            print("Geçersiz miktar!")
            return
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")
        return

    if hesaplar[account_number]["balance"] >= amount:
        hesaplar[account_number]["balance"] -= amount
        hesaplar[account_number]["transactions"].append(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Withdraw: -{amount}"
        )
        HesaplariKaydet(hesaplar)
        print(f"Yeni bakiye: {hesaplar[account_number]['balance']}")
    else:
        print("Yetersiz bakiye!")

# :pushpin: Bakiye sorgulama fonksiyonu
def BakiyeSorgula(hesaplar, account_number):
    print(f"Güncel bakiye: {hesaplar[account_number]['balance']}")

# :pushpin: İşlem geçmişini gösterme fonksiyonu
def IslemGecmisi(hesaplar, account_number):
    print("\n--- İşlem Geçmişi ---")
    for transaction in hesaplar[account_number]["transactions"]:
        print(transaction)
    print(f"Güncel Bakiye: {hesaplar[account_number]['balance']}\n")

# :pushpin: Ana menü ve kullanıcı etkileşimi
MENU = """
Yapmak istediğiniz işlemi seçiniz:
1 - Yeni Hesap Aç
2 - Hesaba Giriş Yap
3 - Çıkış
"""

def main():
    hesaplar = HesaplariYukle()
    
    while True:
        islem = input(MENU)
        if islem == "1":
            HesapOlustur(hesaplar)
        elif islem == "2":
            account_number = HesapGiris(hesaplar)
            if account_number:
                KullaniciMenusu(hesaplar, account_number)
        elif islem == "3":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin!")

if __name__ == "__main__":
    main()