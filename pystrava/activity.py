from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional

import gpxpy


@dataclass
class Activity:

    activity_id: Optional[int] = None
    activity_date: Optional[date] = None
    activity_name: Optional[str] = None
    activity_type: Optional[str] = None
    activity_description: Optional[str] = None
    elapsed_time: Optional[int] = None
    distance: Optional[float] = None
    relative_effort: Optional[int] = None
    commute: Optional[bool] = None
    activity_gear: Optional[str] = None
    filename: Optional[str] = None  # TODO: should this be pathlib.Path type?
    athlete_weight: Optional[float] = None
    bike_weight: Optional[float] = None
    _elapsed_time: Optional[int] = None  # duplicated in CSV source
    moving_time: Optional[int] = None
    distance: Optional[float] = None
    max_speed: Optional[float] = None
    average_speed: Optional[float] = None
    elevation_gain: Optional[float] = None
    elevation_loss: Optional[float] = None
    elevation_low: Optional[float] = None
    elevation_high: Optional[float] = None
    max_grade: Optional[float] = None
    average_grade: Optional[float] = None
    average_positive_grade: Optional[float] = None
    average_negative_grade: Optional[float] = None
    average_cadence: Optional[float] = None
    max_cadence: Optional[float] = None
    max_heart_rate: Optional[int] = None
    average_heart_rate: Optional[float] = None
    max_watts: Optional[int] = None  # TODO: double-check type
    average_watts: Optional[float] = None
    calories: Optional[float] = None
    max_temperature: Optional[int] = None
    average_temperature: Optional[float] = None
    _relative_effort: Optional[int] = None  # duplicated in CSV source
    total_work: Optional[int] = None  # TODO: double-check type
    number_of_runs: Optional[int] = None
    uphill_time: Optional[int] = None
    downhill_time: Optional[int] = None
    other_time: Optional[int] = None
    perceived_exertion: Optional[int] = None
    weighted_average_power: Optional[float] = None
    power_count: Optional[int] = None
    prefer_perceived_exertion: Optional[int] = None
    perceived_relative_effort: Optional[int] = None
    commute: Optional[bool] = None
    total_weight_lifted: Optional[int] = None
    from_upload: Optional[bool] = None
    grade_adjusted_distance: Optional[float] = None
    weather_observation_time: Optional[datetime] = None
    weather_condition: Optional[str] = None  # TODO: double-check type
    weather_temperature: Optional[int] = None  # TODO: double-check type
    apparent_temperature: Optional[int] = None  # TODO: double-check type
    dewpoint: Optional[int] = None  # TODO: double-check type
    humidity: Optional[float] = None  # TODO: double-check type
    weather_pressure: Optional[float] = None  # TODO: double-check type
    wind_speed: Optional[float] = None  # TODO: double-check type
    wind_gust: Optional[float] = None  # TODO: double-check type
    wind_bearing: Optional[float] = None  # TODO: double-check type
    precipitation_intensity: Optional[int] = None  # TODO: double-check type
    sunrise_time: Optional[datetime] = None  # TODO: double-check type
    sunset_time: Optional[datetime] = None  # TODO: double-check type
    moon_phase: Optional[str] = None  # TODO: double-check type
    bike: Optional[int] = None
    gear: Optional[int] = None
    # TODO: double-check type
    precipitation_probability: Optional[float] = None
    precipitation_type: Optional[int] = None  # TODO: double-check type
    cloud_cover: Optional[int] = None  # TODO: double-check type
    weather_visibility: Optional[int] = None  # TODO: double-check type
    uv_index: Optional[int] = None  # TODO: double-check type
    weather_ozone: Optional[int] = None  # TODO: double-check type

    @property
    def gpx(self):

        gpx_file = open(self.filename, "r")
        gpx = gpxpy.parse(gpx_file)
        return gpx

    @property
    def gpx_duration(self):

        duration = self.gpx.get_duration()
        return duration

    @property
    def gpx_moving_data(self):

        moving_data = self.gpx.get_moving_data()
        return moving_data

    @property
    def gpx_uphill_downhill(self):

        uphill_downhill = self.gpx.get_uphill_downhill()
        return uphill_downhill

    @property
    def gpx_elevation(self):

        minimum_maximum = self.gpx.get_elevation_extremes()
        return minimum_maximum
