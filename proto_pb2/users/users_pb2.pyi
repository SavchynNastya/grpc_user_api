from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateUsersRequest(_message.Message):
    __slots__ = ["admin_id", "admin_hash", "user_username", "user_email"]
    ADMIN_ID_FIELD_NUMBER: _ClassVar[int]
    ADMIN_HASH_FIELD_NUMBER: _ClassVar[int]
    USER_USERNAME_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    admin_id: int
    admin_hash: str
    user_username: str
    user_email: str
    def __init__(self, admin_id: _Optional[int] = ..., admin_hash: _Optional[str] = ..., user_username: _Optional[str] = ..., user_email: _Optional[str] = ...) -> None: ...

class CreateUsersResponse(_message.Message):
    __slots__ = ["status", "message", "key_api"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    KEY_API_FIELD_NUMBER: _ClassVar[int]
    status: int
    message: str
    key_api: str
    def __init__(self, status: _Optional[int] = ..., message: _Optional[str] = ..., key_api: _Optional[str] = ...) -> None: ...

class UpdateUserStatusRequest(_message.Message):
    __slots__ = ["admin_id", "admin_hash", "user_username", "status"]
    ADMIN_ID_FIELD_NUMBER: _ClassVar[int]
    ADMIN_HASH_FIELD_NUMBER: _ClassVar[int]
    USER_USERNAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    admin_id: int
    admin_hash: str
    user_username: str
    status: int
    def __init__(self, admin_id: _Optional[int] = ..., admin_hash: _Optional[str] = ..., user_username: _Optional[str] = ..., status: _Optional[int] = ...) -> None: ...

class UpdateUserStatusResponse(_message.Message):
    __slots__ = ["status", "message"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: int
    message: str
    def __init__(self, status: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class CheckAdminRequest(_message.Message):
    __slots__ = ["admin_id", "admin_hash"]
    ADMIN_ID_FIELD_NUMBER: _ClassVar[int]
    ADMIN_HASH_FIELD_NUMBER: _ClassVar[int]
    admin_id: int
    admin_hash: str
    def __init__(self, admin_id: _Optional[int] = ..., admin_hash: _Optional[str] = ...) -> None: ...

class CheckAdminResponse(_message.Message):
    __slots__ = ["status", "message"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: int
    message: str
    def __init__(self, status: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class ReadUsersRequest(_message.Message):
    __slots__ = ["id", "name", "username", "first_email", "second_email", "key", "hash", "salt", "status", "description", "timestamp"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_EMAIL_FIELD_NUMBER: _ClassVar[int]
    SECOND_EMAIL_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    SALT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    id: _containers.RepeatedScalarFieldContainer[int]
    name: _containers.RepeatedScalarFieldContainer[str]
    username: _containers.RepeatedScalarFieldContainer[str]
    first_email: _containers.RepeatedScalarFieldContainer[str]
    second_email: _containers.RepeatedScalarFieldContainer[str]
    key: _containers.RepeatedScalarFieldContainer[str]
    hash: _containers.RepeatedScalarFieldContainer[str]
    salt: _containers.RepeatedScalarFieldContainer[str]
    status: _containers.RepeatedScalarFieldContainer[int]
    description: _containers.RepeatedScalarFieldContainer[str]
    timestamp: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[_Iterable[int]] = ..., name: _Optional[_Iterable[str]] = ..., username: _Optional[_Iterable[str]] = ..., first_email: _Optional[_Iterable[str]] = ..., second_email: _Optional[_Iterable[str]] = ..., key: _Optional[_Iterable[str]] = ..., hash: _Optional[_Iterable[str]] = ..., salt: _Optional[_Iterable[str]] = ..., status: _Optional[_Iterable[int]] = ..., description: _Optional[_Iterable[str]] = ..., timestamp: _Optional[_Iterable[str]] = ...) -> None: ...

class ReadUsersResponse(_message.Message):
    __slots__ = ["status", "message", "data"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: int
    message: str
    data: _containers.RepeatedCompositeFieldContainer[UserObject]
    def __init__(self, status: _Optional[int] = ..., message: _Optional[str] = ..., data: _Optional[_Iterable[_Union[UserObject, _Mapping]]] = ...) -> None: ...

class UserObject(_message.Message):
    __slots__ = ["id", "name", "username", "first_email", "second_email", "key", "hash", "salt", "status", "description", "timestamp"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_EMAIL_FIELD_NUMBER: _ClassVar[int]
    SECOND_EMAIL_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    SALT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    username: str
    first_email: str
    second_email: str
    key: bytes
    hash: bytes
    salt: str
    status: int
    description: str
    timestamp: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., username: _Optional[str] = ..., first_email: _Optional[str] = ..., second_email: _Optional[str] = ..., key: _Optional[bytes] = ..., hash: _Optional[bytes] = ..., salt: _Optional[str] = ..., status: _Optional[int] = ..., description: _Optional[str] = ..., timestamp: _Optional[str] = ...) -> None: ...

class UpdateUsersRequest(_message.Message):
    __slots__ = ["id", "hash", "first_email", "second_email", "username", "description"]
    ID_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    FIRST_EMAIL_FIELD_NUMBER: _ClassVar[int]
    SECOND_EMAIL_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: int
    hash: str
    first_email: str
    second_email: str
    username: str
    description: str
    def __init__(self, id: _Optional[int] = ..., hash: _Optional[str] = ..., first_email: _Optional[str] = ..., second_email: _Optional[str] = ..., username: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class UpdateUsersResponse(_message.Message):
    __slots__ = ["status", "message"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: int
    message: str
    def __init__(self, status: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class DeleteUsersRequest(_message.Message):
    __slots__ = ["admin_id", "admin_hash", "user_name", "user_username", "with_data", "reason"]
    ADMIN_ID_FIELD_NUMBER: _ClassVar[int]
    ADMIN_HASH_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_USERNAME_FIELD_NUMBER: _ClassVar[int]
    WITH_DATA_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    admin_id: int
    admin_hash: str
    user_name: str
    user_username: str
    with_data: bool
    reason: str
    def __init__(self, admin_id: _Optional[int] = ..., admin_hash: _Optional[str] = ..., user_name: _Optional[str] = ..., user_username: _Optional[str] = ..., with_data: bool = ..., reason: _Optional[str] = ...) -> None: ...

class DeleteUsersResponse(_message.Message):
    __slots__ = ["status", "message"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: int
    message: str
    def __init__(self, status: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class ResetUserAuthRequest(_message.Message):
    __slots__ = ["id", "username", "hash"]
    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    id: int
    username: str
    hash: str
    def __init__(self, id: _Optional[int] = ..., username: _Optional[str] = ..., hash: _Optional[str] = ...) -> None: ...

class ResetUserAuthResponse(_message.Message):
    __slots__ = ["status", "message"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: int
    message: str
    def __init__(self, status: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class ResetAdminAuthRequest(_message.Message):
    __slots__ = ["admin_id", "admin_hash", "user_name", "user_username", "reason"]
    ADMIN_ID_FIELD_NUMBER: _ClassVar[int]
    ADMIN_HASH_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_USERNAME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    admin_id: int
    admin_hash: str
    user_name: str
    user_username: str
    reason: str
    def __init__(self, admin_id: _Optional[int] = ..., admin_hash: _Optional[str] = ..., user_name: _Optional[str] = ..., user_username: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class ResetAdminAuthResponse(_message.Message):
    __slots__ = ["status", "message"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: int
    message: str
    def __init__(self, status: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
