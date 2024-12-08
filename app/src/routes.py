# routes.py
from fastapi import APIRouter, HTTPException
from typing import List
from .models import Event
from .file_storage import EventFileManager
from .event_analyzer import EventAnalyzer

router = APIRouter()

@router.get("/events", response_model=List[Event])
async def get_all_events():
    events_data = await EventFileManager.read_events_from_file()
    return events_data

@router.get("/events/filter", response_model=List[Event])
async def get_events_by_filter(date: str = None, organizer: str = None, status: str = None, event_type: str = None):
    events_data = await EventFileManager.read_events_from_file()
    filtered_events = events_data
    if date:
        filtered_events = [event for event in filtered_events if event['date'] == date]
    if organizer:
        filtered_events = [event for event in filtered_events if event['organizer']['name'].lower() == organizer.lower()]
    if status:
        filtered_events = [event for event in filtered_events if event['status'].lower() == status.lower()]
    if event_type:
        filtered_events = [event for event in filtered_events if event['type'].lower() == event_type.lower()]

    return filtered_events

@router.get("/events/{event_id}", response_model=Event)
async def get_event_by_id(event_id: int):
    events_data = await EventFileManager.read_events_from_file()
    event = next((event for event in events_data if event['id'] == event_id), None)
    if event is not None:
        return event
    raise HTTPException(status_code=404, detail="Event not found")

@router.post("/events", response_model=Event)
async def create_event(event: Event):
    events_data = await EventFileManager.read_events_from_file()
    if any(e['id'] == event.id for e in events_data):
        raise HTTPException(status_code=400, detail="Event ID already exists")
    events_data.append(event.dict())
    await EventFileManager.write_events_to_file(events_data)
    return event

@router.put("/events/{event_id}", response_model=Event)
async def update_event(event_id: int, event_update: Event):
    events_data = await EventFileManager.read_events_from_file()
    event_index = next((i for i, event in enumerate(events_data) if event['id'] == event_id), None)
    
    if event_index is None:
        raise HTTPException(status_code=404, detail="Event not found")
    
    events_data[event_index] = event_update.dict()
    await EventFileManager.write_events_to_file(events_data)
    return events_data[event_index]

@router.delete("/events/{event_id}")
async def delete_event(event_id: int):
    events_data = await EventFileManager.read_events_from_file()
    event_index = next((i for i, event in enumerate(events_data) if event['id'] == event_id), None)
    
    if event_index is None:
        raise HTTPException(status_code=404, detail="Event not found")
    
    events_data.pop(event_index)
    await EventFileManager.write_events_to_file(events_data)
    return {"detail": "Event deleted successfully"}

@router.get("/events/joiners/multiple-meetings")
async def get_joiners_multiple_meetings():
    events_data = await EventFileManager.read_events_from_file()
    analyzer = EventAnalyzer()
    joiners = analyzer.get_joiners_multiple_meetings_method(events_data)
    
    if not joiners:
        return {"message": "No joiners attending at least 2 meetings"}
    return joiners
