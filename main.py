import requests
import json
from datetime import datetime
from kave import send_sms
from localconfig import headers
from config import url, roles
from mail import send_smtp_email
from khayyam import JalaliDatetime


# send a requests for get crypto price
def get_rates():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.text)


# save as json file
def archive(timestamp, rates):
    with open(f'archive/{timestamp}.json', 'w') as f:
        f.write(json.dumps(rates))


def body_email(timestamp, rates):
    subject = f'{timestamp} - {datetime.now} rates'
    if roles['body_email']['preferred'] is not None:
        tmp = dict()
        for exc in roles['body_email']['preferred']:
            tmp[exc] = rates[exc]
        rates = tmp

    body = json.dumps(rates)
    print(subject, ' | ', body)

    send_smtp_email(subject, body)


def send_notification(msg):
    # add time to sms msg
    now = JalaliDatetime(datetime.now()).strftime('%y-%b-%d %A  %H:%M')
    msg += now
    send_sms(msg)


def check_notify_roles(rates):
    """
    checked if user roles is true we send a sms for user
    :param rates:request response
    :return:msg
    """
    preferred = roles['notification']['preferred']
    msg = ''
    for exc in preferred.keys():
        if rates[exc] <= preferred[exc]['min']:
            msg += f'{exc} reached min {rates[exc]}'
        if rates[exc] >= preferred[exc]['max']:
            msg += f'{exc} reached max {rates[exc]}'
    return msg


if __name__ == '__main__':
    req = get_rates()
    if roles['archive']:
        archive(req['timestamp'], req['rates'])
    if roles['body_email']['enable']:
        body_email(req['timestamp'], req['rates'])
    if roles['notification']['enable']:
        notification_msg = check_notify_roles(req['rates'])
        if notification_msg:
            send_notification(notification_msg)
