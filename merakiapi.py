import requests
import json

tzlist = ['Africa/Abidjan',
          'Africa/Accra',
          'Africa/Addis_Ababa',
          'Africa/Algiers',
          'Africa/Asmara',
          'Africa/Asmera',
          'Africa/Bamako',
          'Africa/Bangui',
          'Africa/Banjul',
          'Africa/Bissau',
          'Africa/Blantyre',
          'Africa/Brazzaville',
          'Africa/Bujumbura',
          'Africa/Cairo',
          'Africa/Casablanca',
          'Africa/Ceuta',
          'Africa/Conakry',
          'Africa/Dakar',
          'Africa/Dar_es_Salaam',
          'Africa/Djibouti',
          'Africa/Douala',
          'Africa/El_Aaiun',
          'Africa/Freetown',
          'Africa/Gaborone',
          'Africa/Harare',
          'Africa/Johannesburg',
          'Africa/Juba',
          'Africa/Kampala',
          'Africa/Khartoum',
          'Africa/Kigali',
          'Africa/Kinshasa',
          'Africa/Lagos',
          'Africa/Libreville',
          'Africa/Lome',
          'Africa/Luanda',
          'Africa/Lubumbashi',
          'Africa/Lusaka',
          'Africa/Malabo',
          'Africa/Maputo',
          'Africa/Maseru',
          'Africa/Mbabane',
          'Africa/Mogadishu',
          'Africa/Monrovia',
          'Africa/Nairobi',
          'Africa/Ndjamena',
          'Africa/Niamey',
          'Africa/Nouakchott',
          'Africa/Ouagadougou',
          'Africa/Porto-Novo',
          'Africa/Sao_Tome',
          'Africa/Timbuktu',
          'Africa/Tripoli',
          'Africa/Tunis',
          'Africa/Windhoek',
          'America/Adak',
          'America/Anchorage',
          'America/Anguilla',
          'America/Antigua',
          'America/Araguaina',
          'America/Argentina/Buenos_Aires',
          'America/Argentina/Catamarca',
          'America/Argentina/ComodRivadavia',
          'America/Argentina/Cordoba',
          'America/Argentina/Jujuy',
          'America/Argentina/La_Rioja',
          'America/Argentina/Mendoza',
          'America/Argentina/Rio_Gallegos',
          'America/Argentina/Salta',
          'America/Argentina/San_Juan',
          'America/Argentina/San_Luis',
          'America/Argentina/Tucuman',
          'America/Argentina/Ushuaia',
          'America/Aruba',
          'America/Asuncion',
          'America/Atikokan',
          'America/Atka',
          'America/Bahia',
          'America/Bahia_Banderas',
          'America/Barbados',
          'America/Belem',
          'America/Belize',
          'America/Blanc-Sablon',
          'America/Boa_Vista',
          'America/Bogota',
          'America/Boise',
          'America/Buenos_Aires',
          'America/Cambridge_Bay',
          'America/Campo_Grande',
          'America/Cancun',
          'America/Caracas',
          'America/Catamarca',
          'America/Cayenne',
          'America/Cayman',
          'America/Chicago',
          'America/Chihuahua',
          'America/Coral_Harbour',
          'America/Cordoba',
          'America/Costa_Rica',
          'America/Creston',
          'America/Cuiaba',
          'America/Curacao',
          'America/Danmarkshavn',
          'America/Dawson',
          'America/Dawson_Creek',
          'America/Denver',
          'America/Detroit',
          'America/Dominica',
          'America/Edmonton',
          'America/Eirunepe',
          'America/El_Salvador',
          'America/Ensenada',
          'America/Fort_Nelson',
          'America/Fort_Wayne',
          'America/Fortaleza',
          'America/Glace_Bay',
          'America/Godthab',
          'America/Goose_Bay',
          'America/Grand_Turk',
          'America/Grenada',
          'America/Guadeloupe',
          'America/Guatemala',
          'America/Guayaquil',
          'America/Guyana',
          'America/Halifax',
          'America/Havana',
          'America/Hermosillo',
          'America/Indiana/Indianapolis',
          'America/Indiana/Knox',
          'America/Indiana/Marengo',
          'America/Indiana/Petersburg',
          'America/Indiana/Tell_City',
          'America/Indiana/Vevay',
          'America/Indiana/Vincennes',
          'America/Indiana/Winamac',
          'America/Indianapolis',
          'America/Inuvik',
          'America/Iqaluit',
          'America/Jamaica',
          'America/Jujuy',
          'America/Juneau',
          'America/Kentucky/Louisville',
          'America/Kentucky/Monticello',
          'America/Knox_IN',
          'America/Kralendijk',
          'America/La_Paz',
          'America/Lima',
          'America/Los_Angeles',
          'America/Louisville',
          'America/Lower_Princes',
          'America/Maceio',
          'America/Managua',
          'America/Manaus',
          'America/Marigot',
          'America/Martinique',
          'America/Matamoros',
          'America/Mazatlan',
          'America/Mendoza',
          'America/Menominee',
          'America/Merida',
          'America/Metlakatla',
          'America/Mexico_City',
          'America/Miquelon',
          'America/Moncton',
          'America/Monterrey',
          'America/Montevideo',
          'America/Montreal',
          'America/Montserrat',
          'America/Nassau',
          'America/New_York',
          'America/Nipigon',
          'America/Nome',
          'America/Noronha',
          'America/North_Dakota/Beulah',
          'America/North_Dakota/Center',
          'America/North_Dakota/New_Salem',
          'America/Ojinaga',
          'America/Panama',
          'America/Pangnirtung',
          'America/Paramaribo',
          'America/Phoenix',
          'America/Port_of_Spain',
          'America/Port-au-Prince',
          'America/Porto_Acre',
          'America/Porto_Velho',
          'America/Puerto_Rico',
          'America/Rainy_River',
          'America/Rankin_Inlet',
          'America/Recife',
          'America/Regina',
          'America/Resolute',
          'America/Rio_Branco',
          'America/Rosario',
          'America/Santa_Isabel',
          'America/Santarem',
          'America/Santiago',
          'America/Santo_Domingo',
          'America/Sao_Paulo',
          'America/Scoresbysund',
          'America/Shiprock',
          'America/Sitka',
          'America/St_Barthelemy',
          'America/St_Johns',
          'America/St_Kitts',
          'America/St_Lucia',
          'America/St_Thomas',
          'America/St_Vincent',
          'America/Swift_Current',
          'America/Tegucigalpa',
          'America/Thule',
          'America/Thunder_Bay',
          'America/Tijuana',
          'America/Toronto',
          'America/Tortola',
          'America/Vancouver',
          'America/Virgin',
          'America/Whitehorse',
          'America/Winnipeg',
          'America/Yakutat',
          'America/Yellowknife',
          'Antarctica/Casey',
          'Antarctica/Davis',
          'Antarctica/DumontDUrville',
          'Antarctica/Macquarie',
          'Antarctica/Mawson',
          'Antarctica/McMurdo',
          'Antarctica/Palmer',
          'Antarctica/Rothera',
          'Antarctica/South_Pole',
          'Antarctica/Syowa',
          'Antarctica/Troll',
          'Antarctica/Vostok',
          'Arctic/Longyearbyen',
          'Asia/Aden',
          'Asia/Almaty',
          'Asia/Amman',
          'Asia/Anadyr',
          'Asia/Aqtau',
          'Asia/Aqtobe',
          'Asia/Ashgabat',
          'Asia/Ashkhabad',
          'Asia/Baghdad',
          'Asia/Bahrain',
          'Asia/Baku',
          'Asia/Bangkok',
          'Asia/Barnaul',
          'Asia/Beirut',
          'Asia/Bishkek',
          'Asia/Brunei',
          'Asia/Calcutta',
          'Asia/Chita',
          'Asia/Choibalsan',
          'Asia/Chongqing',
          'Asia/Chungking',
          'Asia/Colombo',
          'Asia/Dacca',
          'Asia/Damascus',
          'Asia/Dhaka',
          'Asia/Dili',
          'Asia/Dubai',
          'Asia/Dushanbe',
          'Asia/Gaza',
          'Asia/Harbin',
          'Asia/Hebron',
          'Asia/Ho_Chi_Minh',
          'Asia/Hong_Kong',
          'Asia/Hovd',
          'Asia/Irkutsk',
          'Asia/Istanbul',
          'Asia/Jakarta',
          'Asia/Jayapura',
          'Asia/Jerusalem',
          'Asia/Kabul',
          'Asia/Kamchatka',
          'Asia/Karachi',
          'Asia/Kashgar',
          'Asia/Kathmandu',
          'Asia/Katmandu',
          'Asia/Khandyga',
          'Asia/Kolkata',
          'Asia/Krasnoyarsk',
          'Asia/Kuala_Lumpur',
          'Asia/Kuching',
          'Asia/Kuwait',
          'Asia/Macao',
          'Asia/Macau',
          'Asia/Magadan',
          'Asia/Makassar',
          'Asia/Manila',
          'Asia/Muscat',
          'Asia/Nicosia',
          'Asia/Novokuznetsk',
          'Asia/Novosibirsk',
          'Asia/Omsk',
          'Asia/Oral',
          'Asia/Phnom_Penh',
          'Asia/Pontianak',
          'Asia/Pyongyang',
          'Asia/Qatar',
          'Asia/Qyzylorda',
          'Asia/Rangoon',
          'Asia/Riyadh',
          'Asia/Saigon',
          'Asia/Sakhalin',
          'Asia/Samarkand',
          'Asia/Seoul',
          'Asia/Shanghai',
          'Asia/Singapore',
          'Asia/Srednekolymsk',
          'Asia/Taipei',
          'Asia/Tashkent',
          'Asia/Tbilisi',
          'Asia/Tehran',
          'Asia/Tel_Aviv',
          'Asia/Thimbu',
          'Asia/Thimphu',
          'Asia/Tokyo',
          'Asia/Tomsk',
          'Asia/Ujung_Pandang',
          'Asia/Ulaanbaatar',
          'Asia/Ulan_Bator',
          'Asia/Urumqi',
          'Asia/Ust-Nera',
          'Asia/Vientiane',
          'Asia/Vladivostok',
          'Asia/Yakutsk',
          'Asia/Yekaterinburg',
          'Asia/Yerevan',
          'Atlantic/Azores',
          'Atlantic/Bermuda',
          'Atlantic/Canary',
          'Atlantic/Cape_Verde',
          'Atlantic/Faeroe',
          'Atlantic/Faroe',
          'Atlantic/Jan_Mayen',
          'Atlantic/Madeira',
          'Atlantic/Reykjavik',
          'Atlantic/South_Georgia',
          'Atlantic/St_Helena',
          'Atlantic/Stanley',
          'Australia/ACT',
          'Australia/Adelaide',
          'Australia/Brisbane',
          'Australia/Broken_Hill',
          'Australia/Canberra',
          'Australia/Currie',
          'Australia/Darwin',
          'Australia/Eucla',
          'Australia/Hobart',
          'Australia/LHI',
          'Australia/Lindeman',
          'Australia/Lord_Howe',
          'Australia/Melbourne',
          'Australia/North',
          'Australia/NSW',
          'Australia/Perth',
          'Australia/Queensland',
          'Australia/South',
          'Australia/Sydney',
          'Australia/Tasmania',
          'Australia/Victoria',
          'Australia/West',
          'Australia/Yancowinna',
          'Brazil/Acre',
          'Brazil/DeNoronha',
          'Brazil/East',
          'Brazil/West',
          'Canada/Atlantic',
          'Canada/Central',
          'Canada/Eastern',
          'Canada/East-Saskatchewan',
          'Canada/Mountain',
          'Canada/Newfoundland',
          'Canada/Pacific',
          'Canada/Saskatchewan',
          'Canada/Yukon',
          'CET',
          'Chile/Continental',
          'Chile/EasterIsland',
          'CST6CDT',
          'Cuba',
          'EET',
          'Egypt',
          'Eire',
          'EST',
          'EST5EDT',
          'Etc/GMT',
          'Etc/GMT+0',
          'Etc/GMT+1',
          'Etc/GMT+10',
          'Etc/GMT+11',
          'Etc/GMT+12',
          'Etc/GMT+2',
          'Etc/GMT+3',
          'Etc/GMT+4',
          'Etc/GMT+5',
          'Etc/GMT+6',
          'Etc/GMT+7',
          'Etc/GMT+8',
          'Etc/GMT+9',
          'Etc/GMT0',
          'Etc/GMT-0',
          'Etc/GMT-1',
          'Etc/GMT-10',
          'Etc/GMT-11',
          'Etc/GMT-12',
          'Etc/GMT-13',
          'Etc/GMT-14',
          'Etc/GMT-2',
          'Etc/GMT-3',
          'Etc/GMT-4',
          'Etc/GMT-5',
          'Etc/GMT-6',
          'Etc/GMT-7',
          'Etc/GMT-8',
          'Etc/GMT-9',
          'Etc/Greenwich',
          'Etc/UCT',
          'Etc/Universal',
          'Etc/UTC',
          'Etc/Zulu',
          'Europe/Amsterdam',
          'Europe/Andorra',
          'Europe/Astrakhan',
          'Europe/Athens',
          'Europe/Belfast',
          'Europe/Belgrade',
          'Europe/Berlin',
          'Europe/Bratislava',
          'Europe/Brussels',
          'Europe/Bucharest',
          'Europe/Budapest',
          'Europe/Busingen',
          'Europe/Chisinau',
          'Europe/Copenhagen',
          'Europe/Dublin',
          'Europe/Gibraltar',
          'Europe/Guernsey',
          'Europe/Helsinki',
          'Europe/Isle_of_Man',
          'Europe/Istanbul',
          'Europe/Jersey',
          'Europe/Kaliningrad',
          'Europe/Kiev',
          'Europe/Kirov',
          'Europe/Lisbon',
          'Europe/Ljubljana',
          'Europe/London',
          'Europe/Luxembourg',
          'Europe/Madrid',
          'Europe/Malta',
          'Europe/Mariehamn',
          'Europe/Minsk',
          'Europe/Monaco',
          'Europe/Moscow',
          'Europe/Nicosia',
          'Europe/Oslo',
          'Europe/Paris',
          'Europe/Podgorica',
          'Europe/Prague',
          'Europe/Riga',
          'Europe/Rome',
          'Europe/Samara',
          'Europe/San_Marino',
          'Europe/Sarajevo',
          'Europe/Simferopol',
          'Europe/Skopje',
          'Europe/Sofia',
          'Europe/Stockholm',
          'Europe/Tallinn',
          'Europe/Tirane',
          'Europe/Tiraspol',
          'Europe/Ulyanovsk',
          'Europe/Uzhgorod',
          'Europe/Vaduz',
          'Europe/Vatican',
          'Europe/Vienna',
          'Europe/Vilnius',
          'Europe/Volgograd',
          'Europe/Warsaw',
          'Europe/Zagreb',
          'Europe/Zaporozhye',
          'Europe/Zurich',
          'GB',
          'GB-Eire',
          'GMT',
          'GMT+0',
          'GMT0',
          'GMT-0',
          'Greenwich',
          'Hongkong',
          'HST',
          'Iceland',
          'Indian/Antananarivo',
          'Indian/Chagos',
          'Indian/Christmas',
          'Indian/Cocos',
          'Indian/Comoro',
          'Indian/Kerguelen',
          'Indian/Mahe',
          'Indian/Maldives',
          'Indian/Mauritius',
          'Indian/Mayotte',
          'Indian/Reunion',
          'Iran',
          'Israel',
          'Jamaica',
          'Japan',
          'Kwajalein',
          'Libya',
          'MET',
          'Mexico/BajaNorte',
          'Mexico/BajaSur',
          'Mexico/General',
          'MST',
          'MST7MDT',
          'Navajo',
          'NZ',
          'NZ-CHAT',
          'Pacific/Apia',
          'Pacific/Auckland',
          'Pacific/Bougainville',
          'Pacific/Chatham',
          'Pacific/Chuuk',
          'Pacific/Easter',
          'Pacific/Efate',
          'Pacific/Enderbury',
          'Pacific/Fakaofo',
          'Pacific/Fiji',
          'Pacific/Funafuti',
          'Pacific/Galapagos',
          'Pacific/Gambier',
          'Pacific/Guadalcanal',
          'Pacific/Guam',
          'Pacific/Honolulu',
          'Pacific/Johnston',
          'Pacific/Kiritimati',
          'Pacific/Kosrae',
          'Pacific/Kwajalein',
          'Pacific/Majuro',
          'Pacific/Marquesas',
          'Pacific/Midway',
          'Pacific/Nauru',
          'Pacific/Niue',
          'Pacific/Norfolk',
          'Pacific/Noumea',
          'Pacific/Pago_Pago',
          'Pacific/Palau',
          'Pacific/Pitcairn',
          'Pacific/Pohnpei',
          'Pacific/Ponape',
          'Pacific/Port_Moresby',
          'Pacific/Rarotonga',
          'Pacific/Saipan',
          'Pacific/Samoa',
          'Pacific/Tahiti',
          'Pacific/Tarawa',
          'Pacific/Tongatapu',
          'Pacific/Truk',
          'Pacific/Wake',
          'Pacific/Wallis',
          'Pacific/Yap',
          'Poland',
          'Portugal',
          'PRC',
          'PST8PDT',
          'ROC',
          'ROK',
          'Singapore',
          'Turkey',
          'UCT',
          'Universal',
          'US/Alaska',
          'US/Aleutian',
          'US/Arizona',
          'US/Central',
          'US/Eastern',
          'US/East-Indiana',
          'US/Hawaii',
          'US/Indiana-Starke',
          'US/Michigan',
          'US/Mountain',
          'US/Pacific',
          'US/Pacific-New',
          'US/Samoa',
          'UTC',
          'WET',
          'W-SU',
          'Zulu'
]

BASE_URL = 'https://dashboard.meraki.com/api/v0'

def setbaseurl(hostname):
    BASE_URL = 'https://{0}/api/v0'.format(str(hostname))
    return

def getorganizations(apikey):
    geturl = BASE_URL + '/organizations'
    headers = {
        'x-cisco-meraki-api-key': apikey,
        'Content-Type': 'application/json'
    }
    dashboard = requests.get(geturl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        return json.loads(dashboard.text)

def getclients(apikey,serial):
    geturl = BASE_URL + '/devices/{0}/clients?timespan=86400'.format(str(serial))
    headers = {
        'x-cisco-meraki-api-key': apikey,
        'Content-Type': 'application/json'
    }
    dashboard = requests.get(geturl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        return json.loads(dashboard.text)

def getorgdevices(apikey, organizationid):
    geturl = BASE_URL + '/organizations/{0}/inventory'.format(str(organizationid))
    headers = {
        'x-cisco-meraki-api-key': apikey,
        'Content-Type': 'application/json'
    }
    dashboard = requests.get(geturl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        return json.loads(dashboard.text)


def getnetworkdevices(apikey, networkid):
    geturl = BASE_URL + '/networks/{0}/devices'.format(str(networkid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.get(geturl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        return json.loads(dashboard.text)


def getorgadmins(apikey, organizationid):
    geturl = BASE_URL + '/organizations/{0}/admins'.format(str(organizationid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.get(geturl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        return json.loads(dashboard.text)


def getnetworklist(apikey, organizationid):
    geturl = BASE_URL + '/organizations/{0}/networks'.format(str(organizationid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.get(geturl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        return json.loads(dashboard.text)


def getlicensestate(apikey, organizationid):
    geturl = BASE_URL + '/organizations/{0}/licenseState'.format(str(organizationid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.get(geturl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        return json.loads(dashboard.text)


def getdevicedetail(apikey, networkid, serialnumber):
    geturl = BASE_URL + '/networks/{0}/devices/{1}'.format(str(networkid), str(serialnumber))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.get(geturl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        return json.loads(dashboard.text)


def getnetworkdetail(apikey, networkid):
    geturl = BASE_URL + '/networks/{0}'.format(str(networkid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.get(geturl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        return json.loads(dashboard.text)


def getconfigtemplates(apikey, organizationid):
    geturl = BASE_URL + '/organizations/{0}/configTemplates'.format(str(organizationid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.get(geturl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        return json.loads(dashboard.text)


def getsnmpsettings(apikey, organizationid):
    geturl = BASE_URL + '/organizations/{0}/snmp'.format(str(organizationid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.get(geturl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        return json.loads(dashboard.text)


def getvpnpeers(apikey, organizationid):
    geturl = BASE_URL + '/organizations/{0}/thirdPartyVPNPeers'.format(str(organizationid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.get(geturl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        return json.loads(dashboard.text)


def getsamlroles(apikey, organizationid):
    geturl = BASE_URL + '/organizations/{0}/samlRoles'.format(str(organizationid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.get(geturl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        return json.loads(dashboard.text)


def getswitchstacks(apikey, networkid):
    geturl = BASE_URL + '/networks/{0}/switchStacks'.format(str(networkid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.get(geturl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        return json.loads(dashboard.text)


def getswitchstackmembers(apikey, networkid, stackid):
    geturl = BASE_URL + '/networks/{0}/switchStacks/{1}'.format(str(networkid), str(stackid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.get(geturl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        return json.loads(dashboard.text)


def getvlans(apikey, networkid):
    geturl = BASE_URL + '/networks/{0}/vlans'.format(str(networkid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.get(geturl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if dashboard.status_code == 400:
        print('Network ID {0} does not contain a MX device'.format(str(networkid)))
        return None
    elif statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        return json.loads(dashboard.text)


def getvlandetail(apikey, networkid, vlanid):
    geturl = BASE_URL + '/networks/{0}/vlans/{1}'.format(str(networkid), str(vlanid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.get(geturl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if dashboard.status_code == 400:
        print('Network ID {0} does not contain a MX device'.format(str(networkid)))
        return None
    elif statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        return json.loads(dashboard.text)


def gettemplates(apikey, organizationid):
    geturl = BASE_URL + '/organizations/{0}/configTemplates'.format(str(organizationid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.get(geturl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if dashboard.status_code == 400:
        print('Organization ID {0} does not contain any defined templates'.format(str(organizationid)))
        return None
    elif statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        return json.loads(dashboard.text)


def bindtotemplate(apikey, networkid, templateid, autobind='false'):
    posturl = BASE_URL + '/networks/{0}/bind'.format(str(networkid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    putdata = {
        'configTemplateId': format(str(templateid)),
        'autobind': format(str(autobind))
    }
    dashboard = requests.post(posturl, data=json.dumps(putdata), headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    elif statuscode == '200':
        print('Network ID {0} bound to configuration template ID {1}'.format(str(networkid),str(templateid)))
        return None

def unbindfromtemplate(apikey, networkid):
    posturl = BASE_URL + '/networks/{0}/unbind'.format(str(networkid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.post(posturl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    elif statuscode=='200':
        print('Network ID {0} unbound from configuration template'.format(str(networkid)))
        return None


def deltemplate(apikey, organizationid, templateid):
    delurl = BASE_URL + '/organizations/{0}/configTemplates/{1}'.format(str(organizationid),
                                                                                                str(templateid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.delete(delurl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    # If HTTP 404 is specifically returned, inform that configuration template does not exist
    #

    statuscode = format(str(dashboard.status_code))

    if dashboard.status_code == 204:
        print('Deleted template {0} from Organization ID {1}'.format(str(templateid), str(organizationid)))
        return None
    elif dashboard.status_code == 404:
        print('Configuration Template ID {0} cannot be found, please confirm ID'.format(str(templateid)))
        return None
    elif statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        print('Deletion of Template ID {0} unsuccessful - HTTP Status Code: {1}'.format(str(templateid),
                                                                                        str(statuscode)))
        return None


def updatevlan(apikey, networkid, vlanid, vlanname, mxip, subnetip):
    puturl = BASE_URL + '/networks/{0}/vlans/{1}'.format(str(networkid), str(vlanid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    putdata = {
        'name': format(str(vlanname)),
        'applianceIp': format(str(mxip)),
        'subnet': format(str(subnetip))
    }
    putdata = json.dumps(putdata)
    dashboard = requests.put(puturl, data=putdata, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        print(statuscode)
        return json.loads(dashboard.text)


def addvlan(apikey, networkid, vlanid, vlanname, mxip, subnetip):
    posturl = BASE_URL + '/networks/{0}/vlans'.format(str(networkid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    postdata = {
        'id': format(str(vlanid)),
        'name': format(str(vlanname)),
        'applianceIp': format(str(mxip)),
        'subnet': format(str(subnetip))
    }
    postdata = json.dumps(postdata)
    dashboard = requests.post(posturl, data=postdata, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    # If HTTP 400 is specifically returned, inform that network is currently bound to a template
    #

    statuscode = format(str(dashboard.status_code))

    if dashboard.status_code == 201:
        print('Added VLAN {0} to MX'.format(str(vlanid)))
        return None
    elif dashboard.status_code == 400:
        print('Network is bound to a template - Unable to delete VLAN')
        return None
    elif statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        print(statuscode)
        return None


def delvlan(apikey, networkid, vlanid):
    delurl = BASE_URL + '/networks/{0}/vlans/{1}'.format(str(networkid), str(vlanid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.delete(delurl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    # If HTTP 400 is specifically returned, inform that network is currently bound to a template
    #

    statuscode = format(str(dashboard.status_code))

    if dashboard.status_code == 204:
        print('Deleted VLAN {0} from MX'.format(str(vlanid)))
        return None
    elif dashboard.status_code == 400:
        print('Network is bound to a template - Unable to delete VLAN')
        return None
    elif statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None


def addadmin(apikey, organizationid, email, name, orgaccess=None, tags=None, tagaccess=None, networks=None,
             netaccess=None):
    posturl = BASE_URL + '/organizations/{0}/admins'.format(str(organizationid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }

    posttags = []

    if orgaccess is None and tags is None and networks is None:
        print("Administrator accounts must be granted access to either the Organization, Networks, or Tags")
        return None

    if tags is not None and tagaccess is None:
        print("If tags are defined you must define matching access arguments.\nFor example, tags = ['tag1', 'tag2'], "
              "must have matching access arguments: tagaccess = 'full', 'read-only'")
        return None
    elif tagaccess is not None and tags is None:
        print("If tag access levels are defined you must define matching tag arguments\nFor example, tags = "
              "['tag1', 'tag2'] must have matching access arguments: tagaccess = 'full', 'read-only'")
        return None
    elif tagaccess is None and tags is None:
        pass
    elif len(tags) != len(tagaccess):
        print("The number of tags and access arguments must match.\n")
        print("For example, tags = ['tag1', 'tag2'] must have matching access arguments: tagaccess = "
              "['full', 'read-only']")
        return None
    elif tags is not None and tagaccess is not None:
        x = 0
        while x < len(tags):
            posttags.append({'tag': tags[x],'access': tagaccess[x]})
            x += 1
    else:
        pass

    postnets = []

    if networks is not None and netaccess is None:
        print("If networks are defined you must define matching access arguments\nFor example networks = "
              "['net1', 'net2'] must have matching access arguments: netaccess = 'full', 'read-only'")
        return None
    elif netaccess is not None and networks is None:
        print("If network access levels are defined you must define matching network arguments\nFor example, networks"
              " = ['net1', 'net2'] must have matching access arguments: netaccess = 'full', 'read-only'")
        return None
    elif netaccess is None and networks is None:
        pass
    elif len(networks) != len(netaccess):
        print("The number of networks and access arguments must match.\n")
        print("For example, networks = ['net1', 'net2'] must have matching access arguments: netaccess = "
              "['full', 'read-only']")
        return None
    elif networks is not None and netaccess is not None:
        x = 0
        while x < len(networks):
            postnets.append({'id': networks[x],'access': netaccess[x]})
            x += 1
    else:
        pass
    postdata = []
    if len(posttags) == 0 and len(postnets) == 0:
        postdata = {
            'orgAccess': orgaccess,
            'email': format(str(email)),
            'name': format(str(name))
        }

    elif len(posttags) > 0 and len(postnets) == 0:
        postdata = {
            'name': format(str(name)),
            'email': format(str(email)),
            'orgAccess': orgaccess,
            'tags': posttags
        }

    elif len(postnets) > 0 and len(posttags) == 0:
        postdata = {
            'name': format(str(name)),
            'email': format(str(email)),
            'orgAccess': orgaccess,
            'networks': postnets
        }

    elif len(postnets) > 0 and len(posttags) > 0:
        postdata = {
            'name': format(str(name)),
            'email': format(str(email)),
            'orgAccess': orgaccess,
            'tags': posttags,
            'networks': postnets
        }
    dashboard = requests.post(posturl, data=json.dumps(postdata), headers=headers)
    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    # If HTTP 400 is specifically returned, inform that network is currently bound to a template
    #

    statuscode = format(str(dashboard.status_code))

    if dashboard.status_code == 201:
        print('Added Administrator {0} to Organization ID {1}'.format(str(email), str(organizationid)))
        return None
    elif dashboard.status_code == 400:
        print('Unable to add administrator')
        return None
    elif statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        print(statuscode)
        return None


def deladmin(apikey, organizationid, adminid):
    delurl = BASE_URL + '/organizations/{0}/admins/{1}'.format(str(organizationid),
                                                                                       str(adminid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.delete(delurl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    # If HTTP 400 is specifically returned, inform that network is currently bound to a template
    #

    statuscode = format(str(dashboard.status_code))

    if dashboard.status_code == 204:
        print('Deleted Admin ID {0} from Organization ID {1}'.format(str(adminid), str(organizationid)))
        return None
    elif statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None


def getadmins(apikey, organizationid):
    geturl = BASE_URL + '/organizations/{0}/admins'.format(str(organizationid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.get(geturl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        return json.loads(dashboard.text)


def addnetwork(apikey, organizationID, name, type, tags, tz):
    posturl = BASE_URL + '/organizations/{0}/networks'.format(str(organizationID))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }

    validtz = False
    for zone in tzlist:
        if validtz is False and format(str(tz)) == zone:
            validtz = True
            break
        else:
            validtz = False

    if validtz is False:
        print('Please enter a valid tz value from https://en.wikipedia.org/wiki/List_of_tz_database_time_zones')
        return None

    postdata = {
        'name': format(str(name)),
        'type': format(str(type)),
        'tags': format(str(tags)),
        'timeZone': format(str(tz))
    }
    postdata = json.dumps(postdata)
    dashboard = requests.post(posturl, data=postdata, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    # If HTTP 400 is specifically returned, inform that network is currently bound to a template
    #

    statuscode = format(str(dashboard.status_code))

    if dashboard.status_code == 201:
        print('Added Network {0} to Organization'.format(str(name)))
        return json.loads(dashboard.text)
    elif dashboard.status_code == 400:
        print('A network with the name "{0}" already exists in the organization'.format(str(name)))
        return None
    elif statuscode[:1] == '4' or statuscode[:1] == '5':
        print('An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'
              .format(str(statuscode)))
        return None
    else:
        print('Unknown error - HTTP Status Code {0}'.format(str(statuscode)))
        return None


def delnetwork(apikey, networkid):
    delurl = BASE_URL + '/networks/{0}'.format(str(networkid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.delete(delurl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    # If HTTP 400 is specifically returned, inform that network is currently bound to a template
    #

    statuscode = format(str(dashboard.status_code))

    if dashboard.status_code == 204:
        print('Deleted Network ID {0} from Organization'.format(str(networkid)))
        return None
    elif dashboard.status_code == 404:
        print('Network ID {0} does not exist, please enter a valid network ID')
        return None
    elif statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None

def updateadmin(apikey, organizationid, adminid, email, name=None, orgaccess=None, tags=None, tagaccess=None, networks=None,
             netaccess=None):


    puturl = BASE_URL + '/organizations/{0}/admins/{1}'.format(str(organizationid),str(adminid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
        }

    puttags = []

    if orgaccess is None and tags is None and networks is None and name is None:
        print("Administrator account updates must include Organization, Networks, or Tags permission changes or an updated"
              " name attribute")
        return None

    if tags is not None and tagaccess is None:
        print("If tags are defined you must define matching access arguments.\nFor example, tags = ['tag1', 'tag2'], "
              "must have matching access arguments: tagaccess = 'full', 'read-only'")
        return None
    elif tagaccess is not None and tags is None:
        print("If tag access levels are defined you must define matching tag arguments\nFor example, tags = "
              "['tag1', 'tag2'] must have matching access arguments: tagaccess = 'full', 'read-only'")
        return None
    elif tagaccess is None and tags is None:
        pass
    elif len(tags) != len(tagaccess):
        print("The number of tags and access arguments must match.\n")
        print("For example, tags = ['tag1', 'tag2'] must have matching access arguments: tagaccess = "
              "['full', 'read-only']")
        return None
    elif tags is not None and tagaccess is not None:
        x = 0
        while x < len(tags):
            puttags.append({'tag': tags[x], 'access': tagaccess[x]})
            x += 1
    else:
        pass

    putnets = []

    if networks is not None and netaccess is None:
        print("If networks are defined you must define matching access arguments\nFor example networks = "
              "['net1', 'net2'] must have matching access arguments: netaccess = 'full', 'read-only'")
        return None
    elif netaccess is not None and networks is None:
        print("If network access levels are defined you must define matching network arguments\nFor example, networks"
              " = ['net1', 'net2'] must have matching access arguments: netaccess = 'full', 'read-only'")
        return None
    elif netaccess is None and networks is None:
        pass
    elif len(networks) != len(netaccess):
        print("The number of networks and access arguments must match.\n")
        print("For example, networks = ['net1', 'net2'] must have matching access arguments: netaccess = "
              "['full', 'read-only']")
        return None
    elif networks is not None and netaccess is not None:
        x = 0
        while x < len(networks):
            putnets.append({'id': networks[x], 'access': netaccess[x]})
            x += 1
    else:
        pass
    putdata = []
    if name is not None:
        if len(puttags) == 0 and len(putnets) == 0:
            putdata = {
                'orgAccess': orgaccess,
                'email': format(str(email)),
                'name': format(str(name))
            }

        elif len(puttags) > 0 and len(putnets) == 0:
            putdata = {
                'name': format(str(name)),
                'email': format(str(email)),
                'orgAccess': orgaccess,
                'tags': puttags
                }

        elif len(postnets) > 0 and len(puttags) == 0:
            putdata = {
                'name': format(str(name)),
                'email': format(str(email)),
                'orgAccess': orgaccess,
                'networks': putnets
                }

        elif len(putnets) > 0 and len(puttags) > 0:
            putdata = {
                'name': format(str(name)),
                'email': format(str(email)),
                'orgAccess': orgaccess,
                'tags': puttags,
                'networks': putnets
                }
    elif name is None:
        if len(puttags) > 0 and len(putnets) == 0:
            putdata = {
                'email': format(str(email)),
                'orgAccess': orgaccess,
                'tags': puttags
                }

        elif len(postnets) > 0 and len(puttags) == 0:
            putdata = {
                'email': format(str(email)),
                'orgAccess': orgaccess,
                'networks': putnets
                }

        elif len(putnets) > 0 and len(puttags) > 0:
            putdata = {
                'email': format(str(email)),
                'orgAccess': orgaccess,
                'tags': puttags,
                'networks': putnets
                }
    print(puturl,putdata)
    dashboard = requests.put(puturl, data=json.dumps(putdata), headers=headers)
#
# Check for HTTP 4XX/5XX response code.
# If 4XX/5XX response code, print error message with response code and return None from function
# If HTTP 400 is specifically returned, inform that network is currently bound to a template
#

    statuscode = format(str(dashboard.status_code))

    if dashboard.status_code == 200:
        print('Successfully modified Administrator {0} in Organization ID {1}'.format(str(email), str(organizationid)))
        return None
    elif dashboard.status_code == 400:
        print('Unable to modify Administrator')
        return None
    elif statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        print(statuscode)
        return None

