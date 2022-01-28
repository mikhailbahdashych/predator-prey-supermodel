const dotenv = require('dotenv')
dotenv.config()

const express = require('express');
const consola = require('consola')
const bodyParser = require('body-parser');
const { Nuxt, Builder } = require('nuxt')
const app = express()

const config = require('../nuxt.config.js')
// config.dev = !(process.env.NODE_ENV === 'production')

app.use(bodyParser.json({limit: '1mb'}))

const routes = require('./routes')
app.use('/api', routes)

async function start() {
  const nuxt = new Nuxt(config)

  const { host, port } = nuxt.options.server

  const builder = new Builder(nuxt)
  await builder.build()

  // if (config.dev) {
  //
  // } else {
  //   await nuxt.ready()
  // }

  app.use(nuxt.render)

  app.listen(port, host)
  consola.ready({
    message: `Server listening on http://${host}:${port}`,
    badge: true
  })
}
start()


// const dotenv = require('dotenv')
// dotenv.config()
//
// const express = require('express')
// const bodyParser = require('body-parser')
// const consola = require('consola')
// const { Nuxt, Builder } = require('nuxt')
// const app = express()
//
// app.use(bodyParser.json({ limit: '1mb' }))
//
// // Import and Set Nuxt.js options
// const config = require('../nuxt.config.js')
// config.dev = !(process.env.NODE_ENV === 'production')
//
// const routes = require('./routes')
//
// app.use('/api', routes)
//
// async function start() {
//   const nuxt = new Nuxt(config)
//
//   const { host, port } = nuxt.options.server
//
//   // Build only in dev mode
//   if (config.dev) {
//     const builder = new Builder(nuxt)
//     await builder.build()
//   } else {
//     await nuxt.ready()
//   }
//
//   app.use(nuxt.render)
//
//   app.listen(port, host)
//   consola.ready({
//     message: `Server listening on http://${host}:${port}`,
//     badge: true
//   })
// }
// start()

