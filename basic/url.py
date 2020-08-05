import urllib.parse
import json 
import os

def general_dict(find_value_1):

    dictionary = {"item1": "apple", "item2": "banana", "item3": "berry", "item4": "milk", "item5": "kiwi", "item6": "coffee", "item7": "jam"}
    with open('food.json', 'w') as json_file:
        json.dump(dictionary, json_file)
        print("JSON file saved on local to use")
    for key, value in dictionary.items(): 
        if food == find_value_1:
            print("User entered " + find_value_1, "it's stored in " + key)
            break
    else:
        print("Something went wrong")

def purge(url):
    URL= url
    sliced_url = URL.split()
    os.edited_URI="${URL##*.uk/}"
    SERVICE=`sudo docker service ps test_varnish |grep Running |cut -d " " -f1 $1`
    for SERVICE_ID in $SERVICE:
        IP=`docker inspect $SERVICE_ID |jq -re '.[].NetworksAttachments[1].Addresses[0]' |cut -d'/' -f1`
        echo "$IP"
        curl -v http://$IP:80/$edited_URI
    print("execute success")
    else:
        print("some issue")


# IP='10.0.0.4'
# parsed = urllib.parse.urlparse("http://varnish.qa.n.cit.corp.hmrc.gov.uk/artifactory/cds-playbooks/ansible-programme-vaults-cds")
# replaced = parsed._replace(netloc="http://$IP:80")
# print(replaced)