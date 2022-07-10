import {getUserByToken} from "~/api";

export const verifyClientByToken = async (router, token, nonRedirect = false) => {
  if (!nonRedirect) {
    if (!token) return await router.push({ path: '/' })

    const client = await getUserByToken(token)

    if (!client || client.status === -1) {
      sessionStorage.removeItem('accessToken')
      sessionStorage.removeItem('refreshToken')
      return await router.push({ path: '/' })
    }

    return client
  }
  if (token) {
    const client = await getUserByToken(token)
    if (client.status !== -1) {
      return await router.push({path: `/account/${client.personalId}`})
    } else {
      sessionStorage.removeItem('token')
    }
  }
}
