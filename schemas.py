def individual_data(todo):
    deleted = todo.get('is_deleted', False)
    deleted_at = todo.get('deleted_at')

    if deleted and deleted_at:
        deleted_at_str = deleted_at.strftime('%Y-%m-%d')
    else:
        deleted_at_str = None

    return {
        'id': str(todo['_id']),
        'ts': todo.get('ts'),
        'air_temperature': (todo.get('airTemperature') or {}).get('value'),
        'wind_speed': ((todo.get('wind') or {}).get('speed') or {}).get('rate'),
        'wind_direction': ((todo.get('wind') or {}).get('direction') or {}).get('angle'),
        'precipitation': (todo.get('precipitationEstimatedObservation') or {}).get('estimatedWaterDepth'),
        'sea_temperature': (todo.get('seaSurfaceTemperature') or{}).get('value'),
        'is_deleted': deleted,
        'deleted_at': deleted_at_str
    }
def all_data(todos):
    return[individual_data(todo) for todo in todos]
