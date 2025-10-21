import requests

def fetch_microsoft_jobs(page=1, page_size=20):
    """
    Fetch Microsoft job listings for India (Software & Data roles).

    Returns:
        List of dicts containing {title, location, team, url}.
    """

    url = (
        f"https://gcsservices.careers.microsoft.com/search/api/v1/search"
        f"?lc=India"
        f"&p=Research%2C%20Applied%2C%20%26%20Data%20Sciences"
        f"&p=Software%20Engineering"
        f"&exp=Experienced%20professionals"
        f"&et=Full-Time"
        f"&l=en_us"
        f"&pg={page}"
        f"&pgSz={page_size}"
        f"&o=Recent"
        f"&flt=true"
    )

    headers = {
        "user-agent": "Mozilla/5.0",
        "accept": "application/json",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        results = []
        for job in data.get("operationResult", {}).get("result", []).get("jobs", []):
            results.append({
                "id": job.get("jobId"),
                "title": job.get("title"),
                "location": job.get("properties", []).get("locations", []),
                "team": job.get("profession"),
                "url": f"https://jobs.careers.microsoft.com/global/en/job/{job.get('jobId')}",
            })
        return results

    except Exception as e:
        print("Error fetching Microsoft jobs:", e)
        return []


if __name__ == "__main__":
    jobs = fetch_microsoft_jobs()
    print(f"Fetched {len(jobs)} Microsoft jobs.")
    for job in jobs[:5]:
        print(f"{job['title']} - {job['location']} ({job['team']})")
        print(job['url'])