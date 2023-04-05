from bs4 import BeautifulSoup
import lxml
import requests
#
with open("website.html", "r") as html_file:
    contents = html_file.read()

# Passing the html content to new object from BeautifulSoup class for parsing
soup = BeautifulSoup(contents, "html.parser")

# print(soup.prettify())
# #print(soup.title)
# print(soup.title.string)

# print(soup.a)

# Searching all tags
# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# print(soup.select(".heading"))
#
#
#
# print(soup.find_all("a"))



# Parsing a live website

response = requests.get(url="https://news.ycombinator.com")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

# Find the first anchor tag that has a class of "storylink"

story_link = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []


for article_tag in story_link:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.select(selector="span href")
    article_links.append(link)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
print(article_upvotes)

# print(int(article_upvotes[0].split()[0]))

largest_number = max(article_upvotes)
largets_index = article_upvotes.index(largest_number)
print(article_texts[largets_index])