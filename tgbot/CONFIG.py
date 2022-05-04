import random
import string
import uuid
vendors={'46.101.149.91:5000':['instagram','ok','twitter','facebook','tiktok','skype','youtube'],
         '185.43.7.27':['whatsapp','viber'],
         '185.43.7.27:9012':['viber','telegram','wechat'],
#        '185.43.7.27:9014':['whatsapp','viber']
        }

webhook='https://webhook.gcpud.net/api/connect-gcpud/upload/{}?token=1B39E74CDDEAB7CDBC5292FB4248C'

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return str(uuid.uuid4())
tokens=['1B39E74CDDEAB7CDBC5292FB4248C']