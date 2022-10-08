from django.core.management.base import BaseCommand, CommandError
from job.models import Job
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def parse_post(self):
        import requests
        from bs4 import BeautifulSoup

        header = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/105.0.0.0 Safari/537.36 "
        }

        def all_category():  # повиносити у методи і викликати через self
            url = "https://jobs.dou.ua/"
            req = requests.get(url, headers=header)
            src = req.text

            soup = BeautifulSoup(src, "html.parser")
            all_jobs_category = soup.find_all(class_="cat-link")
            base_url = "{href}&search={search}"
            cat_href = []
            for cat in all_jobs_category:
                cat_href += [
                    (base_url.format(href=cat["href"], search="junior")),
                    (base_url.format(href=cat["href"], search="trainee")),
                    (base_url.format(href=cat["href"], search="intern", )),
                ]
            return cat_href

        def all_vacancies(cat_url):  # повиносити у методи і викликати через self
            req_1 = requests.get(url=cat_url, headers=header)  # зробити функцію
            src_1 = req_1.text
            soup_1 = BeautifulSoup(src_1, "html.parser")

            vacancies = soup_1.find_all(class_="vt")
            for items in vacancies:
                vacancy_url = items.get("href")
                return vacancy_url

        all_category_url = all_category()
        for item in all_category_url:
            url = all_vacancies(item)
            if not url:  # if data != None дорівнює if data:
                print("data was empty, next iteration")
                continue  # break, continue
            req_2 = requests.get(url=url, headers=header)
            src_2 = req_2.text
            soup_2 = BeautifulSoup(src_2, "html.parser")

            vacancy_name = soup_2.find(class_="g-h2").text
            place_info = soup_2.find(class_="place").text
            salary_info = soup_2.find(class_="salary")

            if salary_info is None:
                salary_info = "Не вказано"
            else:
                salary_info = soup_2.find(class_="salary").text
            post_qs = Job.objects.filter(url=url)  # get or create
            if not post_qs:
                post = Job(name=vacancy_name, source=Job.SRC_DOU, url=url, salary_info=salary_info,
                           place_info=place_info)
                post.save()
            else:
                print("Дана вакансія вже є в БД")

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        self.parse_post()

        self.stdout.write(self.style.SUCCESS('Post import done'))
