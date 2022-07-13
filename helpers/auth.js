import {getUserByAccessToken} from "~/api";

export const verifyUserByToken = async (router, token, nonRedirect = false) => {
  if (!nonRedirect) {
    if (!token) return await router.push({ path: '/' })

    const user = await getUserByAccessToken(token)

    if (!user || user.status === -1) {
      sessionStorage.removeItem('accessToken')
      return await router.push({ path: '/' })
    }

    return user
  }
  if (token) {
    const user = await getUserByAccessToken(token)
    if (user.status !== -1) {
      return await router.push({path: `/account/${user.personalId}`})
    } else {
      sessionStorage.removeItem('accessToken')
    }
  }
}
