import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage
    },
    {
      path: '/newQuiz',
      name: 'New Quiz',
      component: NewQuizPage
    }
  ]
})

export default router
