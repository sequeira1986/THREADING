import urllib.request
import time
from concurrent.futures import ThreadPoolExecutor

def dowload_site(url):
    print("Stahujem..."+ url)
    with urllib.request.urlopen(url) as response:
        return  f"Stahnutie {url}: {len(response.read())}bytov"
sites = [
    "https://www.facebook.com/",
    "https://votr.uniba.sk/",
    "https://euba.sk/",
    "https://translate.google.sk/?hl=sk",
    "https://www.facebook.com/",
    "https://docs.python.org/3/library/unittest.html#assert-methods",
    "https://www.mzv.sk/",

    ]

threads = []
start_time = time.time()

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = []
    for site in sites:
        futures.append(executor.submit(dowload_site, site))

    for future in futures:
        result = future.result()
        print(result)

    duration = time.time() - start_time
    print(f"Stiahnute {len(sites)}stranok za {duration} sekund")
