# Generated file, please do not change!!!
import typing

from ...models.product import ProductProjectionPagedQueryResponse
from ..search.by_project_key_product_projections_search_request_builder import (
    ByProjectKeyProductProjectionsSearchRequestBuilder,
)
from ..suggest.by_project_key_product_projections_suggest_request_builder import (
    ByProjectKeyProductProjectionsSuggestRequestBuilder,
)
from .by_project_key_product_projections_by_id_request_builder import (
    ByProjectKeyProductProjectionsByIDRequestBuilder,
)
from .by_project_key_product_projections_key_by_key_request_builder import (
    ByProjectKeyProductProjectionsKeyByKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyProductProjectionsRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def search(self) -> ByProjectKeyProductProjectionsSearchRequestBuilder:
        """This endpoint provides high performance search queries over ProductProjections. The query result contains the
        ProductProjections for which at least one ProductVariant matches the search query. This means that variants can
        be included in the result also for which the search query does not match. To determine which ProductVariants match
        the search query, the returned ProductProjections include the additional field isMatchingVariant.

        """
        return ByProjectKeyProductProjectionsSearchRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def suggest(self) -> ByProjectKeyProductProjectionsSuggestRequestBuilder:
        """The source of data for suggestions is the searchKeyword field in a product"""
        return ByProjectKeyProductProjectionsSuggestRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def with_key(
        self, key: str
    ) -> ByProjectKeyProductProjectionsKeyByKeyRequestBuilder:
        return ByProjectKeyProductProjectionsKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
            client=self._client,
        )

    def with_id(self, id: str) -> ByProjectKeyProductProjectionsByIDRequestBuilder:
        return ByProjectKeyProductProjectionsByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
            client=self._client,
        )

    def get(
        self,
        *,
        staged: bool = None,
        price_currency: str = None,
        price_country: str = None,
        price_customer_group: str = None,
        price_channel: str = None,
        locale_projection: str = None,
        store_projection: str = None,
        expand: str = None,
        sort: str = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: str = None,
        predicate_var: typing.Dict[str, str] = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ProductProjectionPagedQueryResponse":
        """You can use the product projections query endpoint to get the current or staged representations of Products.
        When used with an API client that has the view_published_products:{projectKey} scope,
        this endpoint only returns published (current) product projections.

        """
        params = {
            "staged": staged,
            "priceCurrency": price_currency,
            "priceCountry": price_country,
            "priceCustomerGroup": price_customer_group,
            "priceChannel": price_channel,
            "localeProjection": locale_projection,
            "storeProjection": store_projection,
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
        return self._client._get(
            endpoint=f"/{self._project_key}/product-projections",
            params=params,
            response_class=ProductProjectionPagedQueryResponse,
            headers=headers,
        )