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


class X12EnvelopeOverride(Model):
    """The X12 envelope override settings.

    All required parameters must be populated in order to send to Azure.

    :param target_namespace: Required. The target namespace on which this
     envelope settings has to be applied.
    :type target_namespace: str
    :param protocol_version: Required. The protocol version on which this
     envelope settings has to be applied.
    :type protocol_version: str
    :param message_id: Required. The message id on which this envelope
     settings has to be applied.
    :type message_id: str
    :param responsible_agency_code: Required. The responsible agency code.
    :type responsible_agency_code: str
    :param header_version: Required. The header version.
    :type header_version: str
    :param sender_application_id: Required. The sender application id.
    :type sender_application_id: str
    :param receiver_application_id: Required. The receiver application id.
    :type receiver_application_id: str
    :param functional_identifier_code: The functional identifier code.
    :type functional_identifier_code: str
    :param date_format: Required. The date format. Possible values include:
     'NotSpecified', 'CCYYMMDD', 'YYMMDD'
    :type date_format: str or ~azure.mgmt.logic.models.X12DateFormat
    :param time_format: Required. The time format. Possible values include:
     'NotSpecified', 'HHMM', 'HHMMSS', 'HHMMSSdd', 'HHMMSSd'
    :type time_format: str or ~azure.mgmt.logic.models.X12TimeFormat
    """

    _validation = {
        'target_namespace': {'required': True},
        'protocol_version': {'required': True},
        'message_id': {'required': True},
        'responsible_agency_code': {'required': True},
        'header_version': {'required': True},
        'sender_application_id': {'required': True},
        'receiver_application_id': {'required': True},
        'date_format': {'required': True},
        'time_format': {'required': True},
    }

    _attribute_map = {
        'target_namespace': {'key': 'targetNamespace', 'type': 'str'},
        'protocol_version': {'key': 'protocolVersion', 'type': 'str'},
        'message_id': {'key': 'messageId', 'type': 'str'},
        'responsible_agency_code': {'key': 'responsibleAgencyCode', 'type': 'str'},
        'header_version': {'key': 'headerVersion', 'type': 'str'},
        'sender_application_id': {'key': 'senderApplicationId', 'type': 'str'},
        'receiver_application_id': {'key': 'receiverApplicationId', 'type': 'str'},
        'functional_identifier_code': {'key': 'functionalIdentifierCode', 'type': 'str'},
        'date_format': {'key': 'dateFormat', 'type': 'str'},
        'time_format': {'key': 'timeFormat', 'type': 'str'},
    }

    def __init__(self, *, target_namespace: str, protocol_version: str, message_id: str, responsible_agency_code: str, header_version: str, sender_application_id: str, receiver_application_id: str, date_format, time_format, functional_identifier_code: str=None, **kwargs) -> None:
        super(X12EnvelopeOverride, self).__init__(**kwargs)
        self.target_namespace = target_namespace
        self.protocol_version = protocol_version
        self.message_id = message_id
        self.responsible_agency_code = responsible_agency_code
        self.header_version = header_version
        self.sender_application_id = sender_application_id
        self.receiver_application_id = receiver_application_id
        self.functional_identifier_code = functional_identifier_code
        self.date_format = date_format
        self.time_format = time_format
