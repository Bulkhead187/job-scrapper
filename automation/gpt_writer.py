import openai

def generate_cover_letter(job_description, api_key):
    openai.api_key = api_key
    
    #german prompt
    prompt = f"Schreibe eine kurze, professionelle Bewerbungs-E-Mail für diese Stelle:\n{job_description}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content