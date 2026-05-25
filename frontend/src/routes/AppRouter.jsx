import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom'
import MainLayout from '../layouts/MainLayout'
import LoginPage from '../pages/LoginPage'
import DashboardPage from '../pages/DashboardPage'
import ProtectedRoute from './ProtectedRoute'

function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginPage />} />

        <Route
          path="/"
          element={
            <ProtectedRoute>
              <MainLayout />
            </ProtectedRoute>
          }
        >
          <Route index element={<Navigate to="/dashboard" replace />} />
          <Route path="dashboard" element={<DashboardPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default AppRouter