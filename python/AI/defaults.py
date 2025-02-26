# Copyright (c) 2024 Microsoft Corporation. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project.
#

DEFAULT_ENCODING = "cl100k_base"
#
DEFAULT_LLM_MODEL = "gpt-4o"
DEFAULT_AZURE_LLM_MODEL = "gpt-4o"
DEFAULT_LLM_MAX_TOKENS = 4000
#
# Text Embedding Parameters
DEFAULT_EMBEDDING_MODEL = "text-embedding-ada-002"
DEFAULT_EMBEDDING_BATCH_MAX_TOKENS = 8191
DEFAULT_TEMPERATURE = 0
DEFAULT_MAX_GEN_TOKENS = 4096
DEFAULT_MAX_INPUT_TOKENS = 128000
DEFAULT_OPENAI_VERSION="2023-12-01-preview"


API_BASE_REQUIRED_FOR_AZURE = "api_base is required for Azure OpenAI client"

PICKLE_FILE_NAME = 'embeddings.pickle'


CHUNK_SIZE = 5000
CHUNK_OVERLAP = 0
