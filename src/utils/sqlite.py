import asyncio
import aiosqlite
from aiosqlite.core import Connection
       
       
class SQLError(Exception):
    pass    


async def connect(db: str = "../hadum.db", debug: bool = False):
    conn = await aiosqlite.connect(db)
    if debug:
        print(conn, type(conn))
    return conn
    
    
def main(debug: bool = True):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(connect(debug=debug))
    loop.close()
        
if __name__ == "__main__":
    main(True)