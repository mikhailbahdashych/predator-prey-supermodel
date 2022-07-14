import * as jwt from 'jsonwebtoken';
import jwtKey from '../jwt/public';

export const verifyToken = token => {
  try {
    return jwt.verify(token, jwtKey)
  } catch (e) {
    if (e instanceof jwt.TokenExpiredError)
      return { message: "token-expired" }
    else if (e instanceof jwt.JsonWebTokenError)
      return { message: "invalid-token" }
  }
}
