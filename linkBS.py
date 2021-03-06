from bs4 import BeautifulSoup as bs
import os

DOMAIN = "https://www.wavsource.com"
TIPEFILE = ".wav"
# sys.stdout = open("test.txt", "w")
DataLink = []
folder = "C:\\Users\\LENOVO\\BS"
for filename in os.listdir(folder):
    if filename.endswith(".html"):
        fname = os.path.join(folder, filename)
        print("Filename: {}".format(fname))

        with open(fname, "r") as f:
            soup = bs(f.read(), "html.parser")
            info = soup.find_all("a", href=True)

        for i in info:
            new = i.get("href")
            if "https://www.wavsource.com/snds_2020-10-01" in new:
                print(new)
