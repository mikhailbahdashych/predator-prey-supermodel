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
    const { data } = await api.post('u/s-i', payload)
    return data
  } catch (e) {
    return e.response.data
  }
}

export const signUp = async payload => {
  try {
    const { data } = await api.post('u/s-u', payload)
    return data
  } catch (e) {
    return e.response.data
  }
}

export const logout = async token => {
  try {
    const { data } = await api.post('u/l',{},{
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const confirmAccount = async payload => {
  try {
    const { data } = await api.post('u/l', payload)
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getUserByPersonalId = async personalId => {
  try {
    const { data } = await api.get(`u/${personalId}`)
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getUserSettings = async (token, type) => {
  try {
    const { data } = await api.get(`/u/s/${type}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const changePassword = async (payload, token) => {
  try {
    const { data } = await api.patch('u/p', payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const changeEmail = async (payload, token) => {
  try {
    const { data } = await api.patch('u/e', payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const setTwoFa = async (payload, token) => {
  try {
    const { data } = await api.patch('u/2fa/s', payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const disableTwoFa = async (payload, token) => {
  try {
    const { data } = await api.patch('u/2fa/d', payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const setMobilePhone = async (payload, token) => {
  try {
    const { data } = await api.patch('u/m-p/s', payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const disableMobilePhone = async (payload, token) => {
  try {
    const { data } = await api.patch('u/m-p/d', payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const deleteAccount = async (payload, token) => {
  try {
    const { data } = await api.patch('u/d-a', payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const updateUserPersonalInformation = async (payload, token) => {
  try {
    const { data } = await api.patch(`u/p-i`, payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const createBookmark = async (payload, token) => {
  try {
    const { data } = await api.post('b', payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getBookmarks = async token => {
  try {
    const { data } = await api.get('b', {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const deleteBookmark = async (id, token) => {
  try {
    const { data } = await api.delete(`b/${id}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getRefreshedTokens = async () => {
  try {
    const { data } = await api.get('r-t')
    return data
  } catch (e) {
    return e.response.data
  }
}

export const search = async slug => {
  try {
    const { data } = await api.get('s', {
      params: { slug }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const vote = async (payload, token) => {
  try {
    const { data } = await api.patch(`v/${payload.id}/${payload.vote}/${payload.type}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getQuestion = async slug => {
  try {
    const { data } = await api.get(`q`, {
      params: { slug }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getQuestions = async payload => {
  try {
    const { data } = await api.get(`q/${payload.sort}`)
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getUserQuestions = async payload => {
  try {
    const { data } = await api.get(`u/${payload.personalId}/q/${payload.sort}`)
    return data
  } catch (e) {
    return e.response.data
  }
}

export const createQuestionPost = async (payload, token) => {
  try {
    const { data } = await api.post('q', payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const answerQuestion = async (payload, token) => {
  try {
    const { data } = await api.patch('q/a', payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getBlogPost = async slug => {
  try {
    const { data } = await api.get(`b-p`, {
      params: { slug }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getBlogPosts = async sort => {
  try {
    const { data } = await api.get(`b-p/${sort}`)
    return data
  } catch (e) {
    return e.response.data
  }
}

export const createBlogPost = async (payload, token) => {
  try {
    const { data } = await api.post('b-p', payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const commentBlogPost = async (payload, token) => {
  try {
    const { data } = await api.patch('b-p/c', payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getForumThread = async slug => {
  try {
    const { data } = await api.get(`f-t`, {
      params: { slug }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const getForumThreads = async sort => {
  try {
    const { data } = await api.get(`f-t/${sort}`)
    return data
  } catch (e) {
    return e.response.data
  }
}

export const createForumPost = async (payload, token) => {
  try {
    const { data } = await api.post('f-t', payload, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    return data
  } catch (e) {
    return e.response.data
  }
}

export const commentForumThread = async (payload, token) => {
  try {
    const { data } = await api.patch('f-t/c', payload, {
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
