from flask import Flask,request,send_from_directory
app = Flask(__name__)

@app.route('/checkup', methods=['get'])
def c(messenger:str):
    print(request.args.get('link'))
    print(cfg.replace_sym(request.args.get('link')))
    res=cfg.get_messenger(messenger)['function'](cfg.replace_sym(request.args.get('link')))

    if res.get('first_name', 0) and res['first_name']:
        res['uid_exists']=True
    else:
        res['uid_exists']=False
    if res.get('image') and res['image']:
        image=res['image']
        if image.find('http')==-1 and image.find('i.mycdn.me')==-1:
            try:
                server='http://'+cfg.server
            except:

                server=cfg.get_ip()
            print(server)
            res['image']=f'{server}{image}'
    return res