import os
from unittest.mock import patch
import pytest
from hello_ai import get_client, chat_with_ai


def test_get_client_missing_env_vars():
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError):
            get_client()


def test_get_client():
    with patch.dict(os.environ, {
        'AZURE_OPENAI_API_KEY': 'test-key',
        'AZURE_OPENAI_ENDPOINT': 'https://test.openai.azure.com'
    }, clear=True):
        client = get_client()
        assert client is not None


def test_chat_with_ai():
    mock_response = type('obj', (object,), {
        'choices': [
            type('obj', (object,), {
                'message': type('obj', (object,), {
                    'content': 'こんにちは、田中さん！'
                })
            })
        ]
    })

    with patch.dict(os.environ, {
        'AZURE_OPENAI_API_KEY': 'test-key',
        'AZURE_OPENAI_ENDPOINT': 'https://test.openai.azure.com'
    }):
        client = get_client()
        with patch.object(
                client.chat.completions,
                'create',
                return_value=mock_response):
            response = chat_with_ai("こんにちは！私の名前は田中です。", client)
            assert "こんにちは、田中さん！" in response
