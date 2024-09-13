import scrapy
import pandas as pd

class CompanySpider(scrapy.Spider):
    name = "company_spider"

    # Start requests using a prompt (e.g., diesel generator)
    def __init__(self, prompt=None, *args, **kwargs):
        super(CompanySpider, self).__init__(*args, **kwargs)
        self.prompt = prompt if prompt else "diesel generator"

    def start_requests(self):
        # Replace this with actual search URL for companies
        search_url = f'https://www.linkedin.com/search/results/companies/?keywords={self.prompt}'
        
        yield scrapy.Request(url=search_url, callback=self.parse)

    def parse(self, response):
        companies = []
        for company in response.css('li.company-result-card')[:11]:  # Limit to top 11 companies
            name = company.css('h3::text').get()
            linkedin_url = company.css('a::attr(href)').get()
            description = company.css('p.company-description::text').get()

            companies.append({
                'name': name,
                'linkedin_url': linkedin_url,
                'description': description,
            })
        
        # Save data to CSV
        df = pd.DataFrame(companies)
        df.to_csv('companies.csv', index=False)

        self.log('Saved top 11 companies to companies.csv')
