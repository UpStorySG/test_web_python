<template>
    <div class="contact">
      <h2>Contact Us</h2>
      <form @submit.prevent="handleSubmit">
        <input v-model="form.name" type="text" placeholder="Name" required>
        <input v-model="form.email" type="email" placeholder="Email" required>
        <textarea v-model="form.message" placeholder="Message" required></textarea>
        <button type="submit">Submit</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { reactive } from 'vue'
  import axios from 'axios'
  
  const form = reactive({
    name: '',
    email: '',
    message: ''
  })
  
  const handleSubmit = async () => {
    try {
      await axios.post('http://localhost:5000/api/contact', form)
      alert('Message sent successfully!')
      form.name = ''
      form.email = ''
      form.message = ''
    } catch (error) {
      alert('Failed to send message')
    }
  }
  </script>
  