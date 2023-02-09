const express = require('express')
const SQLMongoParser = require('@synatic/sql-to-mongo');
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.get('/sql2mongo', (req, res) => {
  let q = JSON.stringify(SQLMongoParser.parseSQL("select id from `films` where `id` > 10 limit 10"),null,4);
  res.send(q);
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
