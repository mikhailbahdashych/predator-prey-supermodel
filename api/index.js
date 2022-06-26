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
  const { data } = await api.post('s-i', payload)
  return data
}

export const signUp = async payload => {
  const { data } = await api.post('s-u', payload)
  return data
}
