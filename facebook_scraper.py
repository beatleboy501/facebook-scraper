import requests
from BeautifulSoup import BeautifulSoup
from lxml import html


class FacebookScraper:
    def __init__(self):
        pass

    def get_job_titles_and_links(self, url, id):
        response = requests.get(url)
        soup = BeautifulSoup(response.content)
        divs = soup.findAll('div', attrs={'id': id})
        jobs = divs.pop(0).findAll('a')
        job_title_and_link = {}
        for job in jobs:
            job_title_and_link[job.text] = 'https://www.facebook.com' + job['href']
        return job_title_and_link

    def get_page_text(self, url):
        response = requests.get(url)
        xpath_query = '//*[@id="content"]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]//div/text()'
        tree = html.fromstring(response.content)
        job_description = tree.xpath(xpath_query)
        for description in job_description:
            with open("all_words.txt", "a") as text_file:
                text_file.write(description.encode('utf-8'))

    def get_job_descriptions_for_category(self, new_york_url, category):
        print(category)
        jobs = self.get_job_titles_and_links(new_york_url, category + 'div')
        # TODO: list all job titles and then filter out the non-applicable job titles and list those too
        for job in jobs:
            url = jobs[job]
            self.get_page_text(url)

    def main(self):
        new_york_url = 'https://www.facebook.com/careers/locations/newyork/'
        categories = ['Software Engineering', 'Solutions Engineering', 'Client Solutions', 'GMS Operations',
                      'Instagram', 'Product Marketing, Global Marketing Solutions']
        for category in categories:
            self.get_job_descriptions_for_category(new_york_url, category)


fb_scraper = FacebookScraper()
fb_scraper.main()
