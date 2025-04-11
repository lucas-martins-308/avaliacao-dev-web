from google import genai

def getResponse(prompt):
    client = genai.Client(api_key="AIzaSyAtjR-NH1xb7NNxPoCM39k9Z6mU-23nBM8")

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return(response.text)