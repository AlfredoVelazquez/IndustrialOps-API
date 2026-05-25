import { createContext, useContext, useEffect, useState } from 'react'
import { getCurrentUser, loginUser } from '../services/authService'

const AuthContext = createContext(null)

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null)
  const [token, setToken] = useState(localStorage.getItem('token'))
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    async function loadUser() {
      if (!token) {
        setLoading(false)
        return
      }

      try {
        const currentUser = await getCurrentUser(token)
        setUser(currentUser)
      } catch (error) {
        localStorage.removeItem('token')
        setToken(null)
        setUser(null)
      } finally {
        setLoading(false)
      }
    }

    loadUser()
  }, [token])

  async function login(credentials) {
    const data = await loginUser(credentials)

    localStorage.setItem('token', data.access_token)
    setToken(data.access_token)

    const currentUser = await getCurrentUser(data.access_token)
    setUser(currentUser)

    return currentUser
  }

  function logout() {
    localStorage.removeItem('token')
    setToken(null)
    setUser(null)
  }

  return (
    <AuthContext.Provider value={{ user, token, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth() {
  return useContext(AuthContext)
}