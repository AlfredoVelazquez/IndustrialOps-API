import { Box } from '@mui/material'
import { Outlet } from 'react-router-dom'
import Navbar from '../components/layout/Navbar'
import Sidebar from '../components/layout/Sidebar'

const drawerWidth = 260

function MainLayout() {
  return (
    <Box sx={{ display: 'flex', minHeight: '100vh', bgcolor: '#f5f7fb' }}>
      <Sidebar drawerWidth={drawerWidth} />

      <Box sx={{ flexGrow: 1 }}>
        <Navbar drawerWidth={drawerWidth} />

        <Box
          component="main"
          sx={{
            p: 3,
            mt: 8,
            minHeight: 'calc(100vh - 64px)',
          }}
        >
          <Outlet />
        </Box>
      </Box>
    </Box>
  )
}

export default MainLayout