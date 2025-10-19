import requests

def fetch_uber_jobs(limit=100, page=0):
    """
    Fetch Uber job listings for selected Indian cities.

    Returns:
        List of dicts containing {title, location, team, url}.
    """

    url = "https://www.uber.com/api/loadSearchJobsResults?localeCode=en"

    headers = {
        "content-type": "application/json",
        "x-csrf-token": "x",           # avoids 403
        "user-agent": "Mozilla/5.0",   # helps avoid bot filtering
    }

    body = {
        "limit": limit,
        "page": page,
        "params": {
            "location": [
                {"country": "IND", "region": "Haryana", "city": "Gurgaon"},
                {"country": "IND", "region": "Karnataka", "city": "Bangalore"},
                {"country": "IND", "region": "Telangana", "city": "Hyderabad"}
            ]
        }
    }

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        data = response.json()
        print(data)

        results = []
        # for job in data.get("data", {}).get("list", []):
        #     results.append({
        #         "id": job.get("id"),5
        #         "title": job.get("title"),
        #         "location": job.get("city"),
        #         "team": job.get("department"),
        #         "url": f"https://www.uber.com/global/en/careers/list/{job.get('id')}/"
        #     })
        return results

    except Exception as e:
        print("Error fetching Uber jobs:", e)
        return []


if __name__ == "__main__":
    jobs = fetch_uber_jobs()
    print(f"Fetched {len(jobs)} Uber jobs.")
    for job in jobs[:5]:  # show first 5
        print(f"{job['title']} - {job['location']} ({job['team']})")
        print(job['url'])
