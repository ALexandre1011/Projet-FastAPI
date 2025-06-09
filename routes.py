from fastapi import APIRouter, HTTPException, Depends, Query
from bson.objectid import ObjectId
from datetime import datetime
from configuration import collection
from schemas import all_data
from models import WeatherObservation
from auth import verify_jwt_token

router = APIRouter()

@router.get('/', dependencies=[Depends(verify_jwt_token)])
def get_all_weather_data(skip: int = Query(0, ge=0), limit: int = Query(10, le=100)):
    try:
        data = collection.find({'$or': [{'is_deleted': False}, {'is_deleted': {'$exists': False}}]}).skip(skip).limit(limit)
        return all_data(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {e}')

@router.post('/', dependencies=[Depends(verify_jwt_token)])
def create_weather_data(new_task: WeatherObservation):
    try:
        task_dict = new_task.model_dump()
        task_dict['is_deleted'] = False
        resp = collection.insert_one(task_dict)
        return {'status_code': 200, 'id': str(resp.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {e}')

@router.put('/{task_id}', dependencies=[Depends(verify_jwt_token)])
def update_weather_data(task_id: str, updated_task: WeatherObservation):
    try:
        oid = ObjectId(task_id)
        existing = collection.find_one({'_id': oid, 'is_deleted': False})
        if not existing:
            raise HTTPException(status_code=404, detail='Document not found')
        collection.update_one({'_id': oid}, {'$set': updated_task.model_dump()})
        return {'status_code': 200, 'message': 'Task updated successfully'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {e}')

@router.delete('/{task_id}', dependencies=[Depends(verify_jwt_token)])
def delete_weather_data(task_id: str):
    try:
        oid = ObjectId(task_id)
        existing = collection.find_one({'_id': oid, 'is_deleted': False})
        if not existing:
            raise HTTPException(status_code=404, detail='Document not found')
        collection.update_one({'_id': oid}, {'$set': {'is_deleted': True}})
        return {'status_code': 200, 'message': 'Task deleted successfully'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {e}')
    
@router.get('/deleted', dependencies=[Depends(verify_jwt_token)])
def get_deleted_data():
    try :
        deleted = list(collection.find({'is_deleted': True}))
        if not deleted:
            raise HTTPException(status_code=404, detail='Document not found')
        return all_data(deleted)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {e}')