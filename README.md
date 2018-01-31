# Word Count
Word Count is an user-facing form that counts the number of words in a block of text.

## Prerequisite
- Python 3

## Install app requirements
```
make requirements
```

## Run the app
```
make server
```

## Run specs
```
make tests
```

## Web app
After running the server, access the follow URL on your browser:
`http://localhost:5000/api/`
## Rest API
After running the server, make the follow curl request:
```sh
curl -d '{"text": "some text"}' -H "Content-Type: application/json" -X POST http://0.0.0.0:5000/api/wc
```
Expected response:
```json
{
  "given_text": "some text",
  "words_counted": 2
}
```
