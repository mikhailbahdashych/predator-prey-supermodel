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

router.get(`/g-l-r/:q`, async (req, res) => {
  try {
    const { q } = req.params
    const data = await api.get(`/get-latest-releases/${q}`)
    res.json(data.data)
  } catch (e) {
    console.log(e)
  }
})

router.get(`/g-a/:id`, async (req, res) => {
  try {
    const { id } = req.params
    const data = await api.get(`/get-article/${id}`)
    res.json(data.data)
  } catch (e) {
    console.log(e)
  }
})

router.get(`/g-t/:id`, async (req, res) => {
  try {
    const { id } = req.params
    const data = await api.get(`/get-tip/${id}`)
    res.json(data.data)
  } catch (e) {
    console.log(e)
  }
})

router.get(`/g-w-u/:id`, async (req, res) => {
  try {
    const { id } = req.params
    const data = await api.get(`/get-write-up/${id}`)
    res.json(data)
  } catch (e) {
    console.log(e)
  }
})

router.get(`/g-ctf/:id`, async (req, res) => {
  try {
    const { id } = req.params
    const data = await api.get(`/get-ctf/${id}`)
    res.json(data)
  } catch (e) {
    console.log(e)
  }
})

module.exports = router
