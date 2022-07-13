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

export const getUserByAccessToken = async token => {
  try {
    const { data } = await api.get('g-u-b-t', {
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

export const updateUserPersonalInformation = async payload => {
  try {
    const { data } = await api.patch(`u-u-p-i`, payload, {
      headers: { 'Authorization': `Bearer ${payload.token}` }
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
