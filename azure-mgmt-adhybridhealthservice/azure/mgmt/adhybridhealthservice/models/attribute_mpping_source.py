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


class AttributeMppingSource(Model):
    """The attribute mapping source.

    :param source_attribute: The source attribute.
    :type source_attribute: list[str]
    :param dn_part: The value for dn part.
    :type dn_part: int
    :param script_context: The script context.
    :type script_context: str
    :param constant_value: The constant value.
    :type constant_value: str
    """

    _attribute_map = {
        'source_attribute': {'key': 'sourceAttribute', 'type': '[str]'},
        'dn_part': {'key': 'dnPart', 'type': 'int'},
        'script_context': {'key': 'scriptContext', 'type': 'str'},
        'constant_value': {'key': 'constantValue', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AttributeMppingSource, self).__init__(**kwargs)
        self.source_attribute = kwargs.get('source_attribute', None)
        self.dn_part = kwargs.get('dn_part', None)
        self.script_context = kwargs.get('script_context', None)
        self.constant_value = kwargs.get('constant_value', None)
