# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.error import ErrorResponse
from ...models.product import SuggestionResult

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyProductProjectionsSuggestRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def get(
        self,
        *,
        fuzzy: bool = None,
        staged: bool = None,
        search_keywords: typing.Dict[str, typing.List["str"]] = None,
        sort: typing.List["str"] = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["SuggestionResult"]:
        params = {
            "fuzzy": fuzzy,
            "staged": staged,
            "sort": sort,
            "limit": limit,
            "offset": offset,
            "withTotal": with_total,
        }
        search_keywords and params.update(
            {f"searchKeywords.{k}": v for k, v in search_keywords.items()}
        )
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/product-projections/suggest",
            params=params,
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return SuggestionResult.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            raise self._client._create_exception(None, response)
        warnings.warn("Unhandled status code %d" % response.status_code)
