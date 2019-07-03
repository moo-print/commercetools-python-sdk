# DO NOT EDIT! This file is automatically generated

import marshmallow
import marshmallow_enum

from commercetools import helpers, types
from commercetools.schemas._common import (
    LoggedResourceSchema,
    PagedQueryResponseSchema,
    ReferenceSchema,
    ResourceIdentifierSchema,
)
from commercetools.schemas._type import FieldContainerField

__all__ = [
    "CustomerAddAddressActionSchema",
    "CustomerAddBillingAddressIdActionSchema",
    "CustomerAddShippingAddressIdActionSchema",
    "CustomerChangeAddressActionSchema",
    "CustomerChangeEmailActionSchema",
    "CustomerChangePasswordSchema",
    "CustomerCreateEmailTokenSchema",
    "CustomerCreatePasswordResetTokenSchema",
    "CustomerDraftSchema",
    "CustomerEmailVerifySchema",
    "CustomerPagedQueryResponseSchema",
    "CustomerReferenceSchema",
    "CustomerRemoveAddressActionSchema",
    "CustomerRemoveBillingAddressIdActionSchema",
    "CustomerRemoveShippingAddressIdActionSchema",
    "CustomerResetPasswordSchema",
    "CustomerResourceIdentifierSchema",
    "CustomerSchema",
    "CustomerSetCompanyNameActionSchema",
    "CustomerSetCustomFieldActionSchema",
    "CustomerSetCustomTypeActionSchema",
    "CustomerSetCustomerGroupActionSchema",
    "CustomerSetCustomerNumberActionSchema",
    "CustomerSetDateOfBirthActionSchema",
    "CustomerSetDefaultBillingAddressActionSchema",
    "CustomerSetDefaultShippingAddressActionSchema",
    "CustomerSetExternalIdActionSchema",
    "CustomerSetFirstNameActionSchema",
    "CustomerSetKeyActionSchema",
    "CustomerSetLastNameActionSchema",
    "CustomerSetLocaleActionSchema",
    "CustomerSetMiddleNameActionSchema",
    "CustomerSetSalutationActionSchema",
    "CustomerSetTitleActionSchema",
    "CustomerSetVatIdActionSchema",
    "CustomerSignInResultSchema",
    "CustomerSigninSchema",
    "CustomerTokenSchema",
    "CustomerUpdateActionSchema",
    "CustomerUpdateSchema",
]


class CustomerChangePasswordSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.CustomerChangePassword`."
    id = marshmallow.fields.String(allow_none=True)
    version = marshmallow.fields.Integer(allow_none=True)
    current_password = marshmallow.fields.String(
        allow_none=True, data_key="currentPassword"
    )
    new_password = marshmallow.fields.String(allow_none=True, data_key="newPassword")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.CustomerChangePassword(**data)


class CustomerCreateEmailTokenSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.CustomerCreateEmailToken`."
    id = marshmallow.fields.String(allow_none=True)
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    ttl_minutes = marshmallow.fields.Integer(allow_none=True, data_key="ttlMinutes")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.CustomerCreateEmailToken(**data)


class CustomerCreatePasswordResetTokenSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.CustomerCreatePasswordResetToken`."
    email = marshmallow.fields.String(allow_none=True)
    ttl_minutes = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="ttlMinutes"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.CustomerCreatePasswordResetToken(**data)


class CustomerDraftSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.CustomerDraft`."
    customer_number = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customerNumber"
    )
    email = marshmallow.fields.String(allow_none=True)
    password = marshmallow.fields.String(allow_none=True)
    first_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="firstName"
    )
    last_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lastName"
    )
    middle_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="middleName"
    )
    title = marshmallow.fields.String(allow_none=True, missing=None)
    anonymous_cart_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousCartId"
    )
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )
    date_of_birth = marshmallow.fields.Date(
        allow_none=True, missing=None, data_key="dateOfBirth"
    )
    company_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="companyName"
    )
    vat_id = marshmallow.fields.String(allow_none=True, missing=None, data_key="vatId")
    addresses = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.AddressSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
    )
    default_shipping_address = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="defaultShippingAddress"
    )
    shipping_addresses = marshmallow.fields.List(
        marshmallow.fields.Integer(allow_none=True),
        missing=None,
        data_key="shippingAddresses",
    )
    default_billing_address = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="defaultBillingAddress"
    )
    billing_addresses = marshmallow.fields.List(
        marshmallow.fields.Integer(allow_none=True),
        missing=None,
        data_key="billingAddresses",
    )
    is_email_verified = marshmallow.fields.Bool(
        allow_none=True, missing=None, data_key="isEmailVerified"
    )
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )
    customer_group = marshmallow.fields.Nested(
        nested="commercetools.schemas._customer_group.CustomerGroupResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="customerGroup",
    )
    custom = marshmallow.fields.Nested(
        nested="commercetools.schemas._type.CustomFieldsDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    locale = marshmallow.fields.String(allow_none=True, missing=None)
    salutation = marshmallow.fields.String(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.CustomerDraft(**data)


class CustomerEmailVerifySchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.CustomerEmailVerify`."
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    token_value = marshmallow.fields.String(allow_none=True, data_key="tokenValue")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.CustomerEmailVerify(**data)


class CustomerPagedQueryResponseSchema(PagedQueryResponseSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerPagedQueryResponse`."
    results = marshmallow.fields.Nested(
        nested="commercetools.schemas._customer.CustomerSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.CustomerPagedQueryResponse(**data)


class CustomerReferenceSchema(ReferenceSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerReference`."
    obj = marshmallow.fields.Nested(
        nested="commercetools.schemas._customer.CustomerSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type_id"]
        return types.CustomerReference(**data)


class CustomerResetPasswordSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.CustomerResetPassword`."
    token_value = marshmallow.fields.String(allow_none=True, data_key="tokenValue")
    new_password = marshmallow.fields.String(allow_none=True, data_key="newPassword")
    version = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.CustomerResetPassword(**data)


class CustomerResourceIdentifierSchema(ResourceIdentifierSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerResourceIdentifier`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type_id"]
        return types.CustomerResourceIdentifier(**data)


class CustomerSchema(LoggedResourceSchema):
    "Marshmallow schema for :class:`commercetools.types.Customer`."
    customer_number = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customerNumber"
    )
    email = marshmallow.fields.String(allow_none=True)
    password = marshmallow.fields.String(allow_none=True)
    first_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="firstName"
    )
    last_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lastName"
    )
    middle_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="middleName"
    )
    title = marshmallow.fields.String(allow_none=True, missing=None)
    date_of_birth = marshmallow.fields.Date(
        allow_none=True, missing=None, data_key="dateOfBirth"
    )
    company_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="companyName"
    )
    vat_id = marshmallow.fields.String(allow_none=True, missing=None, data_key="vatId")
    addresses = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.AddressSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )
    default_shipping_address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="defaultShippingAddressId"
    )
    shipping_address_ids = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        missing=None,
        data_key="shippingAddressIds",
    )
    default_billing_address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="defaultBillingAddressId"
    )
    billing_address_ids = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        missing=None,
        data_key="billingAddressIds",
    )
    is_email_verified = marshmallow.fields.Bool(
        allow_none=True, data_key="isEmailVerified"
    )
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )
    customer_group = marshmallow.fields.Nested(
        nested="commercetools.schemas._customer_group.CustomerGroupReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="customerGroup",
    )
    custom = marshmallow.fields.Nested(
        nested="commercetools.schemas._type.CustomFieldsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    locale = marshmallow.fields.String(allow_none=True, missing=None)
    salutation = marshmallow.fields.String(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.Customer(**data)


class CustomerSignInResultSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.CustomerSignInResult`."
    customer = marshmallow.fields.Nested(
        nested="commercetools.schemas._customer.CustomerSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    cart = marshmallow.fields.Dict(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.CustomerSignInResult(**data)


class CustomerSigninSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.CustomerSignin`."
    email = marshmallow.fields.String(allow_none=True)
    password = marshmallow.fields.String(allow_none=True)
    anonymous_cart_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousCartId"
    )
    anonymous_cart_sign_in_mode = marshmallow_enum.EnumField(
        types.AnonymousCartSignInMode,
        by_value=True,
        missing=None,
        data_key="anonymousCartSignInMode",
    )
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.CustomerSignin(**data)


class CustomerTokenSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.CustomerToken`."
    id = marshmallow.fields.String(allow_none=True)
    created_at = marshmallow.fields.DateTime(allow_none=True, data_key="createdAt")
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="lastModifiedAt"
    )
    customer_id = marshmallow.fields.String(allow_none=True, data_key="customerId")
    expires_at = marshmallow.fields.DateTime(allow_none=True, data_key="expiresAt")
    value = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.CustomerToken(**data)


class CustomerUpdateActionSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.CustomerUpdateAction`."
    action = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerUpdateAction(**data)


class CustomerUpdateSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.CustomerUpdate`."
    version = marshmallow.fields.Integer(allow_none=True)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addAddress": "commercetools.schemas._customer.CustomerAddAddressActionSchema",
                "addBillingAddressId": "commercetools.schemas._customer.CustomerAddBillingAddressIdActionSchema",
                "addShippingAddressId": "commercetools.schemas._customer.CustomerAddShippingAddressIdActionSchema",
                "changeAddress": "commercetools.schemas._customer.CustomerChangeAddressActionSchema",
                "changeEmail": "commercetools.schemas._customer.CustomerChangeEmailActionSchema",
                "removeAddress": "commercetools.schemas._customer.CustomerRemoveAddressActionSchema",
                "removeBillingAddressId": "commercetools.schemas._customer.CustomerRemoveBillingAddressIdActionSchema",
                "removeShippingAddressId": "commercetools.schemas._customer.CustomerRemoveShippingAddressIdActionSchema",
                "setCompanyName": "commercetools.schemas._customer.CustomerSetCompanyNameActionSchema",
                "setCustomField": "commercetools.schemas._customer.CustomerSetCustomFieldActionSchema",
                "setCustomType": "commercetools.schemas._customer.CustomerSetCustomTypeActionSchema",
                "setCustomerGroup": "commercetools.schemas._customer.CustomerSetCustomerGroupActionSchema",
                "setCustomerNumber": "commercetools.schemas._customer.CustomerSetCustomerNumberActionSchema",
                "setDateOfBirth": "commercetools.schemas._customer.CustomerSetDateOfBirthActionSchema",
                "setDefaultBillingAddress": "commercetools.schemas._customer.CustomerSetDefaultBillingAddressActionSchema",
                "setDefaultShippingAddress": "commercetools.schemas._customer.CustomerSetDefaultShippingAddressActionSchema",
                "setExternalId": "commercetools.schemas._customer.CustomerSetExternalIdActionSchema",
                "setFirstName": "commercetools.schemas._customer.CustomerSetFirstNameActionSchema",
                "setKey": "commercetools.schemas._customer.CustomerSetKeyActionSchema",
                "setLastName": "commercetools.schemas._customer.CustomerSetLastNameActionSchema",
                "setLocale": "commercetools.schemas._customer.CustomerSetLocaleActionSchema",
                "setMiddleName": "commercetools.schemas._customer.CustomerSetMiddleNameActionSchema",
                "setSalutation": "commercetools.schemas._customer.CustomerSetSalutationActionSchema",
                "setTitle": "commercetools.schemas._customer.CustomerSetTitleActionSchema",
                "setVatId": "commercetools.schemas._customer.CustomerSetVatIdActionSchema",
            },
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.CustomerUpdate(**data)


class CustomerAddAddressActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerAddAddressAction`."
    address = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.AddressSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerAddAddressAction(**data)


class CustomerAddBillingAddressIdActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerAddBillingAddressIdAction`."
    address_id = marshmallow.fields.String(allow_none=True, data_key="addressId")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerAddBillingAddressIdAction(**data)


class CustomerAddShippingAddressIdActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerAddShippingAddressIdAction`."
    address_id = marshmallow.fields.String(allow_none=True, data_key="addressId")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerAddShippingAddressIdAction(**data)


class CustomerChangeAddressActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerChangeAddressAction`."
    address_id = marshmallow.fields.String(allow_none=True, data_key="addressId")
    address = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.AddressSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerChangeAddressAction(**data)


class CustomerChangeEmailActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerChangeEmailAction`."
    email = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerChangeEmailAction(**data)


class CustomerRemoveAddressActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerRemoveAddressAction`."
    address_id = marshmallow.fields.String(allow_none=True, data_key="addressId")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerRemoveAddressAction(**data)


class CustomerRemoveBillingAddressIdActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerRemoveBillingAddressIdAction`."
    address_id = marshmallow.fields.String(allow_none=True, data_key="addressId")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerRemoveBillingAddressIdAction(**data)


class CustomerRemoveShippingAddressIdActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerRemoveShippingAddressIdAction`."
    address_id = marshmallow.fields.String(allow_none=True, data_key="addressId")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerRemoveShippingAddressIdAction(**data)


class CustomerSetCompanyNameActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerSetCompanyNameAction`."
    company_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="companyName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerSetCompanyNameAction(**data)


class CustomerSetCustomFieldActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerSetCustomFieldAction`."
    name = marshmallow.fields.String(allow_none=True)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerSetCustomFieldAction(**data)


class CustomerSetCustomTypeActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerSetCustomTypeAction`."
    type = marshmallow.fields.Nested(
        nested="commercetools.schemas._type.TypeResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    fields = FieldContainerField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerSetCustomTypeAction(**data)


class CustomerSetCustomerGroupActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerSetCustomerGroupAction`."
    customer_group = marshmallow.fields.Nested(
        nested="commercetools.schemas._customer_group.CustomerGroupResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="customerGroup",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerSetCustomerGroupAction(**data)


class CustomerSetCustomerNumberActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerSetCustomerNumberAction`."
    customer_number = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customerNumber"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerSetCustomerNumberAction(**data)


class CustomerSetDateOfBirthActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerSetDateOfBirthAction`."
    date_of_birth = marshmallow.fields.Date(
        allow_none=True, missing=None, data_key="dateOfBirth"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerSetDateOfBirthAction(**data)


class CustomerSetDefaultBillingAddressActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerSetDefaultBillingAddressAction`."
    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerSetDefaultBillingAddressAction(**data)


class CustomerSetDefaultShippingAddressActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerSetDefaultShippingAddressAction`."
    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerSetDefaultShippingAddressAction(**data)


class CustomerSetExternalIdActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerSetExternalIdAction`."
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerSetExternalIdAction(**data)


class CustomerSetFirstNameActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerSetFirstNameAction`."
    first_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="firstName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerSetFirstNameAction(**data)


class CustomerSetKeyActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerSetKeyAction`."
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerSetKeyAction(**data)


class CustomerSetLastNameActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerSetLastNameAction`."
    last_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lastName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerSetLastNameAction(**data)


class CustomerSetLocaleActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerSetLocaleAction`."
    locale = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerSetLocaleAction(**data)


class CustomerSetMiddleNameActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerSetMiddleNameAction`."
    middle_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="middleName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerSetMiddleNameAction(**data)


class CustomerSetSalutationActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerSetSalutationAction`."
    salutation = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerSetSalutationAction(**data)


class CustomerSetTitleActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerSetTitleAction`."
    title = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerSetTitleAction(**data)


class CustomerSetVatIdActionSchema(CustomerUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CustomerSetVatIdAction`."
    vat_id = marshmallow.fields.String(allow_none=True, missing=None, data_key="vatId")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CustomerSetVatIdAction(**data)
