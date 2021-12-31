import axios from "axios";
process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0'

const apiUrl = process.server ? `${process.env.PNB_FRONT}api/` : '/api/';

const api = axios.create({
  baseURL: apiUrl,
  headers: {
    'Content-Type': 'application/json'
  }
})

export const getLatestReleases = async (q) => {
  const { data } =  await api.get(`g-l-r/${q}`)
  return data
}

export const getArticleById = async (id) => {
  const { data } = await api.get(`g-a/${id}`)
  return data
}

export const getTipById = async (id) => {
  const { data } = await api.get(`g-t/${id}`)
  return data
}
