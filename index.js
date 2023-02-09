const express = require('express')
const SQLMongoParser = require('@synatic/sql-to-mongo');
const app = express()
const port = 3000

app.use(express.json()) // for parsing application/json
app.use(express.urlencoded({ extended: true })) // for parsing application/x-www-form-urlencoded


app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.post('/sql2mongo', (req, res) => {
  console.log(req.body)
  let q = JSON.stringify(SQLMongoParser.parseSQL(req.body.query),null,4);
  res.send(q);
  //res.send(req.body);
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
