# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from llama_index.ingestion.client.generated_client.core.datetime_utils import (
    serialize_datetime,
)

from .llm_predictor import LlmPredictor
from .metadata_mode import MetadataMode


class KeywordExtractor(pydantic.BaseModel):
    """
    Keyword extractor. Node-level extractor. Extracts
    `excerpt_keywords` metadata field.

    Args:
        llm_predictor (Optional[LLMPredictor]): LLM predictor
        keywords (int): number of keywords to extract
    """

    is_text_node_only: typing.Optional[bool]
    show_progress: typing.Optional[bool] = pydantic.Field(
        description="Whether to show progress."
    )
    metadata_mode: typing.Optional[MetadataMode] = pydantic.Field(
        description="Metadata mode to use when reading nodes."
    )
    node_text_template: typing.Optional[str] = pydantic.Field(
        description="Template to represent how node text is mixed with metadata text."
    )
    disable_template_rewrite: typing.Optional[bool] = pydantic.Field(
        description="Disable the node template rewrite."
    )
    in_place: typing.Optional[bool] = pydantic.Field(
        description="Whether to process nodes in place."
    )
    llm_predictor: LlmPredictor = pydantic.Field(
        description="The LLMPredictor to use for generation."
    )
    keywords: typing.Optional[int] = pydantic.Field(
        description="The number of keywords to extract."
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
