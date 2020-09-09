import time

started = time.time()


def print_company_info(company):
    time.sleep(1)
    print(time.ctime(), company)


companies = ['ABT', 'ABBV', 'ABMD', 'ATVI', 'ADBE']
for company in companies:
    print_company_info(company)


elapsed = time.time()

print('Time taken: :', elapsed-started)
# Time taken: : 5.033333778381348
