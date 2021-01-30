# Generated file, please do not change!!!
import typing
import warnings

from ...models.importrequests import ImportResponse, ProductVariantPatchRequest
from ..import_operations.by_project_key_product_variant_patches_import_sink_key_by_import_sink_key_import_operations_request_builder import (
    ByProjectKeyProductVariantPatchesImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyProductVariantPatchesImportSinkKeyByImportSinkKeyRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _import_sink_key: str

    def __init__(
        self,
        project_key: str,
        import_sink_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._import_sink_key = import_sink_key
        self._client = client

    def import_operations(
        self,
    ) -> ByProjectKeyProductVariantPatchesImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder:
        return ByProjectKeyProductVariantPatchesImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder(
            project_key=self._project_key,
            import_sink_key=self._import_sink_key,
            client=self._client,
        )

    def post(
        self,
        body: "ProductVariantPatchRequest",
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "ImportResponse":
        """Creates a new import request for product variant patches"""
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/product-variant-patches/importSinkKey={self._import_sink_key}",
            params={},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code in (201, 200):
            return ImportResponse.deserialize(response.json())
        warnings.warn("Unhandled status code %d" % response.status_code)
