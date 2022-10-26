# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.error import ErrorResponse
from ...models.shipping_method import ShippingMethodPagedQueryResponse

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyShippingMethodsMatchingCartRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _store_key: str

    def __init__(
        self,
        project_key: str,
        store_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._store_key = store_key
        self._client = client

    def get(
        self,
        *,
        cart_id: str,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["ShippingMethodPagedQueryResponse"]:
        """Retrieves all the ShippingMethods that can ship to the shipping address of the given Cart in a given Store.
        Each ShippingMethod contains exactly one ShippingRate with the flag `isMatching` set to `true`.
        This ShippingRate is used when the ShippingMethod is [added to the Cart](ctp:api:type:CartSetShippingMethodAction).

        """
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/shipping-methods/matching-cart",
            params={"cartId": cart_id, "expand": expand},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return ShippingMethodPagedQueryResponse.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            raise self._client._create_exception(None, response)
        warnings.warn("Unhandled status code %d" % response.status_code)
