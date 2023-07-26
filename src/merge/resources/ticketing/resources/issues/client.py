# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.remove_none_from_dict import remove_none_from_dict
from .....environment import MergeEnvironment
from ...types.issue import Issue
from ...types.issues_list_request_status import IssuesListRequestStatus
from ...types.paginated_issue_list import PaginatedIssueList


class IssuesClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: SyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        account_token: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        end_user_organization_name: typing.Optional[str] = None,
        first_incident_time_after: typing.Optional[str] = None,
        first_incident_time_before: typing.Optional[str] = None,
        include_muted: typing.Optional[str] = None,
        integration_name: typing.Optional[str] = None,
        last_incident_time_after: typing.Optional[str] = None,
        last_incident_time_before: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        start_date: typing.Optional[str] = None,
        status: typing.Optional[IssuesListRequestStatus] = None,
    ) -> PaginatedIssueList:
        """
        Gets issues.

        Parameters:
            - account_token: typing.Optional[str].

            - cursor: typing.Optional[str]. The pagination cursor value.

            - end_date: typing.Optional[str]. If included, will only include issues whose most recent action occurred before this time

            - end_user_organization_name: typing.Optional[str].

            - first_incident_time_after: typing.Optional[str]. If provided, will only return issues whose first incident time was after this datetime.

            - first_incident_time_before: typing.Optional[str]. If provided, will only return issues whose first incident time was before this datetime.

            - include_muted: typing.Optional[str]. If True, will include muted issues

            - integration_name: typing.Optional[str].

            - last_incident_time_after: typing.Optional[str]. If provided, will only return issues whose last incident time was after this datetime.

            - last_incident_time_before: typing.Optional[str]. If provided, will only return issues whose last incident time was before this datetime.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - start_date: typing.Optional[str]. If included, will only include issues whose most recent action occurred after this time

            - status: typing.Optional[IssuesListRequestStatus]. Status of the issue. Options: ('ONGOING', 'RESOLVED')

                                                                * `ONGOING` - ONGOING
                                                                * `RESOLVED` - RESOLVED
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/ticketing/v1/issues"),
            params=remove_none_from_dict(
                {
                    "account_token": account_token,
                    "cursor": cursor,
                    "end_date": end_date,
                    "end_user_organization_name": end_user_organization_name,
                    "first_incident_time_after": first_incident_time_after,
                    "first_incident_time_before": first_incident_time_before,
                    "include_muted": include_muted,
                    "integration_name": integration_name,
                    "last_incident_time_after": last_incident_time_after,
                    "last_incident_time_before": last_incident_time_before,
                    "page_size": page_size,
                    "start_date": start_date,
                    "status": status,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedIssueList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(self, id: str) -> Issue:
        """
        Get a specific issue.

        Parameters:
            - id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"api/ticketing/v1/issues/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Issue, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncIssuesClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: AsyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        account_token: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        end_user_organization_name: typing.Optional[str] = None,
        first_incident_time_after: typing.Optional[str] = None,
        first_incident_time_before: typing.Optional[str] = None,
        include_muted: typing.Optional[str] = None,
        integration_name: typing.Optional[str] = None,
        last_incident_time_after: typing.Optional[str] = None,
        last_incident_time_before: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        start_date: typing.Optional[str] = None,
        status: typing.Optional[IssuesListRequestStatus] = None,
    ) -> PaginatedIssueList:
        """
        Gets issues.

        Parameters:
            - account_token: typing.Optional[str].

            - cursor: typing.Optional[str]. The pagination cursor value.

            - end_date: typing.Optional[str]. If included, will only include issues whose most recent action occurred before this time

            - end_user_organization_name: typing.Optional[str].

            - first_incident_time_after: typing.Optional[str]. If provided, will only return issues whose first incident time was after this datetime.

            - first_incident_time_before: typing.Optional[str]. If provided, will only return issues whose first incident time was before this datetime.

            - include_muted: typing.Optional[str]. If True, will include muted issues

            - integration_name: typing.Optional[str].

            - last_incident_time_after: typing.Optional[str]. If provided, will only return issues whose last incident time was after this datetime.

            - last_incident_time_before: typing.Optional[str]. If provided, will only return issues whose last incident time was before this datetime.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - start_date: typing.Optional[str]. If included, will only include issues whose most recent action occurred after this time

            - status: typing.Optional[IssuesListRequestStatus]. Status of the issue. Options: ('ONGOING', 'RESOLVED')

                                                                * `ONGOING` - ONGOING
                                                                * `RESOLVED` - RESOLVED
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/ticketing/v1/issues"),
            params=remove_none_from_dict(
                {
                    "account_token": account_token,
                    "cursor": cursor,
                    "end_date": end_date,
                    "end_user_organization_name": end_user_organization_name,
                    "first_incident_time_after": first_incident_time_after,
                    "first_incident_time_before": first_incident_time_before,
                    "include_muted": include_muted,
                    "integration_name": integration_name,
                    "last_incident_time_after": last_incident_time_after,
                    "last_incident_time_before": last_incident_time_before,
                    "page_size": page_size,
                    "start_date": start_date,
                    "status": status,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedIssueList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(self, id: str) -> Issue:
        """
        Get a specific issue.

        Parameters:
            - id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"api/ticketing/v1/issues/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Issue, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
