import redis
def msg_handler():
    r = redis.client.StrictRedis(host='localhost', port=6379, db=0)
    sub = r.pubsub()
    sub.subscribe("my_pubsub_channel")
    while True:
        try:
            msg = sub.get_message()
            if msg:
                if msg['type'] == 'message':
                    print(msg["data"].decode('utf-8'))
        except Exception as Error:
            print(Error)

msg_handler()