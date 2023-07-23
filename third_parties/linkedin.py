import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """
    scrape information from Linkedin Profiles,
    Manually scrape the information from the LinkedIn Profile.
    """
    api_endpoint = linkedin_profile_url
    response = requests.get(api_endpoint)
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications", "accomplishment_publications", "'accomplishment_courses",
                      "accomplishment_projects", "accomplishment_organisations"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
