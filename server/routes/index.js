process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0'
const { Router } = require('express')
const axios = require('axios')
require('dotenv').config()

const api = axios.create({
  baseURL: process.env.NODE_ENV === "development" ? process.env.PNB_API_DEV : process.env.PNB_API_PROD,
})

const router = Router()

router.post('/u/s-i', async (req, res) => {
  try {
    const { data } = await api.post('/user/sign-in', req.body, {
      auth: {
        username: process.env.BASIC_AUTH_USERNAME,
        password: process.env.BASIC_AUTH_PASSWORD
      }
    })

    res.cookie("_rt", data._rt, {
      httpOnly: true,
      secure: process.env.NODE_ENV !== "development",
      maxAge: 7 * 24 * 60 * 60 * 1000
    })
    delete data._rt

    return res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.post('/u/s-u', async (req, res) => {
  try {
    const { data } = await api.post('/user/sign-up', req.body, {
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

router.post('/u/l', async (req, res) => {
  try {
    const { data } = await api.post('/user/logout', {},{
      headers: { 'Authorization': req.headers.authorization }
    })
    res.clearCookie("_rt")
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.get('/u/:personalId', async (req, res) => {
  try {
    const { data } = await api.get(`/user/${req.params.personalId}`,{
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

router.get('/u/s/:type', async (req, res) => {
  try {
    const { data } = await api.get(`/user/settings/${req.params.type}`, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.patch('/u/p', async (req, res) => {
  try {
    const { data } = await api.patch('/user/password', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.patch('/u/e', async (req, res) => {
  try {
    const { data } = await api.patch('/user/email', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.patch('/u/2fa/s', async (req, res) => {
  try {
    const { data } = await api.patch('/user/2fa/set', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.patch('/u/2fa/d', async (req, res) => {
  try {
    const { data } = await api.patch('/user/2fa/disable', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.patch('/u/m-p/s', async (req, res) => {
  try {
    const { data } = await api.patch('/user/mobile-phone/set', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.patch('/u/m-p/d', async (req, res) => {
  try {
    const { data } = await api.patch('/user/mobile-phone/disable', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.patch('/u/d-a', async (req, res) => {
  try {
    const { data } = await api.patch('/user/delete-account', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.patch('/u/p-i', async (req, res) => {
  try {
    const { data } = await api.patch('/user/personal-information', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.post('/b', async (req, res) => {
  try {
    const { data } = await api.post('/bookmark', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.get('/b', async (req, res) => {
  try {
    const { data } = await api.get('/bookmark', {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.delete('/b/:id', async (req, res) => {
  try {
    const { data } = await api.delete(`/bookmark/${req.params.id}`, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.get('/r-t', async (req, res) => {
  try {
    const { data } = await api.get('/refresh-tokens', {
      headers: { 'Cookie': req.headers.cookie },
      auth: {
        username: process.env.BASIC_AUTH_USERNAME,
        password: process.env.BASIC_AUTH_PASSWORD
      }
    })

    res.cookie("_rt", data._rt, {
      httpOnly: true,
      secure: process.env.NODE_ENV !== "development",
      maxAge: 7 * 24 * 60 * 60 * 1000
    })
    delete data._rt

    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
});

router.get('/s', async (req, res) => {
  try {
    const { data } = await api.get('/search', {
      params: {
        slug: req.query.slug
      },
      auth: {
        username: process.env.BASIC_AUTH_USERNAME,
        password: process.env.BASIC_AUTH_PASSWORD
      }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.patch('/v/:id/:vote/:type', async (req, res) => {
  try {
    const { data } = await api.patch(`/vote/${req.params.id}/${req.params.vote}/${req.params.type}`, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.get('/q', async (req, res) => {
  try {
    const { data } = await api.get(`/question`, {
      params: {
        slug: req.query.slug
      },
      auth: {
        username: process.env.BASIC_AUTH_USERNAME,
        password: process.env.BASIC_AUTH_PASSWORD
      }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.get('/q/:sort', async (req, res) => {
  try {
    const { data } = await api.get(`/question/${req.params.sort}`, {
      auth: {
        username: process.env.BASIC_AUTH_USERNAME,
        password: process.env.BASIC_AUTH_PASSWORD
      }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.get('/u/:personalId/q/:sort', async (req, res) => {
  try {
    const { data } = await api.get(`/user/${req.params.personalId}/question/${req.params.sort}`, {
      auth: {
        username: process.env.BASIC_AUTH_USERNAME,
        password: process.env.BASIC_AUTH_PASSWORD
      }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.post('/q', async (req, res) => {
  try {
    const { data } = await api.post('/question', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})


router.patch('/q/a', async (req, res) => {
  try {
    const { data } = await api.patch('/question/answer', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.get('/b-p', async (req, res) => {
  try {
    const { data } = await api.get(`/blog-post`, {
      params: {
        slug: req.query.slug
      },
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

router.get('/b-p/:sort', async (req, res) => {
  try {
    const { data } = await api.get(`/blog-posts/${req.params.sort}`, {
      auth: {
        username: process.env.BASIC_AUTH_USERNAME,
        password: process.env.BASIC_AUTH_PASSWORD
      }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.post('/b-p', async (req, res) => {
  try {
    const { data } = await api.post('/blog-post', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.patch('/b-p/c', async (req, res) => {
  try {
    const { data } = await api.patch('/blog-post/comment', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.get('/f-t', async (req, res) => {
  try {
    const { data } = await api.get(`/forum-thread`, {
      params: {
        slug: req.query.slug
      },
      auth: {
        username: process.env.BASIC_AUTH_USERNAME,
        password: process.env.BASIC_AUTH_PASSWORD
      }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.get('/f-t/:sort', async (req, res) => {
  try {
    const { data } = await api.get(`/forum-thread/${req.params.sort}`, {
      auth: {
        username: process.env.BASIC_AUTH_USERNAME,
        password: process.env.BASIC_AUTH_PASSWORD
      }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.post('/f-t', async (req, res) => {
  try {
    const { data } = await api.post('/forum-thread', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

router.patch('/f-t/c', async (req, res) => {
  try {
    const { data } = await api.patch('/forum-thread/comment', req.body, {
      headers: { 'Authorization': req.headers.authorization }
    })
    res.json(data)
  } catch (e) {
    return res.status(e.response.status).json(e.response.data)
  }
})

module.exports = router
