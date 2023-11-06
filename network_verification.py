import requests
payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '{{X-Cisco-Meraki-API-Key}}'
}

# 1. Verify Network configuration

url = "https://api.meraki.com/api/v1/networks/"

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# 2. Verify Devices in Network
import requests

url = "https://api.meraki.com/api/v1/networks//devices"

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


# 3. Verify MX VLAN configuration
url = "https://api.meraki.com/api/v1/networks//appliance/vlans"

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# 4. Verify MS Port Configuration
url = "https://api.meraki.com/api/v1/devices//switch/ports"

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# 5. Verify MR SSID Configuration
url = "https://api.meraki.com/api/v1/networks//wireless/ssids"

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
