from jinja2 import pass_eval_context
import CONFIG
import checkup.db
import requests
import json
from tinydb import TinyDB, Query

db = TinyDB('data.json')

default_accs={'instagram':'real.rybk',
              'facebook':'giulio.violante.754',
              'twitter':'rybkinxd',
              'ok':'580291599995',
              'whatsapp':'87073373318',
              'telegram':'87073373318',
              'viber':'87073373318',
              'tiktok':'fcbarcelona',
              'youtube':'https://www.youtube.com/c/ivarlamov',
              'wechat':'+77078801908'}
class Checkup_system:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
    status_dict={}
    checkup_now=False
    def _check_server_status(self,server):
        #for media in __get_medias
        #   check all medias for server 
        #return result
        pass
    
    def _get_servers_medias(self):
        return CONFIG.vendors
    
    def _get_servers(self):
        return list(CONFIG.vendors.keys())
    
    def _get_server_status(self,server):
        pass
    
    def _check_media(self,server):
        pass
    
    def _get_medias(self):
        medias=[]
        for medias_array in CONFIG.vendors.values():
            medias+= medias_array
        return set(medias)
    
    def get_servers_info(self):
        data=db.all()
        
        return json.dumps(data[0], indent=2) if data else ''
    def check_servers_info(self):
        if self.checkup_now:
            return 'Уже идет проверка системы, ожидайте уведомления'
        db.truncate()
        self.checkup_now=True
        server_media_dict=self._get_servers_medias()
        return_dict={}
        for server in server_media_dict.keys():
            return_dict[server]={}
            print(server)
            for media in server_media_dict[server]:
                print(media)
                try:
                    request=(requests.get(f'http://{server}/get/{media}?link={default_accs[media]}'))
                    request_json=json.loads(request.text)
                    print(request_json)
                    if request.status_code>500:
                        raise Exception
                    return_dict[server][media] = 'Работает' if request_json['status'] == 'success' else 'Работает но не корректно'

                except Exception as e:
                    print(e)
                    return_dict[server][media]='Не работает вообще'
        self.status_dict=(return_dict)
        db.insert({'data':return_dict})
        return return_dict