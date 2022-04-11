# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import platform_pb2 as platform__pb2


class PlatformStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.broadcastStateTransition = channel.unary_unary(
                '/org.dash.platform.dapi.v0.Platform/broadcastStateTransition',
                request_serializer=platform__pb2.BroadcastStateTransitionRequest.SerializeToString,
                response_deserializer=platform__pb2.BroadcastStateTransitionResponse.FromString,
                )
        self.getIdentity = channel.unary_unary(
                '/org.dash.platform.dapi.v0.Platform/getIdentity',
                request_serializer=platform__pb2.GetIdentityRequest.SerializeToString,
                response_deserializer=platform__pb2.GetIdentityResponse.FromString,
                )
        self.getDataContract = channel.unary_unary(
                '/org.dash.platform.dapi.v0.Platform/getDataContract',
                request_serializer=platform__pb2.GetDataContractRequest.SerializeToString,
                response_deserializer=platform__pb2.GetDataContractResponse.FromString,
                )
        self.getDocuments = channel.unary_unary(
                '/org.dash.platform.dapi.v0.Platform/getDocuments',
                request_serializer=platform__pb2.GetDocumentsRequest.SerializeToString,
                response_deserializer=platform__pb2.GetDocumentsResponse.FromString,
                )
        self.getIdentitiesByPublicKeyHashes = channel.unary_unary(
                '/org.dash.platform.dapi.v0.Platform/getIdentitiesByPublicKeyHashes',
                request_serializer=platform__pb2.GetIdentitiesByPublicKeyHashesRequest.SerializeToString,
                response_deserializer=platform__pb2.GetIdentitiesByPublicKeyHashesResponse.FromString,
                )
        self.getIdentityIdsByPublicKeyHashes = channel.unary_unary(
                '/org.dash.platform.dapi.v0.Platform/getIdentityIdsByPublicKeyHashes',
                request_serializer=platform__pb2.GetIdentityIdsByPublicKeyHashesRequest.SerializeToString,
                response_deserializer=platform__pb2.GetIdentityIdsByPublicKeyHashesResponse.FromString,
                )
        self.waitForStateTransitionResult = channel.unary_unary(
                '/org.dash.platform.dapi.v0.Platform/waitForStateTransitionResult',
                request_serializer=platform__pb2.WaitForStateTransitionResultRequest.SerializeToString,
                response_deserializer=platform__pb2.WaitForStateTransitionResultResponse.FromString,
                )
        self.getConsensusParams = channel.unary_unary(
                '/org.dash.platform.dapi.v0.Platform/getConsensusParams',
                request_serializer=platform__pb2.GetConsensusParamsRequest.SerializeToString,
                response_deserializer=platform__pb2.GetConsensusParamsResponse.FromString,
                )


class PlatformServicer(object):
    """Missing associated documentation comment in .proto file."""

    def broadcastStateTransition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getIdentity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getDataContract(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getDocuments(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getIdentitiesByPublicKeyHashes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getIdentityIdsByPublicKeyHashes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def waitForStateTransitionResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getConsensusParams(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PlatformServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'broadcastStateTransition': grpc.unary_unary_rpc_method_handler(
                    servicer.broadcastStateTransition,
                    request_deserializer=platform__pb2.BroadcastStateTransitionRequest.FromString,
                    response_serializer=platform__pb2.BroadcastStateTransitionResponse.SerializeToString,
            ),
            'getIdentity': grpc.unary_unary_rpc_method_handler(
                    servicer.getIdentity,
                    request_deserializer=platform__pb2.GetIdentityRequest.FromString,
                    response_serializer=platform__pb2.GetIdentityResponse.SerializeToString,
            ),
            'getDataContract': grpc.unary_unary_rpc_method_handler(
                    servicer.getDataContract,
                    request_deserializer=platform__pb2.GetDataContractRequest.FromString,
                    response_serializer=platform__pb2.GetDataContractResponse.SerializeToString,
            ),
            'getDocuments': grpc.unary_unary_rpc_method_handler(
                    servicer.getDocuments,
                    request_deserializer=platform__pb2.GetDocumentsRequest.FromString,
                    response_serializer=platform__pb2.GetDocumentsResponse.SerializeToString,
            ),
            'getIdentitiesByPublicKeyHashes': grpc.unary_unary_rpc_method_handler(
                    servicer.getIdentitiesByPublicKeyHashes,
                    request_deserializer=platform__pb2.GetIdentitiesByPublicKeyHashesRequest.FromString,
                    response_serializer=platform__pb2.GetIdentitiesByPublicKeyHashesResponse.SerializeToString,
            ),
            'getIdentityIdsByPublicKeyHashes': grpc.unary_unary_rpc_method_handler(
                    servicer.getIdentityIdsByPublicKeyHashes,
                    request_deserializer=platform__pb2.GetIdentityIdsByPublicKeyHashesRequest.FromString,
                    response_serializer=platform__pb2.GetIdentityIdsByPublicKeyHashesResponse.SerializeToString,
            ),
            'waitForStateTransitionResult': grpc.unary_unary_rpc_method_handler(
                    servicer.waitForStateTransitionResult,
                    request_deserializer=platform__pb2.WaitForStateTransitionResultRequest.FromString,
                    response_serializer=platform__pb2.WaitForStateTransitionResultResponse.SerializeToString,
            ),
            'getConsensusParams': grpc.unary_unary_rpc_method_handler(
                    servicer.getConsensusParams,
                    request_deserializer=platform__pb2.GetConsensusParamsRequest.FromString,
                    response_serializer=platform__pb2.GetConsensusParamsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'org.dash.platform.dapi.v0.Platform', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Platform(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def broadcastStateTransition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.dash.platform.dapi.v0.Platform/broadcastStateTransition',
            platform__pb2.BroadcastStateTransitionRequest.SerializeToString,
            platform__pb2.BroadcastStateTransitionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getIdentity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.dash.platform.dapi.v0.Platform/getIdentity',
            platform__pb2.GetIdentityRequest.SerializeToString,
            platform__pb2.GetIdentityResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getDataContract(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.dash.platform.dapi.v0.Platform/getDataContract',
            platform__pb2.GetDataContractRequest.SerializeToString,
            platform__pb2.GetDataContractResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getDocuments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.dash.platform.dapi.v0.Platform/getDocuments',
            platform__pb2.GetDocumentsRequest.SerializeToString,
            platform__pb2.GetDocumentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getIdentitiesByPublicKeyHashes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.dash.platform.dapi.v0.Platform/getIdentitiesByPublicKeyHashes',
            platform__pb2.GetIdentitiesByPublicKeyHashesRequest.SerializeToString,
            platform__pb2.GetIdentitiesByPublicKeyHashesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getIdentityIdsByPublicKeyHashes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.dash.platform.dapi.v0.Platform/getIdentityIdsByPublicKeyHashes',
            platform__pb2.GetIdentityIdsByPublicKeyHashesRequest.SerializeToString,
            platform__pb2.GetIdentityIdsByPublicKeyHashesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def waitForStateTransitionResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.dash.platform.dapi.v0.Platform/waitForStateTransitionResult',
            platform__pb2.WaitForStateTransitionResultRequest.SerializeToString,
            platform__pb2.WaitForStateTransitionResultResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getConsensusParams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.dash.platform.dapi.v0.Platform/getConsensusParams',
            platform__pb2.GetConsensusParamsRequest.SerializeToString,
            platform__pb2.GetConsensusParamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
