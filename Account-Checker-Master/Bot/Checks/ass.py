import requests
import time
from datetime import date
from message import Editmessage, Sendmessage, logger

def bin_helper(chat_id, combo):
    status = Sendmessage(chat_id, '<i>Checking....</i>')
    try:
        cc = combo
    except IndexError:
        return Editmessage(chat_id, 'Enter Valid Combo😡😡', status)

    bin_url = 'https://password-gen.ga/bininfo.php?bin='+cc
    head1 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    response = requests.post(bin_url, headers=head1)
    result = response.json()
    bank = result['bank']['name']
    scheme = result['scheme']
    bintype = result['type']
    country = result['country']['name']
    brand = result['level']
    bininfo = f'<b>«——»Bin Data«——»\n\nBin: <code>{cc} </code>\nCountry: {country} \nType: {bintype} \nScheme: {scheme} \nBrand: {brand} \n\nMade By @GravityZR</b>'
    Editmessage(chat_id, bininfo, status)