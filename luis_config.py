#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os

class DefaultConfig:
    """Configuration for the bot."""

    PORT = 3978
    LUIS_AUTHORING_KEY = os.environ.get("LuisAuthKey", "d8356ab281fc47d7becca171b711b8de")
    LUIS_PREDICTION_KEY = os.environ.get("LuisPredKey", "46a7b4f393264ced900a09345d79b2b1")
    LUIS_AUTHORING_END_POINT = os.environ.get("LuisAuthEndPoint", "https://p10luis2023-authoring.cognitiveservices.azure.com/")
    LUIS_PREDICTION_END_POINT = os.environ.get("LuisPredEndPoint", "https://p10-luis-2023.cognitiveservices.azure.com/")
    LUIS_APP_ID = os.environ.get("luis_app_id","ab35a7a8-c3f0-4e7e-a0d0-9fcf16518e50")
    
