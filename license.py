#!/bin/python3
# -*- coding: utf-8 -*-

from __future__ import annotations
import base64
import hashlib
import hmac
import os
import platform
import re
from datetime import datetime, timedelta
import pandas.io.clipboard as clipboard

LICENSE_SECRET = "CL_V51_REPLACE_WITH_YOUR_OWN_SECRET_2026_ENTERPRISE"
expiry = ""
device_prefix = ""
sig = ""

day = datetime.now() + timedelta(days = 1)
expiry = day.strftime("%Y%m%d")
dev_hash = hashlib.sha256(re.sub("\\s+", "", platform.node().strip()).upper().encode("utf-8")).hexdigest().upper()
device_prefix = dev_hash[:12]
payload = f"{dev_hash}|{expiry}"
sig = base64.urlsafe_b64encode(hmac.new(LICENSE_SECRET.encode("utf-8"),payload.encode("utf-8"),hashlib.sha256).digest()).decode("ascii").rstrip("=")[:22].upper()
license = "CLV51-" + expiry + "-" + device_prefix + "-" + sig + ""
print(f"License: {license}")
clipboard.copy(license)

