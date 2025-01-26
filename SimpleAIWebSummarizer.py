# Step 1: Create the prompts

system_prompt = "You are a content curator and you will be summarizing the websites"
user_prompt =  "You are an content curator that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. You will list down any announcements mentioned.\
Respond in markdown."
website = Website("https://cnn.com")
    
# Step 2: Make the messages list

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

# Step 3: Call OpenAI

response =     response = openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages = messages_for(website)
    )

# Step 4: print the result

print(response.choices[0].message.content)
