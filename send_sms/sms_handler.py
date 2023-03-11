from kavenegar import KavenegarAPI, APIException, HTTPException

from config import roles
from localconfig import KAVEH_API_KEY


def send_sms_msg(text):
    try:
        api = KavenegarAPI(KAVEH_API_KEY)
        params = {
            'sender': '1004346',
            'receptor': roles['notification']['receiver'],
            # multiple mobile number, split by comma
            'message': text,
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
