import axios from "axios";
process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0'

const apiUrl = process.server ? `${process.env.PNB_FRONT}api/` : '/api/';

const api = axios.create({
  baseURL: apiUrl,
  headers: {
    'Content-Type': 'application/json'
  }
})

export const getSelectedReleases = async q => {
  const { data } = await api.get(`g-s-r/${q}`)
  return data
}

export const getLatestReleases = async (q) => {
  const { data } =  await api.get(`g-l-r/${q}`)
  return data
}

export const getPostById = async id => {
  const { data } = await api.get(`g-p/${id}`)
  return data
}

export const getPostsByCategory = async d => {
  const { data } = await api.get(`g-p-b-c/${d.category}/${d.from}/${d.to}`)
  return data
}

export const search = async payload => {
  const { data } = await api.post(`search`, payload)
  return data
}

export const sendEmail = async payload => {
  const { data } = await api.post('/s-e', payload)
  return data
}

