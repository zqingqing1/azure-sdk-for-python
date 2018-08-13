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


class VersionSpec(Model):
    """The version properties.

    :param friendly_name: The friendly name
    :type friendly_name: str
    :param display_name: The display name
    :type display_name: str
    :param is_default: Whether or not the version is the default version.
    :type is_default: str
    :param component_versions: The component version property.
    :type component_versions: dict[str, str]
    """

    _attribute_map = {
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'is_default': {'key': 'isDefault', 'type': 'str'},
        'component_versions': {'key': 'componentVersions', 'type': '{str}'},
    }

    def __init__(self, *, friendly_name: str=None, display_name: str=None, is_default: str=None, component_versions=None, **kwargs) -> None:
        super(VersionSpec, self).__init__(**kwargs)
        self.friendly_name = friendly_name
        self.display_name = display_name
        self.is_default = is_default
        self.component_versions = component_versions
