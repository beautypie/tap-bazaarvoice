"""Stream type classes for tap-bazaarvoice."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_bazaarvoice.client import BazaarvoiceStream


class ReviewsStream(BazaarvoiceStream):

    name = "reviews"
    path = "/data/reviews.json?Stats=Reviews&Include=Comments,Products"
    primary_keys = ["Id"]
    replication_key = None  # TODO: Change to LastModificationTime

    schema = th.PropertiesList(
        th.Property("Id", th.StringType),
        th.Property("CID", th.StringType),
        th.Property("SourceClient", th.StringType),
        th.Property("LastModeratedTime", th.DateTimeType),
        th.Property("LastModificationTime", th.DateTimeType),
        th.Property("ProductId", th.StringType),
        th.Property("CampaignId", th.StringType),
        th.Property("ContextDataValuesOrder", th.ArrayType(th.StringType)),
        th.Property("AuthorId", th.StringType),
        th.Property("ContentLocale", th.StringType),
        th.Property("IsFeatured", th.BooleanType),
        th.Property("TotalInappropriateFeedbackCount", th.NumberType),
        th.Property("TotalClientResponseCount", th.NumberType),
        th.Property("TotalCommentCount", th.NumberType),
        th.Property("Rating", th.NumberType),
        th.Property("SecondaryRatingsOrder", th.ArrayType(th.StringType)),
        th.Property("IsRatingsOnly", th.BooleanType),
        th.Property("IsRecommended", th.BooleanType),
        th.Property("TotalFeedbackCount", th.NumberType),
        th.Property("TotalNegativeFeedbackCount", th.NumberType),
        th.Property("TotalPositiveFeedbackCount", th.NumberType),
        th.Property("ModerationStatus", th.StringType),
        th.Property("SubmissionId", th.StringType),
        th.Property("SubmissionTime", th.DateTimeType),
        th.Property("TagDimensionsOrder", th.ArrayType(th.StringType)),
        th.Property("ReviewText", th.StringType),
        th.Property("Title", th.StringType),
        th.Property("UserNickname", th.StringType),
        # TODO: How can we do this with generic JSON keys but same value structure
        # th.Property("ContextDataValues", th.ObjectType(
        #     th.Property("Age", th.ObjectType(
        #         th.Property("Id", th.StringType),
        #         th.Property("Value", th.StringType),
        #         th.Property("ValueLabel", th.StringType),
        #         th.Property("DimensionLabel", th.StringType),
        #     ))
        # )),
        th.Property("SecondaryRatings", th.ObjectType(
            th.Property("Value", th.ObjectType(
                th.Property("Id", th.StringType),
                th.Property("Value", th.NumberType),
                th.Property("MinLabel", th.StringType),
                th.Property("Label", th.StringType),
                th.Property("MaxLabel", th.StringType),
                th.Property("ValueLabel", th.StringType),
                th.Property("ValueRange", th.NumberType),
                th.Property("DisplayType", th.StringType),
            )),
            th.Property("Quality", th.ObjectType(
                th.Property("Id", th.StringType),
                th.Property("Value", th.NumberType),
                th.Property("MinLabel", th.StringType),
                th.Property("Label", th.StringType),
                th.Property("MaxLabel", th.StringType),
                th.Property("ValueLabel", th.StringType),
                th.Property("ValueRange", th.NumberType),
                th.Property("DisplayType", th.StringType),
            )),
            th.Property("TrueToDescription", th.ObjectType(
                th.Property("Id", th.StringType),
                th.Property("Value", th.NumberType),
                th.Property("MinLabel", th.StringType),
                th.Property("Label", th.StringType),
                th.Property("MaxLabel", th.StringType),
                th.Property("ValueLabel", th.StringType),
                th.Property("ValueRange", th.NumberType),
                th.Property("DisplayType", th.StringType),
            )),
        )),
        # th.Property("TagDimensions", th.ObjectType),
        th.Property("RatingRange", th.NumberType),
        # th.Property("Videos", th.ArrayType(th.StringType)),  # no data to verify type
        # th.Property("ClientResponses", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("IsSyndicated", th.BooleanType),
        th.Property("UserLocation", th.StringType),
        # th.Property("BadgesOrder", th.ArrayType(th.StringType)),  # no data to verify type
        # th.Property("Pros", th.StringType),  # no data to verify type
        # th.Property("CommentIds", th.ArrayType(th.NumberType)),  # no data to verify type
        # th.Property("Badges", th.ObjectType),
        # th.Property("AdditionalFieldsOrder", th.ArrayType),  # no data to verify type
        # th.Property("Cons", th.StringType),  # no data to verify type
        th.Property("Helpfulness", th.NumberType),
        # th.Property("ProductRecommendationIds", th.ArrayType(th.NumberType)),  # no data to verify type
        # th.Property("Photos", th.ArrayType(th.StringType)),  # no data to verify type
        # th.Property("AdditionalFields", th.ObjectType),  # no data to verify type
        # th.Property("InappropriateFeedbackList", th.ArrayType(th.StringType)),  # no data to verify type
    ).to_dict()
