# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.customer import CustomerSignInResult, MyCustomerSignin
from ...models.error import ErrorResponse

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyMeLoginRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def post(
        self,
        body: "MyCustomerSignin",
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["CustomerSignInResult"]:
        """Retrieves the authenticated customer (that matches the given email/password pair).

        If used with [an access token for an anonymous session](/../api/authorization#tokens-for-anonymous-sessions), all Orders and Carts that belong to the `anonymousId` are assigned to the newly logged-in Customer.

        - If the Customer does not have a Cart yet, the most recently modified anonymous cart becomes the Customer's Cart.
        - If the Customer already has a Cart, the most recently modified anonymous cart is handled in accordance with [AnonymousCartSignInMode](ctp:api:type:AnonymousCartSignInMode).

        A Cart returned as part of the [CustomerSignInResult](ctp:api:type:CustomerSignInResult) is [recalculated](ctp:api:type:Recalculate) with up-to-date prices, taxes, discounts, and invalid line items removed.

        If an account with the given credentials is not found, an [InvalidCredentials](ctp:api:type:InvalidCredentialsError) error is returned.

        """
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/me/login",
            params={},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code == 200:
            return CustomerSignInResult.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            raise self._client._create_exception(None, response)
        warnings.warn("Unhandled status code %d" % response.status_code)
