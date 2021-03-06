# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .proxy_only_resource_py3 import ProxyOnlyResource


class RelayServiceConnectionEntity(ProxyOnlyResource):
    """Hybrid Connection for an App Service app.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param entity_name:
    :type entity_name: str
    :param entity_connection_string:
    :type entity_connection_string: str
    :param resource_type:
    :type resource_type: str
    :param resource_connection_string:
    :type resource_connection_string: str
    :param hostname:
    :type hostname: str
    :param port:
    :type port: int
    :param biztalk_uri:
    :type biztalk_uri: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'entity_name': {'key': 'properties.entityName', 'type': 'str'},
        'entity_connection_string': {'key': 'properties.entityConnectionString', 'type': 'str'},
        'resource_type': {'key': 'properties.resourceType', 'type': 'str'},
        'resource_connection_string': {'key': 'properties.resourceConnectionString', 'type': 'str'},
        'hostname': {'key': 'properties.hostname', 'type': 'str'},
        'port': {'key': 'properties.port', 'type': 'int'},
        'biztalk_uri': {'key': 'properties.biztalkUri', 'type': 'str'},
    }

    def __init__(self, *, kind: str=None, entity_name: str=None, entity_connection_string: str=None, resource_type: str=None, resource_connection_string: str=None, hostname: str=None, port: int=None, biztalk_uri: str=None, **kwargs) -> None:
        super(RelayServiceConnectionEntity, self).__init__(kind=kind, **kwargs)
        self.entity_name = entity_name
        self.entity_connection_string = entity_connection_string
        self.resource_type = resource_type
        self.resource_connection_string = resource_connection_string
        self.hostname = hostname
        self.port = port
        self.biztalk_uri = biztalk_uri
