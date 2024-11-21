<template>
  <div id="app">
    <nav v-if="isLoggedIn">
      <router-link to="/products">Products</router-link> |
      <router-link to="/contact">Contact</router-link> |
      <a href="#" @click.prevent="handleLogout">Logout</a>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const isLoggedIn = ref(!!localStorage.getItem('token'))


/*************************************************************** 
代码补充区域
代码补充区域
代码补充区域
****************************************************************/
// 监听路由变化更新登录状态
watch(() => router.currentRoute.value, () => {

  isLoggedIn.value = !!localStorage.getItem('token')
})

const handleLogout = async () => {
  try {
    const token = localStorage.getItem('token')
    await axios.post('http://localhost:5000/api/logout', {}, {
      headers: { Authorization: `Bearer ${token}` }
    })
    localStorage.removeItem('token')
    router.push('/login')
  } catch (error) {
    console.error('Logout failed:', error)
  }
}
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
  margin: 0 10px;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.login, .products, .contact {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

form {
  display: flex;
  flex-direction: column;
  gap: 15px;
  max-width: 400px;
  margin: 0 auto;
}

input, textarea {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  padding: 10px 20px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #3aa876;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
  margin: 20px 0;
}

.product-card {
  border: 1px solid #ddd;
  padding: 15px;
  border-radius: 8px;
}

.pagination {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  gap: 10px;
  align-items: center;
}
</style>
