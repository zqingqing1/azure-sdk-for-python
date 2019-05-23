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


class DistributedNodesInfo(Model):
    """This is used to represent the various nodes of the distributed container.

    :param node_name: Name of the node under a distributed container.
    :type node_name: str
    :param status: Status of this Node.
     Failed | Succeeded
    :type status: str
    :param error_detail: Error Details if the Status is non-success.
    :type error_detail: ~azure.mgmt.recoveryservicesbackup.models.ErrorDetail
    """

    _attribute_map = {
        'node_name': {'key': 'nodeName', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'error_detail': {'key': 'errorDetail', 'type': 'ErrorDetail'},
    }

    def __init__(self, **kwargs):
        super(DistributedNodesInfo, self).__init__(**kwargs)
        self.node_name = kwargs.get('node_name', None)
        self.status = kwargs.get('status', None)
        self.error_detail = kwargs.get('error_detail', None)