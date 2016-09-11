#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#

from webapp2 import WSGIApplication
from webapp2 import Route

import handlers

app = WSGIApplication([
    Route('/', handlers.RedirectToMainPage),
    Route(r'/blog<:/?>', handlers.BlogPage),
    Route(r'/blog/.json', handlers.BlogPageJson),
    Route(r'/blog/signup<:/?>', handlers.RegisterPage),
    Route(r'/blog/welcome<:/?>', handlers.WelcomePage),
    Route(r'/blog/login<:/?>', handlers.LoginPage),
    Route(r'/blog/logout<:/?>', handlers.LogoutPage),
    Route(r'/blog/<post_id:\d+>', handler=handlers.PostView),
    Route(r'/blog/<post_id:\d+>.json', handler=handlers.PostViewJson),
    Route(r'/blog/newpost<:/?>', handlers.SubmitPost),
    Route(r'/blog/flush<:/?>', handlers.FlushCache)
], debug=True)
