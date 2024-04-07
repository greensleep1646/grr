
import requests
from bs4 import BeautifulSoup

def email_bul(username):
    url = 'https://www.instagram.com/' + username
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    meta_tags = soup.find_all('meta')
    
    for tag in meta_tags:
        if 'property' in tag.attrs and tag.attrs['property'] == 'og:description':
            content = tag.attrs['content']
            email_index = content.find('E-mail:')
            if email_index != -1:
                email = content[email_index+7:].split(' ')[0]
                print("Kişinin e-posta adresi:", email)
                return email
    
    print("E-posta adresi bulunamadı.")

username = input("Instagram kullanıcı adını girin: ")
email_bul(username)
