import requests
from bs4 import BeautifulSoup
import yaml

def scrape_linkedin_jobs(search_query="Software Engineer"):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.linkedin.com/jobs/search/?keywords={search_query}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    jobs = []
    for job in soup.find_all("div", class_="job-search-card"):
        title = job.find("h3").text.strip()
        company = job.find("a", class_="hidden-nested-link").text.strip()
        jobs.append({"title": title, "company": company})
    
    return jobs

if __name__ == "__main__":
    print(scrape_linkedin_jobs())