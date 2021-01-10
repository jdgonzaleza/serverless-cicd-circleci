from hello_world import hello


def test_hello():
    expected_body = '{"message": "Greetings from the serverless API :) ", "input": null}'
    response = hello(event=None, context=None)
    assert response.get('body') == expected_body
