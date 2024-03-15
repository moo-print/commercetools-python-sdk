# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ..me.by_project_key_in_business_unit_key_by_business_unit_key_me_request_builder import (
    ByProjectKeyInBusinessUnitKeyByBusinessUnitKeyMeRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInBusinessUnitKeyByBusinessUnitKeyRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _business_unit_key: str

    def __init__(
        self,
        project_key: str,
        business_unit_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._business_unit_key = business_unit_key
        self._client = client

    def me(self) -> ByProjectKeyInBusinessUnitKeyByBusinessUnitKeyMeRequestBuilder:
        return ByProjectKeyInBusinessUnitKeyByBusinessUnitKeyMeRequestBuilder(
            project_key=self._project_key,
            business_unit_key=self._business_unit_key,
            client=self._client,
        )
