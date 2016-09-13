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


class X12EnvelopeSettings(Model):
    """X12EnvelopeSettings.

    :param control_standards_id: The controls standards id.
    :type control_standards_id: int
    :param use_control_standards_id_as_repetition_character: The value
     indicating whether to use control standards id as repetition character.
    :type use_control_standards_id_as_repetition_character: bool
    :param sender_application_id: The sender application id.
    :type sender_application_id: str
    :param receiver_application_id: The receiver application id.
    :type receiver_application_id: str
    :param control_version_number: The control version number.
    :type control_version_number: str
    :param interchange_control_number_lower_bound: The interchange  control
     number lower bound.
    :type interchange_control_number_lower_bound: int
    :param interchange_control_number_upper_bound: The interchange  control
     number upper bound.
    :type interchange_control_number_upper_bound: int
    :param rollover_interchange_control_number: The value indicating whether
     to rollover interchange control number.
    :type rollover_interchange_control_number: bool
    :param enable_default_group_headers: The value indicating whether to
     enable default group headers.
    :type enable_default_group_headers: bool
    :param functional_group_id: The functional group id.
    :type functional_group_id: str
    :param group_control_number_lower_bound: The group control number lower
     bound.
    :type group_control_number_lower_bound: int
    :param group_control_number_upper_bound: The group control number upper
     bound.
    :type group_control_number_upper_bound: int
    :param rollover_group_control_number: The value indicating whether to
     rollover group control number.
    :type rollover_group_control_number: bool
    :param group_header_agency_code: The group header agency code.
    :type group_header_agency_code: str
    :param group_header_version: The group header version.
    :type group_header_version: str
    :param transaction_set_control_number_lower_bound: The transaction set
     control number lower bound.
    :type transaction_set_control_number_lower_bound: int
    :param transaction_set_control_number_upper_bound: The transaction set
     control number upper bound.
    :type transaction_set_control_number_upper_bound: int
    :param rollover_transaction_set_control_number: The value indicating
     whether to rollover transaction set control number.
    :type rollover_transaction_set_control_number: bool
    :param transaction_set_control_number_prefix: The transaction set control
     number prefix.
    :type transaction_set_control_number_prefix: str
    :param transaction_set_control_number_suffix: The transaction set control
     number suffix.
    :type transaction_set_control_number_suffix: str
    :param overwrite_existing_transaction_set_control_number: The value
     indicating whether to overwrite existing transaction set control number.
    :type overwrite_existing_transaction_set_control_number: bool
    :param group_header_date_format: The group header date format. Possible
     values include: 'NotSpecified', 'CCYYMMDD', 'YYMMDD'
    :type group_header_date_format: str or :class:`X12DateFormat
     <azure.mgmt.logic.models.X12DateFormat>`
    :param group_header_time_format: The group header time format. Possible
     values include: 'NotSpecified', 'HHMM', 'HHMMSS', 'HHMMSSdd', 'HHMMSSd'
    :type group_header_time_format: str or :class:`X12TimeFormat
     <azure.mgmt.logic.models.X12TimeFormat>`
    :param usage_indicator: The usage indicator. Possible values include:
     'NotSpecified', 'Test', 'Information', 'Production'
    :type usage_indicator: str or :class:`UsageIndicator
     <azure.mgmt.logic.models.UsageIndicator>`
    """ 

    _attribute_map = {
        'control_standards_id': {'key': 'controlStandardsId', 'type': 'int'},
        'use_control_standards_id_as_repetition_character': {'key': 'useControlStandardsIdAsRepetitionCharacter', 'type': 'bool'},
        'sender_application_id': {'key': 'senderApplicationId', 'type': 'str'},
        'receiver_application_id': {'key': 'receiverApplicationId', 'type': 'str'},
        'control_version_number': {'key': 'controlVersionNumber', 'type': 'str'},
        'interchange_control_number_lower_bound': {'key': 'interchangeControlNumberLowerBound', 'type': 'int'},
        'interchange_control_number_upper_bound': {'key': 'interchangeControlNumberUpperBound', 'type': 'int'},
        'rollover_interchange_control_number': {'key': 'rolloverInterchangeControlNumber', 'type': 'bool'},
        'enable_default_group_headers': {'key': 'enableDefaultGroupHeaders', 'type': 'bool'},
        'functional_group_id': {'key': 'functionalGroupId', 'type': 'str'},
        'group_control_number_lower_bound': {'key': 'groupControlNumberLowerBound', 'type': 'int'},
        'group_control_number_upper_bound': {'key': 'groupControlNumberUpperBound', 'type': 'int'},
        'rollover_group_control_number': {'key': 'rolloverGroupControlNumber', 'type': 'bool'},
        'group_header_agency_code': {'key': 'groupHeaderAgencyCode', 'type': 'str'},
        'group_header_version': {'key': 'groupHeaderVersion', 'type': 'str'},
        'transaction_set_control_number_lower_bound': {'key': 'transactionSetControlNumberLowerBound', 'type': 'int'},
        'transaction_set_control_number_upper_bound': {'key': 'transactionSetControlNumberUpperBound', 'type': 'int'},
        'rollover_transaction_set_control_number': {'key': 'rolloverTransactionSetControlNumber', 'type': 'bool'},
        'transaction_set_control_number_prefix': {'key': 'transactionSetControlNumberPrefix', 'type': 'str'},
        'transaction_set_control_number_suffix': {'key': 'transactionSetControlNumberSuffix', 'type': 'str'},
        'overwrite_existing_transaction_set_control_number': {'key': 'overwriteExistingTransactionSetControlNumber', 'type': 'bool'},
        'group_header_date_format': {'key': 'groupHeaderDateFormat', 'type': 'X12DateFormat'},
        'group_header_time_format': {'key': 'groupHeaderTimeFormat', 'type': 'X12TimeFormat'},
        'usage_indicator': {'key': 'usageIndicator', 'type': 'UsageIndicator'},
    }

    def __init__(self, control_standards_id=None, use_control_standards_id_as_repetition_character=None, sender_application_id=None, receiver_application_id=None, control_version_number=None, interchange_control_number_lower_bound=None, interchange_control_number_upper_bound=None, rollover_interchange_control_number=None, enable_default_group_headers=None, functional_group_id=None, group_control_number_lower_bound=None, group_control_number_upper_bound=None, rollover_group_control_number=None, group_header_agency_code=None, group_header_version=None, transaction_set_control_number_lower_bound=None, transaction_set_control_number_upper_bound=None, rollover_transaction_set_control_number=None, transaction_set_control_number_prefix=None, transaction_set_control_number_suffix=None, overwrite_existing_transaction_set_control_number=None, group_header_date_format=None, group_header_time_format=None, usage_indicator=None):
        self.control_standards_id = control_standards_id
        self.use_control_standards_id_as_repetition_character = use_control_standards_id_as_repetition_character
        self.sender_application_id = sender_application_id
        self.receiver_application_id = receiver_application_id
        self.control_version_number = control_version_number
        self.interchange_control_number_lower_bound = interchange_control_number_lower_bound
        self.interchange_control_number_upper_bound = interchange_control_number_upper_bound
        self.rollover_interchange_control_number = rollover_interchange_control_number
        self.enable_default_group_headers = enable_default_group_headers
        self.functional_group_id = functional_group_id
        self.group_control_number_lower_bound = group_control_number_lower_bound
        self.group_control_number_upper_bound = group_control_number_upper_bound
        self.rollover_group_control_number = rollover_group_control_number
        self.group_header_agency_code = group_header_agency_code
        self.group_header_version = group_header_version
        self.transaction_set_control_number_lower_bound = transaction_set_control_number_lower_bound
        self.transaction_set_control_number_upper_bound = transaction_set_control_number_upper_bound
        self.rollover_transaction_set_control_number = rollover_transaction_set_control_number
        self.transaction_set_control_number_prefix = transaction_set_control_number_prefix
        self.transaction_set_control_number_suffix = transaction_set_control_number_suffix
        self.overwrite_existing_transaction_set_control_number = overwrite_existing_transaction_set_control_number
        self.group_header_date_format = group_header_date_format
        self.group_header_time_format = group_header_time_format
        self.usage_indicator = usage_indicator