
# roles = {
#     'archive': True,
#     'body_email': True,
#     'preferred': ['BTC', 'IRR', 'IQD', 'USD', 'CAD', 'AED']
# }
EMAIL_SENDER = 'nima.abbasnejad14@gmail.com'
EMAIL_RECEIVER = 'nimaabbasnejad58@gmail.com'


roles = {
    'archive': True,
    'body_email': {
        'receiver': 'nimaabbasnejad58@gmail.com',
        'enable': True,
        'preferred': ['BTC', 'IRR', 'IQD', 'USD', 'CAD', 'AED']
    },
    'notification': {
        'enable': True,
        'receiver': '09360377091',
        'preferred': {
            'BTC': {'min': 4.453927e-05, 'max': 4.7449858e-05},
            'IRR': {'min': 45023.676998, 'max': 44023.676998}
        }
    }

}
