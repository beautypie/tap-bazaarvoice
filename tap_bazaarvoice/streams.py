"""Stream type classes for tap-bazaarvoice."""

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_bazaarvoice.client import BazaarvoiceStream


class ReviewsStream(BazaarvoiceStream):

    name = "reviews"
    path = "/data/reviews.json?Stats=Reviews,Questions,Answers&Include=Authors,Categories,Comments,Products"
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
        th.Property("ContextDataValues", th.ObjectType(
            th.Property("Id", th.StringType),
            th.Property("Value", th.StringType),
            th.Property("ValueLabel", th.StringType),
            th.Property("DimensionLabel", th.StringType),
        )),
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
        th.Property("TagDimensions", th.ObjectType(
            th.Property("Id", th.StringType),
            th.Property("Label", th.StringType),
            th.Property("Values", th.ArrayType(th.StringType)),
        )),
        th.Property("RatingRange", th.NumberType),
        th.Property("Videos", th.ArrayType(th.ObjectType(
            th.Property("Caption", th.StringType),
            th.Property("VideoId", th.StringType),
            th.Property("VideoIframeUrl", th.StringType),
            th.Property("VideoHost", th.StringType),
            th.Property("VideoThumbnailUrl", th.StringType),
            th.Property("VideoUrl", th.StringType),
        ))),
        th.Property("ClientResponses", th.ArrayType(th.ObjectType(
            th.Property("Department", th.StringType),
            th.Property("Response", th.StringType),
            th.Property("ResponseType", th.StringType),
            th.Property("ResponseSource", th.StringType),
            th.Property("Name", th.StringType),
            th.Property("Date", th.DateTimeType),
            th.Property("SourceClientName", th.StringType),
        ))),
        th.Property("IsSyndicated", th.BooleanType),
        th.Property("UserLocation", th.StringType),
        th.Property("BadgesOrder", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("Pros", th.StringType),  # no data to verify type
        th.Property("CommentIds", th.ArrayType(th.StringType)),
        th.Property("Badges", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("AdditionalFieldsOrder", th.ArrayType(th.NumberType)),  # no data to verify type
        th.Property("Cons", th.StringType),  # no data to verify type
        th.Property("Helpfulness", th.NumberType),
        th.Property("ProductRecommendationIds", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("Photos", th.ArrayType(th.ObjectType(
            th.Property('Id', th.StringType),
            th.Property('Caption', th.StringType),
            th.Property('Sizes', th.ObjectType(
                th.Property('normal', th.ObjectType(
                    th.Property('Id', th.StringType),
                    th.Property('Url', th.StringType),
                )),
                th.Property('thumbnail', th.ObjectType(
                    th.Property('Id', th.StringType),
                    th.Property('Url', th.StringType),
                )),
                th.Property('large', th.ObjectType(
                    th.Property('Id', th.StringType),
                    th.Property('Url', th.StringType),
                )),
            )),
            th.Property('SizesOrder', th.ArrayType(th.StringType)),
        ))),
        th.Property("AdditionalFields", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("InappropriateFeedbackList", th.ArrayType(th.ObjectType(
            th.Property('AuthorId', th.StringType),
            th.Property('SubmissionTime', th.DateTimeType),
        ))),
    ).to_dict()


class ReviewsCommentsStream(BazaarvoiceStream):

    name = "review_comments"
    path = "/data/reviewcomments.json?Include=Authors,Categories,Products,Reviews"
    primary_keys = ["Id"]
    replication_key = None  # TODO: Change to LastModificationTime

    schema = th.PropertiesList(
        th.Property("Id", th.StringType),
        th.Property("CID", th.StringType),
        th.Property("SourceClient", th.StringType),
        th.Property("LastModeratedTime", th.DateTimeType),
        th.Property("LastModificationTime", th.DateTimeType),
        th.Property("ReviewId", th.StringType),
        th.Property("AuthorId", th.StringType),
        th.Property("ContentLocale", th.StringType),
        th.Property("IsFeatured", th.BooleanType),
        th.Property("TotalInappropriateFeedbackCount", th.NumberType),
        th.Property("TotalFeedbackCount", th.NumberType),
        th.Property("TotalNegativeFeedbackCount", th.NumberType),
        th.Property("TotalPositiveFeedbackCount", th.NumberType),
        th.Property("ModerationStatus", th.StringType),
        th.Property("SubmissionTime", th.DateTimeType),
        th.Property("CommentText", th.StringType),
        th.Property("Title", th.StringType),
        th.Property("UserNickname", th.StringType),
        th.Property("Photos", th.ArrayType(th.ObjectType(
            th.Property('Id', th.StringType),
            th.Property('Caption', th.StringType),
            th.Property('Sizes', th.ObjectType(
                th.Property('normal', th.ObjectType(
                    th.Property('Id', th.StringType),
                    th.Property('Url', th.StringType),
                )),
                th.Property('thumbnail', th.ObjectType(
                    th.Property('Id', th.StringType),
                    th.Property('Url', th.StringType),
                )),
                th.Property('large', th.ObjectType(
                    th.Property('Id', th.StringType),
                    th.Property('Url', th.StringType),
                )),
            )),
            th.Property('SizesOrder', th.ArrayType(th.StringType)),
        ))),
        th.Property("StoryId", th.StringType),  # no data to verify type
        th.Property("ProductRecommendationIds", th.ArrayType(th.NumberType)),  # no data to verify type
        th.Property("UserLocation", th.StringType),
        th.Property("CampaignId", th.StringType),  # no data to verify type
        th.Property("InappropriateFeedbackList", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("SubmissionId", th.NumberType),  # no data to verify type
        th.Property("BadgesOrder", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("Badges", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("Videos", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("IsSyndicated", th.BooleanType),
    ).to_dict()


class QuestionsStream(BazaarvoiceStream):

    name = "questions"
    path = "/data/questions.json?Include=Authors,Categories,Products,Answers&Stats=Reviews,Questions,Answers"
    primary_keys = ["Id"]
    replication_key = None  # TODO: Change to LastModificationTime

    schema = th.PropertiesList(
        th.Property("Id", th.StringType),
        th.Property("CID", th.StringType),
        th.Property("SourceClient", th.StringType),
        th.Property("LastModeratedTime", th.DateTimeType),
        th.Property("LastModificationTime", th.DateTimeType),
        th.Property("CategoryId", th.StringType),
        th.Property("AuthorId", th.StringType),
        th.Property("UserLocation", th.StringType),
        th.Property("ContentLocale", th.StringType),
        th.Property("TotalInappropriateFeedbackCount", th.NumberType),
        th.Property("IsFeatured", th.BooleanType),
        th.Property("TotalAnswerCount", th.NumberType),
        th.Property("Photos", th.ArrayType(th.ObjectType(
            th.Property('Id', th.StringType),
            th.Property('Caption', th.StringType),
            th.Property('Sizes', th.ObjectType(
                th.Property('normal', th.ObjectType(
                    th.Property('Id', th.StringType),
                    th.Property('Url', th.StringType),
                )),
                th.Property('thumbnail', th.ObjectType(
                    th.Property('Id', th.StringType),
                    th.Property('Url', th.StringType),
                )),
                th.Property('large', th.ObjectType(
                    th.Property('Id', th.StringType),
                    th.Property('Url', th.StringType),
                )),
            )),
            th.Property('SizesOrder', th.ArrayType(th.StringType)),
        ))),
        th.Property("QuestionDetails", th.StringType),
        th.Property("QuestionSummary", th.StringType),
        th.Property("TotalFeedbackCount", th.NumberType),
        th.Property("TotalNegativeFeedbackCount", th.NumberType),
        th.Property("TotalPositiveFeedbackCount", th.NumberType),
        th.Property("ModerationStatus", th.StringType),
        th.Property("SubmissionTime", th.DateTimeType),
        th.Property("UserNickname", th.StringType),
        th.Property("ContextDataValues", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("ContextDataValuesOrder",  th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("AdditionalFieldsOrder",  th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("Badges", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("BadgesOrder", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("ProductRecommendationIds", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("Videos", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("SubmissionId", th.StringType),  # no data to verify type
        th.Property("CampaignId", th.StringType),  # no data to verify type
        th.Property("TagDimensionsOrder", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("TagDimensions", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("IsSyndicated", th.BooleanType),
        th.Property("InappropriateFeedbackList", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("AdditionalFields", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("ProductId", th.StringType),
        th.Property("AnswerIds", th.ArrayType(th.StringType)),
    ).to_dict()


class ProductsStream(BazaarvoiceStream):

    name = "products"
    path = "/data/products.json?Include=Authors,Categories,Products,Questions,Reviews&Stats=Reviews,Questions,Answers"
    primary_keys = ["Id"]
    replication_key = None  # TODO: Change to LastModificationTime

    schema = th.PropertiesList(
        th.Property("ImageUrl", th.StringType),
        th.Property("Name", th.StringType),
        th.Property("Id", th.StringType),
        th.Property("CategoryId", th.StringType),
        th.Property("BrandExternalId", th.StringType),
        th.Property("Brand", th.ObjectType(
            th.Property("Id", th.StringType),
            th.Property("Name", th.StringType),
        )),
        th.Property("Active", th.BooleanType),
        th.Property("ProductPageUrl", th.StringType),
        th.Property("Disabled", th.BooleanType),
        th.Property("StoryIds", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("ModelNumbers", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("ISBNs", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("FamilyIds", th.ArrayType(th.StringType)),
        th.Property("AttributesOrder", th.ArrayType(th.StringType)),
        th.Property("Description", th.StringType),
        th.Property("QuestionIds", th.ArrayType(th.StringType)),
        th.Property("ManufacturerPartNumbers", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("ReviewIds", th.ArrayType(th.StringType)),
        th.Property("EANs", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("UPCs", th.ArrayType(th.StringType)),  # no data to verify type
        th.Property("Attributes", th.ObjectType(
            th.Property("BV_WB_EXPAND", th.ObjectType(
                    th.Property("Id", th.StringType),
                    th.Property("Values", th.ArrayType(
                        th.ObjectType(
                            th.Property("Value", th.StringType),
                            th.Property("Locale", th.StringType),
                        )
                    )),
                ),
            ),
            th.Property("BV_WB_FAMILY", th.ObjectType(
                th.Property("Id", th.StringType),
                th.Property("Values", th.ArrayType(
                    th.ObjectType(
                        th.Property("Value", th.StringType),
                        th.Property("Locale", th.StringType),
                    )
                )),
                ),
            ),
            th.Property("INVALID_IMAGE_URL", th.ObjectType(
                th.Property("Id", th.StringType),
                th.Property("Values", th.ArrayType(
                    th.ObjectType(
                        th.Property("Value", th.StringType),
                        th.Property("Locale", th.StringType),
                    )
                )),
                ),
            ),
            th.Property("INVALID_PRODUCT_PAGE_URL", th.ObjectType(
                th.Property("Id", th.StringType),
                th.Property("Values", th.ArrayType(
                    th.ObjectType(
                        th.Property("Value", th.StringType),
                        th.Property("Locale", th.StringType),
                    )
                )),
                ),
            ),
        )),
        th.Property("ReviewStatistics", th.ObjectType(
            th.Property("RatingsOnlyReviewCount", th.NumberType),
            th.Property("FeaturedReviewCount", th.NumberType),
            th.Property("RecommendedCount", th.NumberType),
            th.Property("TotalReviewCount", th.NumberType),
            th.Property("NotRecommendedCount", th.NumberType),
            # th.Property("ContextDataDistribution", th.ObjectType(th.StringType)),
            th.Property("ContextDataDistributionOrder", th.ArrayType(th.StringType)),
            th.Property("SecondaryRatingsAveragesOrder", th.ArrayType(th.StringType)),
            # th.Property("TagDistribution", th.ObjectType(th.StringType)),
            th.Property("FirstSubmissionTime", th.DateTimeType),
            th.Property("HelpfulVoteCount", th.NumberType),
            th.Property("TagDistributionOrder", th.ArrayType(th.StringType)),
            th.Property("AverageOverallRating", th.NumberType),
            th.Property("RatingDistribution", th.ArrayType(th.StringType)),
            th.Property("LastSubmissionTime", th.DateTimeType),
            # th.Property("SecondaryRatingsAverages", th.ObjectType(th.StringType)),
            th.Property("OverallRatingRange", th.NumberType),
            th.Property("NotHelpfulVoteCount", th.NumberType),
        )),
        th.Property("TotalReviewCount", th.NumberType),
        th.Property("QAStatistics", th.ObjectType(
            th.Property("QuestionHelpfulVoteCount", th.NumberType),
            th.Property("FeaturedAnswerCount", th.NumberType),
            th.Property("TotalAnswerCount", th.NumberType),
            th.Property("FeaturedQuestionCount", th.NumberType),
            th.Property("QuestionNotHelpfulVoteCount", th.NumberType),
            th.Property("BestAnswerCount", th.NumberType),
            th.Property("AnswerHelpfulVoteCount", th.NumberType),
            th.Property("HelpfulVoteCount", th.NumberType),
            th.Property("AnswerNotHelpfulVoteCount", th.NumberType),
            th.Property("TotalQuestionCount", th.NumberType),
            th.Property("FirstAnswerTime", th.DateTimeType),
            th.Property("LastQuestionAnswerTime", th.DateTimeType),
            th.Property("FirstQuestionTime", th.DateTimeType),
            th.Property("LastAnswerTime", th.DateTimeType),
            th.Property("LastQuestionTime", th.DateTimeType),
            # th.Property("TagDistribution", th.ObjectType(th.StringType)),
            # th.Property("ContextDataDistribution", th.ObjectType(th.StringType)),
            th.Property("TagDistributionOrder", th.ArrayType(th.StringType)),
            th.Property("ContextDataDistributionOrder", th.ArrayType(th.StringType)),
        )),
        th.Property("TotalQuestionCount", th.NumberType),
        th.Property("TotalAnswerCount", th.NumberType),
    ).to_dict()

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "product_id": record["Id"]
        }


class ProductStatisticsStream(BazaarvoiceStream):

    name = "product_statistics"
    parent_stream_type = ProductsStream
    path = "/data/statistics.json?Stats=Reviews,NativeReviews&IncentivizedStats=True&Filter=ProductId:eq:{product_id}"
    primary_keys = ["ProductId"]
    replication_key = None
    ignore_parent_replication_keys = True
    records_jsonpath = "$[*]..ProductStatistics"

    schema = th.PropertiesList(
        th.Property("ProductId", th.StringType),
        th.Property("ReviewStatistics", th.ObjectType(
            th.Property("AverageOverallRating", th.NumberType),
            th.Property("IncentivizedReviewCount", th.NumberType),
            th.Property("OverallRatingRange", th.NumberType),
            th.Property("TotalReviewCount", th.NumberType),
        )),
        th.Property("NativeReviewStatistics", th.ObjectType(
            th.Property("AverageOverallRating", th.NumberType),
            th.Property("IncentivizedReviewCount", th.NumberType),
            th.Property("OverallRatingRange", th.NumberType),
            th.Property("TotalReviewCount", th.NumberType),
        )),
    ).to_dict()
