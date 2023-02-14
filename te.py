import json
import requests
url = "https://dunelmds.riversand.com/api/entityappservice/process"

payload = json.dumps({
  "entity": {
    "type": "stagingitem",
    "properties": {
      "source": "internal"
    },
    "data": {
      "attributes": {
        "thgattSFID": {
          "values": [
            {
              "value": "29112026",
              "source": "internal",
              "locale": "en-GB"
            }
          ]
        },
        "thgattPrpsdSrcOSup": {
          "values": [
            {
              "value": "1",
              "source": "internal",
              "locale": "en-GB"
            }
          ]
        },
        "thgattMerchCatIdFtrSAP": {
          "values": [
            {
              "value": "1",
              "source": "internal",
              "locale": "en-GB"
            }
          ]
        },
        "thgattArclCat": {
          "values": [
            {
              "value": "0",
              "source": "internal",
              "locale": "en-GB"
            }
          ]
        },
        "thgattSlsStTy": {
          "values": [
            {
              "value": "SA",
              "source": "internal",
              "locale": "en-GB"
            }
          ]
        },
        "thgattStatId": {
          "values": [
            {
              "value": "Continued",
              "source": "internal",
              "locale": "en-GB"
            }
          ]
        },
        "thgattVndrId": {
          "values": [
            {
              "id": "2_0_0_0",
              "value": "FIB01",
              "locale": "en-GB",
              "source": "internal"
            }
          ]
        }
      }
    }
  }
})
headers = {
  'Content-Type': 'application/json',
  'x-rdp-version': '8.1',
  'x-rdp-clientId': 'rdpclient',
  'x-rdp-tenantId': 'dunelmds',
  'x-rdp-userId': 'dunelmds@riversand.com',
  'x-rdp-userRoles': '["admin"]',
  'auth-client-id': 'tyuDOOEG1ynRNaZkBddJQ5Tvew2ZXnCP',
  'auth-client-secret': 'Izdd6m847ckpSZTM9aCHRm2lAx72nCIyOrcSNjhwyTS7W4l43k8iAABhOWsFCE0q'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
