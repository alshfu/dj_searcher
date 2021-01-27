import json
import os
import sys

from stripe.http_client import requests
from slugify import slugify, Slugify, UniqueSlugify

from config import Config


proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'dj_searcher.settings'

import django

django.setup()

# from scraping.Models.JobAD.JobAd import JobAd
from scraping.Models.JobAD.JobAd import JobAd
from scraping.Models.location.City import City
from scraping.Models.JobAD.JobTechTaxonomyItem import JobTechTaxonomyItem


class PB(Config):
    job_list = []

    def set_job_list(self):
        for tag in self.get_tag_list():
            query = tag + ' ' + self.get_city()
            search_params = {'q': query, 'limit': 100}
            response = requests.get(self.url, headers=self.headers, params=search_params)
            response.raise_for_status()
            json_response = json.loads(response.content.decode('utf8'))
            hits = json_response['hits']
            for hit in hits:
                url = hit['application_details']['url']
                id = hit['id']
                if url != None:
                    # print(hit)
                    headline = hit['headline']
                    print(url)

                    city = hit['workplace_address']['municipality']
                    print(city)

                    logo_url = hit['logo_url']
                    print(logo_url)

                    description = hit['description']
                    description = description['text']
                    # print(description)

                    occupation = hit['occupation']['label']
                    print(occupation)

                    af_id = id
                    print(id)

                    company = hit['employer']
                    print(company)
                    print('########################')
                    job_ad = JobAd(headline=headline,
                                   city=City(name=city,slug=slugify(city)),
                                   logo_url=logo_url,
                                   description=description,
                                   occupation=JobTechTaxonomyItem(label=occupation),
                                   af_id=af_id)
                    job_ad.save()
            # company = hit['']


    def get_job_list(self):
        return self.job_list


    def read_job_list(self):
        self.set_job_list()
        for job in self.get_job_list():
            pass
            # print(job)


if __name__ == '__main__':
    pb = PB()
    pb.read_job_list()
