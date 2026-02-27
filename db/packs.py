from db import get_Db

async def addPack(packname: str):
    db = get_Db()
    col = db.get_collection('packs')
    add = await col.insert_one({
        "name": packname, 
        "words": ["hello", "world", "swaga", "набор", "слов", "в", "массиве"] #нахуячил заглушку, потом тут будет принимать соо от юзера
    })
    print("Записал на пейджер (БД) " + packname, add.inserted_id)

    
async def getPackByName(packname: str):
    docName = None
    db = get_Db()
    col = db.get_collection('packs')
    document = await col.find_one({"name": packname})
    if document:
        docName = document.get("name")
    return docName
