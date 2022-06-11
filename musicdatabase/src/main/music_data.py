import csv

print("\n")
print("\033[1;32;40m                  _                  _                 ")
print("\033[1;32;40m                 (_)                | |      _         ")
print("\033[1;32;40m ____  _   _  ___ _  ____         _ | | ____| |_  ____   ____  _   _ ")
print("\033[1;32;40m|    \| | | |/___) |/ ___)       / || |/ _  |  _)/ _  | |  _ \| | | |")
print("\033[1;32;40m| | | | |_| |___ | ( (___ ______( (_| ( ( | | |_( ( | |_| | | | |_| |")
print("\033[1;32;40m|_|_|_|\____(___/|_|\____|_______)____|\_||_|\___)_||_(_) ||_/ \__  |")
print("\033[1;32;40m                                                        |_|   (____/ ")
print("\n")

print("\033[1;37;40mWritten by Andrew Franco")
print("@Anderbar on GitHub")
print("\n")
print("Music Database Manager written in Python.", end="")
print("\n")

print("This app utilizes .csv files for reading and writing.")
print("The format of this file should look like this:", end="")
print("\n")
print("\033[1;35;40mNAME, ARTIST, ALBUM, YEAR, DECADE, GENRE, TOPIC, LOCATION of song to listen", end="")
print("\n")

print("\033[1;37;40mPlease read each choice carefully before proceeding.\n")
print("Each option is formatted by what method or basis you would want to find music by.")
print("For example: if you were to pick option 2 which is by Artist, you would be given options based on the artists of the database.")
print("Furthermore on this example, picking artists would be able to filter which songs are by an artist based on input, or you could even print all of the artists in this database.")
print("See songdatabasewriteup.txt for more details on how this works.\n")

print("Search by :\n")

print("[1] Song")
print("[2] Artist")
print("[3] Genre")
print("[4] Year")
print("[5] Decade")
print("[6] Topic")
print("[7] Location\n")

