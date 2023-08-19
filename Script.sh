#!/bin/bash

IP_HOST="192.168.56.107"
RESTCONF_USERNAME="cisco"
RESTCONF_PASSWORD="cisco123!"
DATA_FORMAT="application/yang-data+json"
LOOPBACK_INTERFACE="Loopback199"
LOOPBACK_IP="10.1.99.1"

api_url_put="https://${IP_HOST}/restconf/data/ietf-interfaces:interfaces/interface=${LOOPBACK_INTERFACE}"
api_url_get="https://${IP_HOST}/restconf/data/ietf-interfaces:interfaces"
headers="Accept: ${DATA_FORMAT}"
basicauth="-u ${RESTCONF_USERNAME}:${RESTCONF_PASSWORD}"
yangConfig=$(cat <<EOF
{
  "ietf-interfaces:interface": {
    "name": "${LOOPBACK_INTERFACE}",
    "description": "RESTCONF => ${LOOPBACK_INTERFACE}",
    "type": "iana-if-type:softwareLoopback",
    "enabled": true,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "${LOOPBACK_IP}",
          "netmask": "255.255.255.0"
        }
      ]
    }
  }
}
EOF
)

# Redirect output to check_restconf_api.txt
exec > check_restconf_api.txt

# Print today's date
date

# Print 'START REST API CALL'
echo "START REST API CALL"

# Print '=============' separator
echo "============="

# Print 'FIRST API CALL'
echo "FIRST API CALL"

# Print '=============' separator
echo "============="

# Make PUT request and print status code
curl -k -s -w "Status Code: %{http_code}\n" -X PUT -H "${headers}" -H "Content-Type: ${DATA_FORMAT}" ${basicauth} -d "${yangConfig}" "${api_url_put}"

# Print '=============' separator
echo "============="

# Print 'SECOND API CALL'
echo "SECOND API CALL"

# Print '=============' separator
echo "============="

# Make GET request and print status code and interfaces
curl -k -s -w "Status Code: %{http_code}\n" -X GET -H "${headers}" ${basicauth} "${api_url_get}"

# Print 'END REST API CALL'
echo "END REST API CALL"
# Bash
