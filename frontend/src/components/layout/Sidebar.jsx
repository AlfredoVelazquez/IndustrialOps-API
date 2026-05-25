import DashboardIcon from '@mui/icons-material/Dashboard'
import PrecisionManufacturingIcon from '@mui/icons-material/PrecisionManufacturing'
import {
  Box,
  Divider,
  Drawer,
  List,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Toolbar,
  Typography,
} from '@mui/material'
import { NavLink } from 'react-router-dom'

function Sidebar({ drawerWidth }) {
  const menuItems = [
    {
      text: 'Dashboard',
      icon: <DashboardIcon />,
      path: '/dashboard',
    },
    {
      text: 'Machines',
      icon: <PrecisionManufacturingIcon />,
      path: '/machines',
    },
  ]

  return (
    <Drawer
      variant="permanent"
      sx={{
        display: { xs: 'none', sm: 'block' },
        width: drawerWidth,
        flexShrink: 0,
        '& .MuiDrawer-paper': {
          width: drawerWidth,
          boxSizing: 'border-box',
          bgcolor: '#111827',
          color: '#ffffff',
          borderRight: 'none',
        },
      }}
      open
    >
      <Toolbar>
        <Box>
          <Typography variant="h6" fontWeight={800}>
            IndustrialOps
          </Typography>
          <Typography variant="caption" sx={{ color: '#9ca3af' }}>
            Operations Platform
          </Typography>
        </Box>
      </Toolbar>

      <Divider sx={{ borderColor: '#374151' }} />

      <List sx={{ px: 1.5, py: 2 }}>
        {menuItems.map((item) => (
          <ListItemButton
            key={item.text}
            component={NavLink}
            to={item.path}
            sx={{
              mb: 1,
              borderRadius: 2,
              color: '#d1d5db',
              '&.active': {
                bgcolor: '#2563eb',
                color: '#ffffff',
              },
              '&:hover': {
                bgcolor: '#1f2937',
                color: '#ffffff',
              },
            }}
          >
            <ListItemIcon sx={{ color: 'inherit', minWidth: 40 }}>
              {item.icon}
            </ListItemIcon>
            <ListItemText primary={item.text} />
          </ListItemButton>
        ))}
      </List>
    </Drawer>
  )
}

export default Sidebar