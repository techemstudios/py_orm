# py_orm
Sql Alchemy demo notebook & zappa app API demo with similar notebook sqlalchemy code spread throughout a flask app.

## Examples to test POSTs, PUTs, and DELETEs

### POST / Insert
`curl https://{id}.execute-api.us-east-1.amazonaws.com/dev/api/sites -d '{"name":"Yorktown","stream_id":6}' -X POST -v`

### PUT / Update
`curl https://{id}.execute-api.us-east-1.amazonaws.com/dev/api/streams/5 -d '{"name":"York"}' -X PUT -v`

### DELETE
`curl https://{id}.execute-api.us-east-1.amazonaws.com/dev/api/streams/5 -X DELETE -v`
