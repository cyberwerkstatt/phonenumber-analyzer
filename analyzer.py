from twilio.rest import Client
account_sid = 'your_sid'
auth_token = 'your_token'
client = Client(account_sid, auth_token)

try:
    with open("./testphone.txt") as number:
        for line in number:
            phone_number = client.lookups.phone_numbers(line).fetch(type='carrier')
            carrier = phone_number.carrier["name"]
            country = phone_number.country_code
            number = line
            print("Nummer:",number + " Anbieter:",carrier," Land:",country,"\n")
except KeyboardInterrupt and Exception:
    print("Aborting......")
    print("done!")
        