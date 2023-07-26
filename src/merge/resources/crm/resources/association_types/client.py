# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic
import typing_extensions

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_dict import remove_none_from_dict
from .....environment import MergeEnvironment
from ...types.association_type import AssociationType
from ...types.association_type_request_request import AssociationTypeRequestRequest
from ...types.crm_association_type_response import CrmAssociationTypeResponse
from ...types.meta_response import MetaResponse
from ...types.paginated_association_type_list import PaginatedAssociationTypeList

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AssociationTypesClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: SyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    def custom_object_classes_association_types_list(
        self,
        custom_object_class_id: str,
        *,
        created_after: typing.Optional[str] = None,
        created_before: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[typing_extensions.Literal["target_object_classes"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[str] = None,
        modified_before: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
    ) -> PaginatedAssociationTypeList:
        """
        Returns a list of `AssociationType` objects.

        Parameters:
            - custom_object_class_id: str.

            - created_after: typing.Optional[str]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[str]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - expand: typing.Optional[typing_extensions.Literal["target_object_classes"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - modified_after: typing.Optional[str]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[str]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._environment.value}/",
                f"api/crm/v1/custom-object-classes/{custom_object_class_id}/association-types",
            ),
            params=remove_none_from_dict(
                {
                    "created_after": created_after,
                    "created_before": created_before,
                    "cursor": cursor,
                    "expand": expand,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "modified_after": modified_after,
                    "modified_before": modified_before,
                    "page_size": page_size,
                    "remote_id": remote_id,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedAssociationTypeList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def custom_object_classes_association_types_create(
        self,
        custom_object_class_id: str,
        *,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        model: AssociationTypeRequestRequest,
    ) -> CrmAssociationTypeResponse:
        """
        Creates an `AssociationType` object with the given values.

        Parameters:
            - custom_object_class_id: str.

            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: AssociationTypeRequestRequest.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._environment.value}/",
                f"api/crm/v1/custom-object-classes/{custom_object_class_id}/association-types",
            ),
            params=remove_none_from_dict({"is_debug_mode": is_debug_mode, "run_async": run_async}),
            json=jsonable_encoder({"model": model}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CrmAssociationTypeResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def custom_object_classes_association_types_retrieve(
        self,
        custom_object_class_id: str,
        id: str,
        *,
        expand: typing.Optional[typing_extensions.Literal["target_object_classes"]] = None,
        include_remote_data: typing.Optional[bool] = None,
    ) -> AssociationType:
        """
        Returns an `AssociationType` object with the given `id`.

        Parameters:
            - custom_object_class_id: str.

            - id: str.

            - expand: typing.Optional[typing_extensions.Literal["target_object_classes"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._environment.value}/",
                f"api/crm/v1/custom-object-classes/{custom_object_class_id}/association-types/{id}",
            ),
            params=remove_none_from_dict({"expand": expand, "include_remote_data": include_remote_data}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AssociationType, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def custom_object_classes_association_types_meta_post_retrieve(self, custom_object_class_id: str) -> MetaResponse:
        """
        Returns metadata for `CRMAssociationType` POSTs.

        Parameters:
            - custom_object_class_id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._environment.value}/",
                f"api/crm/v1/custom-object-classes/{custom_object_class_id}/association-types/meta/post",
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


class AsyncAssociationTypesClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: AsyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    async def custom_object_classes_association_types_list(
        self,
        custom_object_class_id: str,
        *,
        created_after: typing.Optional[str] = None,
        created_before: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[typing_extensions.Literal["target_object_classes"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[str] = None,
        modified_before: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
    ) -> PaginatedAssociationTypeList:
        """
        Returns a list of `AssociationType` objects.

        Parameters:
            - custom_object_class_id: str.

            - created_after: typing.Optional[str]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[str]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - expand: typing.Optional[typing_extensions.Literal["target_object_classes"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - modified_after: typing.Optional[str]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[str]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._environment.value}/",
                f"api/crm/v1/custom-object-classes/{custom_object_class_id}/association-types",
            ),
            params=remove_none_from_dict(
                {
                    "created_after": created_after,
                    "created_before": created_before,
                    "cursor": cursor,
                    "expand": expand,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "modified_after": modified_after,
                    "modified_before": modified_before,
                    "page_size": page_size,
                    "remote_id": remote_id,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedAssociationTypeList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def custom_object_classes_association_types_create(
        self,
        custom_object_class_id: str,
        *,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        model: AssociationTypeRequestRequest,
    ) -> CrmAssociationTypeResponse:
        """
        Creates an `AssociationType` object with the given values.

        Parameters:
            - custom_object_class_id: str.

            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: AssociationTypeRequestRequest.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._environment.value}/",
                f"api/crm/v1/custom-object-classes/{custom_object_class_id}/association-types",
            ),
            params=remove_none_from_dict({"is_debug_mode": is_debug_mode, "run_async": run_async}),
            json=jsonable_encoder({"model": model}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CrmAssociationTypeResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def custom_object_classes_association_types_retrieve(
        self,
        custom_object_class_id: str,
        id: str,
        *,
        expand: typing.Optional[typing_extensions.Literal["target_object_classes"]] = None,
        include_remote_data: typing.Optional[bool] = None,
    ) -> AssociationType:
        """
        Returns an `AssociationType` object with the given `id`.

        Parameters:
            - custom_object_class_id: str.

            - id: str.

            - expand: typing.Optional[typing_extensions.Literal["target_object_classes"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._environment.value}/",
                f"api/crm/v1/custom-object-classes/{custom_object_class_id}/association-types/{id}",
            ),
            params=remove_none_from_dict({"expand": expand, "include_remote_data": include_remote_data}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AssociationType, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def custom_object_classes_association_types_meta_post_retrieve(
        self, custom_object_class_id: str
    ) -> MetaResponse:
        """
        Returns metadata for `CRMAssociationType` POSTs.

        Parameters:
            - custom_object_class_id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._environment.value}/",
                f"api/crm/v1/custom-object-classes/{custom_object_class_id}/association-types/meta/post",
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
