import datetime
import random
import time
from colorama import init, Fore
from src import process


def main():
    init(autoreset=True)
    inject = process.ZefoyViews()
    print(
        Fore.GREEN + """
      _____ _ _  __   ___
     |_   _(_) |_\ \ / (_)_____ __ _____
       | | | | / /\ V /| / -_) V  V (_-<
       |_| |_|_\_\ \_/ |_\___|\_/\_//__/
          akuiiki_
    """
    )
    print(Fore.LIGHTYELLOW_EX + "Contoh: https://www.tiktok.com/@simantep.id/video/7159807297198361883")
    url_video = input("Masukan Link Video: ")

    inject.get_session_captcha()
    time.sleep(1)

    if inject.post_solve_captcha(captcha_result=inject.captcha_solver()):

        print("\n[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTGREEN_EX + "Sukses Mengakses Captha.." + "\n")

        while True:

            inject_views = inject.send_views(
                url_video=url_video
            )
            if inject_views:

                if "Mohon coba kembali nanti" in inject_views:
                    print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_views)
                    exit()

                elif "Sukses mengirim views..." in inject_views:
                    print("[ " + str(
                        datetime.datetime.now()) + " ] " + Fore.LIGHTGREEN_EX + inject_views + " to " + Fore.LIGHTYELLOW_EX + "" + url_video,
                          end="\n\n")

                elif "Sesi kadaluarsa, ulangi lagi!" in inject_views:
                    print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_views)
                    exit()

                elif "Coba kembali lagi, Server Penuh." in inject_views:
                    print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_views)
                    time.sleep(random.randint(180))
                    exit()

                else:
                    for i in range(int(inject_views), 0, -1):
                        print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTYELLOW_EX + "Tunggu " + str(
                            i) + " Detik untuk mengirim kembali.", end="\r")
                        time.sleep(1)

                time.sleep(random.randint(1, 5))

            else:
                pass

    else:
        print(Fore.RED + "Gagal mengakses captha")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "Exit")
        exit()
