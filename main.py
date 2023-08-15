import pywhatkit as kit
from colorama import Fore, Style


def print_logo(ascii_art):
    logo = f"""
    {ascii_art}
    """
    print(Fore.RED + logo + Fore.RESET)


def main():
    resim_yolu = input("Lütfen resim dosyasının yolunu girin: ")
    dosya_adi = input(
        "ASCII sanatını kaydetmek istediğiniz dosyanın adını girin (örn. ascii_art.txt): ")
    kaydetme_yolu = dosya_adi

    ascii_sanat = kit.image_to_ascii_art(resim_yolu)
    with open(kaydetme_yolu, "w") as file:
        file.write(ascii_sanat)

    print_logo(ascii_sanat)
    print("ASCII sanatı oluşturuldu ve", kaydetme_yolu, "dosyasına kaydedildi.")
    print("Tamamlandı.")


if __name__ == "__main__":
    main()
