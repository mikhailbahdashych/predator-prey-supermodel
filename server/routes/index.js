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

router.get(`/g-s-r/:q`, async (req, res) => {
  try {
    const { q } = req.params
    const data = await api.get(`/get-selected-releases/${q}`)
    res.json(data.data)
  } catch (e) {
    console.log(e)
  }
})

router.get(`/g-l-r/:q`, async (req, res) => {
  try {
    const { q } = req.params
    const data = await api.get(`/get-latest-releases/${q}`)
    res.json(data.data)
  } catch (e) {
    console.log(e)
  }
})

router.get(`/g-p/:id`, async (req, res) => {
  try {
    const { id } = req.params
    const data = await api.get(`/get-post/${id}`)
    res.json(data.data)
  } catch (e) {
    console.log(e)
  }
})

router.get(`/g-p-b-c/:category/:from/:to`, async (req, res) => {
  try {
    const { category, from, to } = req.params
    const data = await api.get(`/get-posts-by-category/${category}/${from}/${to}`)
    res.json(data.data)
  } catch (e) {
    console.log(e)
  }
})

router.post(`/search`, async (req, res) => {
  try {
    const data = await api.post(`/search`, req.body)
    res.json(data.data)
  } catch (e) {
    console.log(e)
  }
})

router.post('/s-e', async (req, res) => {
  try {
    const data = await api.post('/send-email', req.body)
    res.json(data.data)
  } catch (e) {
    console.log(e)
  }
})

router.get('/test', async (req, res) => {
  try {
    const data = await api.get('/test')
    res.json(data.data)
  } catch (e) {
    console.log(e)
  }
})

module.exports = router
