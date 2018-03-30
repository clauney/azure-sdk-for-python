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


class AvailableProvidersListParameters(Model):
    """Constraints that determine the list of available Internet service
    providers.

    :param azure_locations: A list of Azure regions.
    :type azure_locations: list[str]
    :param country: The country for available providers list.
    :type country: str
    :param state: The state for available providers list.
    :type state: str
    :param city: The city or town for available providers list.
    :type city: str
    """

    _attribute_map = {
        'azure_locations': {'key': 'azureLocations', 'type': '[str]'},
        'country': {'key': 'country', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'city': {'key': 'city', 'type': 'str'},
    }

    def __init__(self, *, azure_locations=None, country: str=None, state: str=None, city: str=None, **kwargs) -> None:
        super(AvailableProvidersListParameters, self).__init__(**kwargs)
        self.azure_locations = azure_locations
        self.country = country
        self.state = state
        self.city = city