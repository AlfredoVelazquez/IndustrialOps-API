import { Box, Paper, Typography } from '@mui/material'

function MachinesPage() {
  return (
    <Box>
      <Typography variant="h4" fontWeight={700} mb={3}>
        Machines
      </Typography>

      <Paper
        elevation={0}
        sx={{
          p: 3,
          borderRadius: 3,
          border: '1px solid #e5e7eb',
        }}
      >
        <Typography>
          Enterprise Machines Module Initialized
        </Typography>
      </Paper>
    </Box>
  )
}

export default MachinesPage