import React, {useState} from 'react'
import TextField from '@mui/material/TextField';

const App = () => {

  const [userId, setUserId] = useState('')
  const [password, setPassword] = useState('')

  return (
    <div>
       <TextField
              required
              label="User ID"
              name="userId"
              val
        />
        <TextField
              required
              label="Password"
              name="password"
        />
    </div>
  )
}

export default App