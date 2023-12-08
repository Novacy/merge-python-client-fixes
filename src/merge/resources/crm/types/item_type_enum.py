# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ItemTypeEnum(str, enum.Enum):
    """
    * `string` - string
    * `number` - number
    * `date` - date
    * `datetime` - datetime
    * `bool` - bool
    * `list` - list
    """

    STRING = "string"
    NUMBER = "number"
    DATE = "date"
    DATETIME = "datetime"
    BOOL = "bool"
    LIST = "list"

    def visit(
        self,
        string: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        date: typing.Callable[[], T_Result],
        datetime: typing.Callable[[], T_Result],
        bool: typing.Callable[[], T_Result],
        list: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ItemTypeEnum.STRING:
            return string()
        if self is ItemTypeEnum.NUMBER:
            return number()
        if self is ItemTypeEnum.DATE:
            return date()
        if self is ItemTypeEnum.DATETIME:
            return datetime()
        if self is ItemTypeEnum.BOOL:
            return bool()
        if self is ItemTypeEnum.LIST:
            return []
