import api from '../api/axiosClient'

export async function getMachines(params = {}) {
  const response = await api.get('/api/machines', {
    params,
  })

  return response.data
}