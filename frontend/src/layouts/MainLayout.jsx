import { Outlet, useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'

function MainLayout() {
  const navigate = useNavigate()
  const { user, logout } = useAuth()

  function handleLogout() {
    logout()
    navigate('/login')
  }

  return (
    <div>
      <header>
        <h2>IndustrialOps</h2>

        <p>
          User: {user?.full_name} | Role: {user?.role}
        </p>

        <button type="button" onClick={handleLogout}>
          Logout
        </button>
      </header>

      <main>
        <Outlet />
      </main>
    </div>
  )
}

export default MainLayout