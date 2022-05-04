"""Bazaarvoice tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_bazaarvoice.streams import (
    AuthorsStream,
    QuestionsStream,
    ProductsStream,
    ProductStatisticsStream,
    ReviewsStream,
    ReviewsCommentsStream,
)
STREAM_TYPES = [
    AuthorsStream,
    QuestionsStream,
    ProductsStream,
    ProductStatisticsStream,
    ReviewsStream,
    ReviewsCommentsStream,
]



class TapBazaarvoice(Tap):
    """Bazaarvoice tap class."""
    name = "tap-bazaarvoice"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            description="The api key obtained from Bazaarvoice"
        ),
        th.Property(
            "environment",
            th.StringType,
            default="production",
            description="Environment to run in, must be one of staging/production"
        ),
        th.Property(
            "api_version",
            th.StringType,
            required=True,
            description="Version of the API to use, i.e. '5.4'"
        ),
        th.Property(
            "page_size",
            th.NumberType,
            default=10,
            description="Page size for pagination"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
