# Generated file, please do not change!!!
import typing
import warnings

from ...models.errors import ErrorResponse
from ...models.importoperations import ImportOperation

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyProductsImportSinkKeyByImportSinkKeyImportOperationsByIdRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _import_sink_key: str
    _id: str

    def __init__(
        self,
        project_key: str,
        import_sink_key: str,
        id: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._import_sink_key = import_sink_key
        self._id = id
        self._client = client

    def get(
        self,
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "ImportOperation":
        """Retrieves the import operation with the given id."""
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/products/importSinkKey={self._import_sink_key}/import-operations/{self._id}",
            params={},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return ImportOperation.deserialize(response.json())
        elif response.status_code in (404, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        warnings.warn("Unhandled status code %d" % response.status_code)
