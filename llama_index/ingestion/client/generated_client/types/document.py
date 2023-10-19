# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from llama_index.ingestion.client.generated_client.core.datetime_utils import (
    serialize_datetime,
)

from .document_relationships_value import DocumentRelationshipsValue


class Document(pydantic.BaseModel):
    """
    Generic interface for a data document.

    This document connects to data sources.
    """

    doc_id: typing.Optional[str] = pydantic.Field(description="Unique ID of the node.")
    embedding: typing.Optional[typing.List[float]] = pydantic.Field(
        description="Embedding of the node."
    )
    extra_info: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        description="A flat dictionary of metadata fields"
    )
    excluded_embed_metadata_keys: typing.Optional[typing.List[str]] = pydantic.Field(
        description="Metadata keys that are excluded from text for the embed model."
    )
    excluded_llm_metadata_keys: typing.Optional[typing.List[str]] = pydantic.Field(
        description="Metadata keys that are excluded from text for the LLM."
    )
    relationships: typing.Optional[
        typing.Dict[str, DocumentRelationshipsValue]
    ] = pydantic.Field(
        description="A mapping of relationships to other node information."
    )
    hash: typing.Optional[str] = pydantic.Field(description="Hash of the node content.")
    text: typing.Optional[str] = pydantic.Field(description="Text content of the node.")
    start_char_idx: typing.Optional[int] = pydantic.Field(
        description="Start char index of the node."
    )
    end_char_idx: typing.Optional[int] = pydantic.Field(
        description="End char index of the node."
    )
    text_template: typing.Optional[str] = pydantic.Field(
        description="Template for how text is formatted, with {content} and {metadata_str} placeholders."
    )
    metadata_template: typing.Optional[str] = pydantic.Field(
        description="Template for how metadata is formatted, with {key} and {value} placeholders."
    )
    metadata_seperator: typing.Optional[str] = pydantic.Field(
        description="Separator between metadata fields when converting to string."
    )
    class_name: typing.Optional[str]

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
