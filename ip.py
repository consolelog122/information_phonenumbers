import phonenumbers
from phonenumbers import timezone, carrier, geocoder
import sys


def information_phone(arg_phone_number):
    try:
        phone_number = phonenumbers.parse(arg_phone_number, None)

        if phonenumbers.is_valid_number(phone_number):
            print("Nomor telepon valid")
            city = timezone.time_zones_for_number(phone_number)
            isp = carrier.name_for_number(phone_number, None)
            country = geocoder.country_name_for_number(phone_number, "en")

            print()
            print(f"City : {city}")
            print(f"Internet service provider : {isp}")
            print(f"Country : {country}")
            print()
        else:
            print("Nomor telepon tidak valid")
    except phonenumbers.phonenumberutil.NumberParseException:
        print("Format nomor telepon tidak valid. Gunakan format seperti +6289123545562")


def get_phone_number():
    print("Masukan no hp dengan contoh +6289123545562")
    print('Jika tidak maka error brutal minimal make "+"')
    return input("Masukan no hp disini : ")


def main():
    while True:
        input_phone_number = get_phone_number()
        information_phone(input_phone_number)

        while True:
            print('Ketik "yes" jika iya, ketik "no" jika tidak')
            input_more = input("Mau lagi? ").lower()
            if input_more in ["yes", "no"]:
                break
            else:
                print("Input tidak valid. Silakan masukkan 'yes' atau 'no'.")

        if input_more == "no":
            print("Terima kasih telah menggunakan layanan ini.")
            sys.exit()


if __name__ == "__main__":
    main()
