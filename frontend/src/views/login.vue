<template>
    <div class="login">
      <h2>Welcome to Portal</h2>
      <form @submit.prevent="handleLogin">
        <input 
          v-model="username" 
          type="text" 
          placeholder="Username" 
          required
        >
        <input 
          v-model="password" 
          type="password" 
          placeholder="Password" 
          required
        >
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  import { useRouter } from 'vue-router'
  
  const username = ref('')
  const password = ref('')
  const router = useRouter()
  
  const handleLogin = async () => {
    try {
      const response = await axios.post('/api/login', {
        username: username.value,
        password: password.value
      })
      localStorage.setItem('token', response.data.token)
      
/*************************************************************** 
代码补充区域
代码补充区域
代码补充区域
****************************************************************/
    } catch (error) {
      alert('Login failed: Invalid credentials')
    }
  }
  </script>
  
  <style scoped>
  .login {
    text-align: center;
  }
  
  h2 {
    color: #2c3e50;
    margin-bottom: 30px;
  }
  
  form {
    display: flex;
    flex-direction: column;
    gap: 15px;
    max-width: 300px;
    margin: 0 auto;
  }
  
  input {
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  
  button {
    padding: 10px;
    background-color: #42b983;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #3aa876;
  }
  </style>
  