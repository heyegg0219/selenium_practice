from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import csv

base = "https:"
options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome('./chromedriver', chrome_options=options)

chrome.get(
    "https://www.104.com.tw/jobs/search/?ro=0&keyword=Python&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area"
    "=6001001001%2C6001001003%2C6001005001%2C6001005002&order=3&asc=1&page=1&mode=s&jobsource=2018indexpoc&langFlag=0"
    "&langStatus=0&recommendJob=1&hotJob=1")
<<<<<<< HEAD

=======
#
>>>>>>> dca1d1ffe46a32cd878dc2fa76f4ac7fbe61b8b9
for x in range(1, 16):  # 執行滾動捲軸15次，每滾動一次就暫停執行程式碼0.5秒
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(0.5)

soup = BeautifulSoup(chrome.page_source, 'html.parser')

data = soup.select('article', {'class': 'b-block--top-bord job-list-item b-clearfix js-job-item'})

all_job_datas = []

for job in data:
    try:
        a_1 = job.find("a", class_="js-job-link").text  # 工作名稱

        a_2 = base + job.find("a", class_="js-job-link").get('href')  # 工作網址

        a_3 = job.find("div", class_="job-list-tag b-content").text  # 公司薪資及內容

        a_4 = job.get('data-cust-name')  # 公司名稱

        a_5 = job.find('ul', class_='b-list-inline b-clearfix job-list-intro b-content').text  # 公司位置

        a_6 = job.find("p", class_="job-list-item__info b-clearfix b-content").text  # 工作內容

        a_7 = job.find("h2", class_="b-tit").findAll("span")[0].text  # 工作更新日期

        a_8 = job.find("ul", class_="b-list-inline b-clearfix").findAll("a")  # 公司網址
        a_9 = base + a_8[0].get('href')

        job_data = {'job_name': a_1, 'company_name': a_4, "company_url": a_9, 'company_content': a_3,
                    "job_content": a_6, 'job_address': a_5, 'job_url': a_2, "job_date": a_7}

        all_job_datas.append(job_data)
    except AttributeError as e:
        print("=" * 50)
        # print(job)
        print(e.args)
        print("=" * 50)

all_job_datas_2 = all_job_datas
print(all_job_datas_2)

columns_name = ["job_date", 'job_name', 'company_name', 'company_content', "job_content", 'job_address', 'job_url',
                "company_url"]  # 第一欄的名稱

with open('104人力銀行.csv', 'w', newline='', encoding='utf-8-sig') as csvFile:  # 定義CSV的寫入檔,並且每次寫入完會換下一行
    dictWriter = csv.DictWriter(csvFile, fieldnames=columns_name)  # 定義寫入器
    dictWriter.writeheader()
    for data in all_job_datas_2:
        dictWriter.writerow(data)

chrome.quit()
