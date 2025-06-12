from fastapi import APIRouter, Query
from models import WeatherObservation
import functions

router = APIRouter()

router.get("/")(functions.get_all_weather_data)
router.post("/")(functions.create_weather_data)
router.put("/{task_id}")(functions.update_weather_data)
router.delete("/{task_id}")(functions.delete_weather_data)
router.get("/deleted")(functions.get_deleted_data)
