from db.connectMongo import get_Collection

async def addPack(packname: str):
    col = await get_Collection()
    add = await col.insert_one({
        "name": packname, 
        "words": ["hello", "world", "swaga", "набор", "слов", "в", "массиве"] #нахуячил заглушку, потом тут будет принимать соо от юзера
    })
    print("Записал на пейджер (БД) " + packname, add.inserted_id)

    
async def getPackByName(packname: str):
    docName = None
    col = await get_Collection()
    document = await col.find_one({"name": packname})
    if document:
        docName = document.get("name")
    return docName
