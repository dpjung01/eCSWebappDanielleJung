# eCSWebappDanielleJung
## **Overview:**
  ##### This web app was created as the next steps in an application process for the position of Engineering Intern at _ezCybersecurity Systems_. Using FastAPI, the web app performs the following functions: 
  * accept input from a user
  * use FastAPI to retrieve information about IP address
  * display ASN prefixes, etc. for IP in a table




## Features
##### This web app accepts IPv4 or IPv6 addresses from a user and returns a table of the IP's information. This includes:
    - prefix
    - IP
    - CIDR
    - ROA_Status
    - Name
    - Description
    - Country
    - Parent Prefix
    - Parent IP
    - Parent CIDR
    - Parent RIR Name
    - Parent Allocation Status

Included in the interface is a "top" button, which when clicked brings the user to the top of the page. This was implemented because the data tables tend to run extremely long.

## Running the Project
 ##### (While creating this project, I used a virtual environment)
 There are pathways linking the three html files to the main.py file, so be sure to have all template files open when running the code. Be sure to run the requirements.txt file as well as it includes the major imports for the code. 
 

## Code Overview

#### main.py
<img width="955" alt="Screen Shot 2021-05-04 at 4 16 48 AM" src="https://user-images.githubusercontent.com/65555501/116983322-8e24a880-ac8f-11eb-8166-a5d8070d72a3.png"> this block of code is probably the most relevant in terms of functionality. This function runs as a background task to retrieve the information of the IP address using the APIs from the bgpy.com website provided. It converts the json str into a pandas dataframe, which puts it into a maleable form to display as a table. 

#### bgpview.py
<img width="530" alt="Screen Shot 2021-05-04 at 4 23 13 AM" src="https://user-images.githubusercontent.com/65555501/116984064-73066880-ac90-11eb-9979-02144a47239b.png"> This function is what main.py calls in the background. It uses the APIs from the bgpy.com site as provided. First, it takes the prefix(es) from the IP address. Because there may be multiple, the second block is a For loop that goes through the entire string and plugs it into the second API, which retrieves all ASN information. 


#### templates (html)

###### home.html and layout.html
<img width="604" alt="Screen Shot 2021-05-04 at 4 27 51 AM" src="https://user-images.githubusercontent.com/65555501/116984654-18b9d780-ac91-11eb-9930-217e28c209a6.png"> this is the code for the "top" button, which allows the user to return directly to the top of the page. Home.html is continued by layout.html and both files' content contain my simple display design for the webapp using frameworks from Semantic UI and html and minimal js. 


#### final product
<img width="1438" alt="Screen Shot 2021-05-04 at 4 32 48 AM" src="https://user-images.githubusercontent.com/65555501/116985219-c9c07200-ac91-11eb-876e-31de1484aab5.png"><img width="499" alt="Screen Shot 2021-05-04 at 4 33 15 AM" src="https://user-images.githubusercontent.com/65555501/116985264-d9d85180-ac91-11eb-9452-eb1cd4d9df04.png">
The final product should look like this. Any submitted IP will appear in the "Your IP" box to the right of the search bar, and a "top" button is included on the bottom right that is activated once the user begins to scroll. 


## bugs
1. url must be 127.0.0.1:8000/asn to be able to run. Without the /asn, the code will not work
2. IPv6 addresses did not seem to work when submitted because of a 503 Server Error, which has more to do on the other end than on mine. When running the get_asninfo function line by line through python, I found that data was still correctly gathered and returned. Because this also happens with certain IPv4 addresses, I assume it has something to do with either the API or being a privatized IP. (error: 503 Server Error: Service Temporarily Unavailable for url: https://api.bgpview.io/asn/7922/prefixes)
3. If a user submits a blank entry (hits 'search' without inputting an IP), a "{"detail":[{"loc":["body","ip"],"msg":"field required","type":"value_error.missing"}]}" error is given
