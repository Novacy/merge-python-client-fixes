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
from ...types.lead import Lead
from ...types.lead_request import LeadRequest
from ...types.lead_response import LeadResponse
from ...types.leads_list_request_expand import LeadsListRequestExpand
from ...types.leads_retrieve_request_expand import LeadsRetrieveRequestExpand
from ...types.meta_response import MetaResponse
from ...types.paginated_lead_list import PaginatedLeadList
from ...types.paginated_remote_field_class_list import PaginatedRemoteFieldClassList

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class LeadsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        converted_account_id: typing.Optional[str] = None,
        converted_contact_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        email_addresses: typing.Optional[str] = None,
        expand: typing.Optional[LeadsListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        owner_id: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        phone_numbers: typing.Optional[str] = None,
        remote_id: typing.Optional[str] = None,
    ) -> PaginatedLeadList:
        """
        Returns a list of `Lead` objects.

        Parameters:
            - converted_account_id: typing.Optional[str]. If provided, will only return leads with this account.

            - converted_contact_id: typing.Optional[str]. If provided, will only return leads with this contact.

            - created_after: typing.Optional[dt.datetime]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[dt.datetime]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - email_addresses: typing.Optional[str]. If provided, will only return contacts matching the email addresses; multiple email_addresses can be separated by commas.

            - expand: typing.Optional[LeadsListRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

            - modified_after: typing.Optional[dt.datetime]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[dt.datetime]. If provided, only objects synced by Merge before this date time will be returned.

            - owner_id: typing.Optional[str]. If provided, will only return leads with this owner.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - phone_numbers: typing.Optional[str]. If provided, will only return contacts matching the phone numbers; multiple phone numbers can be separated by commas.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.
        ---
        from merge.client import Merge
        from merge.resources.crm import LeadsListRequestExpand

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.leads.list(
            expand=LeadsListRequestExpand.CONVERTED_ACCOUNT,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/crm/v1/leads"),
            params=remove_none_from_dict(
                {
                    "converted_account_id": converted_account_id,
                    "converted_contact_id": converted_contact_id,
                    "created_after": serialize_datetime(created_after) if created_after is not None else None,
                    "created_before": serialize_datetime(created_before) if created_before is not None else None,
                    "cursor": cursor,
                    "email_addresses": email_addresses,
                    "expand": expand,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                    "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                    "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                    "owner_id": owner_id,
                    "page_size": page_size,
                    "phone_numbers": phone_numbers,
                    "remote_id": remote_id,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedLeadList, _response.json())  # type: ignore
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
        model: LeadRequest,
    ) -> LeadResponse:
        """
        Creates a `Lead` object with the given values.

        Parameters:
            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: LeadRequest.
        ---
        import datetime

        from merge.client import Merge
        from merge.resources.crm import (
            AddressRequest,
            EmailAddressRequest,
            LeadRequest,
            PhoneNumberRequest,
        )

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.leads.create(
            model=LeadRequest(
                lead_source="API Blogger",
                title="Co-Founder",
                company="Merge API",
                first_name="Gil",
                last_name="Feig",
                addresses=[
                    AddressRequest(
                        street_1="50 Bowling Green Dr",
                        street_2="Golden Gate Park",
                        city="San Francisco",
                        state="CA",
                        postal_code="94122",
                    )
                ],
                email_addresses=[
                    EmailAddressRequest(
                        email_address="merge_is_hiring@merge.dev",
                        email_address_type="Work",
                    )
                ],
                phone_numbers=[
                    PhoneNumberRequest(
                        phone_number="+3198675309",
                        phone_number_type="Mobile",
                    )
                ],
                converted_date=datetime.datetime.fromisoformat(
                    "2022-03-10 00:00:00+00:00",
                ),
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/crm/v1/leads"),
            params=remove_none_from_dict({"is_debug_mode": is_debug_mode, "run_async": run_async}),
            json=jsonable_encoder({"model": model}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(LeadResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[LeadsRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
    ) -> Lead:
        """
        Returns a `Lead` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[LeadsRetrieveRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
        ---
        from merge.client import Merge
        from merge.resources.crm import LeadsRetrieveRequestExpand

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.leads.retrieve(
            id="id",
            expand=LeadsRetrieveRequestExpand.CONVERTED_ACCOUNT,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/crm/v1/leads/{id}"),
            params=remove_none_from_dict(
                {
                    "expand": expand,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Lead, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def meta_post_retrieve(self) -> MetaResponse:
        """
        Returns metadata for `Lead` POSTs.

        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.leads.meta_post_retrieve()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/crm/v1/leads/meta/post"),
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
        client.crm.leads.remote_field_classes_list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/crm/v1/leads/remote-field-classes"),
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


class AsyncLeadsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        converted_account_id: typing.Optional[str] = None,
        converted_contact_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        email_addresses: typing.Optional[str] = None,
        expand: typing.Optional[LeadsListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        owner_id: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        phone_numbers: typing.Optional[str] = None,
        remote_id: typing.Optional[str] = None,
    ) -> PaginatedLeadList:
        """
        Returns a list of `Lead` objects.

        Parameters:
            - converted_account_id: typing.Optional[str]. If provided, will only return leads with this account.

            - converted_contact_id: typing.Optional[str]. If provided, will only return leads with this contact.

            - created_after: typing.Optional[dt.datetime]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[dt.datetime]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - email_addresses: typing.Optional[str]. If provided, will only return contacts matching the email addresses; multiple email_addresses can be separated by commas.

            - expand: typing.Optional[LeadsListRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

            - modified_after: typing.Optional[dt.datetime]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[dt.datetime]. If provided, only objects synced by Merge before this date time will be returned.

            - owner_id: typing.Optional[str]. If provided, will only return leads with this owner.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - phone_numbers: typing.Optional[str]. If provided, will only return contacts matching the phone numbers; multiple phone numbers can be separated by commas.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.
        ---
        from merge.client import AsyncMerge
        from merge.resources.crm import LeadsListRequestExpand

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.leads.list(
            expand=LeadsListRequestExpand.CONVERTED_ACCOUNT,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/crm/v1/leads"),
            params=remove_none_from_dict(
                {
                    "converted_account_id": converted_account_id,
                    "converted_contact_id": converted_contact_id,
                    "created_after": serialize_datetime(created_after) if created_after is not None else None,
                    "created_before": serialize_datetime(created_before) if created_before is not None else None,
                    "cursor": cursor,
                    "email_addresses": email_addresses,
                    "expand": expand,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                    "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                    "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                    "owner_id": owner_id,
                    "page_size": page_size,
                    "phone_numbers": phone_numbers,
                    "remote_id": remote_id,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedLeadList, _response.json())  # type: ignore
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
        model: LeadRequest,
    ) -> LeadResponse:
        """
        Creates a `Lead` object with the given values.

        Parameters:
            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: LeadRequest.
        ---
        import datetime

        from merge.client import AsyncMerge
        from merge.resources.crm import (
            AddressRequest,
            EmailAddressRequest,
            LeadRequest,
            PhoneNumberRequest,
        )

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.leads.create(
            model=LeadRequest(
                lead_source="API Blogger",
                title="Co-Founder",
                company="Merge API",
                first_name="Gil",
                last_name="Feig",
                addresses=[
                    AddressRequest(
                        street_1="50 Bowling Green Dr",
                        street_2="Golden Gate Park",
                        city="San Francisco",
                        state="CA",
                        postal_code="94122",
                    )
                ],
                email_addresses=[
                    EmailAddressRequest(
                        email_address="merge_is_hiring@merge.dev",
                        email_address_type="Work",
                    )
                ],
                phone_numbers=[
                    PhoneNumberRequest(
                        phone_number="+3198675309",
                        phone_number_type="Mobile",
                    )
                ],
                converted_date=datetime.datetime.fromisoformat(
                    "2022-03-10 00:00:00+00:00",
                ),
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/crm/v1/leads"),
            params=remove_none_from_dict({"is_debug_mode": is_debug_mode, "run_async": run_async}),
            json=jsonable_encoder({"model": model}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(LeadResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[LeadsRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
    ) -> Lead:
        """
        Returns a `Lead` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[LeadsRetrieveRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
        ---
        from merge.client import AsyncMerge
        from merge.resources.crm import LeadsRetrieveRequestExpand

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.leads.retrieve(
            id="id",
            expand=LeadsRetrieveRequestExpand.CONVERTED_ACCOUNT,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/crm/v1/leads/{id}"),
            params=remove_none_from_dict(
                {
                    "expand": expand,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Lead, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def meta_post_retrieve(self) -> MetaResponse:
        """
        Returns metadata for `Lead` POSTs.

        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.leads.meta_post_retrieve()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/crm/v1/leads/meta/post"),
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
        await client.crm.leads.remote_field_classes_list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/crm/v1/leads/remote-field-classes"),
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
