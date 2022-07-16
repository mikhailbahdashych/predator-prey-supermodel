process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0'
const { Router } = require('express')
const axios = require('axios')
const dotenv = require('dotenv')
dotenv.config()

const api = axios.create({
  baseURL: process.env.NODE_ENV === "development" ? process.env.PNB_API_DEV : process.env.PNB_API_PROD,
})

const router = Router()

router.post('/s-i', async (req, res) => {
  try {
    const { data } = await api.post('/sign-in', req.body)

    res.cookie("_rt", data._rt, { httpOnly: true, secure: false })
    delete data._rt

    return res.json(data)
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
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.post('/c-e', async (req, res) => {
  try {
    const { data } = await api.post('/change-email', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.post('/s-2fa', async (req, res) => {
  try {
    const { data } = await api.post('/set-2fa', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.post('/d-2fa', async (req, res) => {
  try {
    const { data } = await api.post('/disable-2fa', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.post('/d-a', async (req, res) => {
  try {
    const { data } = await api.post('/delete-account', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.get('/g-r-t', async (req, res) => {
  try {
    const { data } = await api.get('/get-refreshed-tokens', {
      headers: { 'Cookie': req.headers.cookie }
    })

    res.cookie("_rt", data._rt, { httpOnly: true, secure: false })
    delete data._rt

    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.get('/g-u-b-p-id/:personalId', async (req, res) => {
  try {
    const { data } = await api.get(`/get-user-by-personal-id/${req.params.personalId}`,{
      auth: {
        username: process.env.BASIC_AUTH_USERNAME,
        password: process.env.BASIC_AUTH_PASSWORD
      }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.get('/g-u-l-a/:personalId', async (req, res) => {
  try {
    const { data } = await api.get(`/get-user-last-activity/${req.params.personalId}`, {
      auth: {
        username: process.env.BASIC_AUTH_USERNAME,
        password: process.env.BASIC_AUTH_PASSWORD
      }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.get('/g-u-s/:type', async (req, res) => {
  try {
    const { data } = await api.get(`/get-user-settings/${req.params.type}`, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.post('/s', async (req, res) => {
  try {
    const { data } = await api.post('/search', req.body)
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.patch('/u-u-p-i', async (req, res) => {
  try {
    const { data } = await api.patch('/update-user-personal-information', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.patch('/v/:id/:v/:postType', async (req, res) => {
  try {
    const { data } = await api.patch(`/vote/${req.params.id}/${req.params.v}/${req.params.postType}`, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.get('/g-b-p/:id', async (req, res) => {
  try {
    const { data } = await api.get(`/get-blog-post/${req.params.id}`, {
      auth: {
        username: process.env.BASIC_AUTH_USERNAME,
        password: process.env.BASIC_AUTH_PASSWORD
      }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.get('/g-f-t/:id', async (req, res) => {
  try {
    const { data } = await api.get(`/get-forum-thread/${req.params.id}`, {
      auth: {
        username: process.env.BASIC_AUTH_USERNAME,
        password: process.env.BASIC_AUTH_PASSWORD
      }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.get('/g-q/:id', async (req, res) => {
  try {
    const { data } = await api.get(`/get-question/${req.params.id}`, {
      auth: {
        username: process.env.BASIC_AUTH_USERNAME,
        password: process.env.BASIC_AUTH_PASSWORD
      }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.post('/c-b-p', async (req, res) => {
  try {
    const { data } = await api.post('/create-blog-post', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.post('/c-f-p', async (req, res) => {
  try {
    const { data } = await api.post('/create-forum-post', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.post('/c-q-p', async (req, res) => {
  try {
    const { data } = await api.post('/create-question-post', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})


module.exports = router
