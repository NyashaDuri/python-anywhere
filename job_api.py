import requests

def fetch_job_listings(keyword, location):
    # Example API endpoint (replace with actual job API)
    api_url = f"https://api.example.com/jobs?keyword={keyword}&location={location}"
    
    response = requests.get(api_url)
    if response.status_code == 200:
        jobs = response.json()
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
