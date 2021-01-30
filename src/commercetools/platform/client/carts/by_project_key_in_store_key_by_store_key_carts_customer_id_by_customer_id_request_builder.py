# Generated file, please do not change!!!
import typing
import warnings

from ...models.cart import Cart
from ...models.error import ErrorResponse

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyCartsCustomerIdByCustomerIdRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _store_key: str
    _customer_id: str

    def __init__(
        self,
        project_key: str,
        store_key: str,
        customer_id: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._store_key = store_key
        self._customer_id = customer_id
        self._client = client

    def get(
        self,
        *,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Cart"]:
        """Retrieves the active cart of the customer that has been modified most recently in a specific Store.
        The {storeKey} path parameter maps to a Store's key.

        If the cart exists in the commercetools project but does not have the store field, or the store field
        references a different store, this method returns a ResourceNotFound error.

        The cart may not contain up-to-date prices, discounts etc. If you want to ensure they're up-to-date,
        send an Update request with the Recalculate update action instead.

        """
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/carts/customer-id={self._customer_id}",
            params={"expand": expand},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return Cart.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)
