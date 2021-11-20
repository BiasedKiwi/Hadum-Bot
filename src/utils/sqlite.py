import asyncio
import aiosqlite
       
       
class SQLError(Exception):
    pass        


async def run(command: str = None, db: str = "../hadum.db"):
    if command is None:
        raise SQLError("No SQLite command specified")
    cursor = await aiosqlite.connect("../hadum.db")
    await cursor.execute(command)
    
    
def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()
        
if __name__ == "__main__":
    main()