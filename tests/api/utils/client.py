# Copyright (c) 2014 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from cafe.engine.http import client


class AuthClient(client.HTTPClient):

    """Client Objects for Auth call."""

    def __init__(self):
        super(AuthClient, self).__init__()

        self.default_headers['Content-Type'] = 'application/json'
        self.default_headers['Accept'] = 'application/json'

    def authenticate_user(self, auth_url, user_name, api_key):
        """Authenticate using api_key

        TODO (malini-kamalambal): Support getting token with password (or)
                                  api key.
        """
        request_body = {
            'auth': {
                'RAX-KSKEY:apiKeyCredentials': {
                    'username': user_name,
                    'apiKey': api_key
                },
            },
        }
        request_body = json.dumps(request_body)
        url = auth_url + '/tokens'

        response = self.request('POST', url, data=request_body)
        token = response.json()['access']['token']['id']
        tenant_id = response.json()['access']['token']['tenant']['id']
        return token, tenant_id


class DoryClient(client.AutoMarshallingHTTPClient):

    """Client objects for all the Dory api calls."""

    def __init__(self, url, auth_token, tenant_id, serialize_format='json',
                 deserialize_format='json'):
        super(DoryClient, self).__init__(serialize_format,
                                         deserialize_format)
        self.url = url
        self.default_headers['X-Auth-Token'] = auth_token
        self.default_headers['X-Project-Id'] = tenant_id
        self.default_headers['Content-Type'] = 'application/json'
        self.default_headers['Accept'] = 'application/json'

        self.serialize = serialize_format
        self.deserialize_format = deserialize_format

    def ping_dory(self):
        """Ping Dory

        :return: Response Object containing response code 200 and body with
                status of the server
        PUT
        services/{service_name}
        """
        url = self.url
        return self.request('GET', url)
