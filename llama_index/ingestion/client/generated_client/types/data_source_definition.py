# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from llama_index.ingestion.client.generated_client.core.datetime_utils import (
    serialize_datetime,
)

from .configurable_data_source_names import ConfigurableDataSourceNames


class DataSourceDefinition(pydantic.BaseModel):
    """
    Schema for a data source definition.
    """

    label: str = pydantic.Field(
        description="The label field will be used to display the name of the component in the UI"
    )
    json_schema: typing.Dict[str, typing.Any] = pydantic.Field(
        description="The json_schema field can be used by clients to determine how to construct the component"
    )
    source_type: ConfigurableDataSourceNames = pydantic.Field(
        description="The name field will act as the unique identifier of DataSourceDefinition objects"
    )

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
