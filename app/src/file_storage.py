import json
from typing import List, Dict
import aiofiles

class EventFileManager:
    FILE_PATH = "events.json"

    @classmethod
    async def read_events_from_file(cls) -> List[Dict]:
        """Reads events from a file asynchronously and returns them as a list of dictionaries."""
        try:
            async with aiofiles.open(cls.FILE_PATH, 'r', encoding='utf-8') as file:
                content = await file.read()
                return json.loads(content)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @classmethod
    async def write_events_to_file(cls, events: List[Dict]) -> None:
        """Writes a list of dictionaries as events to a file asynchronously."""
        async with aiofiles.open(cls.FILE_PATH, 'w', encoding='utf-8') as file:
            data = json.dumps(events, ensure_ascii=False, indent=4)
            await file.write(data)
