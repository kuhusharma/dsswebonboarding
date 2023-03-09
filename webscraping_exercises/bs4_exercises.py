from bs4 import BeautifulSoup 
import requests

session_object = requests.Session()
web_page = session_object.get("https://realpython.github.io/fake-jobs/")

soup = BeautifulSoup(web_page.content, "html.parser")

# Q1: What does the first p tag look like on this page?
first_p = soup.find(...)
print(first_p.prettify()) # prettify makes the string look nicer when printed
print(first_p.text) # .text grabs the text content from the <p> tag 
# --------------------------

# Q2: How many div tags are there on this page?
all_divs = soup.find_all(...) # this should return a list
print(...)
# --------------------------

# Let's explore the card element. This has information we want to look at!
first_card = soup.find('div', class_=...)
print(first_card.prettify())

# Q3: Take a look at the result. Write code to grab the <a> tag (which holds links) associated with the "Apply" button from the first_card and print it. You can also "inspect element" on the website to see where exactly this is. 
first_apply = first_card.find(..., ..., text=...) # you may not need to fill in all the ellipses -- if they're not used, just delete them.
print(first_apply.prettify())

# Now that we have the <a> tag, here's how we can grab the actual link from it.
first_apply_link = first_apply.attrs['href'] # attrs returns a dictionary formatted like attribute:value. In this case we want "href" which holds the link url.
print(first_apply_link)
# --------------------------

# Q4: Now, using what we've currently learned, grab all the "Apply" links on this webpage -- this information should be in a list. Grabbing the tags should only take one line. But you can take as many lines as you need to get the links themselves.
apply_link_tags = ...
apply_links = []
...

# --------------------------

# Note that this question is particularly challenging but should be possible with the knowledge gained from the previous exercises. 

# Q5: Using the links from the apply_links list, grab all the job descriptions from the pages associated with those links and place them in a list.
 
# A few hints: You can create a temporary soup object, similar to how we created a soup object at the start of this HW! Remember to inspect element to see the structure of the webpage! Additionally you may notice that the <p> tag has no class associated with it, but it's position relative to the other p elements will be consistent amongst all the pages.
descriptions = []

for ...:

print(descriptions[0]) # this should return a description
