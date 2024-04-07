import requests

def e_posta_bul(username):
    url = f"https://www.instagram.com/{username}/?__a=1"
    response = requests.get(url)
    if response.status_code == 200:
        user_data = response.json()
        if 'email' in user_data['graphql']['user']:
            email = user_data['graphql']['user']['email']
            print(f"{username} kullanıcısının e-posta adresi: {email}")
        else:
            print(f"{username} kullanıcısının herkese açık bir e-posta adresi yok.")
    else:
        print("Kullanıcı bulunamadı veya bir hata oluştu.")

username = input("E-postasını bulmak istediğiniz Instagram kullanıcı adını girin: ")
e_posta_bul(username)
