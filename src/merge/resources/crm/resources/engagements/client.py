# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.datetime_utils import serialize_datetime
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_dict import remove_none_from_dict
from ...types.engagement import Engagement
from ...types.engagement_request import EngagementRequest
from ...types.engagement_response import EngagementResponse
from ...types.engagements_list_request_expand import EngagementsListRequestExpand
from ...types.engagements_retrieve_request_expand import (
    EngagementsRetrieveRequestExpand,
)
from ...types.meta_response import MetaResponse
from ...types.paginated_engagement_list import PaginatedEngagementList
from ...types.paginated_remote_field_class_list import PaginatedRemoteFieldClassList
from ...types.patched_engagement_request import PatchedEngagementRequest

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class EngagementsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[EngagementsListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
        started_after: typing.Optional[dt.datetime] = None,
        started_before: typing.Optional[dt.datetime] = None,
    ) -> PaginatedEngagementList:
        """
        Returns a list of `Engagement` objects.

        Parameters:
            - created_after: typing.Optional[dt.datetime]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[dt.datetime]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - expand: typing.Optional[EngagementsListRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

            - modified_after: typing.Optional[dt.datetime]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[dt.datetime]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.

            - started_after: typing.Optional[dt.datetime]. If provided, will only return objects started after this datetime.

            - started_before: typing.Optional[dt.datetime]. If provided, will only return objects started before this datetime.
        ---
        from merge.client import Merge
        from merge.resources.crm import EngagementsListRequestExpand

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.engagements.list(
            expand=EngagementsListRequestExpand.ACCOUNT,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "api/crm/v1/engagements"
            ),
            params=remove_none_from_dict(
                {
                    "created_after": serialize_datetime(created_after)
                    if created_after is not None
                    else None,
                    "created_before": serialize_datetime(created_before)
                    if created_before is not None
                    else None,
                    "cursor": cursor,
                    "expand": expand.value if expand is not None else None,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                    "modified_after": serialize_datetime(modified_after)
                    if modified_after is not None
                    else None,
                    "modified_before": serialize_datetime(modified_before)
                    if modified_before is not None
                    else None,
                    "page_size": page_size,
                    "remote_id": remote_id,
                    "started_after": serialize_datetime(started_after)
                    if started_after is not None
                    else None,
                    "started_before": serialize_datetime(started_before)
                    if started_before is not None
                    else None,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedEngagementList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        model: EngagementRequest,
    ) -> EngagementResponse:
        """
        Creates an `Engagement` object with the given values.

        Parameters:
            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: EngagementRequest.
        ---
        import datetime

        from merge.client import Merge
        from merge.resources.crm import EngagementRequest

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.engagements.create(
            model=EngagementRequest(
                content="Call for negotiation",
                subject="Call from customer",
                start_time=datetime.datetime.fromisoformat(
                    "2022-02-10 00:00:00+00:00",
                ),
                end_time=datetime.datetime.fromisoformat(
                    "2022-02-10 00:05:00+00:00",
                ),
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "api/crm/v1/engagements"
            ),
            params=remove_none_from_dict(
                {"is_debug_mode": is_debug_mode, "run_async": run_async}
            ),
            json=jsonable_encoder({"model": model}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EngagementResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[EngagementsRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
    ) -> Engagement:
        """
        Returns an `Engagement` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[EngagementsRetrieveRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
        ---
        from merge.client import Merge
        from merge.resources.crm import EngagementsRetrieveRequestExpand

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.engagements.retrieve(
            id="id",
            expand=EngagementsRetrieveRequestExpand.ACCOUNT,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/crm/v1/engagements/{id}",
            ),
            params=remove_none_from_dict(
                {
                    "expand": expand.value if expand is not None else None,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Engagement, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def partial_update(
        self,
        id: str,
        *,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        model: PatchedEngagementRequest,
    ) -> EngagementResponse:
        """
        Updates an `Engagement` object with the given `id`.

        Parameters:
            - id: str.

            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: PatchedEngagementRequest.
        ---
        import datetime

        from merge.client import Merge
        from merge.resources.crm import PatchedEngagementRequest

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.engagements.partial_update(
            id="id",
            model=PatchedEngagementRequest(
                owner="0358cbc6-2040-430a-848e-aafacbadf3aa",
                content="Call for negotiation",
                subject="Call from customer",
                engagement_type="0358cbc6-2040-430a-848e-aafacbadf3aa",
                start_time=datetime.datetime.fromisoformat(
                    "2022-02-10 00:00:00+00:00",
                ),
                end_time=datetime.datetime.fromisoformat(
                    "2022-02-10 00:05:00+00:00",
                ),
                account="025fjlc6-6000-430a-848e-aafacbadf4fe",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/crm/v1/engagements/{id}",
            ),
            params=remove_none_from_dict(
                {"is_debug_mode": is_debug_mode, "run_async": run_async}
            ),
            json=jsonable_encoder({"model": model}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EngagementResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def meta_patch_retrieve(self, id: str) -> MetaResponse:
        """
        Returns metadata for `Engagement` PATCHs.

        Parameters:
            - id: str.
        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.engagements.meta_patch_retrieve(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/crm/v1/engagements/meta/patch/{id}",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def meta_post_retrieve(self) -> MetaResponse:
        """
        Returns metadata for `Engagement` POSTs.

        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.engagements.meta_post_retrieve()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                "api/crm/v1/engagements/meta/post",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def remote_field_classes_list(
        self,
        *,
        cursor: typing.Optional[str] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
    ) -> PaginatedRemoteFieldClassList:
        """
        Returns a list of `RemoteFieldClass` objects.

        Parameters:
            - cursor: typing.Optional[str]. The pagination cursor value.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

            - page_size: typing.Optional[int]. Number of results to return per page.
        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.engagements.remote_field_classes_list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                "api/crm/v1/engagements/remote-field-classes",
            ),
            params=remove_none_from_dict(
                {
                    "cursor": cursor,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                    "page_size": page_size,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedRemoteFieldClassList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncEngagementsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[EngagementsListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
    ) -> PaginatedEngagementList:
        """
        Returns a list of `Engagement` objects.

        Parameters:
            - created_after: typing.Optional[dt.datetime]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[dt.datetime]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - expand: typing.Optional[EngagementsListRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

            - modified_after: typing.Optional[dt.datetime]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[dt.datetime]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.
        ---
        from merge.client import AsyncMerge
        from merge.resources.crm import EngagementsListRequestExpand

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.engagements.list(
            expand=EngagementsListRequestExpand.ACCOUNT,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "api/crm/v1/engagements"
            ),
            params=remove_none_from_dict(
                {
                    "created_after": serialize_datetime(created_after)
                    if created_after is not None
                    else None,
                    "created_before": serialize_datetime(created_before)
                    if created_before is not None
                    else None,
                    "cursor": cursor,
                    "expand": expand.value if expand is not None else None,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                    "modified_after": serialize_datetime(modified_after)
                    if modified_after is not None
                    else None,
                    "modified_before": serialize_datetime(modified_before)
                    if modified_before is not None
                    else None,
                    "page_size": page_size,
                    "remote_id": remote_id,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedEngagementList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        model: EngagementRequest,
    ) -> EngagementResponse:
        """
        Creates an `Engagement` object with the given values.

        Parameters:
            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: EngagementRequest.
        ---
        import datetime

        from merge.client import AsyncMerge
        from merge.resources.crm import EngagementRequest

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.engagements.create(
            model=EngagementRequest(
                content="Call for negotiation",
                subject="Call from customer",
                start_time=datetime.datetime.fromisoformat(
                    "2022-02-10 00:00:00+00:00",
                ),
                end_time=datetime.datetime.fromisoformat(
                    "2022-02-10 00:05:00+00:00",
                ),
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "api/crm/v1/engagements"
            ),
            params=remove_none_from_dict(
                {"is_debug_mode": is_debug_mode, "run_async": run_async}
            ),
            json=jsonable_encoder({"model": model}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EngagementResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[EngagementsRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
    ) -> Engagement:
        """
        Returns an `Engagement` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[EngagementsRetrieveRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
        ---
        from merge.client import AsyncMerge
        from merge.resources.crm import EngagementsRetrieveRequestExpand

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.engagements.retrieve(
            id="id",
            expand=EngagementsRetrieveRequestExpand.ACCOUNT,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/crm/v1/engagements/{id}",
            ),
            params=remove_none_from_dict(
                {
                    "expand": expand.value if expand is not None else None,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Engagement, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def partial_update(
        self,
        id: str,
        *,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        model: PatchedEngagementRequest,
    ) -> EngagementResponse:
        """
        Updates an `Engagement` object with the given `id`.

        Parameters:
            - id: str.

            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: PatchedEngagementRequest.
        ---
        import datetime

        from merge.client import AsyncMerge
        from merge.resources.crm import PatchedEngagementRequest

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.engagements.partial_update(
            id="id",
            model=PatchedEngagementRequest(
                owner="0358cbc6-2040-430a-848e-aafacbadf3aa",
                content="Call for negotiation",
                subject="Call from customer",
                engagement_type="0358cbc6-2040-430a-848e-aafacbadf3aa",
                start_time=datetime.datetime.fromisoformat(
                    "2022-02-10 00:00:00+00:00",
                ),
                end_time=datetime.datetime.fromisoformat(
                    "2022-02-10 00:05:00+00:00",
                ),
                account="025fjlc6-6000-430a-848e-aafacbadf4fe",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/crm/v1/engagements/{id}",
            ),
            params=remove_none_from_dict(
                {"is_debug_mode": is_debug_mode, "run_async": run_async}
            ),
            json=jsonable_encoder({"model": model}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EngagementResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def meta_patch_retrieve(self, id: str) -> MetaResponse:
        """
        Returns metadata for `Engagement` PATCHs.

        Parameters:
            - id: str.
        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.engagements.meta_patch_retrieve(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/crm/v1/engagements/meta/patch/{id}",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def meta_post_retrieve(self) -> MetaResponse:
        """
        Returns metadata for `Engagement` POSTs.

        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.engagements.meta_post_retrieve()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                "api/crm/v1/engagements/meta/post",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def remote_field_classes_list(
        self,
        *,
        cursor: typing.Optional[str] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
    ) -> PaginatedRemoteFieldClassList:
        """
        Returns a list of `RemoteFieldClass` objects.

        Parameters:
            - cursor: typing.Optional[str]. The pagination cursor value.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

            - page_size: typing.Optional[int]. Number of results to return per page.
        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.engagements.remote_field_classes_list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                "api/crm/v1/engagements/remote-field-classes",
            ),
            params=remove_none_from_dict(
                {
                    "cursor": cursor,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                    "page_size": page_size,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedRemoteFieldClassList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
