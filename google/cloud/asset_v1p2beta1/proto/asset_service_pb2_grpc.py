# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.asset_v1p2beta1.proto import (
    asset_service_pb2 as google_dot_cloud_dot_asset__v1p2beta1_dot_proto_dot_asset__service__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class AssetServiceStub(object):
    """Asset service definition.
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.CreateFeed = channel.unary_unary(
            "/google.cloud.asset.v1p2beta1.AssetService/CreateFeed",
            request_serializer=google_dot_cloud_dot_asset__v1p2beta1_dot_proto_dot_asset__service__pb2.CreateFeedRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_asset__v1p2beta1_dot_proto_dot_asset__service__pb2.Feed.FromString,
        )
        self.GetFeed = channel.unary_unary(
            "/google.cloud.asset.v1p2beta1.AssetService/GetFeed",
            request_serializer=google_dot_cloud_dot_asset__v1p2beta1_dot_proto_dot_asset__service__pb2.GetFeedRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_asset__v1p2beta1_dot_proto_dot_asset__service__pb2.Feed.FromString,
        )
        self.ListFeeds = channel.unary_unary(
            "/google.cloud.asset.v1p2beta1.AssetService/ListFeeds",
            request_serializer=google_dot_cloud_dot_asset__v1p2beta1_dot_proto_dot_asset__service__pb2.ListFeedsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_asset__v1p2beta1_dot_proto_dot_asset__service__pb2.ListFeedsResponse.FromString,
        )
        self.UpdateFeed = channel.unary_unary(
            "/google.cloud.asset.v1p2beta1.AssetService/UpdateFeed",
            request_serializer=google_dot_cloud_dot_asset__v1p2beta1_dot_proto_dot_asset__service__pb2.UpdateFeedRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_asset__v1p2beta1_dot_proto_dot_asset__service__pb2.Feed.FromString,
        )
        self.DeleteFeed = channel.unary_unary(
            "/google.cloud.asset.v1p2beta1.AssetService/DeleteFeed",
            request_serializer=google_dot_cloud_dot_asset__v1p2beta1_dot_proto_dot_asset__service__pb2.DeleteFeedRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class AssetServiceServicer(object):
    """Asset service definition.
  """

    def CreateFeed(self, request, context):
        """Creates a feed in a parent project/folder/organization to listen to its
    asset updates.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetFeed(self, request, context):
        """Gets details about an asset feed.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListFeeds(self, request, context):
        """Lists all asset feeds in a parent project/folder/organization.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateFeed(self, request, context):
        """Updates an asset feed configuration.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteFeed(self, request, context):
        """Deletes an asset feed.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_AssetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateFeed": grpc.unary_unary_rpc_method_handler(
            servicer.CreateFeed,
            request_deserializer=google_dot_cloud_dot_asset__v1p2beta1_dot_proto_dot_asset__service__pb2.CreateFeedRequest.FromString,
            response_serializer=google_dot_cloud_dot_asset__v1p2beta1_dot_proto_dot_asset__service__pb2.Feed.SerializeToString,
        ),
        "GetFeed": grpc.unary_unary_rpc_method_handler(
            servicer.GetFeed,
            request_deserializer=google_dot_cloud_dot_asset__v1p2beta1_dot_proto_dot_asset__service__pb2.GetFeedRequest.FromString,
            response_serializer=google_dot_cloud_dot_asset__v1p2beta1_dot_proto_dot_asset__service__pb2.Feed.SerializeToString,
        ),
        "ListFeeds": grpc.unary_unary_rpc_method_handler(
            servicer.ListFeeds,
            request_deserializer=google_dot_cloud_dot_asset__v1p2beta1_dot_proto_dot_asset__service__pb2.ListFeedsRequest.FromString,
            response_serializer=google_dot_cloud_dot_asset__v1p2beta1_dot_proto_dot_asset__service__pb2.ListFeedsResponse.SerializeToString,
        ),
        "UpdateFeed": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateFeed,
            request_deserializer=google_dot_cloud_dot_asset__v1p2beta1_dot_proto_dot_asset__service__pb2.UpdateFeedRequest.FromString,
            response_serializer=google_dot_cloud_dot_asset__v1p2beta1_dot_proto_dot_asset__service__pb2.Feed.SerializeToString,
        ),
        "DeleteFeed": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteFeed,
            request_deserializer=google_dot_cloud_dot_asset__v1p2beta1_dot_proto_dot_asset__service__pb2.DeleteFeedRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.asset.v1p2beta1.AssetService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
