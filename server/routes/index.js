/* eslint-disable */
process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0'
const { Router } = require('express')
const axios = require('axios')
const dotenv = require('dotenv')
dotenv.config()

const api = axios.create({
  baseURL: process.env.NODE_ENV === "development" ? process.env.PNB_API_DEV : process.env.PNB_API_PROD
})

const router = Router()

router.post('/s-i', async (req, res) => {
  try {
    const { data } = await api.post('/sign-in', req.body)
    res.json(data)
  } catch (e) {
    throw new Error(e)
  }
});

router.post('/s-u', async (req, res) => {
  try {
    const { data } = await api.post('/sign-up', req.body)
    res.json(data)
  } catch (e) {
    throw new Error(e)
  }
});

router.get('/g-u-b-t', async (req, res) => {
  try {
    const { data } = await api.get('/get-user-by-token', {
      headers: {
        'Authorization': req.headers.authorization,
        'ato': req.headers.ato
      }
    })
    res.json(data)
  } catch (e) {
    throw new Error(e)
  }
})

module.exports = router
