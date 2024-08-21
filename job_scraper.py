import requests
from bs4 import BeautifulSoup

def fetch_job_listings(keyword, location):
    # Example URL (replace with actual job board URL)
    url = f"https://www.examplejobboard.com/jobs?q={keyword}&l={location}"
    
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        jobs = []
        
        for job_elem in soup.find_all('div', class_='job-listing'):
            title_elem = job_elem.find('h2', class_='job-title')
            company_elem = job_elem.find('div', class_='company')
            location_elem = job_elem.find('div', class_='location')
            description_elem = job_elem.find('div', class_='description')
            
            if None in (title_elem, company_elem, location_elem, description_elem):
                continue
            
            job = {
                'title': title_elem.text.strip(),
                'company': company_elem.text.strip(),
                'location': location_elem.text.strip(),
                'description': description_elem.text.strip()
            }
            jobs.append(job)
        
        return jobs
    else:
        print("Failed to fetch job listings")
        return []

def display_jobs(jobs):
    for job in jobs:
        print(f"Title: {job['title']}")
        print(f"Company: {job['company']}")
        print(f"Location: {job['location']}")
        print(f"Description: {job['description']}")
        print("-" * 40)

def main():
    keyword = input("Enter job keyword: ")
    location = input("Enter job location: ")
    
    jobs = fetch_job_listings(keyword, location)
    if jobs:
        display_jobs(jobs)
    else:
        print("No jobs found")

if __name__ == "__main__":
    main()
