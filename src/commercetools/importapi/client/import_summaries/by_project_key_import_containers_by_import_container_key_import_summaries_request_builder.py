# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.importsummaries import ImportSummary

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyImportContainersByImportContainerKeyImportSummariesRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _import_container_key: str

    def __init__(
        self,
        project_key: str,
        import_container_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._import_container_key = import_container_key
        self._client = client

    def get(
        self,
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "ImportSummary":
        """Retrieves an [ImportSummary](ctp:import:type:ImportSummary) for the given import container. An [ImportSummary](ctp:import:type:ImportSummary) is calculated on demand."""
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/import-containers/{self._import_container_key}/import-summaries",
            params={},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return ImportSummary.deserialize(response.json())
        warnings.warn("Unhandled status code %d" % response.status_code)