#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Copyright 2019 The Matrix.org Foundation C.I.C.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from .fakehs import get_shared_fake_hs
from .is_api import IsApi
from .launch_is import get_or_launch_is


class LogoutTest(unittest.TestCase):
    def setUp(self):
        self.fakeHs = get_shared_fake_hs()
        self.fakeHsAddr = self.fakeHs.get_addr()

    def test_logout(self):
        base_url = get_or_launch_is(False)
        api = IsApi(base_url, "v2", None)
        api.make_account(self.fakeHsAddr)

        body = api.account()
        self.assertIn("user_id", body)

        api.logout()

        body = api.account()
        self.assertEqual(body["errcode"], "M_UNAUTHORIZED")


if __name__ == "__main__":
    import sys
    from twisted.python import log

    log.startLogging(sys.stdout)
    unittest.main()
