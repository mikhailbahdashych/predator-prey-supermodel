/* eslint-disable */
process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0'
const { Router } = require('express')
const axios = require('axios')
const dotenv = require('dotenv')
dotenv.config()

const api = axios.create({
  baseURL: process.env.PNB_API
})

const router = Router()

router.get(`/g-a`, async (req, res) => {
  try {
    const data = await api.get(`/get-articles`)
    res.json(data.data)
  } catch (e) {
    console.log(e)
  }
})

module.exports = router
