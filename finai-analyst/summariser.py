from llm_client import PROVIDER, client

def summarise_regulation(text):
    if PROVIDER == "openai":
        prompt = f"""
You are a financial compliance expert. Summarise the following RBI circular into:

1. Summary (<=100 words)
2. Applicability (who is affected)
3. Key operational mandates
4. Implementation deadline
5. Non-compliance penalties

Text:
{text}
"""
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a regulatory compliance summarisation assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    
    elif PROVIDER == "gemini":
        #model = client.GenerativeModel('gemini-1.5-pro-latest') ==> Deprecated
        model = client.GenerativeModel("gemini-2.5-pro")
        # or use flash variants:
        # model = client.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(f"""
You are a financial compliance expert. Summarise the following RBI circular into:

1. Summary (<=100 words)
2. Applicability (who is affected)
3. Key operational mandates
4. Implementation deadline
5. Non-compliance penalties

Text:
{text}
""")
        return response.text
