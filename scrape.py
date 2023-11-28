# import requests

# cookies = {
#     'x-catalyst-session-global': '969d6d226cd2de6d15eb85bf13ec416666007bbf8dec66c3773b8962c1aa0106d74965417d8e0ca9',
#     'x-catalyst-timezone': 'Atlantic/Bermuda',
# }

# headers = {
#     'authority': 'www.registrarofcompanies.gov.bm',
#     'accept': 'text/html, */*; q=0.01',
#     'accept-language': 'en-US,en;q=0.9',
#     'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     # 'cookie': 'x-catalyst-session-global=969d6d226cd2de6d15eb85bf13ec416666007bbf8dec66c3773b8962c1aa0106d74965417d8e0ca9; x-catalyst-timezone=Atlantic/Bermuda',
#     'origin': 'https://www.registrarofcompanies.gov.bm',
#     'referer': 'https://www.registrarofcompanies.gov.bm/bmroc-capr/viewInstance/view.html?id=17ebe370d468cb92b4dfb57869146d98eba25b09afd2764d&_timestamp=7236376463078871',
#     'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
#     'x-catalyst-async': 'true',
#     'x-catalyst-secured': 'true',
#     'x-catalyst-session-global': '969d6d226cd2de6d15eb85bf13ec416666007bbf8dec66c3773b8962c1aa0106d74965417d8e0ca9',
#     'x-requested-with': 'XMLHttpRequest',
#     'x-security-token': 'null',
# }

# params = {
#     'id': '17ebe370d468cb92b4dfb57869146d98eba25b09afd2764d',
# }

# data = {
#     'nodeW656-EntityNameSearchOperator': 'Contains',
#     'Name': 'a',
#     'nodeW663-Advanced': 'N',
#     '_CBASYNCUPDATE_': 'true',
#     '_CBHTMLFRAGNODEID_': 'W650',
#     '_CBHTMLFRAGID_': '1699384411715',
#     '_CBHTMLFRAG_': 'true',
#     '_CBNODE_': 'W672',
#     '_VIKEY_': '9b528876x16a6x4372xb51bx7fee2c906a83',
#     '_CBNAME_': 'buttonPush',
# }

# response = requests.post(
#     'https://www.registrarofcompanies.gov.bm/bmroc-capr/viewInstance/update.html',
#     params=params,
#     cookies=cookies,
#     headers=headers,
#     data=data,
# )


# with open("data.html", "w") as f:
#     f.write(response.text)
# response=requests.get("http//example.com")
# soup=BeautifulSoup(response.content,'lxml')
# print(soup.text)








# tart_number=sys(int(argumnent[0]))>1:

# def skip_page():
#     for i in range (start_number-1):
#         try:
#             next_page=.....
#             next_page.click()
#         except:
#             breaks






import requests
import json
import traceback,sys,time, requests
import re


proxy_list_url = 'https://proxy.webshare.io/api/v2/proxy/list/download/dclobvygwpkwhkglwkfazlkbouwzulwdvcfabqpf/-/any/sourceip/direct/US/'


def crawl():
    response = requests.get(proxy_list_url)
    if response.status_code == 200:
        proxy_list = response.text.replace("\r","").split('\n')
        records = 0
        range_ = (99999999 - 10000)
        for proxy in proxy_list:
            if records >= range_:
                break
            proxy_url = f'http://{proxy}'
            print(proxy_url)
            for i in range(10000, 99999999):
                target_url = 'https://file.dos.pa.gov/api/Records/businesssearch'
                payload = json.dumps({
                    "SEARCH_VALUE": f"{i}",
                    "SEARCH_FILTER_TYPE_ID": "1",
                    "FILING_TYPE_ID": "",
                    "STATUS_ID": "",
                    "FILING_DATE": {
                        "start": None,
                        "end": None
                    }
                })

                headers = {
                    'Accept': '*/*',
                    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                    'Cache-Control': 'no-cache',
                    'Connection': 'keep-alive',
                    'Cookie': 'ASP.NET_SessionId=uciasrmzfsyl1kbkascl1tys',
                    'Origin': 'https://file.dos.pa.gov',
                    'Pragma': 'no-cache',
                    'Referer': 'https://file.dos.pa.gov/search/business',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
                    'authorization': 'undefined',
                    'content-type': 'application/json',
                    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"macOS"'
                }

                try:
                    response = requests.post(target_url,data=payload,headers=headers ,proxies={'http': proxy_url, 'https': proxy_url})
                    response.raise_for_status()  # Raise an error for HTTP status codes other than 200
                    records += 1
                    data =response.json()
                    rows = data['rows']
                    print(rows)
                    for key, value in rows.items():
                        addresses_detail = []
                        people_detail = []
                        fillings_detail = []   
                        title = value['TITLE'][0]
                        reg_num=value['TITLE'][0]
                        match = re.search(r'\((\d+)\)', reg_num)
                        if match:
                            registration_number = match.group(1)
                            
                        url=f"https://file.dos.pa.gov/api/FilingDetail/business/{key}/false"
                        
                        r=requests.get(url,proxies={'http': proxy_url, 'https': proxy_url}).json()
                        drawer_detail_list = r['DRAWER_DETAIL_LIST']
                        for item in drawer_detail_list:
                            if item['LABEL'] == "Initial Filing Date":
                                initial_filing_date = item['VALUE'].replace("/","-")

                            if item['LABEL'] == "Status":
                                status=item['VALUE']
                            
                            if item['LABEL'] == "Formed In":
                                formed_in=item['VALUE']

                            if item['LABEL'] == "Filing Type":
                                filing_type=item['VALUE']
                            
                            if item['LABEL'] == "Mailing Address":
                                mailing=item['VALUE']
                                addresses_detail.append({
                                    "type": "mailing_address",
                                    "address":mailing.replace("\n","").strip()
                                    })
                            
                            if item['LABEL'] == "Foreign Name":
                                foreign=item['VALUE']
                            else:
                                foreign=''

                            if item['LABEL'] == "Filing Subtype":
                                filing_sub_type=item['VALUE']
                            else:
                                filing_sub_type=''

                            if item['LABEL'] == "Principal Address":
                                principal_address=item['VALUE']
                                addresses_detail.append({
                                    "type": "general_address",
                                    "address":principal_address.replace("\n","").strip()
                                })

                            if item['LABEL'] == "Registered Office":
                                registered_office=item['VALUE']
                                addresses_detail.append({
                                    "type": "registered_address",
                                    "address":registered_office.replace("\n"," ").strip()
                                })
                            
                            if item['LABEL']=="Officers":
                                officer=item['VALUE']
                                officer_lines = officer.split('\n')

                                designation = officer_lines[0].strip()
                                name = officer_lines[1].strip()
                                address_lines = officer_lines[2:]
                                adjusted_address_lines = [line.replace('\n', '').replace(" ","").strip() for line in address_lines]

                                address = ' '.join(adjusted_address_lines)
                                people_detail.append({
                                    "designation":designation,
                                    "name":name,
                                    "address":address,

                                })
                            

                            if item['LABEL']=="General Partners":
                                general_patner=item['VALUE']
                                general_line=general_patner.split('\n')

                                general_designation=general_line[0].strip()
                                general_name=general_line[1].strip()


                                people_detail.append({
                                    "designation":general_designation,
                                    "name":general_name,
                                })
                        
                            
                            if item['LABEL']=="Interested Individuals":
                                interested_individual=item['VALUE']

                                interested_line=interested_individual.split('\n')

                                interested_designation=interested_line[0].strip()
                                interested_name=interested_line[1].strip()


                                people_detail.append({
                                    "designation":interested_designation,
                                    "name":interested_name,
                                })

                                
                            if item['LABEL']=="Interested Entities":
                                interested_entities=item['VALUE']

                                entities_line=interested_entities.split('\n')

                                entities_designation=entities_line[0].strip()
                                entities_name=entities_line[1].strip()
                                people_detail.append({
                                    "designation":entities_designation,
                                    "name":entities_name,
                                })

                        filling= r['CERT_BUTTON_REDIRECTS_TO'].replace("/forms/new/8322?type=business&sourceNum=","")
                        url=f"https://file.dos.pa.gov/api/History/business/{filling}"
                        if filling:
                            try:
                                r2=requests.get(url, proxies={'http': proxy_url, 'https': proxy_url}).json()

                                list_data= r2['AMENDMENT_LIST']
                                for data in list_data:
                                    if 'AMENDMENT_TYPE' in data:
                                        filling = data['AMENDMENT_TYPE']

                                    if 'AMENDMENT_NUM' in data:
                                        flling_code = data['AMENDMENT_NUM']

                                    if 'AMENDMENT_DATE' in data:
                                        date = data['AMENDMENT_DATE'].replace("/","-")
                                    if 'EFFECTIVE_DATE' in data:
                                        effective_after = data['EFFECTIVE_DATE'].replace("/","-")

                                    fillings_detail.append({
                                        "title":filling,
                                        "date":effective_after,
                                        "filing_type":filling,
                                        "filing_code":flling_code,
                                        "date":date,
                                        "meta_detail":{
                                            "effective_after":effective_after,
                                            "field":'',
                                            "changed_from":'',
                                            "changed_to":'',
                                        }   
                                    })

                                field_data = r2['HISTORY_LIST']
                                for idx, his_data in enumerate(field_data):
                                    if len(fillings_detail) > idx:
                                        if 'FIELD_NAME' in his_data:
                                            fillings_detail[idx]['meta_detail']['field'] = his_data['FIELD_NAME']
                                        if 'CHANGED_FROM' in his_data:
                                            fillings_detail[idx]['meta_detail']['changed_from'] = his_data['CHANGED_FROM']

                                        if 'CHANGED_TO' in his_data:
                                            fillings_detail[idx]['meta_detail']['changed_to'] = his_data['CHANGED_TO']
                            except:
                                pass
                            
                        OBJ={
                            "name":title,
                            "registration_number":registration_number,
                            "registration_date":initial_filing_date,
                            "status":status,
                            "foreign_name":foreign,
                            "jurisdiction":formed_in,
                            "type":filing_type,
                            "sub_type":filing_sub_type,
                            "addresses_detail":addresses_detail,
                            "people_detail":people_detail,
                            "fillings_detail":fillings_detail,
                        } 
                        print(OBJ)

                  
                    continue

                except:
                    print("Response is not in JSON format.")
                    break
crawl()