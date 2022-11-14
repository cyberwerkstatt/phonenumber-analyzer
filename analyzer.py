from twilio.rest import Client
account_sid = 'your_sid'
auth_token = 'your auth_token'
client = Client(account_sid, auth_token)


with open("<your dierctory with txt-file") as number:
    for line in number:
        try:
            phone_number = client.lookups.phone_numbers(line.strip()).fetch(type='carrier')
            carrier = phone_number.carrier["name"]
            country = phone_number.country_code
            number = line
            print("Nummer:",number + " Anbieter:",carrier," Land:",country,"\n")
        except:
            continue
        
print("done")
        
