import time
import concurrent.futures

# https://docs.python.org/3/library/concurrent.futures.html

started = time.time()


def print_company_info(company):
    time.sleep(1)
    print(time.ctime(), company)


companies = ['ABT', 'ABBV', 'ABMD', 'ATVI', 'ADBE']

size = 5
with concurrent.futures.ThreadPoolExecutor(size) as thp:
    thp.map(print_company_info, companies)
elapsed = time.time()

print('Time taken: : ', elapsed - started)
# Time taken: : 1.0151422023773193
