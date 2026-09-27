# import requests
# import base64
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import pyautogui
# from datetime import datetime, timedelta

# def start_meeting_with_selenium(start_url):
#     options = webdriver.ChromeOptions()
#     options.add_argument('--disable-gpu')
    
#     options.add_argument('--no-sandbox')
#     driver = webdriver.Chrome(options=options)
    
#     try:
#         driver.get(start_url)
#         time.sleep(3)
#         pyautogui.press('tab')
#         pyautogui.press('tab')
#         pyautogui.press('enter')
#     finally:
#         driver.quit()


# def get_access_token():
#     client_id = '6ODnBsOQ3eourV4Oiig2Q'  # Replace with your Client ID
#     client_secret = 'FygiJkTA3A94N62kMoniB8w7ajvgbVS4'  # Replace with your Client Secret

#     # Encode credentials
#     auth_credentials = f"{client_id}:{client_secret}"
#     encoded_auth = base64.b64encode(auth_credentials.encode()).decode()
    
#     # Request token
#     token_url = "https://zoom.us/oauth/token"
#     headers = {
#         'Authorization': f'Basic {encoded_auth}',
#         'Content-Type': 'application/x-www-form-urlencoded'
#     }
#     data = "grant_type=account_credentials&account_id=Wre7dACAT22eZS07nISB4Q"  # Send as a query string

#     response = requests.post(token_url, headers=headers, data=data)
#     print(response.text)
    
#     if response.status_code != 200:
#         print(f"Error getting token: {response.status_code}")
#         print(response.text)
#         return None
    
#     return response.json().get('access_token')

# def stop_meeting(meeting_id, access_token):
#     url = f"https://api.zoom.us/v2/meetings/{meeting_id}/status"
#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "Content-Type": "application/json"
#     }
#     data = {"action": "end"}

#     response = requests.put(url, json=data, headers=headers)

# def get_meeting_details(meeting_id, access_token):
#     meeting_url = f"https://api.zoom.us/v2/meetings/{meeting_id}"
#     headers = {
#         'Authorization': f'Bearer {access_token}',
#         'Content-Type': 'application/json'
#     }
    
#     response = requests.get(meeting_url, headers=headers)
#     if response.status_code != 200:
#         print(f"Error fetching meeting details: {response.status_code}")
#         print(response.text)
#         return None
    
#     return response.json()


# # Main execution
# def main():
#     meeting_id = "87859256795"  # Replace with your scheduled meeting ID
    
#     access_token = get_access_token()
    
#     if not access_token:
#         print("Failed to obtain access token. Check your credentials.")
#         return
    
#     meeting_details = get_meeting_details(meeting_id, access_token)
#     if not meeting_details:
#         print("Failed to fetch meeting details.")
#         return
    
#     # Extract the start_url
#     start_url = meeting_details.get('start_url')
#     if not start_url:
#         print("No start_url found in meeting details.")
#         return
#     start_time = datetime.now()
#     start_meeting_with_selenium(start_url=start_url)

#     while True: 
#         current_time = datetime.now()

#         if current_time - start_time >= timedelta(minutes=7):
#             print("Mematikan meeting")
#             stop_meeting(meeting_id=meeting_id, access_token=access_token)
#             print("Memulai meeting")
#             start_meeting_with_selenium(start_url=start_url)
#             start_time = datetime.now()
#             time.sleep(10)
    
# if __name__ == "__main__":
#     main()

# import requests
# import base64
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import pyautogui
# from datetime import datetime, timedelta

# # Konfigurasi Zoom API
# CLIENT_ID = '6ODnBsOQ3eourV4Oiig2Q'  # Ganti dengan Client ID Anda
# CLIENT_SECRET = 'FygiJkTA3A94N62kMoniB8w7ajvgbVS4'  # Ganti dengan Client Secret Anda
# ACCOUNT_ID = 'Wre7dACAT22eZS07nISB4Q'  # Ganti dengan Account ID Anda
# MEETING_ID = "87859256795"  # Ganti dengan Meeting ID Anda

# def get_access_token():
#     """Mendapatkan access token dari Zoom API"""
#     auth_credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
#     encoded_auth = base64.b64encode(auth_credentials.encode()).decode()
    
#     token_url = "https://zoom.us/oauth/token"
#     headers = {
#         'Authorization': f'Basic {encoded_auth}',
#         'Content-Type': 'application/x-www-form-urlencoded'
#     }
#     data = f"grant_type=account_credentials&account_id={ACCOUNT_ID}"

#     response = requests.post(token_url, headers=headers, data=data)
    
#     if response.status_code != 200:
#         print(f"Error getting token: {response.status_code}")
#         print(response.text)
#         return None
    
#     return response.json().get('access_token')

# def start_meeting_with_selenium(start_url):
#     """Memulai Zoom meeting dengan Selenium"""
#     options = webdriver.ChromeOptions()
#     options.add_argument('--disable-gpu')
#     options.add_argument('--no-sandbox')

#     driver = webdriver.Chrome(options=options)

#     try:
#         driver.get(start_url)
#         time.sleep(3)
#         pyautogui.press('tab')
#         pyautogui.press('tab')
#         pyautogui.press('enter')
#         print("Meeting dimulai...")
#     finally:
#         driver.quit()

# def stop_meeting(meeting_id, access_token):
#     """Menghentikan Zoom meeting"""
#     url = f"https://api.zoom.us/v2/meetings/{meeting_id}/status"
#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "Content-Type": "application/json"
#     }
#     data = {"action": "end"}

#     response = requests.put(url, json=data, headers=headers)
    
#     if response.status_code == 204:
#         print("Meeting dihentikan.")
#     else:
#         print(f"Error menghentikan meeting: {response.status_code}")
#         print(response.text)

# def get_meeting_details(meeting_id, access_token):
#     """Mendapatkan detail Zoom meeting"""
#     url = f"https://api.zoom.us/v2/meetings/{meeting_id}"
#     headers = {
#         'Authorization': f'Bearer {access_token}',
#         'Content-Type': 'application/json'
#     }
    
#     response = requests.get(url, headers=headers)
#     if response.status_code != 200:
#         print(f"Error fetching meeting details: {response.status_code}")
#         print(response.text)
#         return None
    
#     return response.json()

# def start_breakout_rooms(meeting_id, access_token):
#     """Memulai Breakout Rooms secara otomatis"""
#     url = f"https://api.zoom.us/v2/live_meetings/{meeting_id}/breakout_rooms/start"
#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "Content-Type": "application/json"
#     }

#     response = requests.put(url, headers=headers)

#     if response.status_code == 204:
#         print("Breakout Rooms telah dibuka otomatis!")
#     else:
#         print(f"Error membuka Breakout Rooms: {response.status_code}")
#         print(response.text)

# def main():
#     access_token = get_access_token()
    
#     if not access_token:
#         print("Gagal mendapatkan access token. Periksa kredensial Anda.")
#         return
    
#     meeting_details = get_meeting_details(MEETING_ID, access_token)
#     if not meeting_details:
#         print("Gagal mengambil detail meeting.")
#         return

#     # Extract start_url
#     start_url = meeting_details.get('start_url')
#     if not start_url:
#         print("start_url tidak ditemukan dalam detail meeting.")
#         return

#     start_time = datetime.now()
#     start_meeting_with_selenium(start_url=start_url)

#     # Tunggu beberapa detik agar meeting benar-benar berjalan sebelum membuka Breakout Rooms
#     time.sleep(10)
#     start_breakout_rooms(MEETING_ID, access_token)

#     while True: 
#         current_time = datetime.now()

#         if current_time - start_time >= timedelta(minutes=7):
#             print("Menghentikan meeting...")
#             stop_meeting(meeting_id=MEETING_ID, access_token=access_token)
#             print("Memulai meeting kembali...")
#             start_meeting_with_selenium(start_url=start_url)
#             start_time = datetime.now()
#             time.sleep(10)

# if __name__ == "__main__":
#     main()




# import requests
# import base64
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import pyautogui
# from datetime import datetime, timedelta

# # Fungsi untuk membuka Breakout Rooms menggunakan PyAutoGUI
# def open_breakout_rooms():
#     time.sleep(5)

#     # Cari tombol "More" berdasarkan gambar
#     more_button = pyautogui.locateOnScreen("/button/more_button.png")
#     if more_button:
#         pyautogui.click(more_button)
#         time.sleep(3)

#         # Cari tombol "Breakout Rooms" berdasarkan gambar
#         breakout_button = pyautogui.locateOnScreen("/button/breakout_button.png")
#         if breakout_button:
#             pyautogui.click(breakout_button)
#             time.sleep(3)

#             # Cari tombol "Open All Rooms" berdasarkan gambar
#             open_all_button = pyautogui.locateOnScreen("/button/open_all_button.png")
#             if open_all_button:
#                 pyautogui.click(open_all_button)
#                 print("Breakout Rooms dibuka.")
#             else:
#                 print("Tombol 'Open All Rooms' tidak ditemukan.")
#         else:
#             print("Tombol 'Breakout Rooms' tidak ditemukan.")
#     else:
#         print("Tombol 'More' tidak ditemukan.")

# # Fungsi untuk memulai meeting dengan Selenium
# def start_meeting_with_selenium(start_url):
#     options = webdriver.ChromeOptions()
#     options.add_argument('--disable-gpu')
#     options.add_argument('--no-sandbox')
#     driver = webdriver.Chrome(options=options)

#     try:
#         driver.get(start_url)
#         time.sleep(3)
#         pyautogui.press('tab')
#         pyautogui.press('tab')
#         pyautogui.press('enter')

#         # Setelah meeting dimulai, buka Breakout Rooms
#         time.sleep(5)  # Tunggu hingga Zoom terbuka
#         open_breakout_rooms()  # Tidak perlu parameter driver karena pakai PyAutoGUI

#     finally:
#         driver.quit()

# # Fungsi untuk mendapatkan access token dari Zoom API
# def get_access_token():
#     client_id = '6ODnBsOQ3eourV4Oiig2Q'  # Replace with your Client ID
#     client_secret = 'FygiJkTA3A94N62kMoniB8w7ajvgbVS4'  # Replace with your Client Secret

#     auth_credentials = f"{client_id}:{client_secret}"
#     encoded_auth = base64.b64encode(auth_credentials.encode()).decode()
    
#     token_url = "https://zoom.us/oauth/token"
#     headers = {
#         'Authorization': f'Basic {encoded_auth}',
#         'Content-Type': 'application/x-www-form-urlencoded'
#     }
#     data = "grant_type=account_credentials&account_id=Wre7dACAT22eZS07nISB4Q"

#     response = requests.post(token_url, headers=headers, data=data)
    
#     if response.status_code != 200:
#         print(f"Error getting token: {response.status_code}")
#         print(response.text)
#         return None
    
#     return response.json().get('access_token')

# # Fungsi untuk menghentikan meeting
# def stop_meeting(meeting_id, access_token):
#     url = f"https://api.zoom.us/v2/meetings/{meeting_id}/status"
#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "Content-Type": "application/json"
#     }
#     data = {"action": "end"}

#     response = requests.put(url, json=data, headers=headers)

# # Fungsi untuk mendapatkan detail meeting
# def get_meeting_details(meeting_id, access_token):
#     meeting_url = f"https://api.zoom.us/v2/meetings/{meeting_id}"
#     headers = {
#         'Authorization': f'Bearer {access_token}',
#         'Content-Type': 'application/json'
#     }
    
#     response = requests.get(meeting_url, headers=headers)
#     if response.status_code != 200:
#         print(f"Error fetching meeting details: {response.status_code}")
#         print(response.text)
#         return None
    
#     return response.json()

# # Main execution
# def main():
#     meeting_id = "87859256795"  # Replace dengan Meeting ID
    
#     access_token = get_access_token()
    
#     if not access_token:
#         print("Failed to obtain access token. Check your credentials.")
#         return
    
#     meeting_details = get_meeting_details(meeting_id, access_token)
#     if not meeting_details:
#         print("Failed to fetch meeting details.")
#         return
    
#     # Extract the start_url
#     start_url = meeting_details.get('start_url')
#     if not start_url:
#         print("No start_url found in meeting details.")
#         return
    
#     start_time = datetime.now()
#     start_meeting_with_selenium(start_url=start_url)

#     while True: 
#         current_time = datetime.now()

#         if current_time - start_time >= timedelta(minutes=3):
#             print("Mematikan meeting")
#             stop_meeting(meeting_id=meeting_id, access_token=access_token)
#             print("Memulai meeting")
#             start_meeting_with_selenium(start_url=start_url)
#             start_time = datetime.now()

# if __name__ == "__main__":
#     main()

import requests
import base64
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from datetime import datetime, timedelta

# Fungsi untuk membuka Breakout Rooms menggunakan PyAutoGUI
import time
import pyautogui

def open_breakout_rooms():
    time.sleep(5)

    try:
        # Cari tombol "More" berdasarkan gambar
        more_button = pyautogui.locateOnScreen("button/more_button.png" , confidence=0.8)
        if more_button:
            pyautogui.click(more_button)
            print("Tombol 'More' ditemukan dan diklik.")
            time.sleep(1)

            breakout_button = pyautogui.locateOnScreen("button/breakout_button.png", confidence=0.8)
            if breakout_button:
                pyautogui.click(breakout_button)
                print("Tombol 'Breakout Rooms' ditemukan dan diklik.")
                time.sleep(1)

                open_all_button = pyautogui.locateOnScreen("button/open_all_button.png", confidence=0.8)
                if open_all_button:
                    pyautogui.click(open_all_button)
                    print("Breakout Rooms dibuka.")
                    time.sleep(1)

                    options_button = pyautogui.locateOnScreen("button/options.png", confidence=0.8)
                    if options_button:
                        pyautogui.click(options_button)
                        print("Tombol 'Options' ditemukan dan diklik.")
                        time.sleep(1)

                        allow_participants_to_choose_room = pyautogui.locateOnScreen("button/allow_participants_tochoose_room.png", confidence=0.8)
                        if allow_participants_to_choose_room:
                            pyautogui.click(allow_participants_to_choose_room)
                            print("Opsi 'Allow participants to choose room' dicentang.")
                        else:
                            print("Opsi 'Allow participants to choose room' tidak ditemukan.")
                    else:
                        print("Tombol 'Options' tidak ditemukan.")
                else:
                    print("Tombol 'Open All Rooms' tidak ditemukan.")
            else:
                print("Tombol 'Breakout Rooms' tidak ditemukan.")
        else:
            print("Tombol 'More' tidak ditemukan.")
    except Exception as e:
        print(f"Error saat mencari atau mengklik tombol: {e}")

def start_meeting_with_selenium(start_url):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(start_url)
        time.sleep(3)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')

        # Setelah meeting dimulai, buka Breakout Rooms
        time.sleep(5)
        open_breakout_rooms() 

    finally:
        driver.quit()

# Fungsi untuk mendapatkan access token dari Zoom API
def get_access_token():
    client_id = '6ODnBsOQ3eourV4Oiig2Q'  # Replace with your Client ID
    client_secret = 'FygiJkTA3A94N62kMoniB8w7ajvgbVS4'  # Replace with your Client Secret

    auth_credentials = f"{client_id}:{client_secret}"
    encoded_auth = base64.b64encode(auth_credentials.encode()).decode()
    
    token_url = "https://zoom.us/oauth/token"
    headers = {
        'Authorization': f'Basic {encoded_auth}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = "grant_type=account_credentials&account_id=Wre7dACAT22eZS07nISB4Q"

    response = requests.post(token_url, headers=headers, data=data)
    
    if response.status_code != 200:
        print(f"Error getting token: {response.status_code}")
        print(response.text)
        return None
    
    return response.json().get('access_token')

# Fungsi untuk menghentikan meeting
def stop_meeting(meeting_id, access_token):
    url = f"https://api.zoom.us/v2/meetings/{meeting_id}/status"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {"action": "end"}

    response = requests.put(url, json=data, headers=headers)

# Fungsi untuk mendapatkan detail meeting
def get_meeting_details(meeting_id, access_token):
    meeting_url = f"https://api.zoom.us/v2/meetings/{meeting_id}"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(meeting_url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching meeting details: {response.status_code}")
        print(response.text)
        return None
    
    return response.json()

# Main execution
def main():
    meeting_id = "87859256795"  # Replace dengan Meeting ID
    
    access_token = get_access_token()
    
    if not access_token:
        print("Failed to obtain access token. Check your credentials.")
        return
    
    meeting_details = get_meeting_details(meeting_id, access_token)
    if not meeting_details:
        print("Failed to fetch meeting details.")
        return
    
    # Extract the start_url
    start_url = meeting_details.get('start_url')
    if not start_url:
        print("No start_url found in meeting details.")
        return
    
    start_time = datetime.now()
    start_meeting_with_selenium(start_url=start_url)

    while True: 
        current_time = datetime.now()

        if current_time - start_time >= timedelta(minutes=2):
            print("Mematikan meeting")
            stop_meeting(meeting_id=meeting_id, access_token=access_token)
            print("Memulai meeting")
            start_meeting_with_selenium(start_url=start_url)
            start_time = datetime.now()

if __name__ == "__main__":
    main()
