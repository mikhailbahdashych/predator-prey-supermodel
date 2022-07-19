import axios from "axios";
process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0'

const apiUrl = process.server ? `${process.env.PNB_FRONT}api/` : '/api/';

const api = axios.create({
  baseURL: apiUrl,
  headers: {
    'Content-Type': 'application/json'
  }
})

export const signIn = async payload => {
  try {
    const { data } = await api.post('s-i', payload)
    return data
  } catch (e) {
    return e.response.data
  }
}

export const signUp = async payload => {
  try {
    const { data } = await api.post('s-u', payload)
    return data
  } catch (e) {
    return e.response.data
  }
}

export const changePassword = async (payload, token) => {
  try {
    const { data } = await api.post('c-p', payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const changeEmail = async (payload, token) => {
  try {
    const { data } = await api.post('c-e', payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const setTwoFa = async (payload, token) => {
  try {
    const { data } = await api.post('s-2fa', payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const disableTwoFa = async (payload, token) => {
  try {
    const { data } = await api.post('d-2fa', payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const deleteAccount = async (payload, token) => {
  try {
    const { data } = await api.post('d-a', payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getRefreshedTokens = async () => {
  try {
    const { data } = await api.get('g-r-t')
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getUserByPersonalId = async personalId => {
  try {
    const { data } = await api.get(`g-u-b-p-id/${personalId}`)
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getUserLastActivity = async personalId => {
  try {
    const { data } = await api.get(`g-u-l-a/${personalId}`)
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getUserSettings = async (token, type) => {
  try {
    const { data } = await api.get(`/g-u-s/${type}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const search = async slug => {
  try {
    const { data } = await api.get('/s', {
      params: { slug }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const updateUserPersonalInformation = async (payload, token) => {
  try {
    const { data } = await api.patch(`u-u-p-i`, payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const vote = async (payload, token) => {
  try {
    const { data } = await api.patch(`/v/${payload.id}/${payload.v}/${payload.type}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getQuestionBySlug = async (slug) => {
  try {
    const { data } = await api.get(`/g-q-b-s`, {
      params: { slug }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getBlogPosts = async by => {
  try {
    const { data } = await api.get(`/g-b-ps/${by}`)
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getForumThreads = async by => {
  try {
    const { data } = await api.get(`/g-f-ts/${by}`)
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getQuestions = async by => {
  try {
    const { data } = await api.get(`/g-qs/${by}`)
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getBlogPost = async id => {
  try {
    const { data } = await api.get(`/g-b-p/${id}`)
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getForumThread = async id => {
  try {
    const { data } = await api.get(`/g-f-t/${id}`)
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getQuestion = async id => {
  try {
    const { data } = await api.get(`/g-q/${id}`)
    return data
  } catch (e) {
    return e.response.data
  }
}

export const createBlogPost = async (payload, token) => {
  try {
    const { data } = await api.post('/c-b-p', payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const createForumPost = async (payload, token) => {
  try {
    const { data } = await api.post('/c-f-t', payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const createQuestionPost = async (payload, token) => {
  try {
    const { data } = await api.post('/c-q', payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getAvailableFlags = async payload => {
  const { data } = await api.get('https://flagcdn.com/en/codes.json')
  return data
}
