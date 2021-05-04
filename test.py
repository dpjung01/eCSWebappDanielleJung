def testString():
    print( "**** This is a test ****!")
    testString =  "**** This is a test ****!"
    return testString

def testList():
    #initialize to empty
    testString = ""

    thislist = ["apple", "banana", "cherry"]
    for x in thislist:
       print(x)
       testString = testString + "<td data-label='prefix'>" + x + "</td>"
    return testString


def fetch_asninfo(ipaddrstr):

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

    #for asnstr in asnlist:
    url_prefix = ('{}/{}/prefixes').format(BASE_URL_ASN, asnstr)
    r = requests.get(url_prefix)
    r.raise_for_status()
    if r.status_code == 200:
        if r.json()['status'] == 'ok':
            response_data = r.json()['data']
        error = True
    
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

    summary()    

def summary():
    summary = ''
    for i in response_data['ipv4_prefixes']:
        line = [i['prefix'],i['ip'],i['name'],i['description'],i['country_code']]
        line_str = ','.join(str(i) for i in line) + '\n'
        summary += line_str
    print(summary)

def print_output(data):
    print(data.summary)
