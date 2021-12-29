"""REST client handling, including BazaarvoiceStream base class."""

import requests
from typing import Any, Dict, Optional, Iterable

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream
from singer_sdk.authenticators import APIKeyAuthenticator


class BazaarvoiceStream(RESTStream):
    """Bazaarvoice stream class."""

    @property
    def url_base(self) -> str:
        return 'https://stg.api.bazaarvoice.com' if self.config["environment"] == 'staging' else 'https://api.bazaarvoice.com'

    records_jsonpath = "$.Results[*]"

    @property
    def authenticator(self) -> APIKeyAuthenticator:
        """Return a new authenticator object."""
        return APIKeyAuthenticator.create_for_stream(
            self,
            key="passkey",
            value=self.config.get("api_key"),
            location="params"
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        return headers

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        if self.next_page_token_jsonpath:
            all_matches = extract_jsonpath(
                self.next_page_token_jsonpath, response.json()
            )
            first_match = next(iter(all_matches), None)
            next_page_token = first_match
        else:
            response_json = response.json()
            if response_json["TotalResults"] > response_json["Offset"] + self.config["page_size"]:
                next_page_token = {
                    "Offset": response_json["Offset"] + self.config["page_size"],
                    "Limit": self.config["page_size"]
                }
            else:
                next_page_token = None
        return next_page_token

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {
            "apiversion": self.config["api_version"],
            "Offset": 0,
            "Limit": self.config["page_size"]
        }
        if next_page_token:
            params["Offset"] = next_page_token["Offset"]
            params["Limit"] = next_page_token["Limit"]
        if self.replication_key:
            params["sort"] = "asc"
            params["order_by"] = self.replication_key
        return params

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())
