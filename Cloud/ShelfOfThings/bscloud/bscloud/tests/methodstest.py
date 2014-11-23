"""
<Short description of file contents>
Copyright (C) 2013  Victor Polevoy (vityatheboss@gmail.com)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = 'Victor Polevoy'

import requests

host = 'http://iot.vpolevoy.com'
# host = 'http://localhost:8000'

headers = {"content-type": "application/x-www-form-urlencoded"}
# answer = requests.patch('%s/api/product/1/' % host, data='name=219dfsfjazafaka', headers=headers)

# answer = requests.post('%s/api/jobs/' % host, data='product_id=ds', headers=headers)
answer = requests.delete('%s/api/jobs/1/' % host)

print('answer: %s' % answer)
