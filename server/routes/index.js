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
    return res.status(e.response.status).json(e.response.data)
  }
});

router.post('/s-u', async (req, res) => {
  try {
    const { data } = await api.post('/sign-up', req.body)
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.post('/c-p', async (req, res) => {
  try {
    const { data } = await api.post('/change-password', req.body, {
      headers: { 'ato': req.headers.ato }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.get('/g-u-b-t', async (req, res) => {
  try {
    const { data } = await api.get('/get-user-by-token', {
      headers: { 'ato': req.headers.ato }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.get('/g-u-b-p-id/:personalId', async (req, res) => {
  try {
    const { data } = await api.get(`/get-user-by-personal-id/${req.params.personalId}`)
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.get('/g-u-p-i', async (req, res) => {
  try {
    const { data } = await api.get('/get-user-personal-information', {
      headers: { 'ato': req.headers.ato }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.patch('/u-u-p-i', async (req, res) => {
  try {
    const { data } = await api.patch('/update-user-personal-information', req.body, {
      headers: { 'ato': req.headers.ato }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.get('/g-u-s-s', async (req, res) => {
  try {
    const { data } = await api.get('/get-user-security-settings', {
      headers: { 'ato': req.headers.ato }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.patch('/u-u-s-s', async (req, res) => {
  try {
    const { data } = await api.patch('/update-user-security-settings', req.body, {
      headers: { 'ato': req.headers.ato }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.post('/s-2fa', async (req, res) => {
  try {
    const { data } = await api.post('/set-2fa', req.body, {
      headers: { 'ato': req.headers.ato }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.post('/d-2fa', async (req, res) => {
  try {
    const { data } = await api.post('/disable-2fa', req.body, {
      headers: { 'ato': req.headers.ato }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.get('/g-u-l-a/:personalId', async (req, res) => {
  try {
    const { data } = await api.get(`/get-user-last-activity/${req.params.personalId}`)
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

module.exports = router
