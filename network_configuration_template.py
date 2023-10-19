import requests
import json

# STEP 1: CREATE NETWORK

url = "https://api.meraki.com/api/v1/organizations//networks"

payload = json.dumps({
  "name": "<string>",
  "productTypes": [
    "<string>",
    "<string>"
  ],
  "tags": [
    "<string>",
    "<string>"
  ],
  "timeZone": "<string>",
  "copyFromNetworkId": "<string>",
  "notes": "<string>"
})
headers = {
  'X-Cisco-Meraki-API-Key': '{{X-Cisco-Meraki-API-Key}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

# STEP 2: CLAIM DEVICES

url = "https://api.meraki.com/api/v1/organizations//claim"

payload = json.dumps({
  "orders": [
    "<string>",
    "<string>"
  ],
  "serials": [
    "<string>",
    "<string>"
  ],
  "licenses": [
    {
      "key": "<string>",
      "mode": "<string>"
    },
    {
      "key": "<string>",
      "mode": "<string>"
    }
  ]
})
headers = {
  'X-Cisco-Meraki-API-Key': '{{X-Cisco-Meraki-API-Key}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

# STEP 3: CREATE VLANS ON MX

url = "https://api.meraki.com/api/v1/networks//appliance/vlans"

payload = json.dumps({
  "id": "<string>",
  "name": "<string>",
  "subnet": "<string>",
  "applianceIp": "<string>",
  "groupPolicyId": "<string>"
})
headers = {
  'X-Cisco-Meraki-API-Key': '{{X-Cisco-Meraki-API-Key}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

# STEP 4: CONFIGURE SWITCH PORTS

url = "https://api.meraki.com/api/v1/devices//switch/ports/"

payload = json.dumps({
  "name": "<string>",
  "tags": [
    "<string>",
    "<string>"
  ],
  "enabled": "<boolean>",
  "type": "<string>",
  "vlan": "<integer>",
  "voiceVlan": "<integer>",
  "allowedVlans": "<string>",
  "poeEnabled": "<boolean>",
  "isolationEnabled": "<boolean>",
  "rstpEnabled": "<boolean>",
  "stpGuard": "<string>",
  "linkNegotiation": "<string>",
  "portScheduleId": "<string>",
  "udld": "<string>",
  "accessPolicyType": "<string>",
  "accessPolicyNumber": "<integer>",
  "macAllowList": [
    "<string>",
    "<string>"
  ],
  "stickyMacAllowList": [
    "<string>",
    "<string>"
  ],
  "stickyMacAllowListLimit": "<integer>",
  "stormControlEnabled": "<boolean>",
  "flexibleStackingEnabled": "<boolean>"
})
headers = {
  'X-Cisco-Meraki-API-Key': '{{X-Cisco-Meraki-API-Key}}',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

# STEP 5: CREATE WIFI SSIDS

url = "https://api.meraki.com/api/v1/networks//wireless/ssids/"

payload = json.dumps({
  "name": "<string>",
  "enabled": "<boolean>",
  "authMode": "<string>",
  "enterpriseAdminAccess": "<string>",
  "encryptionMode": "<string>",
  "psk": "<string>",
  "wpaEncryptionMode": "<string>",
  "dot11w": {
    "enabled": "<boolean>",
    "required": "<boolean>"
  },
  "dot11r": {
    "enabled": "<boolean>",
    "adaptive": "<boolean>"
  },
  "splashPage": "<string>",
  "splashGuestSponsorDomains": [
    "<string>",
    "<string>"
  ],
  "oauth": {
    "allowedDomains": [
      "<string>",
      "<string>"
    ]
  },
  "localRadius": {
    "cacheTimeout": "<integer>",
    "passwordAuthentication": {
      "enabled": "<boolean>"
    },
    "certificateAuthentication": {
      "enabled": "<boolean>",
      "useLdap": "<boolean>",
      "useOcsp": "<boolean>",
      "ocspResponderUrl": "<string>",
      "clientRootCaCertificate": {
        "contents": "<string>"
      }
    }
  },
  "ldap": {
    "servers": [
      {
        "host": "<string>",
        "port": "<integer>"
      },
      {
        "host": "<string>",
        "port": "<integer>"
      }
    ],
    "credentials": {
      "distinguishedName": "<string>",
      "password": "<string>"
    },
    "baseDistinguishedName": "<string>",
    "serverCaCertificate": {
      "contents": "<string>"
    }
  },
  "activeDirectory": {
    "servers": [
      {
        "host": "<string>",
        "port": "<integer>"
      },
      {
        "host": "<string>",
        "port": "<integer>"
      }
    ],
    "credentials": {
      "logonName": "<string>",
      "password": "<string>"
    }
  },
  "radiusServers": [
    {
      "host": "<string>",
      "port": "<integer>",
      "secret": "<string>",
      "radsecEnabled": "<boolean>",
      "caCertificate": "<string>"
    },
    {
      "host": "<string>",
      "port": "<integer>",
      "secret": "<string>",
      "radsecEnabled": "<boolean>",
      "caCertificate": "<string>"
    }
  ],
  "radiusProxyEnabled": "<boolean>",
  "radiusTestingEnabled": "<boolean>",
  "radiusCalledStationId": "<string>",
  "radiusAuthenticationNasId": "<string>",
  "radiusServerTimeout": "<integer>",
  "radiusServerAttemptsLimit": "<integer>",
  "radiusFallbackEnabled": "<boolean>",
  "radiusCoaEnabled": "<boolean>",
  "radiusFailoverPolicy": "<string>",
  "radiusLoadBalancingPolicy": "<string>",
  "radiusAccountingEnabled": "<boolean>",
  "radiusAccountingServers": [
    {
      "host": "<string>",
      "port": "<integer>",
      "secret": "<string>",
      "radsecEnabled": "<boolean>",
      "caCertificate": "<string>"
    },
    {
      "host": "<string>",
      "port": "<integer>",
      "secret": "<string>",
      "radsecEnabled": "<boolean>",
      "caCertificate": "<string>"
    }
  ],
  "radiusAccountingInterimInterval": "<integer>",
  "radiusAttributeForGroupPolicies": "<string>",
  "ipAssignmentMode": "<string>",
  "useVlanTagging": "<boolean>",
  "concentratorNetworkId": "<string>",
  "vlanId": "<integer>",
  "defaultVlanId": "<integer>",
  "apTagsAndVlanIds": [
    {
      "tags": [
        "<string>",
        "<string>"
      ],
      "vlanId": "<integer>"
    },
    {
      "tags": [
        "<string>",
        "<string>"
      ],
      "vlanId": "<integer>"
    }
  ],
  "walledGardenEnabled": "<boolean>",
  "walledGardenRanges": [
    "<string>",
    "<string>"
  ],
  "radiusOverride": "<boolean>",
  "radiusGuestVlanEnabled": "<boolean>",
  "radiusGuestVlanId": "<integer>",
  "minBitrate": "<float>",
  "bandSelection": "<string>",
  "perClientBandwidthLimitUp": "<integer>",
  "perClientBandwidthLimitDown": "<integer>",
  "perSsidBandwidthLimitUp": "<integer>",
  "perSsidBandwidthLimitDown": "<integer>",
  "lanIsolationEnabled": "<boolean>",
  "visible": "<boolean>",
  "availableOnAllAps": "<boolean>",
  "availabilityTags": [
    "<string>",
    "<string>"
  ],
  "mandatoryDhcpEnabled": "<boolean>",
  "adultContentFilteringEnabled": "<boolean>",
  "dnsRewrite": {
    "enabled": "<boolean>",
    "dnsCustomNameservers": [
      "<string>",
      "<string>"
    ]
  }
})
headers = {
  'X-Cisco-Meraki-API-Key': '{{X-Cisco-Meraki-API-Key}}',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

