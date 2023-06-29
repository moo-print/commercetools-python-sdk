# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.common import ProjectContext

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class FrontasticContextRequestBuilder:
    _client: "BaseClient"

    def __init__(
        self,
        client: "BaseClient",
    ):
        self._client = client

    def get(
        self,
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "ProjectContext":
        """Returns information about the project locales setup and the environment in which the requested host acts in. \
        
        Headers&#58;
        
        - `Accept` - `application/json` - Required
        
        """
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/frontastic/context", params={}, headers=headers, options=options
        )
        if response.status_code == 200:
            return ProjectContext.deserialize(response.json())
        warnings.warn("Unhandled status code %d" % response.status_code)
