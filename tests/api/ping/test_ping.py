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

import ddt

from tests.api import base
from tests.api.utils.schema import response


@ddt.ddt
class TestPing(base.TestBase):

    """Tests for Services."""

    def setUp(self):
        super(TestPing, self).setUp()

    @ddt.file_data('data_ping.json')
    def test_ping(self, test_data):

        resp = self.client.ping_dory()
        self.assertEqual(resp.status_code, 200)

        response_body = resp.json()
        self.assertSchema(response_body, response.ping_dory)

    def tearDown(self):
        super(TestPing, self).tearDown()
