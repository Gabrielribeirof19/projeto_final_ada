const express = require('express')
const bodyParser = require('body-parser')
const db = require('./db')

const app = express()

app.set('view engine', 'ejs')
app.use(bodyParser.urlencoded({ extended: true }))

app.get('/', async (req, res) => {

  const filmes = await db.query("SELECT * FROM filmes")

  res.render('index', { filmes: filmes.rows })
})

app.listen(3000, () => {
  console.log("Servidor rodando")
})