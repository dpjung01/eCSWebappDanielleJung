import json
import sys
import requests
import pandas as pd
# input is ip address
# grab all asn's 
# in loop query bgpview for each asn and display info
#ipaddrstr = "24.23.201.228"

def get_asninfo(ipaddrstr):

    BASE_URL_IP = 'https://api.bgpview.io/ip'
    BASE_URL_ASN = 'https://api.bgpview.io/asn'

    url_ip = ('{}/{}').format(BASE_URL_IP, ipaddrstr)
    r = requests.get(url_ip)
    r.raise_for_status()
    if r.status_code == 200:
        if r.json()['status'] == 'ok':
            response_data = r.json()['data']
        error = True
    jsondump = json.dumps(response_data)

    #this list only gets unique asn values
    asnlist = list({i['asn']['asn'] for i in response_data['prefixes']})
    #return asnlist

    allasninfo = ""
    for asnstr in asnlist:
        url_prefix = ('{}/{}/prefixes').format(BASE_URL_ASN, asnstr)
        r = requests.get(url_prefix)
        r.raise_for_status()
        if r.status_code == 200:
            if r.json()['status'] == 'ok':
                response_data = r.json()['data']
            error = True
        allasninfo = allasninfo + json.dumps(response_data)

        #response_data is sent to the html web page as a string
        #javascript can convert it from string to json object if all key values are in double quotes
        #since response_data dumps key values as double quotes - yay
    return allasninfo
    # entire results
    #jsondump = json.dumps(response_data)

    # displays list of prefix only
    #prefixlist = [i['prefix'] for i in response_data['ipv4_prefixes']]

    #to get each ip4 prefix entry
    #for key in response_data['ipv4_prefixes']:
    #   print(key)
    #>>> type(prefixlist)
    #<class 'list'>
    #>>> type(key)
    #<class 'dict'>

def main():
    print("hello") 
    get_asninfo("24.23.201.228")

if __name__=='__main__':
    main()


def test_input():
    info = {"ipv4_prefixes": [{"prefix": "23.24.0.0/15", "ip": "23.24.0.0", "cidr": 15, "roa_status": "Valid", "name": "CBC-ALLOC-4", "description": "Comcast Cable Communications, LLC", "country_code": "US", "parent": {"prefix": "23.24.0.0/15", "ip": "23.24.0.0", "cidr": 15, "rir_name": "ARIN", "allocation_status": "unknown"}}, 
    {"prefix": "23.30.0.0/15", "ip": "23.30.0.0", "cidr": 15, "roa_status": "Valid", "name": "CBC-CM-4", "description": "Comcast Cable Communications, LLC", "country_code": "US", "parent": {"prefix": "23.30.0.0/15", "ip": "23.30.0.0", "cidr": 15, "rir_name": "ARIN", "allocation_status": "unknown"}}
    ]}
    return info

def transform_input():
    info = test_input()
    rows = []
    
    dict_list = info["ipv4_prefixes"]
    for data in dict_list:
        current_row = []
        for key in data:
            if key == "parent":
                for parent_key in data["parent"]:
                    current_row.append(data["parent"][parent_key])
            else:
                current_row.append(data[key])
        
        rows.append(current_row)

    print(rows)
    print("\n")
    table = pd.DataFrame(rows, columns=['Prefix', 'IP', 'CIDR', 'ROA_Status', 'Name', 'Description', 'Country', 'Parent Prefix', 'Parent IP', 'Parent CIDR', 'Parent RIR Name', 'Parent Allocation Status'])
    return table


def main():
    print(transform_input())

if __name__=='__main__':
    main()