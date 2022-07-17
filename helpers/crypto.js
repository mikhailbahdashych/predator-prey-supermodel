import * as jwt from 'jsonwebtoken';
import jwtKey from '../jwt/public';

export const verifyToken = token => {
  try {
    return jwt.verify(token, jwtKey)
  } catch (e) {
    if (e instanceof jwt.TokenExpiredError || e instanceof jwt.JsonWebTokenError)
      return { message: "token-expired" }
  }
}
