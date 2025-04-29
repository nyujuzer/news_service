from requests import get, post
from google import genai
import json
from pydantic import BaseModel
from enum import Enum
from .settings import GOOGLE_KEY, NEWS_KEY

client = genai.Client(api_key=GOOGLE_KEY)

# Define the categories/tags for the articles
class tags(Enum):
    POLITICS = "Politics"
    ECONOMY = "Economy"
    TECHNOLOGY = "Technology"
    HEALTH = "Health"
    ENTERTAINMENT = "Entertainment"
    SPORTS = "Sports"
    ENVIRONMENT = "Environment"
    INTERNATIONAL = "International"
    CULTURE = "Culture"
    OPINION = "Opinion"
    INVESTIGATIONS = "Investigations"
    BREAKING_NEWS = "Breaking News"
    CONSPIRACIES = "Conspiracies"
    HUMAN_INTEREST = "Human Interest"
    CELEBRITIES = "Celebrities"
    SCIENCE = "Science"
    CRIME = "Crime"
    MILITARY = "Military"
    FAITH = "Faith"
    WEIRD_NEWS = "Weird News"
    UFO_SIGHTINGS = "UFO Sightings"
    CORPORATE_SCANDALS = "Corporate Scandals"
    ARTIFICIAL_INTELLIGENCE = "Artificial Intelligence"
    HISTORICAL_REVISIONISM = "Historical Revisionism"
    AGRICULTURE = "Agriculture"
    EDUCATION = "Education"
    SOCIAL_MEDIA = "Social Media"
    SECRET_SOCIETIES = "Secret Societies"
    REAL_ESTATE = "Real Estate"

# Define the structure of the article
class article(BaseModel):
  title: str
  body_text: str
  tags: list[tags]



def get_news():
    # Fetch the latest news articles
    response = get(f"https://newsdata.io/api/1/latest?apikey={NEWS_KEY}&language=en").json()
    articles = response['results']
    
    # Extract titles and descriptions from the articles
    extracted_titles_desc = extract_titles_desc(articles)
    
    # Pass the extracted titles and descriptions to the AI for satire generation
    articleList = get_new_articles(extracted_titles_desc)
    return articleList
def get_new_articles(extracted_titles_desc):
    return_list = []
    
    for i in extracted_titles_desc:
        prompt = f"Imagine you are a world-class satirist. You are handed the following article: {i['title']} - {i['description']}.\n\nNow, use your comedic genius to write a long, satirical article poking fun at this. Make it funny, absurd, and revealing about the insanity that exists in the world today. Tag your article appropriately, like 'Politics,' 'Economy,' 'Weird News,' etc. Be sure to add the title and a body of text to your satirical article."
        # Generate satirical article based on the original news article
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=prompt,
            config={
                'response_mime_type': 'application/json',
                'response_schema': list[article],
            },
        )
        
        responseJSON = json.loads(response.text)
        return_list.append({
            "title": responseJSON[0]['title'], 
            "body_text": responseJSON[0]['body_text'], 
            "tags": responseJSON[0]["tags"]
        })
    
    return return_list

def extract_titles_desc(articles):
     # Extract titles and descriptions from the fetched articles
    return_object_list = []
    for article in articles:
        return_object_list.append({
            "title": article['title'], 
            "description": article['description']
        })
    return return_object_list