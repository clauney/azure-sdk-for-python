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

from msrest.serialization import Model


class Principal(Model):
    """Deny assignment principal.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Object ID of the Azure AD principal (user, group, or service
     principal) to which the deny assignment applies. An empty guid
     '00000000-0000-0000-0000-000000000000' as principal id and principal type
     as 'Everyone' represents all users, groups and service principals.
    :vartype id: str
    :ivar type: Type of object represented by principal id (user, group, or
     service principal). An empty guid '00000000-0000-0000-0000-000000000000'
     as principal id and principal type as 'Everyone' represents all users,
     groups and service principals.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(Principal, self).__init__(**kwargs)
        self.id = None
        self.type = None
