# Generated file, please do not change!!!
import typing
import warnings

from ...models.error import ErrorResponse
from ...models.shipping_method import (
    ShippingMethod,
    ShippingMethodDraft,
    ShippingMethodPagedQueryResponse,
)
from ..matching_cart.by_project_key_shipping_methods_matching_cart_request_builder import (
    ByProjectKeyShippingMethodsMatchingCartRequestBuilder,
)
from ..matching_location.by_project_key_shipping_methods_matching_location_request_builder import (
    ByProjectKeyShippingMethodsMatchingLocationRequestBuilder,
)
from ..matching_orderedit.by_project_key_shipping_methods_matching_orderedit_request_builder import (
    ByProjectKeyShippingMethodsMatchingOrdereditRequestBuilder,
)
from .by_project_key_shipping_methods_by_id_request_builder import (
    ByProjectKeyShippingMethodsByIDRequestBuilder,
)
from .by_project_key_shipping_methods_key_by_key_request_builder import (
    ByProjectKeyShippingMethodsKeyByKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyShippingMethodsRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_key(self, key: str) -> ByProjectKeyShippingMethodsKeyByKeyRequestBuilder:
        return ByProjectKeyShippingMethodsKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
            client=self._client,
        )

    def matching_cart(self) -> ByProjectKeyShippingMethodsMatchingCartRequestBuilder:
        """Get ShippingMethods for a cart"""
        return ByProjectKeyShippingMethodsMatchingCartRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def matching_orderedit(
        self,
    ) -> ByProjectKeyShippingMethodsMatchingOrdereditRequestBuilder:
        """Get ShippingMethods for an order edit"""
        return ByProjectKeyShippingMethodsMatchingOrdereditRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def matching_location(
        self,
    ) -> ByProjectKeyShippingMethodsMatchingLocationRequestBuilder:
        """Get ShippingMethods for a location"""
        return ByProjectKeyShippingMethodsMatchingLocationRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def with_id(self, id: str) -> ByProjectKeyShippingMethodsByIDRequestBuilder:
        return ByProjectKeyShippingMethodsByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
            client=self._client,
        )

    def get(
        self,
        *,
        expand: typing.List["str"] = None,
        sort: typing.List["str"] = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: typing.List["str"] = None,
        predicate_var: typing.Dict[str, typing.List["str"]] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["ShippingMethodPagedQueryResponse"]:
        """Query shipping-methods"""
        params = {
            "expand": expand,
            "sort": sort,
            "limit": limit,
            "offset": offset,
            "withTotal": with_total,
            "where": where,
        }
        predicate_var and params.update(
            {f"var.{k}": v for k, v in predicate_var.items()}
        )
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/shipping-methods",
            params=params,
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return ShippingMethodPagedQueryResponse.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)

    def post(
        self,
        body: "ShippingMethodDraft",
        *,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["ShippingMethod"]:
        """Create ShippingMethod"""
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/shipping-methods",
            params={"expand": expand},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code in (201, 200):
            return ShippingMethod.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        elif response.status_code == 200:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)
