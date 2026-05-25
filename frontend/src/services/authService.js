import axiosClient from '../api/axiosClient'

export async function loginUser(credentials) {
  const formData = new URLSearchParams()

  formData.append('username', credentials.username)
  formData.append('password', credentials.password)

  const response = await axiosClient.post(
    '/api/auth/login',
    formData,
    {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    },
  )

  return response.data
}

export async function getCurrentUser(token) {
  const response = await axiosClient.get('/api/users/me', {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  })

  return response.data
}