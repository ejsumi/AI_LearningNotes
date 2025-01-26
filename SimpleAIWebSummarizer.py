#This code snippet utilizes OpenAI's gpt-4o-mini model to summarize a website. 
#It begins by defining two prompts: a system prompt instructing the model to function as a content curator for website summarization, 
#and a user prompt that provides more specific guidelines, such as disregarding navigation elements and presenting announcements in markdown format. 
#Subsequently, it constructs a list of messages encompassing both the system and user prompts. 
#Then, it employs the OpenAI API (not explicitly included in this snippet) to transmit these messages and obtain a response. 
#Finally, the code extracts and displays the summarized content from the OpenAI response.

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

response = openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages = messages_for(website)
    )

# Step 4: print the result

print(response.choices[0].message.content)
