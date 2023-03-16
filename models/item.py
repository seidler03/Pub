from redis_om import HashModel

class Item(HashModel):
    Nome: str
    Url: str
    Key: str
    Priority: str
