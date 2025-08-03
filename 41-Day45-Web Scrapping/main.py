from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    content = file.read()
    

soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup)
# print(soup.prettify())
# print(soup.a)

all_tags = soup.find_all(name="a")

for a_tag_content in all_tags:
    # print(a_tag_content.string)
    print(a_tag_content.getText() + "Links: " + a_tag_content.get("href"))


heading = soup.find(name="h1", id="name")
print(heading)
print(heading.getText())

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
print("Company URL: " + company_url.get("href"))

name = soup.select_one("#name")
print(name)
headings = soup.select(".heading")
print(headings)