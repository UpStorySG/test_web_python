<template>
    <div class="products">
      <h2>Products</h2>
      <div class="products-grid">
        <div v-for="product in products" :key="product.id" class="product-card">
          <!-- 代码补充区域: 展示product的name, description, price -->
          <!-- 代码补充区域 -->
        </div>
      </div>
      <div class="pagination">
        <button @click="changePage(-1)" :disabled="currentPage === 1">Previous</button>
        <span>Page {{ currentPage }}</span>
        <button @click="changePage(1)" :disabled="currentPage * 10 >= totalProducts">Next</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  
  const products = ref([])
  const currentPage = ref(1)
  const totalProducts = ref(0)
  
  const fetchProducts = async () => {
    const response = await axios.get(`http://localhost:5000/api/products?page=${currentPage.value}`)
    products.value = response.data.products
    totalProducts.value = response.data.total
  }
  
  const changePage = (delta) => {
    currentPage.value += delta
    fetchProducts()
  }
  
  onMounted(fetchProducts)
  </script>
  