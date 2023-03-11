import json
from datetime import datetime
from fixer import get_rates
from config import roles
from localconfig import api_key
from mail import send_email
from khayyam import JalaliDatetime
from send_sms import send_sms_msg


def archive(timestamp, rates):
    # save as json file
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

    send_email(subject, body)


def send_notification(msg):
    # add time to sms msg
    now = JalaliDatetime(datetime.now()).strftime('%y-%b-%d %A  %H:%M')
    msg += now
    send_sms_msg(msg)


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
    req = get_rates(api_key)
    if roles['archive']:
        archive(req['timestamp'], req['rates'])
    if roles['body_email']['enable']:
        body_email(req['timestamp'], req['rates'])
    if roles['notification']['enable']:
        notification_msg = check_notify_roles(req['rates'])
        if notification_msg:
            send_notification(notification_msg)
