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


class Agent(Model):
    """The agent details.

    :param tenant_id: The tenant Id.
    :type tenant_id: str
    :param machine_id: The machine Id.
    :type machine_id: str
    :param credential: The agent credential details.
    :type credential:
     list[~azure.mgmt.adhybridhealthservice.models.Credential]
    :param machine_name: The machine name.
    :type machine_name: str
    :param agent_version: The agent version.
    :type agent_version: str
    :param created_date: The date and time, in UTC, when the agent was
     created.
    :type created_date: datetime
    :param key:  The connector hash key.
    :type key: str
    """

    _attribute_map = {
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'machine_id': {'key': 'machineId', 'type': 'str'},
        'credential': {'key': 'credential', 'type': '[Credential]'},
        'machine_name': {'key': 'machineName', 'type': 'str'},
        'agent_version': {'key': 'agentVersion', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'key': {'key': 'key', 'type': 'str'},
    }

    def __init__(self, *, tenant_id: str=None, machine_id: str=None, credential=None, machine_name: str=None, agent_version: str=None, created_date=None, key: str=None, **kwargs) -> None:
        super(Agent, self).__init__(**kwargs)
        self.tenant_id = tenant_id
        self.machine_id = machine_id
        self.credential = credential
        self.machine_name = machine_name
        self.agent_version = agent_version
        self.created_date = created_date
        self.key = key
