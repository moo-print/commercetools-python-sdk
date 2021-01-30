# Generated file, please do not change!!!
import typing
import warnings

from ...models.image_search import ImageSearchResponse
from ..config.by_project_key_image_search_config_request_builder import (
    ByProjectKeyImageSearchConfigRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyImageSearchRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def config(self) -> ByProjectKeyImageSearchConfigRequestBuilder:
        return ByProjectKeyImageSearchConfigRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def post(
        self,
        body: typing.BinaryIO,
        *,
        limit: int = None,
        offset: int = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "ImageSearchResponse":
        """Accepts an image file and returns similar products from product catalogue."""
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/image-search",
            params={"limit": limit, "offset": offset},
            data=body.read(),
            headers={"Content-Type": "multipart/form-data", **headers},
            options=options,
        )
        if response.status_code == 200:
            return ImageSearchResponse.deserialize(response.json())
        warnings.warn("Unhandled status code %d" % response.status_code)
