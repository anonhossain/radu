import base64
from typing import List
import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel


class Quote(BaseModel):
    event_name: str
    quote: str

class QuoteGenerator:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key)

    def generate_quote(self, event_name: str, event_description: str, category: str, number: int):
        """Generate multiple inspirational quotes for a given category (using yield)."""
        for _ in range(number):
            prompt = f"""
                The name of the event is {event_name}, and the event description is: {event_description}.

                    Please provide a motivational quote to encourage, motivate the user and that must be highly relevance to the {category} category.

                    Strict guidelines to follow:

                    The quote must be high quality a precise one.
                    The quote must be emotional and inspiring, and it should resonate with the user's feelings and aspirations.
                    The quote must not include the author's name. If the quote is AI-generated, then also do not show that is AI-generated or unkown or anything.
                    The quote must be inspirational, and relevant to {event_name}, {event_description}, and the {category} category.

                    Please ensure the output follows this exact JSON format:

                    {{
                    "event_name": "{event_name}",
                    "quote": "quote"
                    
                    }}
                    Now, provide one valid, high-quality, and inspirational quote related to the {event_description} and the {category} category . 
                """
            
            try:
                response = self.client.chat.completions.create(
                    model="gpt-4-turbo", #gpt-4o gpt-4-turbo-2024-04-09
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that generates inspirational, ,motivational quotes both from author also by self generation."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=50,
                    temperature=0.7
                )
                yield response.choices[0].message.content.strip()
            except Exception as e:
                yield {"error": str(e)}


    def generate_quote2(self, mood: str, event_name: str, event_description: str, category: str, number: int, language: str): 
        """Generate multiple inspirational quotes for a given category (using yield).""" 
        for _ in range(number): 
            prompt = f""" 
            The name of the event is {event_name}, and the event description is: {event_description}. 
            The user is feeling {mood}.  
            Please provide a motivational quote to encourage, motivate the user and that must be highly relevance to the {category} category.
            The language of the quote should be in {language}. 
            
            Strict guidelines to follow: 
            The quote must be high quality a precise and short one. 
            The quote must be emotional and inspiring, and it should resonate with the user's feelings and aspirations. 
            The quote must not include the author's name. 
            If the quote is AI-generated, then also do not show that is AI-generated or unkown or anything. 
            The quote must be inspirational, and relevant to {event_name}, {event_description}, and the {category} category. 
            Based on all the event_name of the day make the quote more relevant to the user and the event_name of the day.
             
            Please ensure the output follows this exact JSON format: 
            {{ "event_name": "{event_name}", "quote": "quote" }} 
            Now, provide one valid, high-quality, and inspirational quote related to the {event_description} and the {category} category . 
            """ 
            
            try: 
                response = self.client.chat.completions.create( 
                    model="gpt-5.6-luna", #gpt-4o gpt-4-turbo-2024-04-09 
                    messages=[ 
                        {"role": "system", "content": "You are a helpful assistant that generates inspirational, ,motivational quotes both from author also by self generation."}, 
                        {"role": "user", "content": prompt} ], 
                        max_completion_tokens=150, 
                        reasoning_effort="high" 
                        ) 
                yield response.choices[0].message.content.strip() 
            except Exception as e: 
                yield {"error": str(e)}

# Test 
if __name__ == "__main__":
    generator = QuoteGenerator()
    mood = "inspired"
    event_name = "International Women's Day"
    event_description = "A global day celebrating the social, economic, cultural, and political achievements of women"
    category = "Empowerment"
    number = 1
    language = "English"

    for quote in generator.generate_quote2(mood, event_name, event_description, category, number, language):
        print(quote)
