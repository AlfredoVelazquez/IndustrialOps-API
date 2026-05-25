import {
  Alert,
  Box,
  CircularProgress,
  Paper,
  Typography,
} from '@mui/material'
import { DataGrid } from '@mui/x-data-grid'
import { useEffect, useState } from 'react'
import { getMachines } from '../services/machineService'

function MachinesPage() {
  const [machines, setMachines] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  async function fetchMachines() {
    try {
      setLoading(true)

      const data = await getMachines({
        page: 1,
        page_size: 10,
      })

      setMachines(data.items || [])
    } catch (err) {
      console.error(err)
      setError('Failed to load machines')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchMachines()
  }, [])

  const columns = [
    {
      field: 'id',
      headerName: 'ID',
      width: 90,
    },
    {
      field: 'name',
      headerName: 'Machine Name',
      flex: 1,
    },
    {
      field: 'status',
      headerName: 'Status',
      width: 150,
    },
    {
      field: 'location',
      headerName: 'Location',
      flex: 1,
    },
  ]

  return (
    <Box>
      <Typography variant="h4" fontWeight={700} mb={3}>
        Machines
      </Typography>

      <Paper
        elevation={0}
        sx={{
          height: 600,
          borderRadius: 3,
          border: '1px solid #e5e7eb',
          overflow: 'hidden',
        }}
      >
        {error && (
          <Alert severity="error" sx={{ m: 2 }}>
            {error}
          </Alert>
        )}

        {loading ? (
          <Box
            sx={{
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center',
              height: '100%',
            }}
          >
            <CircularProgress />
          </Box>
        ) : (
          <DataGrid
            rows={machines}
            columns={columns}
            disableRowSelectionOnClick
            initialState={{
              pagination: {
                paginationModel: {
                  pageSize: 10,
                  page: 0,
                },
              },
            }}
            pageSizeOptions={[5, 10, 20]}
          />
        )}
      </Paper>
    </Box>
  )
}

export default MachinesPage