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

export const getUserByToken = async token => {
  try {
    const { data } = await api.get('g-u-b-t', {
      headers: {
        'Authorization': `Bearer ${token}`,
        'ato': token
      }
    })
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
