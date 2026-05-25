import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'

function LoginPage() {
  const navigate = useNavigate()
  const { login } = useAuth()

  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  async function handleLogin(e) {
    e.preventDefault()

    try {
      const user = await login({
        username,
        password,
      })

      console.log('Current user:', user)

      alert('Login successful')

      navigate('/dashboard')
    } catch (error) {
      console.error(error)

      alert('Invalid credentials')
    }
  }

  return (
    <div>
      <h1>Login</h1>

      <form onSubmit={handleLogin}>
        <div>
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>

        <div>
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>

        <button type="submit">
          Login
        </button>
      </form>
    </div>
  )
}

export default LoginPage