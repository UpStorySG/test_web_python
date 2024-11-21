import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/login.vue'
import Products from '../views/products.vue'
import Contact from '../views/contact.vue'

const routes = [
    {
        path: '/',
        name: 'Login',
        component: Login
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/products',
        name: 'Products',
        component: Products
    },
    {
        path: '/contact',
        name: 'Contact',
        component: Contact
    }
]

export const router = createRouter({
    history: createWebHistory(),
    routes
})
