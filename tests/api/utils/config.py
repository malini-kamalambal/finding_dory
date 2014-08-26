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

from cafe.engine.models import data_interfaces


class DoryConfig(data_interfaces.ConfigSectionInterface):
    """Defines the config values for dory."""
    SECTION_NAME = 'dory'

    @property
    def base_url(self):
        """dory endpoint."""
        return self.get('base_url')


class DoryServerConfig(data_interfaces.ConfigSectionInterface):
    """Defines the config values for starting (or not) a Dory server."""
    SECTION_NAME = 'dory_server'

    @property
    def run_server(self):
        """Boolean value indicating whether to start a Dory server."""
        return self.get_boolean('run_server')


class AuthConfig(data_interfaces.ConfigSectionInterface):
    """Defines the auth config values."""
    SECTION_NAME = 'auth'

    @property
    def auth_enabled(self):
        """Auth On/Off."""
        return self.get_boolean('auth_enabled')

    @property
    def base_url(self):
        """Auth endpoint."""
        return self.get('base_url')

    @property
    def user_name(self):
        """The name of the user, if applicable."""
        return self.get('user_name')

    @property
    def api_key(self):
        """The user's api key, if applicable."""
        return self.get_raw('api_key')
