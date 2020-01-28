import requests
from bs4 import BeautifulSoup

url = input("Enter SO thread url: ")
thread = requests.get(url)
soup = BeautifulSoup(thread.text, 'html.parser')
ele_qhead = soup.find(class_='question-hyperlink')
eles_ups = soup.find_all(class_='js-vote-count grid--cell fc-black-500 fs-title grid fd-column ai-center')
ele_tAns = soup.find(class_='subheader answers-subheader').contents[1].contents[0]
eles_ans = soup.find(class_='answer accepted-answer')
ans_by = eles_ans.findChildren(class_='user-details')[1].contents[1].contents[0]
ans_text = eles_ans.findChild(class_='post-text').getText()
print('QUESTION:')
print('Upvotes: ', eles_ups[0].contents[0])
print('Question: ', ele_qhead.contents[0])
print()
print('ANSWERS:')
print('Total ', ele_tAns.strip())
print('Top answer upvotes:', eles_ups[1].contents[0])
print('By:', ans_by)
print('Soultion: ', ans_text)