from llm_client import PROVIDER, client

def generate_business_insights(summary_text):
    if PROVIDER == "openai":
        prompt = f"""
You are a fintech business analyst. Based on the following regulation summary, generate:

1. Operational changes required
2. Key business risks
3. Suggested implementation steps

Summary:
{summary_text}
"""
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a business operations analyst for fintech compliance."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    
    elif PROVIDER == "gemini":
        #model = client.GenerativeModel('gemini-1.5-pro-latest')
        model = client.GenerativeModel("gemini-2.5-pro")
        response = model.generate_content(f"""
You are a fintech business analyst. Based on the following regulation summary, generate:

1. Operational changes required
2. Key business risks
3. Suggested implementation steps

Summary:
{summary_text}
""")
        return response.text
