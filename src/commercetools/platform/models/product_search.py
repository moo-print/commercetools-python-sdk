# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen

import datetime
import enum
import typing

from ._abstract import _BaseType
from .error import ErrorResponse
from .search import SearchFieldType, SearchSortOrder

if typing.TYPE_CHECKING:
    from .error import ErrorObject
    from .product import ProductProjection
    from .search import SearchFieldType, SearchQuery, SearchSorting, SearchSortOrder

__all__ = [
    "ProductPagedSearchResponse",
    "ProductSearchErrorResponse",
    "ProductSearchFacetCountExpression",
    "ProductSearchFacetCountLevelEnum",
    "ProductSearchFacetCountValue",
    "ProductSearchFacetDistinctBucketSortBy",
    "ProductSearchFacetDistinctBucketSortExpression",
    "ProductSearchFacetDistinctExpression",
    "ProductSearchFacetDistinctValue",
    "ProductSearchFacetExpression",
    "ProductSearchFacetRangesExpression",
    "ProductSearchFacetRangesFacetRange",
    "ProductSearchFacetRangesValue",
    "ProductSearchFacetResult",
    "ProductSearchFacetResultBucket",
    "ProductSearchFacetResultBucketEntry",
    "ProductSearchFacetResultCount",
    "ProductSearchFacetScope",
    "ProductSearchFacetScopeEnum",
    "ProductSearchMatchingVariantEntry",
    "ProductSearchMatchingVariants",
    "ProductSearchProjectionParams",
    "ProductSearchRequest",
    "ProductSearchResult",
]


class ProductPagedSearchResponse(_BaseType):
    #: Total number of results matching the query.
    total: int
    #: Number of [elements skipped](/../api/general-concepts#offset).
    offset: int
    #: Number of [results requested](/../api/general-concepts#limit).
    limit: int
    #: Results for [facets](/../api/projects/product-search#facets) when requested.
    facets: typing.List["ProductSearchFacetResult"]
    #: Search result containing the Products matching the search query.
    results: typing.List["ProductSearchResult"]

    def __init__(
        self,
        *,
        total: int,
        offset: int,
        limit: int,
        facets: typing.List["ProductSearchFacetResult"],
        results: typing.List["ProductSearchResult"]
    ):
        self.total = total
        self.offset = offset
        self.limit = limit
        self.facets = facets
        self.results = results

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductPagedSearchResponse":
        from ._schemas.product_search import ProductPagedSearchResponseSchema

        return ProductPagedSearchResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_search import ProductPagedSearchResponseSchema

        return ProductPagedSearchResponseSchema().dump(self)


class ProductSearchErrorResponse(ErrorResponse):

    def __init__(
        self,
        *,
        status_code: int,
        message: str,
        errors: typing.Optional[typing.List["ErrorObject"]] = None
    ):

        super().__init__(status_code=status_code, message=message, errors=errors)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSearchErrorResponse":
        from ._schemas.product_search import ProductSearchErrorResponseSchema

        return ProductSearchErrorResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_search import ProductSearchErrorResponseSchema

        return ProductSearchErrorResponseSchema().dump(self)


class ProductSearchMatchingVariantEntry(_BaseType):
    #: Unique identifier of the variant.
    id: int
    #: SKU of the matching variant.
    sku: typing.Optional[str]

    def __init__(self, *, id: int, sku: typing.Optional[str] = None):
        self.id = id
        self.sku = sku

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSearchMatchingVariantEntry":
        from ._schemas.product_search import ProductSearchMatchingVariantEntrySchema

        return ProductSearchMatchingVariantEntrySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_search import ProductSearchMatchingVariantEntrySchema

        return ProductSearchMatchingVariantEntrySchema().dump(self)


class ProductSearchMatchingVariants(_BaseType):
    #: Whether the search criteria definitely matches all Variants of the returned Product, like for Product-level fields. Is always `false` for search expressions on Variant-level fields.
    all_matched: bool
    #: The variants matching the search criteria or empty if all matched.
    matched_variants: typing.List["ProductSearchMatchingVariantEntry"]

    def __init__(
        self,
        *,
        all_matched: bool,
        matched_variants: typing.List["ProductSearchMatchingVariantEntry"]
    ):
        self.all_matched = all_matched
        self.matched_variants = matched_variants

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSearchMatchingVariants":
        from ._schemas.product_search import ProductSearchMatchingVariantsSchema

        return ProductSearchMatchingVariantsSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_search import ProductSearchMatchingVariantsSchema

        return ProductSearchMatchingVariantsSchema().dump(self)


class ProductSearchProjectionParams(_BaseType):
    #: Expands a `value` of type [Reference](ctp:api:type:Reference) in a [ProductProjection](ctp:api:type:ProductProjection).
    #: In case the referenced object does not exist, the API returns the non-expanded reference.
    expand: typing.Optional[typing.List["str"]]
    #: Set to `true` to retrieve the [staged](ctp:api:type:CurrentStaged) Product Projection
    staged: typing.Optional[bool]
    #: The currency used for [Product price selection](/../api/pricing-and-discounts-overview#product-price-selection).
    price_currency: typing.Optional[str]
    #: The country used for [Product price selection](/../api/pricing-and-discounts-overview#product-price-selection). Can only be used **in conjunction with** the `priceCurrency` parameter.
    price_country: typing.Optional[str]
    #: `id` of an existing [CustomerGroup](ctp:api:type:CustomerGroup) used for [Product price selection](/../api/pricing-and-discounts-overview#product-price-selection). Can only be used **in conjunction with** the `priceCurrency` parameter.
    price_customer_group: typing.Optional[str]
    #: `id` of an existing [Channel](ctp:api:type:Channel) used for [Product price selection](/../api/pricing-and-discounts-overview#product-price-selection). Can only be used **in conjunction with** the `priceCurrency` parameter.
    price_channel: typing.Optional[str]
    #: Used for [locale-based projection](ctp:api:type:ProductProjectionLocales).
    locale_projection: typing.Optional[typing.List["str"]]
    #: `key` of an existing [Store](ctp:api:type:Store).
    #: If the Store has defined some languages, countries, distribution or supply Channels,
    #: they are used for projections based on [locale](ctp:api:type:ProductProjectionLocales), [price](ctp:api:type:ProductProjectionPrices),
    #: and [inventory](ctp:api:type:ProductProjectionInventoryEntries).
    #: If the Store has defined [Product Selections](ctp:api:type:ProductSelection), they have no effect on the results of this query.
    store_projection: typing.Optional[str]

    def __init__(
        self,
        *,
        expand: typing.Optional[typing.List["str"]] = None,
        staged: typing.Optional[bool] = None,
        price_currency: typing.Optional[str] = None,
        price_country: typing.Optional[str] = None,
        price_customer_group: typing.Optional[str] = None,
        price_channel: typing.Optional[str] = None,
        locale_projection: typing.Optional[typing.List["str"]] = None,
        store_projection: typing.Optional[str] = None
    ):
        self.expand = expand
        self.staged = staged
        self.price_currency = price_currency
        self.price_country = price_country
        self.price_customer_group = price_customer_group
        self.price_channel = price_channel
        self.locale_projection = locale_projection
        self.store_projection = store_projection

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSearchProjectionParams":
        from ._schemas.product_search import ProductSearchProjectionParamsSchema

        return ProductSearchProjectionParamsSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_search import ProductSearchProjectionParamsSchema

        return ProductSearchProjectionParamsSchema().dump(self)


class ProductSearchRequest(_BaseType):
    #: The search query against [searchable Product fields](/../api/projects/product-search#searchable-product-fields).
    query: typing.Optional["SearchQuery"]
    #: Controls how results to your query are sorted. If not provided, the results are sorted by relevance in descending order.
    sort: typing.Optional[typing.List["SearchSorting"]]
    #: The maximum number of search results to be returned.
    limit: typing.Optional[int]
    #: The number of search results to be skipped in the response for pagination.
    offset: typing.Optional[int]
    #: The search can return Products where not all Product Variants match the search criteria. If `true`, the response will include a field called `matchingVariants` that contains the `sku` of Product Variants that match the search query. If the query does not specify any variant-level criteria, `matchingVariants` will be null signifying that all Product Variants are a match.
    mark_matching_variants: typing.Optional[bool]
    #: Set this field to `{}` to get the [ProductProjection](ctp:api:type:ProductProjection) included in the [ProductSearchResult](ctp:api:type:ProductSearchResult).
    #: Include query parameters for controlling [Reference Expansion](/../api/general-concepts#reference-expansion) or [projections](/../api/projects/productProjections#projection-dimensions) according to your needs.
    #: If not set, the result does not include the Product Projection.
    product_projection_parameters: typing.Optional["ProductSearchProjectionParams"]
    #: Set this field to request [facets](/../api/projects/product-search#facets).
    facets: typing.Optional[typing.List["ProductSearchFacetExpression"]]
    #: Specify an additional filter on the result of the `query` after the API calculated `facets`.
    #: This feature assists you in implementing faceted search.
    post_filter: typing.Optional["SearchQuery"]

    def __init__(
        self,
        *,
        query: typing.Optional["SearchQuery"] = None,
        sort: typing.Optional[typing.List["SearchSorting"]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        mark_matching_variants: typing.Optional[bool] = None,
        product_projection_parameters: typing.Optional[
            "ProductSearchProjectionParams"
        ] = None,
        facets: typing.Optional[typing.List["ProductSearchFacetExpression"]] = None,
        post_filter: typing.Optional["SearchQuery"] = None
    ):
        self.query = query
        self.sort = sort
        self.limit = limit
        self.offset = offset
        self.mark_matching_variants = mark_matching_variants
        self.product_projection_parameters = product_projection_parameters
        self.facets = facets
        self.post_filter = post_filter

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductSearchRequest":
        from ._schemas.product_search import ProductSearchRequestSchema

        return ProductSearchRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_search import ProductSearchRequestSchema

        return ProductSearchRequestSchema().dump(self)


class ProductSearchResult(_BaseType):
    #: Unique identifier of the Product.
    id: str
    #: Contains Product Projection data for Products matching the `projection` field in the Search Products request.
    product_projection: typing.Optional["ProductProjection"]
    #: Describes the variants that matched the search criteria.
    matching_variants: typing.Optional["ProductSearchMatchingVariants"]

    def __init__(
        self,
        *,
        id: str,
        product_projection: typing.Optional["ProductProjection"] = None,
        matching_variants: typing.Optional["ProductSearchMatchingVariants"] = None
    ):
        self.id = id
        self.product_projection = product_projection
        self.matching_variants = matching_variants

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductSearchResult":
        from ._schemas.product_search import ProductSearchResultSchema

        return ProductSearchResultSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_search import ProductSearchResultSchema

        return ProductSearchResultSchema().dump(self)


class ProductSearchFacetCountLevelEnum(enum.Enum):
    PRODUCTS = "products"
    VARIANTS = "variants"


class ProductSearchFacetCountValue(_BaseType):
    #: Name of the count facet to appear in the [ProductSearchFacetResultCount](ctp:api:type:ProductSearchFacetResultCount).
    name: str
    #: Whether the facet must consider only the Products resulting from the search (`query`) or all the Products (`all`).
    scope: typing.Optional["ProductSearchFacetScopeEnum"]
    #: Additional filtering expression to apply to the search result before calculating the facet.
    filter: typing.Optional["SearchQuery"]
    #: Specify whether to count Products (`products`) or Product Variants (`variants`).
    level: typing.Optional["ProductSearchFacetCountLevelEnum"]

    def __init__(
        self,
        *,
        name: str,
        scope: typing.Optional["ProductSearchFacetScopeEnum"] = None,
        filter: typing.Optional["SearchQuery"] = None,
        level: typing.Optional["ProductSearchFacetCountLevelEnum"] = None
    ):
        self.name = name
        self.scope = scope
        self.filter = filter
        self.level = level

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSearchFacetCountValue":
        from ._schemas.product_search import ProductSearchFacetCountValueSchema

        return ProductSearchFacetCountValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_search import ProductSearchFacetCountValueSchema

        return ProductSearchFacetCountValueSchema().dump(self)


class ProductSearchFacetDistinctBucketSortBy(enum.Enum):
    COUNT = "count"
    KEY = "key"


class ProductSearchFacetDistinctBucketSortExpression(_BaseType):
    #: Defines whether to sort by bucket count or key.
    by: "ProductSearchFacetDistinctBucketSortBy"
    #: Defines the sorting order.
    order: "SearchSortOrder"

    def __init__(
        self, *, by: "ProductSearchFacetDistinctBucketSortBy", order: "SearchSortOrder"
    ):
        self.by = by
        self.order = order

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSearchFacetDistinctBucketSortExpression":
        from ._schemas.product_search import (
            ProductSearchFacetDistinctBucketSortExpressionSchema,
        )

        return ProductSearchFacetDistinctBucketSortExpressionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_search import (
            ProductSearchFacetDistinctBucketSortExpressionSchema,
        )

        return ProductSearchFacetDistinctBucketSortExpressionSchema().dump(self)


class ProductSearchFacetDistinctValue(_BaseType):
    #: Name of the distinct facet to appear in the [ProductSearchFacetResultBucket](ctp:api:type:ProductSearchFacetResultBucket).
    name: str
    #: Whether the facet must consider only the Products resulting from the search (`query`) or all the Products (`all`).
    scope: typing.Optional["ProductSearchFacetScopeEnum"]
    #: Additional filtering expression to apply to the search result before calculating the facet.
    filter: typing.Optional["SearchQuery"]
    #: Specify whether to count Products (`products`) or Product Variants (`variants`).
    level: typing.Optional["ProductSearchFacetCountLevelEnum"]
    #: The [searchable Product field](/api/projects/product-search#searchable-product-fields) to facet on.
    field: str
    #: Specify which bucket keys the facets results should include.
    includes: typing.Optional[typing.List["str"]]
    #: Define how the buckets are sorted.
    sort: typing.Optional["ProductSearchFacetDistinctBucketSortExpression"]
    #: Maximum number of buckets to return.
    limit: typing.Optional[int]
    #: String value specifying linguistic and regional preferences using the [IETF language tag format](https://en.wikipedia.org/wiki/IETF_language_tag), as described in [BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). The format combines language, script, and region using hyphen-separated subtags. For example: `en`, `en-US`, `zh-Hans-SG`.
    language: typing.Optional[str]
    #: If the `field` is not standard, this must be the Attribute type.
    field_type: typing.Optional["SearchFieldType"]
    #: Default value to use if the specified field is not present on some Products.
    missing: typing.Optional[str]

    def __init__(
        self,
        *,
        name: str,
        scope: typing.Optional["ProductSearchFacetScopeEnum"] = None,
        filter: typing.Optional["SearchQuery"] = None,
        level: typing.Optional["ProductSearchFacetCountLevelEnum"] = None,
        field: str,
        includes: typing.Optional[typing.List["str"]] = None,
        sort: typing.Optional["ProductSearchFacetDistinctBucketSortExpression"] = None,
        limit: typing.Optional[int] = None,
        language: typing.Optional[str] = None,
        field_type: typing.Optional["SearchFieldType"] = None,
        missing: typing.Optional[str] = None
    ):
        self.name = name
        self.scope = scope
        self.filter = filter
        self.level = level
        self.field = field
        self.includes = includes
        self.sort = sort
        self.limit = limit
        self.language = language
        self.field_type = field_type
        self.missing = missing

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSearchFacetDistinctValue":
        from ._schemas.product_search import ProductSearchFacetDistinctValueSchema

        return ProductSearchFacetDistinctValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_search import ProductSearchFacetDistinctValueSchema

        return ProductSearchFacetDistinctValueSchema().dump(self)


class ProductSearchFacetExpression(typing.Dict[str, typing.Any]):
    pass


class ProductSearchFacetCountExpression(ProductSearchFacetExpression):
    #: Definition of the count facet.
    count: "ProductSearchFacetCountValue"

    def __init__(self, *, count: "ProductSearchFacetCountValue"):
        self.count = count

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSearchFacetCountExpression":
        from ._schemas.product_search import ProductSearchFacetCountExpressionSchema

        return ProductSearchFacetCountExpressionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_search import ProductSearchFacetCountExpressionSchema

        return ProductSearchFacetCountExpressionSchema().dump(self)


class ProductSearchFacetDistinctExpression(ProductSearchFacetExpression):
    #: Definition of the distinct facet.
    distinct: "ProductSearchFacetDistinctValue"

    def __init__(self, *, distinct: "ProductSearchFacetDistinctValue"):
        self.distinct = distinct

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSearchFacetDistinctExpression":
        from ._schemas.product_search import ProductSearchFacetDistinctExpressionSchema

        return ProductSearchFacetDistinctExpressionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_search import ProductSearchFacetDistinctExpressionSchema

        return ProductSearchFacetDistinctExpressionSchema().dump(self)


class ProductSearchFacetRangesExpression(ProductSearchFacetExpression):
    #: Definition of the ranges facet.
    ranges: "ProductSearchFacetRangesValue"

    def __init__(self, *, ranges: "ProductSearchFacetRangesValue"):
        self.ranges = ranges

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSearchFacetRangesExpression":
        from ._schemas.product_search import ProductSearchFacetRangesExpressionSchema

        return ProductSearchFacetRangesExpressionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_search import ProductSearchFacetRangesExpressionSchema

        return ProductSearchFacetRangesExpressionSchema().dump(self)


class ProductSearchFacetRangesFacetRange(_BaseType):
    """Values for `from` and `to` must be a number or [DateTime](ctp:api:type:DateTime)."""

    #: Starting value of the bucket (inclusive).
    from_: typing.Optional[typing.Any]
    #: Ending value of the bucket (non-inclusive).
    to: typing.Optional[typing.Any]
    #: Key to assign the bucket.
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        from_: typing.Optional[typing.Any] = None,
        to: typing.Optional[typing.Any] = None,
        key: typing.Optional[str] = None
    ):
        self.from_ = from_
        self.to = to
        self.key = key

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSearchFacetRangesFacetRange":
        from ._schemas.product_search import ProductSearchFacetRangesFacetRangeSchema

        return ProductSearchFacetRangesFacetRangeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_search import ProductSearchFacetRangesFacetRangeSchema

        return ProductSearchFacetRangesFacetRangeSchema().dump(self)


class ProductSearchFacetRangesValue(_BaseType):
    #: Name of the ranges facet to appear in the [ProductSearchFacetResultBucket](ctp:api:type:ProductSearchFacetResultBucket).
    name: str
    #: Whether the facet must consider only the Products resulting from the search (`query`) or all the Products (`all`).
    scope: typing.Optional["ProductSearchFacetScopeEnum"]
    #: Additional filtering expression to apply to the search result before calculating the facet.
    filter: typing.Optional["SearchQuery"]
    #: Specify whether to count Products (`products`) or Product Variants (`variants`).
    level: typing.Optional["ProductSearchFacetCountLevelEnum"]
    #: The [searchable Product field](/api/projects/product-search#searchable-product-fields) to facet on.
    field: str
    #: Define ranges for the facet.
    ranges: typing.List["ProductSearchFacetRangesFacetRange"]
    #: String value specifying linguistic and regional preferences using the [IETF language tag format](https://en.wikipedia.org/wiki/IETF_language_tag), as described in [BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). The format combines language, script, and region using hyphen-separated subtags. For example: `en`, `en-US`, `zh-Hans-SG`.
    language: typing.Optional[str]
    #: If the `field` is not standard, this must be the Attribute type.
    field_type: typing.Optional["SearchFieldType"]

    def __init__(
        self,
        *,
        name: str,
        scope: typing.Optional["ProductSearchFacetScopeEnum"] = None,
        filter: typing.Optional["SearchQuery"] = None,
        level: typing.Optional["ProductSearchFacetCountLevelEnum"] = None,
        field: str,
        ranges: typing.List["ProductSearchFacetRangesFacetRange"],
        language: typing.Optional[str] = None,
        field_type: typing.Optional["SearchFieldType"] = None
    ):
        self.name = name
        self.scope = scope
        self.filter = filter
        self.level = level
        self.field = field
        self.ranges = ranges
        self.language = language
        self.field_type = field_type

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSearchFacetRangesValue":
        from ._schemas.product_search import ProductSearchFacetRangesValueSchema

        return ProductSearchFacetRangesValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_search import ProductSearchFacetRangesValueSchema

        return ProductSearchFacetRangesValueSchema().dump(self)


class ProductSearchFacetResult(_BaseType):
    #: Name of the facet.
    name: str

    def __init__(self, *, name: str):
        self.name = name

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSearchFacetResult":
        from ._schemas.product_search import ProductSearchFacetResultSchema

        return ProductSearchFacetResultSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_search import ProductSearchFacetResultSchema

        return ProductSearchFacetResultSchema().dump(self)


class ProductSearchFacetResultBucket(ProductSearchFacetResult):
    """Result of a [distinct facet](/../api/projects/product-search#distinct-facets) or a [ranges facet](/../api/projects/product-search#ranges-facets)."""

    #: Contains results of the facet.
    buckets: typing.List["ProductSearchFacetResultBucketEntry"]

    def __init__(
        self, *, name: str, buckets: typing.List["ProductSearchFacetResultBucketEntry"]
    ):
        self.buckets = buckets

        super().__init__(name=name)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSearchFacetResultBucket":
        from ._schemas.product_search import ProductSearchFacetResultBucketSchema

        return ProductSearchFacetResultBucketSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_search import ProductSearchFacetResultBucketSchema

        return ProductSearchFacetResultBucketSchema().dump(self)


class ProductSearchFacetResultBucketEntry(_BaseType):
    #: Key of the bucket.
    key: str
    #: Number of values in the bucket.
    count: int

    def __init__(self, *, key: str, count: int):
        self.key = key
        self.count = count

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSearchFacetResultBucketEntry":
        from ._schemas.product_search import ProductSearchFacetResultBucketEntrySchema

        return ProductSearchFacetResultBucketEntrySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_search import ProductSearchFacetResultBucketEntrySchema

        return ProductSearchFacetResultBucketEntrySchema().dump(self)


class ProductSearchFacetResultCount(ProductSearchFacetResult):
    """Result of a [count facet](/../api/projects/product-search#count-facets)."""

    #: Number of Products (or Product Variants) matching the query.
    value: int

    def __init__(self, *, name: str, value: int):
        self.value = value

        super().__init__(name=name)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSearchFacetResultCount":
        from ._schemas.product_search import ProductSearchFacetResultCountSchema

        return ProductSearchFacetResultCountSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_search import ProductSearchFacetResultCountSchema

        return ProductSearchFacetResultCountSchema().dump(self)


class ProductSearchFacetScope(enum.Enum):
    ALL = "all"
    QUERY = "query"


class ProductSearchFacetScopeEnum(enum.Enum):
    ALL = "all"
    QUERY = "query"
