# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from mlagents_envs.communicator_objects.agent_info_pb2 import (
    AgentInfoProto as mlagents_envs___communicator_objects___agent_info_pb2___AgentInfoProto,
)

from typing import (
    Iterable as typing___Iterable,
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


class UnityRLOutputProto(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ListAgentInfoProto(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def value(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[mlagents_envs___communicator_objects___agent_info_pb2___AgentInfoProto]: ...

        def __init__(self,
            *,
            value : typing___Optional[typing___Iterable[mlagents_envs___communicator_objects___agent_info_pb2___AgentInfoProto]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UnityRLOutputProto.ListAgentInfoProto: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"value"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> None: ...

    class AgentInfosEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> UnityRLOutputProto.ListAgentInfoProto: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[UnityRLOutputProto.ListAgentInfoProto] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UnityRLOutputProto.AgentInfosEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"value"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    side_channel = ... # type: builtin___bytes

    @property
    def agentInfos(self) -> typing___MutableMapping[typing___Text, UnityRLOutputProto.ListAgentInfoProto]: ...

    def __init__(self,
        *,
        agentInfos : typing___Optional[typing___Mapping[typing___Text, UnityRLOutputProto.ListAgentInfoProto]] = None,
        side_channel : typing___Optional[builtin___bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> UnityRLOutputProto: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"agentInfos",u"side_channel"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"agentInfos",b"agentInfos",u"side_channel",b"side_channel"]) -> None: ...
