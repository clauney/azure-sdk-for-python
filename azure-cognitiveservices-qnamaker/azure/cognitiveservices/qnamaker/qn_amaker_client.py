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

from msrest.service_client import SDKClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from msrest.pipeline import ClientRawResponse
from . import models


class QnAMakerClientConfiguration(Configuration):
    """Configuration for QnAMakerClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param endpoint: Supported Cognitive Services endpoints (protocol and
     hostname, for example: https://westus.api.cognitive.microsoft.com).
    :type endpoint: str
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    """

    def __init__(
            self, endpoint, credentials):

        if endpoint is None:
            raise ValueError("Parameter 'endpoint' must not be None.")
        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        base_url = '{Endpoint}/qnamaker/v4.0'

        super(QnAMakerClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-cognitiveservices-qnamaker/{}'.format(VERSION))

        self.endpoint = endpoint
        self.credentials = credentials


class QnAMakerClient(SDKClient):
    """An API for QnAMaker Service

    :ivar config: Configuration for client.
    :vartype config: QnAMakerClientConfiguration

    :param endpoint: Supported Cognitive Services endpoints (protocol and
     hostname, for example: https://westus.api.cognitive.microsoft.com).
    :type endpoint: str
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    """

    def __init__(
            self, endpoint, credentials):

        self.config = QnAMakerClientConfiguration(endpoint, credentials)
        super(QnAMakerClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '4.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)


    def get_endpoint_keys(
            self, custom_headers=None, raw=False, **operation_config):
        """Gets endpoint keys for an endpoint.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: EndpointKeysDTO or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.qnamaker.models.EndpointKeysDTO or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.qnamaker.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_endpoint_keys.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('EndpointKeysDTO', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_endpoint_keys.metadata = {'url': '/endpointkeys'}

    def refresh_endpoint_keys(
            self, key_type, custom_headers=None, raw=False, **operation_config):
        """Re-generates an endpoint key.

        :param key_type: type of Key
        :type key_type: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: EndpointKeysDTO or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.qnamaker.models.EndpointKeysDTO or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.qnamaker.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.refresh_endpoint_keys.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'keyType': self._serialize.url("key_type", key_type, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('EndpointKeysDTO', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    refresh_endpoint_keys.metadata = {'url': '/endpointkeys/{keyType}'}

    def download_alterations(
            self, custom_headers=None, raw=False, **operation_config):
        """Download alterations from runtime.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: WordAlterationsDTO or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.qnamaker.models.WordAlterationsDTO or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.qnamaker.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.download_alterations.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('WordAlterationsDTO', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    download_alterations.metadata = {'url': '/alterations'}

    def replace_alterations(
            self, word_alterations, custom_headers=None, raw=False, **operation_config):
        """Replace alterations data.

        :param word_alterations: Collection of word alterations.
        :type word_alterations:
         list[~azure.cognitiveservices.qnamaker.models.AlterationsDTO]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.qnamaker.models.ErrorResponseException>`
        """
        word_alterations1 = models.WordAlterationsDTO(word_alterations=word_alterations)

        # Construct URL
        url = self.replace_alterations.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(word_alterations1, 'WordAlterationsDTO')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.ErrorResponseException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    replace_alterations.metadata = {'url': '/alterations'}

    def get_knowledgebasesforuser(
            self, custom_headers=None, raw=False, **operation_config):
        """Gets all knowledgebases for a user.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: KnowledgebasesDTO or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.qnamaker.models.KnowledgebasesDTO or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.qnamaker.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_knowledgebasesforuser.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('KnowledgebasesDTO', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_knowledgebasesforuser.metadata = {'url': '/knowledgebases'}

    def get_operation_details(
            self, operation_id, custom_headers=None, raw=False, **operation_config):
        """Gets details of a specific long running operation.

        :param operation_id: Operation id.
        :type operation_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Operation or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.qnamaker.models.Operation or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.qnamaker.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_operation_details.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'operationId': self._serialize.url("operation_id", operation_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('Operation', response)
            header_dict = {
                'RetryAfter': 'int',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    get_operation_details.metadata = {'url': '/operations/{operationId}'}

    def get_knowledgebase_details(
            self, kb_id, custom_headers=None, raw=False, **operation_config):
        """Gets details of a specific knowledgebase.

        :param kb_id: Knowledgebase id.
        :type kb_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: KnowledgebaseDTO or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.qnamaker.models.KnowledgebaseDTO or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.qnamaker.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_knowledgebase_details.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'kbId': self._serialize.url("kb_id", kb_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('KnowledgebaseDTO', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_knowledgebase_details.metadata = {'url': '/knowledgebases/{kbId}'}

    def delete_knowledgebase(
            self, kb_id, custom_headers=None, raw=False, **operation_config):
        """Deletes the knowledgebase and all its data.

        :param kb_id: Knowledgebase id.
        :type kb_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.qnamaker.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete_knowledgebase.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'kbId': self._serialize.url("kb_id", kb_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.ErrorResponseException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete_knowledgebase.metadata = {'url': '/knowledgebases/{kbId}'}

    def publish_knowledgebase(
            self, kb_id, custom_headers=None, raw=False, **operation_config):
        """Publishes all changes in test index of a knowledgebase to its prod
        index.

        :param kb_id: Knowledgebase id.
        :type kb_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.qnamaker.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.publish_knowledgebase.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'kbId': self._serialize.url("kb_id", kb_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.ErrorResponseException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    publish_knowledgebase.metadata = {'url': '/knowledgebases/{kbId}'}

    def replace_knowledgebase(
            self, kb_id, qn_alist, custom_headers=None, raw=False, **operation_config):
        """Replace knowledgebase contents.

        :param kb_id: Knowledgebase id.
        :type kb_id: str
        :param qn_alist: List of Q-A (QnADTO) to be added to the
         knowledgebase. Q-A Ids are assigned by the service and should be
         omitted.
        :type qn_alist: list[~azure.cognitiveservices.qnamaker.models.QnADTO]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.qnamaker.models.ErrorResponseException>`
        """
        replace_kb = models.ReplaceKbDTO(qn_alist=qn_alist)

        # Construct URL
        url = self.replace_knowledgebase.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'kbId': self._serialize.url("kb_id", kb_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(replace_kb, 'ReplaceKbDTO')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.ErrorResponseException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    replace_knowledgebase.metadata = {'url': '/knowledgebases/{kbId}'}

    def update_knowledgebase(
            self, kb_id, update_kb, custom_headers=None, raw=False, **operation_config):
        """Asynchronous operation to modify a knowledgebase.

        :param kb_id: Knowledgebase id.
        :type kb_id: str
        :param update_kb: Post body of the request.
        :type update_kb:
         ~azure.cognitiveservices.qnamaker.models.UpdateKbOperationDTO
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Operation or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.qnamaker.models.Operation or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.qnamaker.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.update_knowledgebase.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'kbId': self._serialize.url("kb_id", kb_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(update_kb, 'UpdateKbOperationDTO')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [202]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 202:
            deserialized = self._deserialize('Operation', response)
            header_dict = {
                'Location': 'str',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    update_knowledgebase.metadata = {'url': '/knowledgebases/{kbId}'}

    def create_knowledgebase(
            self, create_kb_payload, custom_headers=None, raw=False, **operation_config):
        """Asynchronous operation to create a new knowledgebase.

        :param create_kb_payload: Post body of the request.
        :type create_kb_payload:
         ~azure.cognitiveservices.qnamaker.models.CreateKbDTO
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Operation or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.qnamaker.models.Operation or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.qnamaker.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.create_knowledgebase.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(create_kb_payload, 'CreateKbDTO')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [202]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 202:
            deserialized = self._deserialize('Operation', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_knowledgebase.metadata = {'url': '/knowledgebases/create'}

    def download_knowledgebase(
            self, kb_id, environment, custom_headers=None, raw=False, **operation_config):
        """Download the knowledgebase.

        :param kb_id: Knowledgebase id.
        :type kb_id: str
        :param environment: Specifies whether environment is Test or Prod.
         Possible values include: 'Prod', 'Test'
        :type environment: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: QnADocumentsDTO or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.qnamaker.models.QnADocumentsDTO or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.qnamaker.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.download_knowledgebase.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'kbId': self._serialize.url("kb_id", kb_id, 'str'),
            'environment': self._serialize.url("environment", environment, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('QnADocumentsDTO', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    download_knowledgebase.metadata = {'url': '/knowledgebases/{kbId}/{environment}/qna'}
