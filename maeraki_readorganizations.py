import merakiapi

#
# Sample Python Script Using Meraki API module to pull a list of organizations, Devices and Clients connected to a specific device
# Enter API Key and Organization ID into variables
# API Key can be generated in the modify user section in the dashboard

apikey = 'xxxxxxxx'
organizationid = 'xxxxxx'

# Setting the BASE_URL to your dashboard URL in case dashboard.meraki.com does not work
#merakiapi.BASE_URL = 'https://xxxx.meraki.com/api/v0'
merakiapi.setbaseurl('dashboard.meraki.com')

print merakiapi.getorganizations(apikey)
