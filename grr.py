import requests

def get_email_from_instagram(username):
    url = f"https://www.instagram.com/{username}/?__a=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        email = data['graphql']['user']['business_email']
        return email
    else:
        return None

# Replace 'username' with the Instagram username of the person you want to get the email from
username = 'heroin__needles'
email = get_email_from_instagram(username)
if email:
    print(f"The email address of {username} is: {email}")
else:
    print(f"Could not retrieve the email address for {username}")
