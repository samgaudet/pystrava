from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional

import gpxpy


@dataclass
class Activity:

    activity_id: Optional[int]
    activity_date: Optional[date]
    activity_name: Optional[str]
    activity_type: Optional[str]
    activity_description: Optional[str]
    elapsed_time: Optional[int]
    distance: Optional[float]
    relative_effort: Optional[int]
    commute: Optional[bool]
    activity_gear: Optional[str]
    filename: Optional[str]  # TODO: should this be pathlib.Path type?
    athlete_weight: Optional[float]
    bike_weight: Optional[float]
    _elapsed_time: Optional[int]  # duplicated in CSV source
    moving_time: Optional[int]
    distance: Optional[float]
    max_speed: Optional[float]
    average_speed: Optional[float]
    elevation_gain: Optional[float]
    elevation_loss: Optional[float]
    elevation_low: Optional[float]
    elevation_high: Optional[float]
    max_grade: Optional[float]
    average_grade: Optional[float]
    average_positive_grade: Optional[float]
    average_negative_grade: Optional[float]
    average_cadence: Optional[float]
    max_cadence: Optional[float]
    max_heart_rate: Optional[int]
    average_heart_rate: Optional[float]
    max_watts: Optional[int]  # TODO: double-check type
    average_watts: Optional[float]
    calories: Optional[float]
    max_temperature: Optional[int]
    average_temperature: Optional[float]
    _relative_effort: Optional[int]  # duplicated in CSV source
    total_work: Optional[int]  # TODO: double-check type
    number_of_runs: Optional[int]
    uphill_time: Optional[int]
    downhill_time: Optional[int]
    other_time: Optional[int]
    perceived_exertion: Optional[int]
    weighted_average_power: Optional[float]
    power_count: Optional[int]
    prefer_perceived_exertion: Optional[int]
    perceived_relative_effort: Optional[int]
    commute: Optional[bool]
    total_weight_lifted: Optional[int]
    from_upload: Optional[bool]
    grade_adjusted_distance: Optional[float]
    weather_observation_time: Optional[datetime]
    weather_condition: Optional[str]  # TODO: double-check type
    weather_temperature: Optional[int]  # TODO: double-check type
    apparent_temperature: Optional[int]  # TODO: double-check type
    dewpoint: Optional[int]  # TODO: double-check type
    humidity: Optional[float]  # TODO: double-check type
    weather_pressure: Optional[float]  # TODO: double-check type
    wind_speed: Optional[float]  # TODO: double-check type
    wind_gust: Optional[float]  # TODO: double-check type
    wind_bearing: Optional[float]  # TODO: double-check type
    precipitation_intensity: Optional[int]  # TODO: double-check type
    sunrise_time: Optional[datetime]  # TODO: double-check type
    sunset_time: Optional[datetime]  # TODO: double-check type
    moon_phase: Optional[str]  # TODO: double-check type
    bike: Optional[int]
    gear: Optional[int]
    precipitation_probability: Optional[float]  # TODO: double-check type
    precipitation_type: Optional[int]  # TODO: double-check type
    cloud_cover: Optional[int]  # TODO: double-check type
    weather_visibility: Optional[int]  # TODO: double-check type
    uv_index: Optional[int]  # TODO: double-check type
    weather_ozone: Optional[int]  # TODO: double-check type

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
