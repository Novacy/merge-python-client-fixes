# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_dict import remove_none_from_dict
from .....environment import MergeEnvironment
from ...types.file_storage_folder_response import FileStorageFolderResponse
from ...types.folder import Folder
from ...types.folder_request import FolderRequest
from ...types.folders_list_request_expand import FoldersListRequestExpand
from ...types.folders_retrieve_request_expand import FoldersRetrieveRequestExpand
from ...types.meta_response import MetaResponse
from ...types.paginated_folder_list import PaginatedFolderList

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class FoldersClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: SyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        created_after: typing.Optional[str] = None,
        created_before: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        drive_id: typing.Optional[str] = None,
        expand: typing.Optional[FoldersListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[str] = None,
        modified_before: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        parent_folder_id: typing.Optional[str] = None,
        remote_id: typing.Optional[str] = None,
    ) -> PaginatedFolderList:
        """
        Returns a list of `Folder` objects.

        Parameters:
            - created_after: typing.Optional[str]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[str]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - drive_id: typing.Optional[str]. If provided, will only return folders in this drive.

            - expand: typing.Optional[FoldersListRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - modified_after: typing.Optional[str]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[str]. If provided, only objects synced by Merge before this date time will be returned.

            - name: typing.Optional[str]. If provided, will only return folders with this name. This performs an exact match.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - parent_folder_id: typing.Optional[str]. If provided, will only return folders in this parent folder. If null, will return folders in root directory.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/filestorage/v1/folders"),
            params=remove_none_from_dict(
                {
                    "created_after": created_after,
                    "created_before": created_before,
                    "cursor": cursor,
                    "drive_id": drive_id,
                    "expand": expand,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "modified_after": modified_after,
                    "modified_before": modified_before,
                    "name": name,
                    "page_size": page_size,
                    "parent_folder_id": parent_folder_id,
                    "remote_id": remote_id,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedFolderList, _response.json())  # type: ignore
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
        model: FolderRequest,
    ) -> FileStorageFolderResponse:
        """
        Creates a `Folder` object with the given values.

        Parameters:
            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: FolderRequest.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/filestorage/v1/folders"),
            params=remove_none_from_dict({"is_debug_mode": is_debug_mode, "run_async": run_async}),
            json=jsonable_encoder({"model": model}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(FileStorageFolderResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[FoldersRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
    ) -> Folder:
        """
        Returns a `Folder` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[FoldersRetrieveRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"api/filestorage/v1/folders/{id}"),
            params=remove_none_from_dict({"expand": expand, "include_remote_data": include_remote_data}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Folder, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def meta_post_retrieve(self) -> MetaResponse:
        """
        Returns metadata for `FileStorageFolder` POSTs.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/filestorage/v1/folders/meta/post"),
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


class AsyncFoldersClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: AsyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        created_after: typing.Optional[str] = None,
        created_before: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        drive_id: typing.Optional[str] = None,
        expand: typing.Optional[FoldersListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[str] = None,
        modified_before: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        parent_folder_id: typing.Optional[str] = None,
        remote_id: typing.Optional[str] = None,
    ) -> PaginatedFolderList:
        """
        Returns a list of `Folder` objects.

        Parameters:
            - created_after: typing.Optional[str]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[str]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - drive_id: typing.Optional[str]. If provided, will only return folders in this drive.

            - expand: typing.Optional[FoldersListRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - modified_after: typing.Optional[str]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[str]. If provided, only objects synced by Merge before this date time will be returned.

            - name: typing.Optional[str]. If provided, will only return folders with this name. This performs an exact match.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - parent_folder_id: typing.Optional[str]. If provided, will only return folders in this parent folder. If null, will return folders in root directory.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/filestorage/v1/folders"),
            params=remove_none_from_dict(
                {
                    "created_after": created_after,
                    "created_before": created_before,
                    "cursor": cursor,
                    "drive_id": drive_id,
                    "expand": expand,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "modified_after": modified_after,
                    "modified_before": modified_before,
                    "name": name,
                    "page_size": page_size,
                    "parent_folder_id": parent_folder_id,
                    "remote_id": remote_id,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedFolderList, _response.json())  # type: ignore
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
        model: FolderRequest,
    ) -> FileStorageFolderResponse:
        """
        Creates a `Folder` object with the given values.

        Parameters:
            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: FolderRequest.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/filestorage/v1/folders"),
            params=remove_none_from_dict({"is_debug_mode": is_debug_mode, "run_async": run_async}),
            json=jsonable_encoder({"model": model}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(FileStorageFolderResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[FoldersRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
    ) -> Folder:
        """
        Returns a `Folder` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[FoldersRetrieveRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"api/filestorage/v1/folders/{id}"),
            params=remove_none_from_dict({"expand": expand, "include_remote_data": include_remote_data}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Folder, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def meta_post_retrieve(self) -> MetaResponse:
        """
        Returns metadata for `FileStorageFolder` POSTs.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/filestorage/v1/folders/meta/post"),
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
