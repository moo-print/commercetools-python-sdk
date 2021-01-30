# Generated file, please do not change!!!
import typing
import warnings

from ...models.product import Product

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyProductsByIDImagesRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _id: str

    def __init__(
        self,
        project_key: str,
        id: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._id = id
        self._client = client

    def post(
        self,
        body: typing.BinaryIO,
        *,
        filename: str = None,
        variant: float = None,
        sku: str = None,
        staged: bool = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "Product":
        """Uploads a binary image file to a given product variant. The supported image formats are JPEG, PNG and GIF."""
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/products/{self._id}/images",
            params={
                "filename": filename,
                "variant": variant,
                "sku": sku,
                "staged": staged,
            },
            data=body.read(),
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return Product.deserialize(response.json())
        warnings.warn("Unhandled status code %d" % response.status_code)
