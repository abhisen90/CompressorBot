#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from . import *

try:
    APP_ID = 1110326
    API_HASH = "c07f965414908bce7b8aa9252f89f0ad"
    BOT_TOKEN = "5741747814:AAHiY3CBRRqwaN_8T8j-eeeQxPBqDSPe_rA"
    OWNER = 5710115145
    LOG = -1001814180831
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
