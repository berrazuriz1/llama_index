# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from llama_index.ingestion.client.core.datetime_utils import serialize_datetime

from .etl_job_names import EtlJobNames
from .status_enum import StatusEnum


class ConfiguredTransformationExecution(pydantic.BaseModel):
    """
    Schema for a job that executes a transform step in a pipeline.
    """

    id: typing.Optional[str] = pydantic.Field(description="Unique identifier")
    created_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="Creation datetime"
    )
    updated_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="Update datetime"
    )
    job_name: EtlJobNames
    status: StatusEnum
    started_at: typing.Optional[dt.datetime]
    ended_at: typing.Optional[dt.datetime]
    partitions: typing.Optional[typing.Dict[str, str]] = pydantic.Field(
        description="Partition information"
    )
    pipeline_id: str
    configured_transformation_id: str

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
