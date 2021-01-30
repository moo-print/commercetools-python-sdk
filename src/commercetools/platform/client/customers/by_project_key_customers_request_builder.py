# Generated file, please do not change!!!
import typing
import warnings

from ...models.customer import (
    CustomerDraft,
    CustomerPagedQueryResponse,
    CustomerSignInResult,
)
from ...models.error import ErrorResponse
from ..confirm.by_project_key_customers_email_confirm_request_builder import (
    ByProjectKeyCustomersEmailConfirmRequestBuilder,
)
from ..email_token.by_project_key_customers_email_token_request_builder import (
    ByProjectKeyCustomersEmailTokenRequestBuilder,
)
from ..password.by_project_key_customers_password_request_builder import (
    ByProjectKeyCustomersPasswordRequestBuilder,
)
from ..password_token.by_project_key_customers_password_token_request_builder import (
    ByProjectKeyCustomersPasswordTokenRequestBuilder,
)
from ..reset.by_project_key_customers_password_reset_request_builder import (
    ByProjectKeyCustomersPasswordResetRequestBuilder,
)
from .by_project_key_customers_by_id_request_builder import (
    ByProjectKeyCustomersByIDRequestBuilder,
)
from .by_project_key_customers_email_token_by_email_token_request_builder import (
    ByProjectKeyCustomersEmailTokenByEmailTokenRequestBuilder,
)
from .by_project_key_customers_key_by_key_request_builder import (
    ByProjectKeyCustomersKeyByKeyRequestBuilder,
)
from .by_project_key_customers_password_token_by_password_token_request_builder import (
    ByProjectKeyCustomersPasswordTokenByPasswordTokenRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyCustomersRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_password_token(
        self, password_token: str
    ) -> ByProjectKeyCustomersPasswordTokenByPasswordTokenRequestBuilder:
        return ByProjectKeyCustomersPasswordTokenByPasswordTokenRequestBuilder(
            password_token=password_token,
            project_key=self._project_key,
            client=self._client,
        )

    def with_email_token(
        self, email_token: str
    ) -> ByProjectKeyCustomersEmailTokenByEmailTokenRequestBuilder:
        return ByProjectKeyCustomersEmailTokenByEmailTokenRequestBuilder(
            email_token=email_token,
            project_key=self._project_key,
            client=self._client,
        )

    def email_token(self) -> ByProjectKeyCustomersEmailTokenRequestBuilder:
        """To verify a customer's email, an email token can be created. This should be embedded in a link and sent to the
        customer via email. When the customer clicks on the link, the "verify customer's email" endpoint should be called,
        which sets customer's isVerifiedEmail field to true.

        """
        return ByProjectKeyCustomersEmailTokenRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def email_confirm(self) -> ByProjectKeyCustomersEmailConfirmRequestBuilder:
        return ByProjectKeyCustomersEmailConfirmRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def password(self) -> ByProjectKeyCustomersPasswordRequestBuilder:
        return ByProjectKeyCustomersPasswordRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def password_reset(self) -> ByProjectKeyCustomersPasswordResetRequestBuilder:
        return ByProjectKeyCustomersPasswordResetRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def password_token(self) -> ByProjectKeyCustomersPasswordTokenRequestBuilder:
        """The following workflow can be used to reset the customer's password:

        * Create a password reset token and send it embedded in a link to the customer.
        * When the customer clicks on the link, the customer is retrieved with the token.
        * The customer enters a new password and the "reset customer's password" endpoint is called.

        """
        return ByProjectKeyCustomersPasswordTokenRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def with_key(self, key: str) -> ByProjectKeyCustomersKeyByKeyRequestBuilder:
        return ByProjectKeyCustomersKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
            client=self._client,
        )

    def with_id(self, id: str) -> ByProjectKeyCustomersByIDRequestBuilder:
        return ByProjectKeyCustomersByIDRequestBuilder(
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
    ) -> typing.Optional["CustomerPagedQueryResponse"]:
        """Query customers"""
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
            endpoint=f"/{self._project_key}/customers",
            params=params,
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return CustomerPagedQueryResponse.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)

    def post(
        self,
        body: "CustomerDraft",
        *,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["CustomerSignInResult"]:
        """Creates a customer. If an anonymous cart is passed in,
        then the cart is assigned to the created customer and the version number of the Cart will increase.
        If the ID of an anonymous session is given, all carts and orders will be assigned to the created customer.

        """
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/customers",
            params={"expand": expand},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code in (201, 200):
            return CustomerSignInResult.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        elif response.status_code == 200:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)
