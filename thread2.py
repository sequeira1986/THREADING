import urllib.request
import time

def download_site(url):
    with urllib.request.urlopen(url) as response:
        print(f"Stiahnutie {url}: {len(response.read())} bytov")

sites = [
    "https://www.facebook.com/",
    "https://votr.uniba.sk/",
    "https://euba.sk/",
    "https://translate.google.sk/?hl=sk",
    "https://www.facebook.com/",
    "https://docs.python.org/3/library/unittest.html#assert-methods",
    "https://www.mzv.sk/",
    #"https://www.minv.sk/",
    #"https://www.minv.sk/?NAKA"

]

start_time = time.time()
for site in sites:
    download_site(site)

duration = time.time() - start_time
print(f"Stiahnutých {len(sites)} stránok za {duration} sekúnd")
